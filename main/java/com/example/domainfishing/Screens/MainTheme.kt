package com.example.domainfishing.Screens

import androidx.compose.foundation.Image

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.aspectRatio


import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Button

import androidx.compose.material3.MaterialTheme

import androidx.compose.material3.OutlinedTextField

import androidx.compose.material3.Text

import androidx.compose.runtime.Composable

import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier

import androidx.compose.ui.graphics.Color

import androidx.compose.ui.res.painterResource
import androidx.compose.ui.unit.dp
import androidx.hilt.navigation.compose.hiltViewModel
import com.example.domainfishing.R
import com.example.domainfishing.stateHandling.ApiState
import com.example.domainfishing.viewmodel.AppViewModel


@Composable
fun MainAppScreen(viewModel: AppViewModel = hiltViewModel()) {
    val urlInput = remember { mutableStateOf("") } // Holds the user-entered URL
    val resultMessage = remember { mutableStateOf("") } // Holds the result text
    val showDialog = remember { mutableStateOf(false) } // Controls dialog visibility
    val state by viewModel.state.collectAsState() // Observes the ViewModel's state

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp), // Adds padding around the column
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Image(painter = painterResource(id = R.drawable.logo), contentDescription = "Logo",
            modifier = Modifier.aspectRatio(1f).size(250.dp)
            )
        // Title
        Text(
            text = "Phishing URL Predictor",
            style = MaterialTheme.typography.headlineMedium,
            color = MaterialTheme.colorScheme.primary,
            modifier = Modifier.padding(bottom = 24.dp)
        )

        // Input field for URL
        OutlinedTextField(
            value = urlInput.value,
            onValueChange = { urlInput.value = it },
            label = { Text("Enter URL") },
            modifier = Modifier
                .fillMaxWidth()
                .padding(bottom = 16.dp),
            singleLine = true
        )

        // Predict button
        Button(
            onClick = { viewModel.PredictPhishing(urlInput.value) },
            modifier = Modifier
                .fillMaxWidth()
                .height(56.dp),
            shape = MaterialTheme.shapes.medium
        ) {
            Text(
                text = "Predict",
                style = MaterialTheme.typography.bodyLarge,
                color = Color.White
            )
        }

        // Space between button and API response
        Spacer(modifier = Modifier.height(24.dp))

        // Observe API state
        when (val currentState = state) {
            is ApiState.Loading -> {
                Text(
                    text = "",
                    color = Color.Gray,
                    modifier = Modifier.padding(top = 16.dp)
                )
            }

            is ApiState.Success -> {
                resultMessage.value = if (currentState.data.prediction == 1) {
                    "The URL is Phishing"
                } else {
                    "The URL is Safe"
                }
                showDialog.value = true // Show dialog when result is available
            }

            is ApiState.Error -> {
                resultMessage.value = "Error: ${currentState.message}"
                showDialog.value = true // Show dialog on error
            }
        }

        // Display the dialog box
        if (showDialog.value) {
            AlertDialog(
                onDismissRequest = { showDialog.value = false },
                title = {
                    Text(text = "Prediction Result")
                },
                text = {
                    Column(horizontalAlignment = Alignment.CenterHorizontally, verticalArrangement = Arrangement.Center) {
                        val imageRes = if (resultMessage.value.contains("Phishing")) {
                            R.drawable.fail // Replace with your "phishing" image
                        } else {
                            R.drawable.sucess // Replace with your "safe" image
                        }
                        Image(
                            painter = painterResource(id = imageRes),
                            contentDescription = null,
                            modifier = Modifier
                                .size(100.dp)
                                .padding(bottom = 16.dp)
                        )
                        Text(
                            text = resultMessage.value,
                            style = MaterialTheme.typography.bodyLarge,
                            color = if (resultMessage.value.contains("Phishing")) Color.Red else Color.Green
                        )
                    }
                },
                confirmButton = {
                    Button(onClick = { showDialog.value = false }) {
                        Text("GO TO WEBSITE")
                    }
                }
            )
        }
    }
}

