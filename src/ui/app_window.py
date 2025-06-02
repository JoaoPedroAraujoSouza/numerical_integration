from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QComboBox, QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem,
    QHeaderView, QSizePolicy, QSpacerItem
)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from src.integration.simpson import simpson_integrate
from src.integration.trapezoidal import trapezoidal_integrate
from src.storage.csv_handler import save_result_csv, load_results_csv
import sys
import numpy as np
import os

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Numerical Integration")
        self.setMinimumSize(600, 520)
        self.setStyleSheet("""
            QWidget { background: #f0f4f8; }
            QLabel { font-size: 15px; color: #273c75; }
            QLineEdit, QComboBox {
                font-size: 15px;
                padding: 6px;
                border-radius: 4px;
                border: 1px solid #d1d8e0;
                background: #fff;
                color: #222;
            }
            QComboBox QAbstractItemView {
                color: #222;
                background: #fff;
            }
            QPushButton {
                background: #4078c0;
                color: #222;
                border-radius: 6px;
                padding: 8px 20px;
                font-weight: bold;
            }
            QPushButton:hover { background: #305080; }
            QTableWidget, QTableWidget QTableCornerButton::section {
                background: #fff;
                border-radius: 6px;
                color: #222;
            }
            QHeaderView::section {
                background: #e6e9ef;
                color: #222;
                font-weight: bold;
                border: 1px solid #d1d8e0;
            }
        """)
        self.last_result = None
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        main_layout.setContentsMargins(30, 20, 30, 20)
        main_layout.setSpacing(18)

        title = QLabel("Numerical Integration Calculator")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setStyleSheet("color: #273c75; margin-bottom: 10px;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Inputs
        input_layout = QHBoxLayout()
        input_layout.setSpacing(12)

        self.func_input = QLineEdit()
        self.func_input.setPlaceholderText("e.g. x**2 + 3*x")
        self.func_input.setText("x**2")
        input_layout.addLayout(self._labeled("f(x):", self.func_input))

        self.a_input = QLineEdit()
        self.a_input.setPlaceholderText("a")
        self.a_input.setFixedWidth(60)
        self.a_input.setText("0")
        input_layout.addLayout(self._labeled("a:", self.a_input))

        self.b_input = QLineEdit()
        self.b_input.setPlaceholderText("b")
        self.b_input.setFixedWidth(60)
        self.b_input.setText("1")
        input_layout.addLayout(self._labeled("b:", self.b_input))

        self.n_input = QLineEdit()
        self.n_input.setPlaceholderText("n")
        self.n_input.setFixedWidth(60)
        self.n_input.setText("100")
        input_layout.addLayout(self._labeled("n:", self.n_input))

        self.method_combo = QComboBox()
        self.method_combo.addItems(["Trapezoidal", "Simpson"])
        self.method_combo.setFixedWidth(120)
        input_layout.addLayout(self._labeled("Method:", self.method_combo))

        main_layout.addLayout(input_layout)

        # Calculate button centered
        calc_layout = QHBoxLayout()
        calc_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.calc_btn = QPushButton("Calculate")
        self.calc_btn.setIcon(QIcon.fromTheme("system-search"))
        self.calc_btn.clicked.connect(self.calculate)
        calc_layout.addWidget(self.calc_btn)
        calc_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(calc_layout)

        # Result
        self.result_label = QLabel("Result: ---")
        self.result_label.setFont(QFont("Arial", 15, QFont.Bold))
        self.result_label.setStyleSheet("color: #273c75; margin-top: 10px;")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.result_label)

        # Save/load buttons
        btns_layout = QHBoxLayout()
        btns_layout.setSpacing(16)
        self.save_btn = QPushButton("Save result")
        self.save_btn.setIcon(QIcon.fromTheme("document-save"))
        self.save_btn.clicked.connect(self.save_result)
        btns_layout.addWidget(self.save_btn)
        self.load_btn = QPushButton("Load CSV")
        self.load_btn.setIcon(QIcon.fromTheme("document-open"))
        self.load_btn.clicked.connect(self.load_results)
        btns_layout.addWidget(self.load_btn)
        main_layout.addLayout(btns_layout)

        # Results table
        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels(["Function", "a", "b", "n", "Method", "Result"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.setFixedHeight(180)
        main_layout.addWidget(self.table)

        self.setLayout(main_layout)

    def _labeled(self, text, widget):
        box = QVBoxLayout()
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        box.addWidget(label)
        box.addWidget(widget)
        return box

    def calculate(self):
        try:
            func_str = self.func_input.text().strip()
            a = float(self.a_input.text())
            b = float(self.b_input.text())
            n = int(self.n_input.text())
            method = self.method_combo.currentText().lower()

            def func(x):
                return eval(func_str, {"x": x, "np": np, "__builtins__": {}})

            if method == "trapezoidal":
                result = trapezoidal_integrate(func, a, b, n)
            else:
                result = simpson_integrate(func, a, b, n)

            self.result_label.setText(f"Result: {result:.6f}")
            self.last_result = (func_str, str(a), str(b), str(n), method, f"{result:.6f}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error while calculating: {e}")

    def save_result(self):
        if not self.last_result:
            QMessageBox.warning(self, "Warning", "No result to save.")
            return
        path, _ = QFileDialog.getSaveFileName(self, "Save CSV", os.getcwd(), "CSV Files (*.csv)")
        if path:
            try:
                save_result_csv(path, *self.last_result)
                QMessageBox.information(self, "Saved", "Result saved successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error while saving: {e}")

    def load_results(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open CSV", os.getcwd(), "CSV Files (*.csv)")
        if path:
            try:
                results = load_results_csv(path)
                self.table.setRowCount(0)
                for row in results:
                    row_pos = self.table.rowCount()
                    self.table.insertRow(row_pos)
                    for col, val in enumerate(row):
                        self.table.setItem(row_pos, col, QTableWidgetItem(str(val)))
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error while loading: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec())