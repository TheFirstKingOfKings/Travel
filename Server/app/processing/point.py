import math


class Point:
    longitude = None
    latitude = None

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def get_point(self):
        return self.longitude, self.latitude

    def get_long(self):
        return self.longitude

    def get_lat(self):
        return self.latitude

    def get_distance(self, point):
        R = 6371
        dLatitude = self.deg2rad(point.get_lat() - self.get_lat())
        dLongitude = self.deg2rad(point.get_long() - self.get_long())
        a = math.sin(dLatitude/2) * math.sin(dLatitude/2)
        + math.cos(self.deg2rad(self.get_lat())) * math.cos(self.deg2rad(point.get_lat())) * math.sin(dLongitude/2) * math.sin(dLongitude/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = R * c
        return distance

    def deg2rad(self, deg):
        return deg * (math.pi/180)
