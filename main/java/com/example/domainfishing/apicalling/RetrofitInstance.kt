package com.example.domainfishing.apicalling

import com.example.domainfishing.APIURLS.ApiUrls
import okhttp3.OkHttpClient
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory


object RetrofitInstance {
    fun provideApi()=Retrofit.Builder().baseUrl(ApiUrls.BASE_URL).client(
        OkHttpClient.Builder().build()
    ).addConverterFactory(GsonConverterFactory.create()).build().create(ApiService::class.java)
}
