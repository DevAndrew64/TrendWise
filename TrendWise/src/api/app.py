from flask import Flask, jsonify
from src.data_ingestion.google_trends_scraper import get_google_trends
from src.processing.data_cleaner import clean_data
from src.models.trendwise import train_model
import pandas as pd
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.data_ingestion.google_trends_scraper import get_google_trends

app = Flask(__name__)

@app.route('/predict/<keyword>', methods=['GET'])
def predict(keyword):
    data = get_google_trends([keyword])
    data = clean_data(data)
    
    model = train_model(data, keyword)
    future_timestamps = np.array([(data.index[-1].timestamp() + i * 86400) for i in range(30)]).reshape(-1, 1)
    predictions = model.predict(future_timestamps)
    
    return jsonify({"keyword": keyword, "predictions": predictions.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
