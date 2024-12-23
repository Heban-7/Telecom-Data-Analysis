import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.linear_model import LinearRegression
from sqlalchemy import create_engine, Table, Column, String, Float, MetaData

def satisfaction_analysis(df):

    engagement_features = ['Dur. (ms)', 'Total Data Volume']

    scaler = StandardScaler()
    df_engagement = scaler.fit_transform(df[engagement_features])

    # KMeans Clustering for Engagement
    kmeans_eng = KMeans(n_clusters=3, random_state=42).fit(df_engagement)
    df['engagement_cluster'] = kmeans_eng.labels_
    less_engaged_cluster_center = kmeans_eng.cluster_centers_[df['engagement_cluster'].value_counts().idxmin()]
    df['engagement_score'] = np.linalg.norm(df_engagement - less_engaged_cluster_center, axis=1)

    # Standardize engagement and experience metrics
    experience_features = ['Avg RTT DL (ms)', 'Avg RTT UL (ms)', 'Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)']

    scaler = StandardScaler()
    df_experience = scaler.fit_transform(df[experience_features])

    # KMeans Clustering for Experience
    kmeans_exp = KMeans(n_clusters=3, random_state=42).fit(df_experience)
    df['experience_cluster'] = kmeans_exp.labels_
    worst_experience_cluster_center = kmeans_exp.cluster_centers_[df['experience_cluster'].value_counts().idxmin()]
    df['experience_score'] = np.linalg.norm(df_experience - worst_experience_cluster_center, axis=1)
    
    # Satisfaction Score
    df['satisfaction_score'] = (df['engagement_score'] + df['experience_score']) / 2

    return df

def top_10_satisfied_customer(df):
    top_10_satisfied = df[['MSISDN/Number', 'satisfaction_score']].sort_values(by='satisfaction_score', ascending=False).head(10)
    print(top_10_satisfied)


def kmeans_clustering(df):
    # KMeans Clustering (k=2)
    satisfaction_features = ['engagement_score', 'experience_score']
    kmeans_sat = KMeans(n_clusters=2, random_state=42).fit(df[satisfaction_features])
    df['satisfaction_cluster'] = kmeans_sat.labels_

    #  Aggregate Satisfaction and Experience Scores per Cluster
    cluster_summary = df.groupby('satisfaction_cluster').agg({
        'satisfaction_score': 'mean',
        'experience_score': 'mean'
    }).reset_index()
    print(cluster_summary)