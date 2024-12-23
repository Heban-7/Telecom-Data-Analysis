from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def user_engagement(data):
    # Aggregate Engagement Metrics per Customer (MSISDN)
    user_engagement = data.groupby('MSISDN/Number').agg({
        'Dur. (ms)': 'sum',
        'Total UL (Bytes)': 'sum',
        'Total DL (Bytes)': 'sum'
    }).rename(columns={
        'Dur. (ms)': 'Total_Duration_ms',
        'Total UL (Bytes)': 'Total_UL_Bytes',
        'Total DL (Bytes)': 'Total_DL_Bytes'
    })

    # Calculate Total Session Traffic
    user_engagement['Total_Traffic_Bytes'] = user_engagement['Total_UL_Bytes'] + user_engagement['Total_DL_Bytes']

    #Top 10 Customers per Engagement Metric
    top_10_duration = user_engagement.sort_values(by='Total_Duration_ms', ascending=False).head(10)
    top_10_traffic = user_engagement.sort_values(by='Total_Traffic_Bytes', ascending=False).head(10)

    # Display Top 10 Results
    print("Top 10 Customers by Duration:\n", top_10_duration)
    print("\nTop 10 Customers by Traffic:\n", top_10_traffic)

def aggregate_session(df):
    """
    Aggregate session data for applications.
    """
    apps_columns = [
        'Social Media DL (Bytes)', 'Social Media UL (Bytes)', 'Google DL (Bytes)',
        'Google UL (Bytes)', 'Email DL (Bytes)', 'Email UL (Bytes)',
        'Youtube DL (Bytes)', 'Youtube UL (Bytes)', 'Netflix DL (Bytes)',
        'Netflix UL (Bytes)', 'Gaming DL (Bytes)', 'Gaming UL (Bytes)',
        'Other DL (Bytes)', 'Other UL (Bytes)'
    ]
    aggregated_data = df.groupby('Bearer Id')[apps_columns].sum()
    print("Aggregated User Data Head:")
    return aggregated_data.head()

def correlation_matrix(aggregated_data):
    # Correlation matrix for aggrigated data
    corr = aggregated_data.corr()
    return corr

def cluster_summary(df):
    """
    Perform user engagement analysis using clustering.
    """
    # Engagement Metrics
    engagement_metrics = df.groupby('Bearer Id').agg({
        'Dur. (ms)': 'sum',
        'Total UL (Bytes)': 'sum',
        'Total DL (Bytes)': 'sum',
        'Total Data Volume': 'sum',
    }).rename(columns={
        'Dur. (ms)': 'Total Duration',
        'Total UL (Bytes)': 'Total UL',
        'Total D: (Bytes)': 'Total DL',
        'Total Data Volume': 'Total Data Volume',
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