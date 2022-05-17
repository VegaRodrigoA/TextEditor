# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QCloseEvent
import PyPDF2


class miEditor(QMainWindow):

    def __init__(self):
        super(miEditor,self).__init__()
        uic.loadUi('untitled.ui',self)
        self.show()
        
        self.setWindowTitle("Cuaderno de notas")
        self.action12.triggered.connect(lambda: self.cambioTamaño(12))
        self.action15.triggered.connect(lambda: self.cambioTamaño(15))
        self.action20.triggered.connect(lambda: self.cambioTamaño(20))
        self.action70.triggered.connect(lambda: self.cambioTamaño(25))
        self.action30.triggered.connect(lambda: self.cambioTamaño(30))
        self.action35.triggered.connect(lambda: self.cambioTamaño(35))
        self.action40.triggered.connect(lambda: self.cambioTamaño(40))
        self.action45.triggered.connect(lambda: self.cambioTamaño(45))
        self.actionAbrir.triggered.connect(lambda: self.abrir())
        self.actionGuardar.triggered.connect(lambda: self.Guardar())
        #self.actionCerrar.triggered.connect(lambda: self.closeEvent(QCloseEvent()))
        #self.actionCerrar.triggered.connect(exit())
        self.actionCerrar.triggered.connect(lambda: self.close_Event())
    
    
    def cambioTamaño(self,size):
        self.plainTextEdit.setFont(QFont("FreeMono",size))
    
    def abrir(self):
        options = QFileDialog().Options()
        archivo , _= QFileDialog().getOpenFileName()
        print(archivo)# Agregar un try except para avisar de errores
        if archivo != "":#agregar si termina en .pdf abrir con pypdf
            if archivo[-3:] != "pdf":
                with open(archivo,"r") as f:
                    self.plainTextEdit.setPlainText(f.read())
            
            elif archivo[-3:] == "pdf":
                # creating a pdf file object 
                pdfFileObj = open(archivo, 'rb')
                # creating a pdf reader object 
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                num = pdfReader.numPages
                i = 0
                string = ""
                while i < num:
                    pageObj2 = pdfReader.getPage(i)
                    string = string + pageObj2.extractText() 
                    i +=1
                self.plainTextEdit.setPlainText(string)
                
    
    def Guardar(self):
        try:
            options = QFileDialog().Options()
            archivo , _ = QFileDialog().getSaveFileName()
            print(archivo)
            if archivo != "":#si termina en .pdf guardar con pypdf
                if archivo[-3:] != "pdf":
                    with open(archivo,"w") as f:
                        f.write(self.plainTextEdit.toPlainText())
                else:
                    # creating a pdf file object 
                    pdfFileObj = open(archivo, 'wb')
                    # creating a pdf writer object 
                    pdfWriter = PyPDF2.PdfFileWriter(pdfFileObj)
                    num = self.plainTextEdit.getPage
                    i = 0
                    string = ""
                    while i < num:
                        pageObj2 = pdfReader.getPage(i)
                        string = string + pageObj2.extractText() 
                        i +=1
                    #self.plainTextEdit.setPlainText(string)
                
                return QCloseEvent()
            else:
                print("aca es")
                #return event.ignore()
        except:
            print("error")
            informe = QMessageBox('',"Error en guardado","No se pudo guardar")
            
    
    def close_Event(self,event = QCloseEvent):
        if self.plainTextEdit.toPlainText() != "":
            dialogo = QMessageBox()
            dialogo.setText("¿Quiere guardar su trabajo?")
            dialogo.addButton(QPushButton("Cancelar"),QMessageBox.RejectRole)
            dialogo.addButton(QPushButton("NO"),QMessageBox.NoRole)
            dialogo.addButton(QPushButton("SI"),QMessageBox.YesRole)
            
            respuesta = dialogo.exec()
            if respuesta == 2:
                self.Guardar()
                #self.close()
                
            elif respuesta == 0:
                event.ignore()
            elif respuesta == 1:
                self.close()
    
    def closeEvent(self, event):
        self.close_Event(event = event)

def main():
    app = QApplication([])
    window = miEditor()
    app.exec_()
    
if __name__ == '__main__':
    main()
    
