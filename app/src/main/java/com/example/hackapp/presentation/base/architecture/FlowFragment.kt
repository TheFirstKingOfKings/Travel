package com.example.hackapp.presentation.base.architecture

import org.koin.core.qualifier.named

abstract class FlowFragment : BaseFragment() {

    private val flowCiceroneQualifier
        get() = named(fragmentScopeName + "CICERONE")

}