package com.example.hackapp.presentation.base.architecture

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.arellomobile.mvp.MvpAppCompatFragment
import org.koin.core.qualifier.named

abstract class BaseFragment : MvpAppCompatFragment(), BaseView {

    abstract val layoutRes: Int

    protected lateinit var fragmentScopeName: String

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View = inflater.inflate(layoutRes, container, false)
}