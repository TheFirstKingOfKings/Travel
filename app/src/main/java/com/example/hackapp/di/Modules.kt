package com.example.hackapp.di

import org.koin.dsl.module
import ru.terrakok.cicerone.Cicerone
import ru.terrakok.cicerone.NavigatorHolder
import ru.terrakok.cicerone.Router

val appModule = module {

    /** -----  App Navigation  ----- */
//    single { AppLauncher(get(), get(), get(), get(), get(DI.Qualifiers.APP_ROUTER)) }
    single<Cicerone<Router>>(DI.Qualifiers.APP_CICERONE) { Cicerone.create() }
    single<Router>(DI.Qualifiers.APP_ROUTER) { get<Cicerone<Router>>(DI.Qualifiers.APP_CICERONE).router }
    single<NavigatorHolder>(DI.Qualifiers.APP_NAV_HOLDER) {
        get<Cicerone<Router>>(DI.Qualifiers.APP_CICERONE).navigatorHolder
    }

}
