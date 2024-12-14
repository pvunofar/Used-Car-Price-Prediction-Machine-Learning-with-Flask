# Used Car Price Prediction Web
> This project predicts the prices of used cars using machine learning models like **Random Forest** and **Linear Regression**. A **Flask** web application is used to create a user interface where users can input car details and receive predicted prices.

### _Dataset_
The dataset used in this project is available:
- [Cardetails.csv](/Cardetails.csv): Contains car features like name, year, selling price, kilometers driven, fuel type, seller type, transmission, number of previous owners, mileage, engine capacity, max power, torque, and number of seats.
### _Open source library_
[![Scikit-learn Logo](https://i.imgur.com/U6Q2RXg.png)](https://scikit-learn.org/stable/)
### _Libraries used_
- pandas
`` import pandas as pd `` 
- numpy
`` import numpy as np ``
- matplotlib
`` import matplotlib.pyplot as plt ``
- seaborn
`` import seaborn as sns ``
- regex
`` import re ``
- sklearn
`` from sklearn.model_selection import train_test_split ``
`` from sklearn.linear_model import LinearRegression ``
`` from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error ``
`` from sklearn.ensemble import RandomForestRegressor ``
- joblib
`` import joblib ``
 - flask
`` from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory ``
### _Images_

![](https://i.imgur.com/5Otbn8d.png)
![](https://i.imgur.com/G76NLdc.png)