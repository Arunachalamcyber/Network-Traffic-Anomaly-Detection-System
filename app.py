import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('packets_with_anomalies.csv')   # Data loading

    print(df.columns)  # To verify columns in the console

    anomalies = df[df['is_anomaly'] == True]


    # Convert DataFrame to list of dicts (records) to pass to template
    anomalies_records = anomalies.to_dict(orient='records')

    # Pass the list of anomaly records to the template
    return render_template('index.html', anomalies=anomalies_records)

if __name__ == '__main__':
    app.run(debug=True)
