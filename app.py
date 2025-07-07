
from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/api/cme')
def detect_cme():
    np.random.seed(42)
    time_range = pd.date_range(start='2024-08-25', periods=100, freq='1min')
    flux = np.random.normal(10, 2, 100)
    density = np.random.normal(5, 1, 100)
    temperature = np.random.normal(1e5, 2e4, 100)
    speed = np.random.normal(400, 50, 100)

    flux_density = flux * density
    temp_speed_ratio = temperature / speed
    cme_flag = ((flux_density > 90) & (temp_speed_ratio > 300)).astype(int)

    data = []
    for i in range(100):
        data.append({
            'time': str(time_range[i]),
            'flux': round(flux[i], 2),
            'density': round(density[i], 2),
            'temperature': round(temperature[i], 2),
            'speed': round(speed[i], 2),
            'flux_density': round(flux_density[i], 2),
            'temp_speed_ratio': round(temp_speed_ratio[i], 2),
            'cme_flag': int(cme_flag[i])
        })

    return jsonify(data)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
