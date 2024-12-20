package com.example.domainfishing.di

import com.example.domainfishing.repo.Repository
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object DiObject {
@Provides
fun providerepo():Repository{
    return Repository()
}

}