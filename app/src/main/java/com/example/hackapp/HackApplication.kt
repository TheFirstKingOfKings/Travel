package com.example.hackapp

import android.app.Application
import android.content.Context

class HackApplication : Application() {

    companion object {

        @JvmStatic
        lateinit var appContext: Context
            private set

    }

}