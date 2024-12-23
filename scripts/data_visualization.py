import pandas as np
import matplotlib.pyplot as plt
import seaborn as sns

def top_hand_set_plot(df):
    """
    Plot top 10 handsets bar plot.
    """
    top_handsets = df['Handset Type'].value_counts().head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_handsets.values, y=top_handsets.index, palette='viridis')
    plt.title('Top 10 Handsets')
    plt.xlabel('Count')
    plt.ylabel('Handset Type')
    plt.show()

def top_manufacturer_handset_plot(df):
    """
    Plot top 3 handset manufacturers bar plot.
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    top_handsets = df['Handset Manufacturer'].value_counts().head(3)
    plt.figure(figsize=(6, 4))
    sns.barplot(x=top_handsets.values, y=top_handsets.index, palette='viridis')
    plt.title('Top 3 Handset Manufacturer')
    plt.xlabel('Count')
    plt.ylabel('Manufacturer')
    plt.show()


def corrilation_visualization(corr):
    plt.figure(figsize = (12,12))
    sns.heatmap(corr, annot= True, cmap = 'coolwarm')
    plt.title('Correlation Matrix of Selected Variables')
    plt.show

def aggregate_Visualization(col_sum):
    #Plot column sum of aggregate session
    fig, ax = plt.subplots(figsize = (12,10))
    plt.bar(col_sum.index, col_sum.values)
    plt.xticks(rotation = 90)
    plt.ylabel("Sum of Data (Bytes)")
    plt.xlabel("Columns")
    plt.tight_layout()
    plt.show()


def top_50_throughput_destribution_per_handset(user_experience):
    # Throughput Distribution per Handset Type
    
    throughput_distribution = user_experience.groupby('Handset Type')['Avg_Throughput_DL_kbps'].mean().sort_values(ascending=False)
    throughput_distribution[:50].plot(kind='bar', figsize=(12, 6))
    plt.title('Average Throughput per Handset Type')
    plt.ylabel('Average Throughput (kbps)')
    plt.show()

def lest_50_throughput_destribution_per_handset(user_experience):
    # Throughput Distribution per Handset Type
    throughput_distribution = user_experience.groupby('Handset Type')['Avg_Throughput_DL_kbps'].mean().sort_values(ascending=False)
    throughput_distribution[len(throughput_distribution) -50:].plot(kind='bar', figsize=(12, 6))
    plt.title('Average Throughput per Handset Type')
    plt.ylabel('Average Throughput (kbps)')
    plt.show()