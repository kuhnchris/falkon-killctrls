import Falkon
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMenu

CAPTURE_KEY = "Ctrl+S"

class KillCtrlSPlugin(Falkon.PluginInterface, QtCore.QObject):
    def init(self, state, settingsPath):
        falkonApp = Falkon.MainApplication.instance()
        plugins = falkonApp.plugins()
        plugins.mainWindowCreated.connect(self.mainWindowCreated)
        self.capturedObject = []
        if falkonApp.getWindow() != None:
            self.mainWindowCreated(falkonApp.getWindow())


    def findQTObjectShortcut(self, c) -> bool:       
        if type(c) == QtWidgets.QShortcut:
            qsc: QtWidgets.QShortcut = c
            if self.findQTObjectShortcut(qsc.key()):
                self.capturedObject.append(qsc)
                return True
        
        if type(c) == QtGui.QKeySequence:
            qks: QtGui.QKeySequence = c
            #print(qks.toString())
            if (qks.toString() == CAPTURE_KEY):
                print("We found the requested key (",CAPTURE_KEY,")!")
                self.capturedObject.append(qks)
                return True

        if type(c) == QtWidgets.QMenuBar:
            qmb: QtWidgets.QMenuBar = c
            for a_ in qmb.actions():
                if self.findQTObjectShortcut(a_):
                    self.capturedObject.append(c)
                    return True
            for c_ in qmb.children():
                if self.findQTObjectShortcut(c_):
                    self.capturedObject.append(c)
                    return True

        if type(c) == QtWidgets.QAction:
            a: QtWidgets.QAction = c      
            for c_ in a.children():
                if self.findQTObjectShortcut(c_):
                    self.capturedObject.append(a)
                    return True
            if a.menu() != None:
                if self.findQTObjectShortcut(a.menu()):
                    self.capturedObject.append(a)
                    return True
            for a_ in a.shortcuts():
                if self.findQTObjectShortcut(a_):
                    self.capturedObject.append(a)
                    return True

        if type(c) == QtWidgets.QMenu:
            qm: QtWidgets.QMenu = c
            for a_ in qm.actions():
                if self.findQTObjectShortcut(a_):
                    self.capturedObject.append(c)
                    return True
            

    def mainWindowCreated(self, window):
        for c in window.children():
            if self.findQTObjectShortcut(c):
                print("Found the object in following path:",self.capturedObject)
                print("proceeding to eliminate key...")
                self.capturedObject.pop(0)
                offendingAction: QtWidgets.QAction = self.capturedObject[0]
                offendingAction.setShortcut(QtGui.QKeySequence())
                print("the offender should be neutralized.")
                
    def unload(self):   
        print("Plugin unloaded. G'bye")

    def testPlugin(self):
        return True
    
    

Falkon.registerPlugin(KillCtrlSPlugin())
