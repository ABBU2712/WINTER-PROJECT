# Spotify Genre Analysis (Winter Project)

**Description**

This project is aimed at predicting the genre of a song based on its features using a Spotify dataset. The dataset was obtained from Kaggle.

## Table of Contents

- [Spotify Genre Analysis (Winter Project)](#spotify-genre-analysis-winter-project)
  - [Description](#description)
  - [Project Steps](#project-steps)
  - [Getting Started](#getting-started)
  - [Productionalizing the Model](#productionalizing-the-model)


## Description

This project utilizes a dataset of songs on Spotify to predict their genre based on various song features. By analyzing the data, the project aims to create an accurate genre classification model.

## Project Steps

The project involves several key steps:

1. **Data Reading**: Obtaining and importing the Spotify dataset from Kaggle.
2. **Data Normalization**: Ensuring data consistency and format.
3. **Feature Engineering**: Creating new features or modifying existing ones.
4. **Outlier Detection**: Identifying and handling outliers in the data.
5. **K-Nearest Neighbors (KNN)**: Applying the KNN algorithm to classify songs into genres and determining the optimal value of K.
6. **Random Forest Classifier**: Using the Random Forest classifier to improve genre classification accuracy.
7. **Productionalizing the Model**: Deploying the model for real-world use using Heroku and the Streamlit library. Model serialization (pickling) is done to convert the model into bytes for deployment.

## Getting Started

### Prerequisites

Before you start, make sure you have the following prerequisites in place:

- python >= 3.6
- numpy
- pandas
- matplotlib
- heroku
- seaborn
- sklearn

### Installation

To get the project up and running, follow these installation steps:

Use pip install for the installation

## Productionalizing the Model

Learn how to deploy the genre prediction model on Heroku using Streamlit. Be sure to detail the steps required for users to access the deployed model.

