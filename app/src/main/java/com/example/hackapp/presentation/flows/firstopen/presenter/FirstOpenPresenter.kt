package com.example.hackapp.presentation.flows.firstopen.presenter

import com.example.hackapp.presentation.Screens
import com.example.hackapp.presentation.base.architecture.BasePresenter

class FirstOpenPresenter : BasePresenter<FirstOpenView>() {

    override fun onFirstViewAttach() {
        viewState?.setLaunchScreen(Screens.TravelEasy)
    }
}