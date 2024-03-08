import sys
import re
from PyQt5.QtWidgets import QDialog, QApplication
from morze import *
class morze(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.work)
        self.show()
    def work(self):
        alpha = {'А':'*-', 'Б':'-***', 'В':'*--', 'Г': '--*', 'Д':'-**', 'Е':'*', 'Ж':'***-',
            'З':'--**', 'И':'**', 'Й':'*---', 'К':'-*-', 'Л':'*-**', "М":'--', 'Н':'-*', 'О':'---',
            'П':'*--*', 'Р':'*-*', 'С':'***', 'Т':"-", "У":'**-', 'Ф':'**-*', 'Х':'****', 'Ц':'-*-*',
            'Ч':'---*', "Ш":'----', 'Щ':'--*-', 'Ъ':'*--*-*', 'Ы': '-*--', 'Ь':'-**-', "Э":"**-**", "Ю":'**--', 'Я':'*-*-',
            '1':'*----', '2':'**---', '3':'***--', '4':'****-', '5':'*****', '6':'-****', '7':'--***', '8':'---**', '9':'----*', '0':'-----', ' ':'    '}
        take_text = self.ui.textEdit.toPlainText().upper()
        c = ''
        g = ''
        check = 0
        new_dist = {}
        for key, value in alpha.items():
            new_dist[value] = key
        if self.ui.radioButton.isChecked() == True:
            try:
                text = re.sub(r'\s+', ' ', take_text)
                for i in range(len(text)):
                    c += (alpha[take_text[i]])
                    if i != len(take_text) - 1:
                        c += " "
                self.ui.textEdit_2.setPlainText(c)
            except:
                pass
        elif self.ui.radioButton_2.isChecked()==True:
            try:
                for i in take_text:
                    if "    " in take_text:
                        take_text = take_text.replace("    "," ")
                take_text = take_text.split(" ")
                for i in range(len(take_text)):
                    if take_text[i] == '' and check == 0:
                        check = 1
                    elif take_text == "" and check == 1:
                        del take_text[i]
                    else:
                        check = 0
                for i in take_text:
                    if i == '':
                        g+=(new_dist["    "])
                    else:
                        g+=(new_dist[i])
                self.ui.textEdit_2.setPlainText(g.title())

            except:
                pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    start = morze()
    start.show()
    sys.exit(app.exec_())