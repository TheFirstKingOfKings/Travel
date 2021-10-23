import datetime


#from overpy import Overpass, Element, Node, Way, Area

from osmapi import OsmApi
from OSMPythonTools import api,  nominatim, data, element
from OSMPythonTools import overpass as ovp
import osmnx as ox
import networkx as nx

from app.processing.point import Point

#api = Overpass()
osm = OsmApi(api="https://master.apis.dev.openstreetmap.org/",  username="vapewalker@mail.ru", password="13241111q")

G = ox.graph_from_place('Kostroma, Russia', network_type='walk')


class Processing:
    totalCostLowBorder          = 0
    totalCostHighBorder         = None
    roadCost                    = None
    totalLength                 = None
    totalTime                   = 0
    totalCost                   = 0
    wayOfTravel                 = None
    dateStart                   = datetime.datetime.today()
    dateEnd                     = None
    desiredTime                 = None
    touristsCategory            = None  # array?
    touristsQuantity            = 1  # Количество отдыхающих
    wouldToEat                  = False
    typeOfEating                = 0  # Самостоятельно
    stageQuantity               = 0  # Количество остановок
    stages                      = []
    stagesDuration              = 0
    roadDuration                = 0
    stagesCost                  = 0
    isHybrid                    = False

    pointA                      = None
    pointB                      = None

    def __init__(self, data):
        self.pointA = Point(float(data['pointA'].split()[0]), float(data['pointA'].split()[1]))
        self.pointB = Point(float(data['pointB'].split()[0]), float(data['pointB'].split()[1]))

    def toStr(self):
        return str(self.pointA) + ' ' + str(self.pointB) + ' ' + str(self.count_length().totalLength) + str(
            self.take_decision())

    def count_length(self):
        self.totalLength = self.pointA.get_distance(self.pointB)
        print(self.totalLength)
        return self

    def get_date_range(self):
        return self.dateEnd - self.dateStart

    def take_decision(self):
        nmt = nominatim.Nominatim()
        areaId = nmt.query('Moscow, Russia').areaId()
        query = ovp.overpassQueryBuilder(area=areaId, elementType=['way', 'relation'], selector='"natural"="water"',
                                     includeGeometry=True)
        # osm.ChangesetCreate({u"comment": u"My first test"})
        # print(osm.NodeCreate({u"lon": 57.74705, u"lat": 40.97366, u"tag": {}}))
        lat_ESB = self.pointA.get_lat()
        lng_ESB =self.pointA.get_long()
        lat_target = self.pointB.get_lat()
        lng_target = self.pointB.get_long()

        fig, ax = ox.plot_graph(G, figsize=(5, 5), close=False, show=False)
        ax.scatter(lng_target, lat_target, c='red', s=100) # Moscow
        ax.scatter(lng_ESB, lat_ESB, c='green', s=500) # Anapa
        nearest_edges = ox.nearest_edges(G, lng_target, lat_target)
        nearest_edge_ESB = ox.nearest_edges(G, lat_ESB, lng_ESB)
        route = nx.shortest_path(G, nearest_edge_ESB[0], nearest_edges[0])
        fig, ax = ox.plot_graph_route(G, route, figsize=(5, 5))
        #ox.plot_route_folium(G, route, 'https://api06.dev.openstreetmap.org/')
        # print(osm.NodeCreate({u"lon": 57.74933, u"lat": 40.97189, u"tag": {}}))
        # print(osm.Map(57.74705, 40.97189, 57.74933, 40.97366))
        # osm.flush()
        # osm.ChangesetClose()
        # query = api.query('''
        #     [out:json];
        #     node({0},{1},{2},{3});
        #     out;
        # '''.format(self.pointA.get_long(), self.pointA.get_lat(), self.pointB.get_long(), self.pointB.get_lat()))
        return fig, ax
        # return areaId

    def count_travel_cost(self):
        ###
        return {"car": 3, 'plane': 10, "train": 4}

    def count_cost_by_way_of_travel(self):
        if self.wayOfTravel == 'walk':
            self.roadCost = 1
        elif self.wayOfTravel == 'car':
            self.roadCost = 2
        elif self.wayOfTravel == 'plane':
            self.roadCost = 3
        return self

    def add_cost_of_stages(self):
        for stage in self.stages:
            self.stagesCost += stage.cost
        return self

    def add_time_of_stages(self):
        for stage in self.stages:
            self.stagesDuration += stage.time
        return self

    def count_time_by_way_of_travel(self):
        if self.wayOfTravel == 'walk':
            self.roadDuration = 30
        elif self.wayOfTravel == 'car':
            self.roadDuration = 20
        elif self.wayOfTravel == 'plane':
            self.roadDuration = 10
        return self

    def count(self):
        self.totalCost += self.stagesCost + self.roadCost
        self.totalTime += self.stagesDuration + self.roadDuration
        return self

    def process(self):
        standartHoursOnMarch = 5  # 1 hour stage
        stageCountBeforeNightStage = 2

        if self.stageQuantity is None:
            if self.desiredTime is not None:

                if self.wayOfTravel is None:
                    allCosts = self.count_travel_cost()
                    lowerCost = allCosts[0]
                    for wayOfTravel in allCosts:
                        if allCosts[wayOfTravel] < lowerCost:
                            if self.desiredTime < standartHoursOnMarch and wayOfTravel == 'walk':
                                lowerCost = allCosts[wayOfTravel]
                            elif self.desiredTime > standartHoursOnMarch and wayOfTravel == 'car':
                                lowerCost = allCosts[wayOfTravel]
                            elif self.totalLength > 500 and wayOfTravel == 'plane':
                                lowerCost = allCosts[wayOfTravel]

                if self.wayOfTravel is not None:
                    self.count_cost_by_way_of_travel().add_cost_of_stages()\
                        .count_time_by_way_of_travel().count()

            if self.desiredTime is not None and self.desiredTime > standartHoursOnMarch:
                self.stageQuantity = self.desiredTime / standartHoursOnMarch

        if self.stageQuantity is not None:
            if self.desiredTime is not None:

                if self.wayOfTravel is None:
                    allCosts = self.count_travel_cost()
                    lowerCost = allCosts[0]
                    for wayOfTravel in allCosts:
                        if allCosts[wayOfTravel] < lowerCost:
                            lowerCost = allCosts[wayOfTravel]

                if self.wayOfTravel is not None:
                    self.count_cost_by_way_of_travel().add_cost_of_stages()\
                        .count_time_by_way_of_travel().count()

            if self.desiredTime is not None and self.desiredTime > standartHoursOnMarch:
                self.stageQuantity = self.desiredTime / standartHoursOnMarch
