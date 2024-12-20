package com.example.domainfishing.apicalling

import com.example.domainfishing.APIURLS.ApiUrls
import com.example.domainfishing.response.DomainPhishingResponse
import retrofit2.Response
import retrofit2.http.Field
import retrofit2.http.FormUrlEncoded
import retrofit2.http.POST

interface ApiService {
   @FormUrlEncoded
   @POST(ApiUrls.PREDICT)
   suspend fun predictphishing(@Field("url") url:String):Response<DomainPhishingResponse>
}