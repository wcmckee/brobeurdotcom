<html><body><p>I need to work with classes and functions more. 


[prettify=python]

import maya.cmds as cmds



class CreateCube(Cube):
    def cubaNow(self):
        cmds.polyCube
        
x = CreateCube()

x.cubaNow()
        
# Error: line 1: NameError: file <maya console> line 3: name 'Cube' is not defined # 

import maya.cmds as cmds



class CreateCube(object):
    def cubaNow(self):
        cmds.polyCube
        
x = CreateCube()

x.cubaNow()
        
x.cubaNow()

cmds.polyCube

# Result: <built-in method polycube of module object at> # 

cmds.polyCube()

# Result: [u'pCube1', u'polyCube1'] # 

class CreateCube(object):
    def cubaNow(self):
        cmds.polyCube()
        
x = CreateCube()

x.cubaNow()

x.cubaNow()

class CreateCube(object):
    def cubaNow(self):
        cmds.polyCube(n='myCube')
        cmds.select('myCube')
        
        
x = CreateCube()

x.cubaNow()

cmds.move(0,5,0)

cmds.polyCreateFacet()

# Error: line 1: RuntimeError: file <maya console> line 1: Not enough points : minimum 3. # 

cmds.split()

# Error: line 1: AttributeError: file <maya console> line 1: 'module' object has no attribute 'split' # 

cmds.scale(3,0,0)

cmds.scale(1, 3, 1)

import random 

ranNumz = random.randint(2,6)

ranHamz = ranNumz / 2

class CreateCube(object):
    def cubaNow(self):
        cmds.polyCube(n='willCube')
        cmds.select(n='willCube')
        cmds.scale(ranNumz, ranHamz, ranHamz)
        
x = CreateCube()

x.cubaNow()

# Error: line 1: TypeError: file <maya console> line 7: Invalid flag 'n' # 

import random 

ranNumz = random.randint(2,6)

ranHamz = ranNumz / 2

class CreateCube(object):
    def cubaNow(self):
        cmds.polyCube()
        cmds.select()
        cmds.scale(ranNumz, ranHamz, ranHamz)
        
x = CreateCube()

x.cubaNow()

import random 

ranNumz = random.randint(2,6)

ranHamz = ranNumz / 2

class CreateCube(object):
    def cubaNow(self):
        cmds.polyCube()
        cmds.scale(ranNumz, ranHamz, ranHamz)
        
x = CreateCube()

x.cubaNow()

import random 

ranNumz = random.randint(2,6)

ranHamz = ranNumz / 2

class CreateCube(object):
    def cubaNow(self):
        cmds.polyCube()
        cmds.scale(ranNumz, ranHamz, ranHamz)
        
x = CreateCube()

x.cubaNow()

import random 

ranNumz = random.randint(2,6)

ranHamz = ranNumz / 2

