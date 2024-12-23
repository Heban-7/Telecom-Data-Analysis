import pandas as pd

def top_handset_type(df):
    """
    Identify top 10 handsets used by customers.
    """
    top_handsets = df['Handset Type'].value_counts().head(10)
    print("Top 10 Handsets:")
    print(top_handsets)

def top_3_handset_manufacturer(df):
    """
    Identify top 3 handset manufacturers.
    """
    top_manufacturers = df['Handset Manufacturer'].value_counts().head(3)
    print("Top 3 Manufacturers:")
    print(top_manufacturers)

def handsets_per_manufacturer(df):
    """
    Identify top 5 handsets per top 3 manufacturers.
    """
    df['Handset Manufacturer'] = df['Handset Type'].str.split().str[0]
    top_manufacturers = df['Handset Manufacturer'].value_counts().head(3)
    for manufacturer in top_manufacturers.index:
        top_handsets_per_manufacturer = df[df['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(5)
        print(f"Top 5 Handsets for {manufacturer}:")
        print(top_handsets_per_manufacturer)


