package com.example.hackapp.di

import org.koin.core.qualifier.named

object DI {

    object Qualifiers {

        val APP_CICERONE = named("APP_CICERONE")
        val APP_ROUTER = named("APP_ROUTER")
        val APP_NAV_HOLDER = named("APP_NAV_HOLDER")

    }

}