# MayaPyMainWindow.py
# (C)2013
# Scott Ernst

from PySide import QtGui

from pyglass.windows.PyGlassWindow import PyGlassWindow

from mayapy.views.home.MayaPyHomeWidget import MayaPyHomeWidget
from mayapy.views.assignment1.Assignment1Widget import Assignment1Widget
from mayapy.views.assignment2.Assignment2Widget import Assignment2Widget
from mayapy.views.assignment4.Assignment4Widget import Assignment4Widget
from mayapy.views.assignment5.Assignment5Widget import Assignment5Widget
from mayapy.views.FinalProject.FinalProjectWidget import FinalProjectWidget


#___________________________________________________________________________________________________ MayaPyMainWindow
class MayaPyMainWindow(PyGlassWindow):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, **kwargs):
        PyGlassWindow.__init__(
            self,
            widgets={
                'home':MayaPyHomeWidget,
                'assignment1':Assignment1Widget,
                'assignment2':Assignment2Widget,
                'assignment4':Assignment4Widget,
                'assignment5':Assignment5Widget,
                'FinalProject':FinalProjectWidget},
            title='MayaPy',
            **kwargs )

        self.setMinimumSize(1024,480)
        self.setContentsMargins(0, 0, 0, 0)

        widget = self._createCentralWidget()
        layout = QtGui.QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        widget.setLayout(layout)

        self.setActiveWidget('home')
