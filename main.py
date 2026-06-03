from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from backend.services.traffic_analyzer import TrafficAnalyzer
from backend.services.prediction_engine import PredictionEngine
from backend.services.anomaly_detector import AnomalyDetector

app = FastAPI(
    title="PredictFlow AI"
)


@app.get("/", response_class=HTMLResponse)
def dashboard():

    analyzer = TrafficAnalyzer("traffic_logs.csv")
    predictor = PredictionEngine("traffic_logs.csv")

    summary = analyzer.get_summary()
    prediction = predictor.predict_next_request()

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>PredictFlow AI Dashboard</title>

        <style>

            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f9;
                margin: 0;
                padding: 0;
            }}

            .header {{
                background-color: #111827;
                color: white;
                text-align: center;
                padding: 30px;
            }}

            .header h1 {{
                margin-bottom: 10px;
            }}

            .container {{
                width: 90%;
                margin: 30px auto;
            }}

            .stats {{
                display: flex;
                justify-content: center;
                gap: 20px;
                flex-wrap: wrap;
                margin-bottom: 40px;
            }}

            .stat-card {{
                background: white;
                width: 250px;
                padding: 20px;
                text-align: center;
                border-radius: 15px;
                box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
            }}

            .stat-card h2 {{
                color: #2563eb;
                margin: 10px 0;
            }}

            .cards {{
                display: flex;
                gap: 20px;
                flex-wrap: wrap;
                justify-content: center;
            }}

            .card {{
                background: white;
                width: 280px;
                padding: 25px;
                border-radius: 16px;
                box-shadow: 0px 6px 15px rgba(0,0,0,0.1);
                text-align: center;
                transition: 0.3s;
            }}

            .card:hover {{
                transform: translateY(-8px);
                box-shadow: 0px 12px 25px rgba(0,0,0,0.15);
            }}

            .card h2 {{
                color: #1f2937;
                margin-bottom: 15px;
            }}

            .card p {{
                color: #6b7280;
                line-height: 1.6;
                min-height: 80px;
            }}

            .btn {{
                display: inline-block;
                margin-top: 10px;
                padding: 12px 20px;
                text-decoration: none;
                background-color: #2563eb;
                color: white;
                border-radius: 8px;
                font-weight: bold;
            }}

            .btn:hover {{
                background-color: #1d4ed8;
            }}

            footer {{
                text-align: center;
                margin-top: 50px;
                padding: 20px;
                color: gray;
            }}

        </style>
    </head>

    <body>

        <div class="header">
            <h1>🌐 PredictFlow AI</h1>
            <p>
                PredictFlow AI — Intelligent API Traffic Prediction & Scaling Engine
            </p>
        </div>

        <div class="container">

            <div class="stats">

                <div class="stat-card">
                    <h3>📈 Average Requests</h3>
                    <h2>{summary["average_requests"]:.0f}</h2>
                </div>

                <div class="stat-card">
                    <h3>💻 Max CPU Usage</h3>
                    <h2>{summary["max_cpu"]}%</h2>
                </div>

                <div class="stat-card">
                    <h3>🤖 Predicted Requests</h3>
                    <h2>{prediction:.0f}</h2>
                </div>

            </div>

            <div class="cards">

                <div class="card">
                    <h2>📊 Traffic Analytics</h2>
                    <p>
                        Analyze API traffic, request volume,
                        CPU utilization and memory consumption.
                    </p>
                    <a class="btn" href="/summary">
                        View Analytics
                    </a>
                </div>

                <div class="card">
                    <h2>🤖 AI Forecasting</h2>
                    <p>
                        Predict future API request load using
                        Machine Learning algorithms.
                    </p>
                    <a class="btn" href="/predict">
                        Run Prediction
                    </a>
                </div>

                <div class="card">
                    <h2>🚨 Anomaly Detection</h2>
                    <p>
                        Identify unusual traffic spikes and
                        abnormal system behavior instantly.
                    </p>
                    <a class="btn" href="/anomalies">
                        Detect Anomalies
                    </a>
                </div>

                <div class="card">
                    <h2>📘 Developer Portal</h2>
                    <p>
                        Explore REST APIs, endpoints and
                        interactive Swagger documentation.
                    </p>
                    <a class="btn" href="/docs">
                        Open Docs
                    </a>
                </div>

            </div>

        </div>

        <footer>
            PredictFlow AI • Python • FastAPI • Scikit-Learn • SQLite
        </footer>

    </body>
    </html>
    """


@app.get("/summary")
def summary():

    analyzer = TrafficAnalyzer(
        "traffic_logs.csv"
    )

    return analyzer.get_summary()


@app.get("/predict")
def predict():

    predictor = PredictionEngine(
        "traffic_logs.csv"
    )

    return {
        "predicted_requests":
        predictor.predict_next_request()
    }


@app.get("/anomalies")
def anomalies():

    detector = AnomalyDetector(
        "traffic_logs.csv"
    )

    return detector.detect_anomalies()