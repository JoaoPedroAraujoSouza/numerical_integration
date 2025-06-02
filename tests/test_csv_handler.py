import os
import tempfile
from src.storage.csv_handler import save_result_csv, load_results_csv

def test_save_and_load_result_csv():
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp:
        path = tmp.name

    try:
        save_result_csv(path, "x**2", 0, 1, 100, "trapezoidal", 0.3333)
        results = load_results_csv(path)
        assert results == [["x**2", "0", "1", "100", "trapezoidal", "0.3333"]]
    finally:
        os.remove(path)

def test_load_empty_csv():
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp:
        path = tmp.name
    try:
        results = load_results_csv(path)
        assert results == []
    finally:
        os.remove(path)