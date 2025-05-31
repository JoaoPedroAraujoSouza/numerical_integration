import csv

def save_result_csv(path, func_repr, a, b, n, method, result):
    with open(path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([func_repr, a, b, n, method, result])

def load_results_csv(path):
    results = []
    with open(path, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            results.append(row)
    return results