import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QApplication, QLabel, QPushButton


class CalculadoraAreaCubo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculadora de área para cubos')

        widget_principal = QWidget()
        self.setCentralWidget(widget_principal)

        layout = QVBoxLayout()
        widget_principal.setLayout(layout)

        self.txt_largura = QLineEdit()
        self.txt_altura = QLineEdit()
        self.txt_comprimento = QLineEdit()

        layout.addWidget(QLabel('Largura'))
        layout.addWidget(self.txt_largura)
        layout.addWidget(QLabel('Altura'))
        layout.addWidget(self.txt_altura)
        layout.addWidget(QLabel('Comprimento'))
        layout.addWidget(self.txt_comprimento)

        self.btn_calcular = QPushButton('Calcular área')
        layout.addWidget(self.btn_calcular)

        self.lbl_resultado = QLabel('Área do cubo: ')
        layout.addWidget(self.lbl_resultado)

        self.btn_calcular.clicked.connect(self.calcular_area)

    def calcular_area(self):

        try:
            largura = float(self.txt_largura.text())
        except ValueError:
            self.lbl_resultado.setText(f'O valor da largura não é válido.')

        try:
            altura = float(self.txt_altura.text())
        except ValueError:
            self.lbl_resultado.setText(f'O valor da altura não é válido.')

        try:
            comprimento = float(self.txt_comprimento.text())
        except ValueError:
            self.lbl_resultado.setText(f'O valor do comprimento não é válido.')

        area = largura * altura * comprimento

        self.lbl_resultado.setText(f'A área do cubo é {round(area, 2)}.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculadora = CalculadoraAreaCubo()
    calculadora.show()
    sys.exit(app.exec())
