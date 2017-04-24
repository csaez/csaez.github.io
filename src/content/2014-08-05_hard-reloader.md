Title: Hard Reloader for Maya
Author: Cesar Saez
Tags: code, tools

Hi folks,

Do you remember [this handy trick to quickly reload a python package](http://cesarsaez.me/2013/10/hard_reload.html)?

Well, __I use it all the time!__ so I made this little GUI helper. It's
really simple, but makes my life much easier when it comes to test WIP
code within Maya.

![HardReloader for Maya]({filename}images/hard_reloader.gif "HardReloader for Maya")

### Installation:

Save the code below as `hard_reloader.py` into your Maya script directory
(or somewhere else in your PYTHONPATH).

    :::python
    import sys
    from PySide import QtGui, QtCore
    from shiboken import wrapInstance
    from maya import OpenMayaUI


    class HardReloader(QtGui.QDialog):

        def __init__(self, *args, **kwds):
            super(HardReloader, self).__init__(*args, **kwds)
            self.setWindowTitle(type(self).__name__)
            self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
            self.initUI()

        def initUI(self):
            self.ui_lineEdit = QtGui.QLineEdit(self)
            ui_completer = QtGui.QCompleter(
                [i.split(".")[0] for i in sys.modules.keys()], self)
            ui_completer.setCompletionMode(QtGui.QCompleter.InlineCompletion)
            ui_completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
            self.ui_lineEdit.setCompleter(ui_completer)
            hbox = QtGui.QHBoxLayout()
            hbox.addWidget(self.ui_lineEdit)
            self.setLayout(hbox)
            self.ui_lineEdit.returnPressed.connect(self.accept)

        def accept(self):
            module = self.ui_lineEdit.text().lower()
            if len(module):
                for k in sys.modules.keys():
                    if k.lower().startswith(module):
                        del sys.modules[k]
            self.close()


    def get_parent():
        ptr = OpenMayaUI.MQtUtil.mainWindow()
        return wrapInstance(long(ptr), QtGui.QMainWindow)


    def show():
        HardReloader(get_parent()).exec_()



> As you can see, hard_reloader has a dependency on PySide (shipped with
> Maya >= 2014). If PySide is not your favourite flavor, you can easily switch
> imports to PyQt (`PySide`->`PyQt4` and `shiboken`->`sip`).



### Ussage:

Just import it and call its `show` function (put this in a shelf or assign a hotkey).

    :::python
    import hard_reloader
    hard_reloader.show()


That's it, happy coding! ;-)
