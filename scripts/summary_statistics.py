# Import basic Libraries
import pandas as pd
# import scipy
import numpy as np
# from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

def data_summary(data):
    print("Head of the data")
    print(data.head())

    print("\n\nData shape")
    print(data.shape)

    print("\n\nData Information")
    print(data.info())

    print("\n\nData Discription")
    print(data.describe())

    print("Check Missing Values")
    print(data.isnull().sum())
