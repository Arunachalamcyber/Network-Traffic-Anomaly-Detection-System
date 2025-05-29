import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import IsolationForest

def load_data(path='packets.csv'):
    df = pd.read_csv(path)
    return df

def preprocess(df):
    le_src = LabelEncoder()
    le_dst = LabelEncoder()
    le_proto = LabelEncoder()

    df['src_enc'] = le_src.fit_transform(df['src'])
    df['dst_enc'] = le_dst.fit_transform(df['dst'])
    df['proto_enc'] = le_proto.fit_transform(df['proto'])

    X = df[['src_enc', 'dst_enc', 'length', 'proto_enc']]
    return X, df

def train_and_predict(df):
    X, df = preprocess(df)
    model = IsolationForest(contamination=0.05)
    model.fit(X)
    df['anomaly'] = model.predict(X)
    return df

if __name__ == "__main__":
    df = load_data()
    df = train_and_predict(df)
    df.to_csv('packets_with_anomalies.csv', index=False)
    print("Anomaly detection complete, results saved to packets_with_anomalies.csv")
s