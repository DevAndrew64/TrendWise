from pytrends.request import TrendReq
import pandas as pd

def get_google_trends(keywords):
    proxies = ["http://44.219.175.186:8080", "http://204.236.137.68:8080"]  # Usa proxies reales aquí
    pytrends = TrendReq(hl="en-US", tz=360, proxies=proxies)
    # pytrends = TrendReq(hl='es-CO', tz=300)  # Español, zona horaria de Colombia
    pytrends.build_payload(keywords, cat=0, timeframe='today 3-m', geo='CO', gprop='')  # Región Colombia
    trend_data = pytrends.interest_over_time()
    
    if 'isPartial' in trend_data.columns:
        trend_data.drop(columns=['isPartial'], inplace=True)
    
    return trend_data

