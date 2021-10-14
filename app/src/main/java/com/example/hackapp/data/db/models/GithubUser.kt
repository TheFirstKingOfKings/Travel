package com.example.hackapp.data.db.models

//@Entity(tableName = "users")
data class GithubUser(
//    @PrimaryKey val id: Long,
    val login: String,
    val avatar_url: String
) {
}