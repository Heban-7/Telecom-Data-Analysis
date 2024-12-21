import pandas as np
import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualization:
    def __init__(self, df):
        self.df = df

    def top_hand_set_plot(self):
        # Top Handsets Bar Plot
        top_handsets = self.df['Handset Type'].value_counts().head(10)
        plt.figure(figsize=(12, 6))
        sns.barplot(x=top_handsets.values, y=top_handsets.index, palette='viridis')
        plt.title('Top 10 Handsets')
        plt.xlabel('Count')
        plt.ylabel('Handset Type')
        plt.show()
    
    def top_manufacturer_handset_plot(self):
        # Top Handsets Bar Plot
        top_handsets = self.df['Handset Manufacturer'].value_counts().head(3)
        plt.figure(figsize=(6, 4))
        sns.barplot(x=top_handsets.values, y=top_handsets.index, palette='viridis')
        plt.title('Top 3 Handset Manufacturer')
        plt.xlabel('Count')
        plt.ylabel('Manufacturer')
        plt.show()

    """
    def plot_visualizations(self):
        # Generate visualizations for key metrics.

        # Total Data Volume Distribution
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df['total_data_volume'], kde=True, bins=30, color='blue')
        plt.title('Total Data Volume Distribution')
        plt.xlabel('Total Data Volume')
        plt.ylabel('Frequency')
        plt.show()

    # Duration vs. Total Data Volume Scatter Plot
        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            x=self.df['Dur. (ms)'],
            y=self.df['total_data_volume'],
            hue=self.df['Handset Manufacturer'],
            palette='tab10' )
        plt.title('Duration vs. Total Data Volume by Manufacturer')
        plt.xlabel('Duration (ms)')
        plt.ylabel('Total Data Volume')
        plt.legend(title='Manufacturer', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.show()
    """
