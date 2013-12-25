# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

#----------------------------------------------------------
# File: room_maker.py
# Automatic generation of rooms
# Author: Antonio Vazquez (antonioya)
#
#----------------------------------------------------------
import bpy
import math
from tools import *

#------------------------------------------------------------------------------
# Generate mesh data
# All custom values are passed using self container (self.myvariable)
#------------------------------------------------------------------------------
def create_mesh(self,context):
    # deactivate others
    for o in bpy.data.objects:
        if (o.select == True):
            o.select = False
    bpy.ops.object.select_all(False)
    # Create room
    myRoom = create_room(self,context,"Room",get_BlendUnits(self.room_height))
    myRoom.select = True
    bpy.context.scene.objects.active = myRoom
    # Mark Seams
    select_vertices(myRoom,[0,1])   
    mark_seam(myRoom) 
    # Unwrap
    unwrap_mesh(myRoom)
    
    remove_doubles(myRoom)
    set_normals(myRoom,not self.inverse) # inside/outside

    if (self.wall_width > 0.0):
        set_modifier_solidify(myRoom,get_BlendUnits(self.wall_width))
        
    # Create baseboard
    if (self.baseboard):
        myBase = create_room(self,context,"Baseboard",get_BlendUnits(self.base_height),True)
        set_normals(myBase,self.inverse) # inside/outside room
        if (self.base_width > 0.0):
            set_modifier_solidify(myBase,get_BlendUnits(self.base_width))
        myBase.parent = myRoom    
        # Mark Seams
        select_vertices(myBase,[0,1])   
        mark_seam(myBase) 
        # Unwrap
        unwrap_mesh(myBase)
        
    # Create floor
    if (self.floor):
        myFloor = create_floor(self,context,"Floor",myRoom)
        myFloor.parent = myRoom    
        # Unwrap
        unwrap_mesh(myFloor)

    # Create ceiling
    if (self.ceiling):
        myCeiling = create_floor(self,context,"Ceiling",myRoom)
        myCeiling.parent = myRoom    
        # Unwrap
        unwrap_mesh(myCeiling)

    # Create materials        
    if (self.crt_mat):
        # Wall material (two faces)
        mat = create_diffuse_material("Wall_material",False,0.765, 0.650, 0.588,0.8,0.621,0.570,0.1,True)
        set_material(myRoom,mat)
        # Baseboard material
        if (self.baseboard):
            mat = create_diffuse_material("Baseboard_material",False,0.8, 0.8, 0.8)
            set_material(myBase,mat)
        
        # Ceiling material
        if (self.ceiling):
            mat = create_diffuse_material("Ceiling_material",False,0.95, 0.95, 0.95)
            set_material(myCeiling,mat)
            
        # Floor material    
        if (self.floor):
            mat = create_brick_material("Floor_material",False,0.711, 0.668, 0.668,0.8,0.636,0.315)
            set_material(myFloor,mat)
          
    bpy.ops.object.select_all(False)    
    myRoom.select = True
    bpy.context.scene.objects.active = myRoom
            
    return
#------------------------------------------------------------------------------
# Verify visibility of walls
#------------------------------------------------------------------------------
def check_visibility(h,base):
    # Visible
    if (h == '0'):
        return True
    # Wall
    if (h == '2'):
        if (base == True):
            return False
        else:
            return True
    # Baseboard
    if (h == '1'):
        if (base == True):
            return True
        else:
            return False
    # Hidden
    if (h == '3'):
        return False

