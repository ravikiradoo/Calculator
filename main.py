import sys,math
from PyQt5.QtWidgets import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Button:
    def __init__(self,text,results):
        self.b=QPushButton(str(text))
        self.text=text
        self.results=results
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self,v):
        value=self.results.text()

        if v=="=":
            self.result=str(eval(value))
            self.results.setText(self.result)
        elif v=="AC":
            self.results.setText("")
        elif v=="√":
            value=float(value)
            self.results.setText(str(math.sqrt(value)))

        elif v=="C":
            value=value[:-1]
            self.results.setText(value)
        else:
            value = value + v
            self.results.setText(value)


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.StartApp()

    def StartApp(self):
        grid=QGridLayout()

        results=QLineEdit()
        grid.addWidget(results,0,0,1,4)

        buttons=["AC","√","C","/",
                "7","8","9","*",
                "4","5","6","-",
                "1","2","3","+",
                "0",".","="
                ]




        row=1
        col=0
        for button in buttons:
            if col>3:
                row+=1
                col=0

            ButtonObject=Button(button,results)
            if button=="0":
                grid.addWidget(ButtonObject.b,row,col,1,2)
                col+=2
            else:
                grid.addWidget(ButtonObject.b, row, col, 1, 1)
                col += 1

        self.setLayout(grid)

        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Application()
    sys.exit(app.exec_())



