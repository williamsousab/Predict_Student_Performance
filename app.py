#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Carregar o modelo treinado e o scaler
best_rf_model = joblib.load('best_rf_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    data_df = pd.DataFrame([data])
    data_scaled = scaler.transform(data_df)
    prediction = best_rf_model.predict(data_scaled)
    return jsonify(prediction.tolist())

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




