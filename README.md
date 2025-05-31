# Numerical Integration Project

Academic project for calculating definite integrals using numerical methods in Python. The project features a graphical interface, CSV data storage, and automated testing.

## Objective

Implement and compare different numerical integration methods (Simpson and Trapezoidal), allowing the user to:
- Calculate definite integrals of user-provided functions.
- Visualize results in a graphical interface.
- Store results in CSV files.

## Project Structure

```
.
├── src/
│   ├── integration/
│   │   ├── simpson.py
│   │   └── trapezoidal.py
│   ├── main.py
│   ├── storage/
│   │   └── csv_handler.py
│   ├── ui/
│   │   └── app_window.py
│   └── utils/
│       └── error.py
├── tests/
│   ├── test_simpson.py
│   ├── test_trapezoidal.py
│   └── test_csv_handler.py
├── requirements.txt
├── README.md
└── LICENSE
```

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/numerical_integration.git
   cd numerical_integration
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the project:**
   ```bash
   python src/main.py
   ```

## Testing

To run automated tests:
```bash
pytest tests/
```

## Features

- **Trapezoidal Method:** Implementation of the trapezoidal rule for integration.
- **Simpson Method:** Implementation of Simpson’s rule for integration.
- **Graphical Interface:** User can input functions, set limits, and view results.
- **CSV Storage:** Calculation results can be saved to and loaded from CSV files.
- **Error Handling:** Input validation and user-friendly error messages.

## Contributing

1. Create a branch `feature/your-feature` from `develop`.
2. Make clear, atomic commits.
3. Open a Pull Request to `develop` with a clear description of your changes.
4. Wait for review and merge.

## License

This project is under the MIT license. See the [LICENSE](LICENSE) file for details.

---
Project developed by JoaoPedroAraujoSouza and collaborators.
