from PyQt5 import QtCore, QtGui, QtWidgets
from icons_rc_py import iconsCalculadora3_rc
from calculadora import Ui_root  

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_root()
        self.ui.setupUi(self)
        
        self.ui.BTN_CALCULAR.clicked.connect(self.calcular_regra_de_tres)
    
    def calcular_regra_de_tres(self):
        try:
            valor1 = float(self.ui.TXT_VALOR1.text())
            valor2 = float(self.ui.TXT_VALOR2.text())
            valor3 = float(self.ui.TXT_VALOR3.text())
            resultado = (valor1 * valor3) / valor2
            self.ui.label_resultado.setText(f"Resultado: {resultado:.2f}")
        except ValueError:
            self.ui.label_resultado.setText("Erro: Insira valores válidos!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())