package com.example.domainfishing.repo

import android.util.Log
import com.example.domainfishing.apicalling.RetrofitInstance
import com.example.domainfishing.response.DomainPhishingResponse
import retrofit2.Response

class Repository {
    private val retrofitInstance=RetrofitInstance.provideApi()
    suspend fun predictPhishing(url:String):Response<DomainPhishingResponse> {

        return  retrofitInstance.predictphishing(url)

    }



}