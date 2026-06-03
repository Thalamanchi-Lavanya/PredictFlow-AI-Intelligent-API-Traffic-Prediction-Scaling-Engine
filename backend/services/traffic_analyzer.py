import pandas as pd
import numpy as np


class TrafficAnalyzer:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def get_summary(self):
        return {
            "average_requests": float(np.mean(self.df["requests"])),
            "max_cpu": int(np.max(self.df["cpu"])),
            "average_memory": float(np.mean(self.df["memory"]))
        }
        