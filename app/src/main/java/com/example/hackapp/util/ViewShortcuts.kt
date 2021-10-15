package com.example.hackapp.util

import android.content.Context
import android.view.View
import android.view.inputmethod.InputMethodManager
import com.example.hackapp.HackApplication

fun View.hideKeyboard() {
    getInputMethodManager()?.hideSoftInputFromWindow(windowToken, 0)
}

private fun getInputMethodManager(): InputMethodManager? =
        HackApplication.appContext.getSystemService(Context.INPUT_METHOD_SERVICE)
                as? InputMethodManager