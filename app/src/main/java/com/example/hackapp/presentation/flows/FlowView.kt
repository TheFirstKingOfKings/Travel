package com.example.hackapp.presentation.flows

import com.arellomobile.mvp.viewstate.strategy.OneExecutionStateStrategy
import com.arellomobile.mvp.viewstate.strategy.StateStrategyType
import com.example.hackapp.presentation.base.architecture.BaseView
import ru.terrakok.cicerone.android.support.SupportAppScreen

interface FlowView : BaseView {

    @StateStrategyType(OneExecutionStateStrategy::class)
    fun setLaunchScreen(vararg screens: SupportAppScreen)

}