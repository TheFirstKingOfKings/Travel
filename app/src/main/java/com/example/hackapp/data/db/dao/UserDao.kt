package com.example.hackapp.data.db.dao

import androidx.lifecycle.LiveData
import com.example.hackapp.data.db.models.GithubUser

//@Dao
interface UserDao {

//    @Query("SELECT * FROM users")
    fun findAll(): LiveData<List<GithubUser>>

//    @Insert(onConflict = OnConflictStrategy.REPLACE)
    fun add(users: List<GithubUser>)

}