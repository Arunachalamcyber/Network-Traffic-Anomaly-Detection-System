from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('packets_with_anomalies.csv')
    anomalies = df[df['anomaly'] == -1]
    anomalies = anomalies.to_dict(orient='records')
    return render_template('index.html', anomalies=anomalies)

if __name__ == '__main__':
    app.run(debug=True)
