import numpy as np
import time

def generate_data():
    x = np.linspace(0, 10, 50)
    y = np.sin(x + time.time())
    return {
        "x": x.tolist(),
        "y": y.tolist()
    }
