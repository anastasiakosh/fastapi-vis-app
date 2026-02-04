from prometheus_client import Counter, generate_latest

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests"
)

def metrics():
    REQUEST_COUNT.inc()
    return generate_latest()
