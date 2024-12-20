package com.example.domainfishing.viewmodel

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.domainfishing.repo.Repository
import com.example.domainfishing.response.DomainPhishingResponse
import com.example.domainfishing.stateHandling.ApiState
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class AppViewModel @Inject constructor(private  val repository: Repository) : ViewModel() {

    private val _state=MutableStateFlow<ApiState<DomainPhishingResponse>>(ApiState.Loading)
    val state:StateFlow<ApiState<DomainPhishingResponse>> = _state
    var data:Int=0
    fun PredictPhishing(url:String){
        viewModelScope.launch {
            try {
                val post=repository.predictPhishing(url)
                _state.value=ApiState.Success(post.body()!!)
                data=post.body()!!.prediction
                Log.d("PhishingSucess",post.body().toString())
            }catch (e:Exception){
                _state.value=ApiState.Error(e.message.toString())
                Log.d("PhishingError",e.message.toString())
            }

        }
    }


}


