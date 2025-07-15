import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        label1 = QLabel("#1", self)
        
        label1.setStyleSheet("background-color: red;")
        
        vbox = QVBoxLayout()
        
        vbox.addWidget(label1)
        
        central_widget.setLayout(vbox)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
    