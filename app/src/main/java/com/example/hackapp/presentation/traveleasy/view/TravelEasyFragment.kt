package com.example.hackapp.presentation.traveleasy.view

import android.os.Bundle
import android.text.SpannableString
import android.text.style.StyleSpan
import android.view.View
import com.example.hackapp.R
import com.example.hackapp.presentation.base.architecture.BaseFragment
import com.example.hackapp.util.setSafeOnClickListener
import kotlinx.android.synthetic.main.fragment_travel_easy.*


class TravelEasyFragment : BaseFragment() {

    override val layoutRes = R.layout.fragment_travel_easy

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        setControlElements()
        btn_have_account?.setSafeOnClickListener {

        }
        btn_sign_up?.setSafeOnClickListener {

        }
    }

    private fun setControlElements() {
        btn_have_account?.text = SpannableString(
            getString(R.string.have_account)
        ).apply {
            setSpan(
                StyleSpan(R.style.SingInPoppinsBold),
                START_POSITION,
                getString(R.string.have_account).length,
                0
            )
        }
    }

    companion object {

        private const val START_POSITION = 15

    }

}