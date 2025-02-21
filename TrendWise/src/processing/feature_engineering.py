import pandas as pd

def generate_features(df):
    df['day_of_week'] = df.index.dayofweek
    df['week_of_year'] = df.index.isocalendar().week
    df['month'] = df.index.month
    return df
