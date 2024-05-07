# Devices-Price-Classification-System-using-Python-and-Spring-Boot

The Devices Price Classification System predicts the price range of devices based on their specifications. This repository contains the implementation of the machine learning model and the RESTful API for interacting with the model.

## Project Structure
- `model.ipynb`: Jupyter Notebook containing the machine learning model development process.
- `pipeline.pkl`: Serialized machine learning model.
- `app.py`: Flask application serving as the RESTful API.

## Running the Application
To run the application:
1. Open `model.ipynb` and run the notebook to train the machine learning model and serialize it.
2. Execute `app.py` to start the Flask application serving the RESTful API.

## Interacting with API Endpoints
The following RESTful endpoints are available:
- `/predict`: POST request to predict the price of a device by sending its specifications.

## Usage
1. Train the machine learning model using `model.ipynb`.
2. Start the Flask application using `app.py`.
3. Send POST requests to `/predict` endpoint with device specifications to get price predictions.
