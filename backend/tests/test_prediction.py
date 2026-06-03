from backend.services.prediction_engine import PredictionEngine


def test_prediction():

    predictor = PredictionEngine(
        "traffic_logs.csv"
    )

    value = predictor.predict_next_request()

    assert value > 0