#------------------------------------------------------------------------------
# Create Room/baseboard
# Some custom values are passed using self container (self.myvariable)
#------------------------------------------------------------------------------
def create_room(self,context,objName,height,baseboard = False):

    myVertex = []
    myFaces = []
    lastFace = 0
    #---------------------------------
    # Horizontal (First)
    #---------------------------------
    if (self.wall_num >= 1):
        # Calculate size using angle
        sizeX = math.cos(math.radians(self.r01)) * get_BlendUnits(self.w01)
        sizeY = math.sin(math.radians(self.r01)) * get_BlendUnits(self.w01)

        if (self.a01 == False or baseboard == True):
            myVertex.extend([(0.0,0.0,0.0),(0.0,0.0,height)
                             ,(sizeX,sizeY,height)
                             ,(sizeX,sizeY,0.0)])
            if (check_visibility(self.h01,baseboard)):
                myFaces.extend([(0,1,2,3)])
            lastFace = 2
            lastX = sizeX
            lastY = sizeY
        else:
            mid = get_BlendUnits(self.w01 / 2 + ((self.w01 / 2) * self.f01))
            midX = math.cos(math.radians(self.r01)) * mid
            midY = math.sin(math.radians(self.r01)) * mid
            
            # first
            myVertex.extend([(0.0,0.0,0.0)
                             ,(0.0,0.0,height)
                             ,(midX,midY,height + get_BlendUnits(self.m01))
                             ,(midX,midY,0.0)])
            if (math.fabs(self.f01) != 1):
                if (check_visibility(self.h01,baseboard)):
                    myFaces.extend([(0,1,2,3)])  
            # second
            myVertex.extend([(sizeX,sizeY,0.0),(sizeX,sizeY,height)])
            if (check_visibility(self.h01,baseboard)):
                if (math.fabs(self.f01) != 1): 
                    myFaces.extend([(2,3,4,5)])
                else:    
                    myFaces.extend([(0,1,5,4),(1,2,5)])
            
            lastFace = 4
                
            lastX = sizeX
            lastY = sizeY
        
    #---------------------------------
    # Vertical
    #---------------------------------
    if (self.wall_num >= 2):
        myDat = make_wall(self.a01,
                              self.a02,self.w02,self.m02,self.f02
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r02,self.h02)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]
        
    # Horizontal
    if (self.wall_num >= 3):
        myDat = make_wall(self.a02,
                              self.a03,self.w03,self.m03,self.f03
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r03,self.h03)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]
        
    # Vertical
    if (self.wall_num >= 4):
        myDat = make_wall(self.a03,
                              self.a04,self.w04,self.m04,self.f04
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r04,self.h04)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]
        
    # Horizontal
    if (self.wall_num >= 5):
        myDat = make_wall(self.a04,
                              self.a05,self.w05,self.m05,self.f05
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r05,self.h05)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]
        
    # Vertical
    if (self.wall_num >= 6):
        myDat = make_wall(self.a05,
                              self.a06,self.w06,self.m06,self.f06
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r06,self.h06)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]

    # Horizontal
    if (self.wall_num >= 7):
        myDat = make_wall(self.a06,
                              self.a07,self.w07,self.m07,self.f07
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r07,self.h07)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]
        
    # Vertical
    if (self.wall_num >= 8):
        myDat = make_wall(self.a07,
                              self.a08,self.w08,self.m08,self.f08
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r08,self.h08)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]

    # Horizontal
    if (self.wall_num >= 9):
        myDat = make_wall(self.a08,
                              self.a09,self.w09,self.m09,self.f09
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r09,self.h09)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]
        
    # Vertical
    if (self.wall_num >= 10):
        myDat = make_wall(self.a09,
                              self.a10,self.w10,self.m10,self.f10
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r10,self.h10)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]

    # Horizontal
    if (self.wall_num >= 11):
        myDat = make_wall(self.a10,
                              self.a11,self.w11,self.m11,self.f11
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r11,self.h11)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]
        
    # Vertical
    if (self.wall_num >= 12):
        myDat = make_wall(self.a11,
                              self.a12,self.w12,self.m12,self.f12
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r12,self.h12)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]

    # Horizontal
    if (self.wall_num >= 13):
        myDat = make_wall(self.a12,
                              self.a13,self.w13,self.m13,self.f13
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r13,self.h13)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]
        
    # Vertical
    if (self.wall_num >= 14):
        myDat = make_wall(self.a13,
                              self.a14,self.w14,self.m14,self.f14
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r14,self.h14)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]

    # Horizontal
    if (self.wall_num >= 15):
        myDat = make_wall(self.a14,
                              self.a15,self.w15,self.m15,self.f15
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r15,self.h15)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]
        
    # Vertical
    if (self.wall_num >= 16):
        myDat = make_wall(self.a15,
                              self.a16,self.w16,self.m16,self.f16
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r16,self.h16)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]

    # Horizontal
    if (self.wall_num >= 17):
        myDat = make_wall(self.a16,
                              self.a17,self.w17,self.m17,self.f17
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r17,self.h17)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]
        
    # Vertical
    if (self.wall_num >= 18):
        myDat = make_wall(self.a17,
                              self.a18,self.w18,self.m18,self.f18
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r18,self.h18)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]

    # Horizontal
    if (self.wall_num >= 19):
        myDat = make_wall(self.a18,
                              self.a19,self.w19,self.m19,self.f19
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r19,self.h19)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]

    # Vertical
    if (self.wall_num >= 20):
        myDat = make_wall(self.a19,
                              self.a20,self.w20,self.m20,self.f20
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r20,self.h20)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]

    # Horizontal
    if (self.wall_num >= 21):
        myDat = make_wall(self.a20,
                              self.a21,self.w21,self.m21,self.f21
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r21,self.h21)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]

    # Vertical
    if (self.wall_num >= 22):
        myDat = make_wall(self.a21,
                              self.a22,self.w22,self.m22,self.f22
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r22,self.h22)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]

    # Horizontal
    if (self.wall_num >= 23):
        myDat = make_wall(self.a22,
                              self.a23,self.w23,self.m23,self.f23
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r23,self.h23)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]

    # Vertical
    if (self.wall_num >= 24):
        myDat = make_wall(self.a23,
                              self.a24,self.w24,self.m24,self.f24
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r24,self.h24)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]

    # Horizontal
    if (self.wall_num >= 25):
        myDat = make_wall(self.a24,
                              self.a25,self.w25,self.m25,self.f25
                              ,baseboard,lastFace
                              ,lastX,lastY,height,myVertex,myFaces,self.r25,self.h25)
        lastX = myDat[0]
        lastY = myDat[1]
        lastFace = myDat[2]
        
    # Close room
    if (self.merge == True):
        if (baseboard == False):     
            if ((self.wall_num == 1 and self.a01 == True)
            or (self.wall_num == 2 and self.a02 == True)
            or (self.wall_num == 3 and self.a03 == True)
            or (self.wall_num == 4 and self.a04 == True)
            or (self.wall_num == 5 and self.a05 == True)
            or (self.wall_num == 6 and self.a06 == True)
            or (self.wall_num == 7 and self.a07 == True)
            or (self.wall_num == 8 and self.a08 == True)
            or (self.wall_num == 9 and self.a09 == True)
            or (self.wall_num == 10 and self.a10 == True)
            or (self.wall_num == 11 and self.a11 == True)
            or (self.wall_num == 12 and self.a12 == True)
            or (self.wall_num == 13 and self.a13 == True)
            or (self.wall_num == 14 and self.a14 == True)
            or (self.wall_num == 15 and self.a15 == True)
            or (self.wall_num == 16 and self.a16 == True)
            or (self.wall_num == 17 and self.a17 == True)
            or (self.wall_num == 18 and self.a18 == True)
            or (self.wall_num == 19 and self.a19 == True)
            or (self.wall_num == 20 and self.a20 == True)
            or (self.wall_num == 21 and self.a21 == True)
            or (self.wall_num == 22 and self.a22 == True)
            or (self.wall_num == 23 and self.a23 == True)
            or (self.wall_num == 24 and self.a24 == True)
            or (self.wall_num == 25 and self.a25 == True)):
                myFaces.extend([(0,1,lastFace + 1, lastFace)])
            else:   
                myFaces.extend([(0,1,lastFace, lastFace + 1)])
        else:
            myFaces.extend([(0,1,self.wall_num * 2, self.wall_num * 2 + 1)])   
        
        
    mymesh = bpy.data.meshes.new(objName)
    myobject = bpy.data.objects.new(objName, mymesh)
    
    if (baseboard == False):
        myobject.location = bpy.context.scene.cursor_location
    else:
        myobject.location = (0,0,0)
        
    bpy.context.scene.objects.link(myobject)
    
    mymesh.from_pydata(myVertex, [], myFaces)
    mymesh.update(calc_edges=True)
    
    return myobject
