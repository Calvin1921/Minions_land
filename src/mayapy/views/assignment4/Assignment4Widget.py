# Assignment1Widget.py
# (C)2013
# Scott Ernst

import nimble
import random
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget

#___________________________________________________________________________________________________ Assignment1Widget
class Assignment4Widget(PyGlassWidget):
    """A class for Assignment 4"""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment1Widget."""
        super(Assignment4Widget, self).__init__(parent, **kwargs)
        self.cubeButton.clicked.connect(self._CreateCubeButton)
        self.homeBtn.clicked.connect(self._handleReturnHome)
        self.perturbButton.clicked.connect(self._perturbButton)
        self.sphereButton.clicked.connect(self._CreateSphereButton)

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _CreateCubeButton
    def _CreateCubeButton(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.

        """
        cube = cmds.polyCube(w=50,h=50,d=50,name="cube1")
        cmds.select(cube)
        response = nimble.createRemoteResponse(globals())
        response.put('name', cube)
#___________________________________________________________________________________________________ _CreateSphereButton
    def _CreateSphereButton(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.

        """
        sphere = cmds.polySphere(r=50.0, name='sphere1')
        cmds.select(sphere)
        response = nimble.createRemoteResponse(globals())
        response.put('name', sphere)
#___________________________________________________________________________________________________ _perturbButton
    def _perturbButton(self):
        def MoveVertex(min, max):
            cmds.select(ado=True)
            selected = cmds.ls(selection=True, long=True)

            for object in selected:
                total = cmds.polyEvaluate(object, vertex=True)
                for i in range(total):

                    randNumX = random.uniform(min, max)
                    randNumY = random.uniform(min, max)
                    randNumZ = random.uniform(min, max)
                    vertex = object+'.vtx['+str(i)+']'
                    cmds.select(vertex)
                    cmds.move(randNumX, randNumY, randNumZ, relative=True)

        max = float(self.positiveText.text())
        min = float(self.nagativeText.text())
        MoveVertex(min, max)

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
