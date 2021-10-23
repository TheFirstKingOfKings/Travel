package com.example.hackapp.presentation.base.architecture

import com.arellomobile.mvp.MvpPresenter

abstract class BasePresenter<V: BaseView> : MvpPresenter<V>() {
}