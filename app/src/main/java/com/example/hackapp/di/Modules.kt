package com.example.hackapp.di

import io.noties.markwon.Markwon
import io.noties.markwon.inlineparser.MarkwonInlineParserPlugin
import org.koin.android.ext.koin.androidContext
import org.koin.dsl.module

val appModule = module {

    /** -----  App Navigation  ----- */
//    single { AppLauncher(get(), get(), get(), get(), get(DI.Qualifiers.APP_ROUTER)) }
//    single<Cicerone<Router>>(DI.Qualifiers.APP_CICERONE) { Cicerone.create() }
//    single<Router>(DI.Qualifiers.APP_ROUTER) { get<Cicerone<Router>>(DI.Qualifiers.APP_CICERONE).router }
//    single<NavigatorHolder>(DI.Qualifiers.APP_NAV_HOLDER) {
//        get<Cicerone<Router>>(DI.Qualifiers.APP_CICERONE).navigatorHolder
//    }

    /** ---- UI Utils ---- */
    single {
        Markwon.builder(androidContext())
            .usePlugin(MarkwonInlineParserPlugin.create())
            .build()
    }

}
