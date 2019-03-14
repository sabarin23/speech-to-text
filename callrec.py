import sys
import os
import ctypes
import win32process
import speech_recognition as sr
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox)

from rec import Ui_Recorder



class MainWindow(QMainWindow, Ui_Recorder):
    # Maintain the list of browser windows so that they do not get garbage
    # collected.
    _window_list = []

    def __init__(self):
        super(MainWindow, self).__init__()

        MainWindow._window_list.append(self)

        self.setupUi(self)

        self.pushButton.clicked.connect(self.processrecord)

        self.pushButton_2.clicked.connect(self.processcopy)

        self.pushButton_3.clicked.connect(self.processclear)

    def processrecord(self):

        global TEXT, TEXT1
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Say something... ")
            #self.pushButton.setStyleSheet("background-color: red");
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            TEXT = r.recognize_google(audio, language='ta-IN')
            TEXT1 = self.textEdit.toPlainText()
            self.textEdit.setText(TEXT1+" "+TEXT)
            print(TEXT)
            #print("TEXT: " + r.recognize_google(audio, language='ta-IN'))

        except sr.UnknownValueError:
            print("Couldn't understand")

        except sr.RequestError as e:
            print("Couldn't request results; {}".format(e))


    def processcopy(self):
        self.textEdit.selectAll()
        self.textEdit.copy()

    def processclear(self):
        self.textEdit.clear()


hwnd = ctypes.windll.kernel32.GetConsoleWindow()
if hwnd != 0:
    ctypes.windll.user32.ShowWindow(hwnd, 0)
    ctypes.windll.kernel32.CloseHandle(hwnd)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    os.system('taskkill /PID ' + str(pid) + ' /f')

if __name__ == "__main__":
    a = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(a.exec_())