class CreateCube(object):
    def cubaNow(self):
        cmds.polyCube()
        cmds.scale(ranNumz, ranHamz, ranHamz)
        cmds.polySplit(ip=[(2, 0.1, 3, 0.5, (0, 2, -1, 0.0),
        (0, 0.9)])
x = CreateCube()

x.cubaNow()

# Error: line 1: invalid syntax # 

import random 

ranNumz = random.randint(2,6)

ranHamz = ranNumz / 2

class CreateCube(object):
    def cubaNow(self):
        cmds.polyCube()
        cmds.scale(ranNumz, ranHamz, ranHamz)
        cmds.polySplit()
x = CreateCube()

x.cubaNow()

# Error: line 1: RuntimeError: file <maya console> line 8: Need at least one "-ep" or "-ip" flag (edge split point). # 

import random 

ranNumz = random.randint(2,6)

ranHamz = ranNumz / 2

class CreateCube(object):
    def cubaNow(self):
        cmds.polyCube()
        cmds.scale(ranNumz, ranHamz, ranHamz)
        cmds.polySplit( ip=[(2, 0.1), (3, 0.5), (0, 2, -1, 0.0), (0, 0.9)] )
x = CreateCube()

x.cubaNow()

# Warning: Can't perform polySplit1 on selection # 

for i in range (10):
    lisx.append(random.randrange(1,101,1))
print lisx

# Error: line 1: NameError: file <maya console> line 2: name 'lisx' is not defined # 

lisx = []



for i in range (10):
    lisx.append(random.randrange(1,101,1))
print lisx

[9, 19, 84, 84, 19, 52, 50, 63, 86, 17]

cmds.polySplitRing(sma=180, wt=0.2)

# Warning: Can't perform polySplitRing1 on selection # 

# Result: [u'polySplitRing1'] # 

cmds.polySplitRing(sma=180, wt=0.6)

# Warning: Can't perform polySplitRing2 on selection # 

# Result: [u'polySplitRing2'] # 

cmds.polyCut()

# Result: [u'polyCut1'] # 

cmds.polyCut([5:20], cd=Y, df=1, ch=1)

# Error: line 1: invalid syntax # 

cmds.polyCut(cd=Y, df=1, ch=1)

# Error: line 1: NameError: file <maya console> line 1: name 'Y' is not defined # 

cmds.polyCut(cd='Y', df=1, ch=1)

# Result: [u'polyCut2'] # 

cmds.polyTriangulate()

# Result: [u'polyTriangulate1'] # 

cmds.polyChipOff()

# Result: [u'polyChipOff1'] # 

cmds.polyDuplicateAndConnect()

# Error: line 1: RuntimeError: file <maya console> line 1: duplicate  pCube8.f[*] ;

Line 1.21: Syntax error

duplicate  pCube8.f[*] ;

Line 1.21: Syntax error

duplicate  pCube8.f[*] ;

Line 1.21: Syntax error

duplicate  pCube8.f[*] ;

Line 1.21: Syntax error

duplicate  pCube8.f[*] ;

Line 1.21: Syntax error

duplicate  pCube8.f[*] ;

Line 1.21: Syntax error

duplicate  pCube8.f[*] ;

Line 1.21: Syntax error

duplicate  pCube8.f[*] ;

Line 1.21: Syntax error # 

cmds.polyDuplicateAndConnect()

# Result: [u'pCube9'] # 

cmds.move(1,0,0)

cmds.polyDuplicateEdge(e[0,10], of=0.8)



# Error: line 1: NameError: file <maya console> line 1: name 'e' is not defined # 

cmds.polyDuplicateEdge()



# Result: [u'polyDuplicateEdge1'] # 

cmds.polyExtrudeFacet(kft=False, ltz=.3, ls=(.2, .2, 0) )

# Result: [u'polyExtrudeFace1'] # 

cmds.polyExtrudeFacet(kft=False, ltz=.3, ls=(0, 0, 0) )

# Result: [u'polyExtrudeFace1'] # 

cmds.polyExtrudeFacet(kft=False, ltz=5, ls=(.2, .2, 0) )

# Result: [u'polyExtrudeFace1'] # 

cmds.polyExtrudeFacet(kft=False, ltz=.3, ls=(0, .2, 0) )

# Result: [u'polyExtrudeFace1'] # 

cmds.polyExtrudeFacet(kft=False, ltz=.3, ls=(.2, .2, 0) )

# Result: [u'polyExtrudeFace2'] # 

cmds.polyExtrudeFacet(kft=True, ltz=.3, ls=(.2, .2, 0) )

# Result: [u'polyExtrudeFace2'] # 

cmds.polyExtrudeFacet(kft=False, z=.3, ls=(.2, .2, 0) )

# Error: line 1: TypeError: file <maya console> line 1: Invalid flag 'z' # 

cmds.polyExtrudeFacet(kft=False, ltz=.3, ls=(.02, .02, 0) )

# Result: [u'polyExtrudeFace2'] # 

import random 

ranNumz = random.randint(2,6)

ranHamz = ranNumz / 2

class CreateCube(object):
    def cubaNow(self):
        cmds.polyCube()
        cmds.select()
        cmds.scale(ranNumz, ranHamz, ranHamz)
        cmds.polyExtrudeFacet(kft=False, ltz=.3, ls=(.2, .2, 0) )
        
x = CreateCube()

x.cubaNow()



import random 

ranNumz = random.randint(2,6)

ranHamz = ranNumz / 2

class CreateCube(object):
    def cubaNow(self):
        cmds.polyCube()
        cmds.select()
        cmds.scale(ranNumz, ranHamz, ranHamz)
        cmds.polyExtrudeFacet(kft=False, ltz=.3, ls=(.2, .2, 0) )
        cmds.polySelect(edgeBorder=[0,3])
        
x = CreateCube()

x.cubaNow()

import random 

ranNumz = random.randint(2,6)

ranHamz = ranNumz / 2

class CreateCube(object):
    def cubaNow(self):
        cmds.polyCube()
        cmds.select()
        cmds.scale(ranNumz, ranHamz, ranHamz)
        cmds.polyExtrudeFacet(kft=False, ltz=.3, ls=(1, 1, 0) )
        cmds.polySelect(edgeBorder=[0,3])
        
x = CreateCube()

x.cubaNow()

import random 

ranNumz = random.randint(2,6)

ranHamz = ranNumz / 2

class CreateCube(object):
    def cubaNow(self):
        cmds.polyCube()
        cmds.select()
        cmds.scale(ranNumz, ranHamz, ranHamz)
        cmds.polyExtrudeFacet(kft=False, ltz=.3, ls=(ranHamz, .2, 0) )
        
x = CreateCube()

x.cubaNow()

cameraName = cmds.camera()



cameraShape = cameraName[1]

focalLength = cmds.camera(cameraShape, q=True, fl=True)

focalLength = cmds.camera(cameraShape, q=False, fl=True)



# Error: line 1: RuntimeError: file <maya console> line 1: Too many objects or values. # 

focalLength = cmds.camera(cameraShape, q=True, fl=True)



cmds.camera(cameraShape, rotation =[90,0,0])

# Error: line 1: RuntimeError: file <maya console> line 1: Too many objects or values. # 

cmds.camera(cameraShape, rotation =[90,0,0])

# Error: line 1: RuntimeError: file <maya console> line 1: Too many objects or values. # 

cmds.camera(cameraShape, rotation=90,0,0)

# Error: line 1: non-keyword arg after keyword arg # 

cmds.camera(cameraShape, rotation=90)



# Error: line 1: TypeError: file <maya console> line 1: Invalid arguments for flag 'rotation'.  Expected ( angle, angle, angle ), got int # 

cmds.camera(shutterAngle=90)

# Result: [u'camera2', u'cameraShape2'] # 

cmds.camera(shutterAngle=180)

# Result: [u'camera3', u'cameraShape3'] # 

cmds.polyMirrorFace( 'poly1', direction=0, mergeMode=1 )



# Error: line 1: ValueError: file <maya console> line 1: No object matches name: poly1 # 

cmds.polyMirrorFace()



# Result: [u'polyMirror1'] # 

cmds.select(f[4])

# Error: line 1: NameError: file <maya console> line 1: name 'f' is not defined # 

cmds.rotate( 0, 0, 45, r=True, os=True )



cmds.rotate( 0, 0, 180, 'poly2', r=True, os=True )



# Error: line 1: ValueError: file <maya console> line 1: No object matches name: poly2 # 

cmds.rotate( 0, 0, 180, r=True, os=True )



cmds.rotate( 0, 0, 180, r=True, os=True )

[/prettify]

</maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></maya></built-in></maya></p></body></html>