#------------------------------------------------------------------------------
# Make a Wall
#------------------------------------------------------------------------------
def make_wall(prv,advance,size,over,factor,baseboard,lastFace,lastX,lastY,height,myVertex,myFaces,angle,hide):
    
    # if angle negative, calculate real
    # use add because the angle is negative 
    if (angle < 0):
        angle = 360 + angle
    # Verify Units    
    size = get_BlendUnits(size)
    over = get_BlendUnits(over)
    
    # Calculate size using angle
    sizeX = math.cos(math.radians(angle)) * size
    sizeY = math.sin(math.radians(angle)) * size
    
    # Create faces
    if (advance == False or baseboard == True):
        myVertex.extend([(lastX + sizeX,lastY + sizeY,height)
                         ,(lastX + sizeX,lastY + sizeY,0.0)])
        if (check_visibility(hide,baseboard)):
            if (prv == False or baseboard == True):
                myFaces.extend([(lastFace,lastFace + 2,lastFace + 3,lastFace + 1)]) # no advance
            else:
                myFaces.extend([(lastFace,lastFace + 1,lastFace + 2,lastFace + 3)]) # advance
            
        lastFace = lastFace + 2
    else:
        mid = size / 2 + ((size / 2) * factor)
        midX = math.cos(math.radians(angle)) * mid
        midY = math.sin(math.radians(angle)) * mid
        # first
        myVertex.extend([(lastX + midX,lastY + midY,height + over)
                         ,(lastX + midX,lastY + midY,0.0)])
        if (check_visibility(hide,baseboard)):
            if (math.fabs(factor) != 1):
                if (prv == False):
                    myFaces.extend([(lastFace,lastFace + 2,lastFace + 3,lastFace + 1)]) # no advance
                else:
                    myFaces.extend([(lastFace,lastFace + 1,lastFace + 2,lastFace + 3)]) # advance
        # second
        myVertex.extend([(lastX + sizeX,lastY + sizeY,0.0)
                         ,(lastX + sizeX,lastY + sizeY,height)])
        if (check_visibility(hide,baseboard)):
            if (math.fabs(factor) != 1): 
                myFaces.extend([(lastFace + 2,lastFace + 3,lastFace + 4,lastFace+ 5)])
            else:   
                if (prv == False):
                    myFaces.extend([(lastFace, lastFace + 5, lastFace + 4, lastFace + 1)
                                   ,(lastFace, lastFace + 2, lastFace + 5)])
                else:
                    myFaces.extend([(lastFace, lastFace + 4, lastFace + 5, lastFace + 1)
                               ,(lastFace + 1, lastFace + 2, lastFace + 5)])
            
        lastFace = lastFace + 4
        
    lastX = lastX + sizeX
    lastY = lastY + sizeY
    
        
    return (lastX,lastY,lastFace)

