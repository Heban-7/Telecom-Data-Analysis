import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def experiance_analysis(data):
    # Aggregate per customer the following metrics
    user_experience = data.groupby('MSISDN/Number').agg({
        'Avg RTT DL (ms)': 'mean',
        'Avg RTT UL (ms)': 'mean',
        'Avg Bearer TP DL (kbps)': 'mean',
        'Avg Bearer TP UL (kbps)': 'mean',
        'Handset Type': lambda x: x.mode()[0] if not x.mode().empty else np.nan
    }).rename(columns={
        'Avg RTT DL (ms)': 'Avg_RTT_DL_ms',
        'Avg RTT UL (ms)': 'Avg_RTT_UL_ms',
        'Avg Bearer TP DL (kbps)': 'Avg_Throughput_DL_kbps',
        'Avg Bearer TP UL (kbps)': 'Avg_Throughput_UL_kbps'
    })
    return user_experience