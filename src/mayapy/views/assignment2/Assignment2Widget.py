# Assignment2Widget.py
# (C)2013
# Scott Ernst

import nimble
from nimble import cmds
import random
from pyglass.widgets.PyGlassWidget import PyGlassWidget

#___________________________________________________________________________________________________ Assignment2Widget
class Assignment2Widget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment2Widget."""
        super(Assignment2Widget, self).__init__(parent, **kwargs)
        self.waterButton.clicked.connect(self._handleExampleButton)
        self.homeBtn.clicked.connect(self._handleReturnHome)

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleExampleButton(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.

        """

        random.seed(1234)

        #check
        sphereList = cmds.ls('hydrogen1','hydrogen2', 'oxygen','H2O')

        if len(sphereList)>0:
            cmds.delete(sphereList)

        #create 2 hydrogen and oxygen
        h1 = cmds.polySphere(r=12.0, name='hydrogen1')
        h2 = cmds.polySphere(r=12.0, name='hydrogen2')
        oxygen = cmds.polySphere(r=15.0, name='oxygen')


        #move
        cmds.move(-15,0,0,h1)
        cmds.move(15,0,0,h2)
        cmds.xform(h1, piv=[0,0,0],ws=True)
        cmds.xform(h2, piv=[0,0,0],ws=True)
        cmds.rotate(0,'75',0,h1)

        #group hydrogen and oxygen together
        H2O = cmds.group(empty=True, name='H2O#')
        cmds.parent('hydrogen1','hydrogen2','oxygen','H2O1')

        #add color
        def createMaterial( name, color, type ):
            cmds.sets( renderable=True, noSurfaceShader=True, empty=True, name=name + 'SG' )
            cmds.shadingNode( type, asShader=True, name=name )
            cmds.setAttr( name+'.color', color[0], color[1], color[2], type='double3')
            cmds.connectAttr(name+'.outColor', name+'SG.surfaceShader')

        def assignMaterial (name, object):
            cmds.sets(object, edit=True, forceElement=name+'SG')

        def assignNewMaterial( name, color, type, object):
            createMaterial (name, color, type)
            assignMaterial (name, object)

        #H is white and O is red
        assignNewMaterial('Red', (1,0,0), 'lambert', 'oxygen');
        assignNewMaterial('White',(1,1,1),'lambert', 'hydrogen1');
        assignMaterial('White', 'hydrogen2');

        #key frame
        def keyFullRotation( pObjectName, pStartTime, pEndTime, pTargetAttribute,pValueStart, pvalueEnd ):
            keyt = (pStartTime[0], pStartTime[0])
            cmds.cutKey( pObjectName, time=(keyt, keyt), attribute=pTargetAttribute )
            cmds.setKeyframe( pObjectName, time=pStartTime, attribute=pTargetAttribute, value=pValueStart )
            cmds.setKeyframe( pObjectName, time=pEndTime, attribute=pTargetAttribute, value=pvalueEnd )
            #cmds.selectKey( pObjectName, time=(pStartTime, [pEndTime]), attribute=pTargetAttribute, keyframe=True )

        #duplicate H2O
        for i in range(1,52):
            cmds.duplicate(H2O)
            #get random coord
            x = random.uniform(-200,200)
            y = random.uniform(0,300)
            z = random.uniform(-200,200)

            cmds.move(x,y,z, H2O)


            xRot = random.uniform(0,360)
            yRot = random.uniform(0,360)
            zRot = random.uniform(0,360)

            cmds.rotate(xRot,yRot,zRot,H2O)

            startTime = cmds.playbackOptions(minTime=1 )
            endTime = cmds.playbackOptions( maxTime=30 )

            h2o = "H2O"+str(i)

            for y in range(3):
                coordsX = cmds.getAttr( h2o+'.translateX' )
                coordsY = cmds.getAttr( h2o+'.translateY' )
                coordsZ = cmds.getAttr( h2o+'.translateZ' )

                ranStartX = int(random.uniform(0,15))
                ranStartY = int(random.uniform(0,15))
                ranStartZ = int(random.uniform(0,15))

                ranEndX = int(random.uniform(15,30))
                ranEndY = int(random.uniform(15,30))
                ranEndZ = int(random.uniform(15,30))

                x = random.uniform(coordsX-50,coordsX+50)
                y = random.uniform(coordsY,coordsY+50)
                z = random.uniform(coordsZ-50,coordsZ+50)
                #print x,y,z

                keyFullRotation( h2o, ranStartZ, 15, 'translateZ',coordsZ,z)
                keyFullRotation( h2o, ranStartX, 15, 'translateX', coordsX,x)
                keyFullRotation( h2o, ranStartY, 15, 'translateY', coordsY,y)

                keyFullRotation( h2o, 15, ranEndZ, 'translateZ',z,coordsZ)
                keyFullRotation( h2o, 15, ranEndX, 'translateX', x,coordsX)
                keyFullRotation( h2o, 15, ranEndY, 'translateY', y,coordsY)

                RcoordsX = cmds.getAttr( h2o+'.rotateX' )
                RcoordsY = cmds.getAttr( h2o+'.rotateY' )
                RcoordsZ = cmds.getAttr( h2o+'.rotateZ' )

                xRot = random.uniform(0,360)
                yRot = random.uniform(0,360)
                zRot = random.uniform(0,360)

                keyFullRotation( h2o, ranStartZ, 15, 'rotateZ',RcoordsZ,zRot)
                keyFullRotation( h2o, ranStartX, 15, 'rotateX', RcoordsX,xRot)
                keyFullRotation( h2o, ranStartY, 15, 'rotateY', RcoordsY,zRot)

                keyFullRotation( h2o, 15, ranEndZ, 'rotateZ',zRot,RcoordsZ)
                keyFullRotation( h2o, 15, ranEndX, 'rotateX', xRot,RcoordsX)
                keyFullRotation( h2o, 15, ranEndY, 'rotateY', zRot,RcoordsY)

        print 'done'
        cmds.delete('H2O52')
#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')