#------------------------------------------------------------------------------
# Create Floor or Ceiling
#------------------------------------------------------------------------------
def create_floor(self,context,typ,myRoom):
    bpy.context.scene.objects.active = myRoom

    myVertex = []
    myFaces = []
    verts = []
    
    obverts = bpy.context.active_object.data.vertices
    for vertex in obverts:
        verts.append(tuple(vertex.co))
    # Loop only selected
    i = 0 
    for e in verts:
        if (typ == "Floor"):
            if(e[2] == 0.0):
                myVertex.extend([(e[0],e[1],e[2])])
                i = i + 1    
        else: # ceiling
            if(round(e[2],5) == round(get_BlendUnits(self.room_height),5)):
                myVertex.extend([(e[0],e[1],e[2])])    
                i = i + 1
    
    # Create faces
    fa = []
    for f in range(0,i):
        fa.extend([f])
                        
    myFaces.extend([fa])
        
        
    mymesh = bpy.data.meshes.new(typ)
    myobject = bpy.data.objects.new(typ, mymesh)
    
    myobject.location = (0,0,0)
    bpy.context.scene.objects.link(myobject)
    
    mymesh.from_pydata(myVertex, [], myFaces)
    mymesh.update(calc_edges=True)
    
    return myobject

#----------------------------------------------
# Code to run alone the script
#----------------------------------------------
if __name__ == "__main__":
    create_mesh(0)
    print("Executed")
