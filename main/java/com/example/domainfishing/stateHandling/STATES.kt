package com.example.domainfishing.stateHandling

sealed class ApiState<out T> {
    data class Success<T>(val data: T) : ApiState<T>() // Represents a successful response.
    data class Error(val message: String) : ApiState<Nothing>() // Represents an error state.
    object Loading : ApiState<Nothing>() // Represents a loading state.
}