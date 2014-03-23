# Assignment1Widget.py
# (C)2013
# Scott Ernst

import nimble
import random
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget

#___________________________________________________________________________________________________ Assignment1Widget
class Assignment5Widget(PyGlassWidget):
    """A class for Assignment 5"""
#===================================================================================================
#                                                                                       C L A S S
    created = ''
#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment1Widget."""
        super(Assignment5Widget, self).__init__(parent, **kwargs)
        #create

        self.cubeButton.clicked.connect(self._CreateCubeButton)
        self.sphereButton.clicked.connect(self._CreateSphereButton)
        #apply
        self.addButton.clicked.connect(self._addButton)
        self.applyButton.clicked.connect(self._applyButton)
        self.clearKeys.clicked.connect(self._clearKeys)
        self.homeBtn.clicked.connect(self._handleReturnHome)
        self.playblast.clicked.connect(self._playblast)


#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _CreateCubeButton
    def _CreateCubeButton(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.

        """
        cube = cmds.polyCube(w=20,h=20,d=20,name="cube1")
        cmds.duplicate('cube1')
        response = nimble.createRemoteResponse(globals())
        response.put('name', cube)
        global created
        created = 'cube'
#___________________________________________________________________________________________________ _CreateSphereButton
    def _CreateSphereButton(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.

        """
        sphere = cmds.polySphere(r=20, name="sphere1")
        cmds.duplicate('sphere1')
        response = nimble.createRemoteResponse(globals())
        response.put('name', sphere)
        global created
        created = 'sphere'
#___________________________________________________________________________________________________ _addButton
    def _addButton(self):
        type = self._checkType()
        print type
        cmds.select(created+'1', type+'1Handle')
        cmds.createDisplayLayer(nr=True, name='layer1')
        cmds.setAttr('layer1.visibility', 0 )
#___________________________________________________________________________________________________ _handleReturnHome
    def _applyButton(self):
        totalTime = float(self.AnimationTime.text())*24
        endTime = cmds.playbackOptions( maxTime=totalTime )
        #translateX = float(self.FromXValue.text())
        translateY = float(self.FromYValue.text())
        #translateZ = float(self.FromZValue.text())

        #toTranslateX = float(self.ToXValue.text())
        toTranslateY = float(self.ToYValue.text())
        #toTranslateZ = float(self.ToZValue.text())

        #if translateX=='' or translateY=='' or translateZ=='' or toTranslateX=='' or toTranslateY=='' or toTranslateZ=='':

        cmds.setKeyframe( created+'1', time=0, attribute='translateY', value=translateY )
        cmds.setKeyframe( created+'2', time=0, attribute='translateY', value=-translateY )

        cmds.setKeyframe( created+'1', time=totalTime, attribute='translateY', value=toTranslateY )
        cmds.setKeyframe( created+'2', time=totalTime, attribute='translateY', value=toTranslateY )

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
#
    def _checkType(self):
        highBound = float(self.HightBound.text())
        lowBound = float(self.LowBound.text())
        curvature = float(self.Curvature.text())
        factor =  float(self.Factor.text())
        cmds.select(created+'2')
        if self.BendRadioButton.isChecked():
            type= 'bend'
            cmds.nonLinear( type='bend', highBound=highBound, lowBound=lowBound, curvature=curvature)
        if self.SquashRadioButton.isChecked():
            type = 'squash'
            cmds.nonLinear( type='squash', highBound=highBound, lowBound=lowBound, factor=factor)
        print type
        return   type
#
    def _clearKeys(self):
        totalTime = float(self.AnimationTime.text())*24
        cmds.select(ado=True)
        mySel = cmds.ls(sl=1)
        cmds.cutKey(mySel,clear=True)
#
    def _playblast(self):
        cmds.playblast(filename='Movie',percent = 100)