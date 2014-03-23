# Assignment1Widget.py
# (C)2013
# Scott Ernst

import nimble
import random
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget

#___________________________________________________________________________________________________ Assignment1Widget
class FinalProjectWidget(PyGlassWidget):
    """A class for Final project"""
#===================================================================================================
#                                                                                       C L A S S
    created = ''
#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment1Widget."""
        super(FinalProjectWidget, self).__init__(parent, **kwargs)
        #create

        self.Facialbtn.clicked.connect(self._Facialbtn)
        self.walkbtn.clicked.connect(self._walkHandle)
        self.standbtn.clicked.connect(self._standHandle)
        self.camerabtn.clicked.connect(self._cameraHandle)

        self.clearKeys.clicked.connect(self._clearKeys)
        self.homeBtn.clicked.connect(self._handleReturnHome)
        self.playblast.clicked.connect(self._playblast)


#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _CreateCubeButton
    def _Facialbtn(self):
        if self.normal.isChecked():
            facial = 'none'
        if self.sad.isChecked():
            facial = 'sad'
        if self.scary.isChecked():
            facial = 'Scary'
        if self.smile.isChecked():
            facial = 'smile'
        if self.laugh.isChecked():
            facial = 'laugh'
        cmds.setAttr("Mouth_Facial.none",0)
        cmds.setAttr("Mouth_Facial.sad",0)
        cmds.setAttr("Mouth_Facial.Scary",0)
        cmds.setAttr("Mouth_Facial.smile",0)
        cmds.setAttr("Mouth_Facial.laugh",0)

        cmds.setAttr("Mouth_Facial."+facial,1)
#___________________________________________________________________________________________________ _CreateSphereButton
    def _walkHandle(self):
        cmds.setKeyframe( 'Left_leg', time=0, attribute='rotateX', value=47.732 )
        cmds.setKeyframe( 'Right_leg', time=0, attribute='rotateX', value=-32.235 )
        cmds.setKeyframe( 'Right_leg', time=12, attribute='rotateX', value=47.732 )
        cmds.setKeyframe( 'Left_leg', time=12, attribute='rotateX', value=-32.235 )

#___________________________________________________________________________________________________ _CreateSphereButton
    def _standHandle(self):
        cmds.setAttr('Left_leg.rotateX', -0.883)
        cmds.setAttr('Right_leg.rotateX',-5.039)
#___________________________________________________________________________________________________ _CreateCubeButton
    def _cameraHandle(self):
        if self.Front.isChecked():
            camera = 'Front'
            attr='translateZ'
            value1=100
            value2=220

        if self.Back.isChecked():
            camera = 'Back'
            attr='translateZ'
            value1=-100
            value2=-220

        if self.Left.isChecked():
            camera = 'Left'
            attr='translateX'
            value1=100
            value2=220

        if self.Right.isChecked():
            camera = 'Right'
            attr='translateX'
            value1=-100
            value2=-220

        cmds.lookThru( camera)
        cmds.setKeyframe( camera, time=0, attribute=attr, value=value1 )
        cmds.setKeyframe( camera, time=24, attribute=attr, value=value2)

    def _clearKeys(self):
        totalTime = float(self.AnimationTime.text())*24
        cmds.select(ado=True)
        mySel = cmds.ls(sl=1)
        cmds.cutKey(mySel,clear=True)
#
    def _playblast(self):
        cmds.playblast(filename='Movie',percent = 100)

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')