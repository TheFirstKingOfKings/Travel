package com.example.hackapp.presentation

import androidx.fragment.app.Fragment
import com.example.hackapp.presentation.traveleasy.view.TravelEasyFragment
import ru.terrakok.cicerone.android.support.SupportAppScreen

object Screens {

    object TravelEasy : SupportAppScreen() {
        override fun getFragment(): Fragment = TravelEasyFragment()
    }

}