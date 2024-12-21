import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class TelecomEDA:
    """
    A class to perform exploratory data analysis for telecom datasets.
    """
    def __init__(self, df):
        self.df = df

    def top_handset_type(self):

        # Identify top 10 handsets used by customers
        top_handsets = self.df['Handset Type'].value_counts().head(10)
        print("Top 10 Handsets:")
        print(top_handsets)

    def top_3_handset_manufacturer(self):
        # Identify top 3 handset manufacturers
        top_manufacturers = self.df['Handset Manufacturer'].value_counts().head(3)
        print("Top 3 Manufacturers:")
        print(top_manufacturers)

    def aggregate_session(self):
        # Aggregate session data for applications
        apps_columns = ['Social Media DL (Bytes)',
       'Social Media UL (Bytes)', 'Google DL (Bytes)', 'Google UL (Bytes)',
       'Email DL (Bytes)', 'Email UL (Bytes)', 'Youtube DL (Bytes)',
       'Youtube UL (Bytes)', 'Netflix DL (Bytes)', 'Netflix UL (Bytes)',
       'Gaming DL (Bytes)', 'Gaming UL (Bytes)', 'Other DL (Bytes)',
       'Other UL (Bytes)',]
        self.df['total_data_volume'] = self.df['Total UL (Bytes)'] + self.df['Total DL (Bytes)']
        aggregated_data = self.df.groupby('Bearer Id')[apps_columns + ['total_data_volume']].sum()
        print("Aggregated User Data:")
        return aggregated_data.head()

    def user_engagement_analysis(self):

        # Engagement Metrics
        engagement_metrics = self.df.groupby('Bearer Id').agg({
            'Dur. (ms)': 'sum',
            'total_data_volume': 'sum',
        }).rename(columns={
            'Dur. (ms)': 'Total Duration',
            'total_data_volume': 'Total Data Volume',
        })

        # Normalize metrics
        scaler = StandardScaler()
        normalized_metrics = scaler.fit_transform(engagement_metrics)

        # K-Means Clustering
        kmeans = KMeans(n_clusters=3, random_state=42)
        engagement_metrics['Cluster'] = kmeans.fit_predict(normalized_metrics)

        # Visualize Clusters
        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            x=engagement_metrics['Total Duration'],
            y=engagement_metrics['Total Data Volume'],
            hue=engagement_metrics['Cluster'],
            palette='viridis'
        )
        plt.title('User Engagement Clusters')
        plt.xlabel('Total Duration')
        plt.ylabel('Total Data Volume')
        plt.legend(title='Cluster')
        plt.show()

        print("Cluster Summary:")
        print(engagement_metrics.groupby('Cluster').mean())



