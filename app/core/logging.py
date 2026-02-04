import logging

def setup_logging(level: str):
    logging.basicConfig(
       level=level.upper(),
       format="%(asctime)s | %(levelname)s | %(message)s"
    )
