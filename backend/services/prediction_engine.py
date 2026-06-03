import pandas as pd
from sklearn.linear_model import LinearRegression


class PredictionEngine:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def predict_next_request(self):

        X = self.df.index.values.reshape(-1, 1)
        y = self.df["requests"]

        model = LinearRegression()

        model.fit(X, y)

        next_index = [[len(self.df)]]

        prediction = model.predict(next_index)

        return float(prediction[0])