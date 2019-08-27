# Traffic-Congestion-EDA
The objective of this project is to study the effectiveness of various machine learning models for the analysis and forecasting of a road traffic data timeseries. Subsequently, the most suitable model for the use-case has been determined and a prototype application called Traffic Congestion Management System is developed using R and Shiny Dashboard. The web application can predict the traffic conditions for a particular road intersection by training with the traffic data in a timeseries format.

This repository is the exploratory data analysis for the road traffic dataset used in the Traffic Congestion project. The EDA is performed using Python and its libraries - statsmodel, matplotlib, pandas and numpy. Check the Jupyter Notebook <a href='Traffic Congestion - Data Exploration.ipynb'>here</a>.

## Table of Content
- [Introduction](#introduction)
- [Hypothesis Testing](#hypothesis-testing)
- [Stationarity of Timeseries](#stationarity-of-timeseries)
- [Decomposition of Timeseries](#decomposition-of-timeseries)
- [ACF and PACF Analysis](#acf-and-pacf-analysis)
- [Conclusion](#conclusion)

## Introduction
### Timeseries Description
- The  timeseries used for this road traffic data analysis is obtained from data.gov.uk.
- The data is taken from the year 2010 to 2014 (1826 days) at a duration of 15 minutes. 
- For every 24 hours we have 96 observations. Hence, a total of `1826*96 = 175296` observations are recorded. 
- Following is a simple line plot of all the 175296 observations.

<p align="center"><img src="readme/graphs/01.png" title="Line Plot" width=100%></p>

## Proposed Machine Learning Model for the problem
For the given use case, the Autoregressive-Integrated-Moving-Average Model (ARIMA) is considered for forecasting. The results of AR, MA, ARMA and ARIMA models will be analyzed. However, before moving forward to the forecasting stage, we will study the pre-conditions of these models.
- Hypothesis for the trend and seasonality in the timeseries will be tested
- Stationarity of the timeseries will be tested using Dicky-Fuller Test
- Decomposition of timeseries will be performed to obtain the residual timeseries 
- ACF and PACF analysis will be performed

## Hypothesis Testing


## Stationarity of Timeseries


## Decomposition of Timeseries


## ACF and PACF Analysis


## Conclusion
