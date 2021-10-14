package com.example.hackapp.presentation.base.architecture

import androidx.fragment.app.Fragment
import org.koin.core.qualifier.named

abstract class BaseFragment : Fragment() {

    protected lateinit var fragmentScopeName: String


}