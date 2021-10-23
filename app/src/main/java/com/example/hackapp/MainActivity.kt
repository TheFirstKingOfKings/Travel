package com.example.hackapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.navigation.NavController
import androidx.navigation.Navigation
import com.example.hackapp.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    lateinit var mNavController: NavController
//    private var _binding: ActivityMainBinding? = null
//    val mBinding = _binding!!


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
//        _binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(R.layout.activity_main)
        mNavController = Navigation.findNavController(this, R.id.nav_host_fragment_container)
    }

    override fun onDestroy() {
        super.onDestroy()
//        _binding = null
    }
}