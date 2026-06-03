import pandas as pd
from sklearn.ensemble import IsolationForest


class AnomalyDetector:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def detect_anomalies(self):

        model = IsolationForest(
            contamination=0.2,
            random_state=42
        )

        self.df["anomaly"] = model.fit_predict(
            self.df[["requests", "cpu", "memory"]]
        )

        anomalies = self.df[
            self.df["anomaly"] == -1
        ]

        return anomalies.to_dict(
            orient="records"
        )