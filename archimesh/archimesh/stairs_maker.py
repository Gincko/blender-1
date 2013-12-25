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
# File: stairs_maker.py
# Automatic generation of stairs
# Author: Antonio Vazquez (antonioya)
#
#----------------------------------------------------------
import bpy
import mathutils
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
    
    #------------------------
    # Create stairs
    #------------------------
    myData = create_stairs(self,context,"Stairs")
    myStairs = myData[0]
    myStairs.select = True
    bpy.context.scene.objects.active = myStairs
    remove_doubles(myStairs)
    set_normals(myStairs)
    set_modifier_mirror(myStairs,"X")
    #------------------------
    # Create curve handles        
    #------------------------
    if (self.curve):
        x = myStairs.location.x
        y = myStairs.location.y
        z = myStairs.location.z
        
        last = myData[1]
        x1 = last[1]# use y
        
        myP = [((0,0,0),(- 0.25, 0, 0),(0.25, 0, 0))
              ,((x1,0,0),(x1- 0.25, 0, 0),(x1 + 0.25, 0, 0))] # double element
        myCurve = create_bezier("Stairs_handle", myP,(x,y,z))
        set_modifier_curve(myStairs,myCurve)

    #------------------------
    # Create materials        
    #------------------------
    if (self.crt_mat):
        # Stairs material
        mat = create_diffuse_material("Stairs_material",False,0.8, 0.8, 0.8)
        set_material(myStairs,mat)
        
            
    bpy.ops.object.select_all(False)    
    myStairs.select = True
    bpy.context.scene.objects.active = myStairs

    return
#------------------------------------------------------------------------------
# Create rectangular Stairs
#------------------------------------------------------------------------------
def create_stairs(self,context,objName):
         
    myVertex = []
    myFaces = []
    index = 0

    lastPoint = (0,0,0)
    for s in range(0,self.step_num):
        if (self.model == "1"):
            myData = create_rect_step(self,context,lastPoint,myVertex,myFaces,index,s) 
        if (self.model == "2"):
            myData = create_round_step(self,context,lastPoint,myVertex,myFaces,index,s) 
        index = myData[0]
        lastPoint = myData[1]       
    
    mesh = bpy.data.meshes.new(objName)
    myobject = bpy.data.objects.new(objName, mesh)
    
    myobject.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(myobject)
    
    mesh.from_pydata(myVertex, [], myFaces)
    mesh.update(calc_edges=True)
   
    return (myobject,lastPoint)
#------------------------------------------------------------------------------
# Create rectangular step
#------------------------------------------------------------------------------
def create_rect_step(self,context,origin,myVertex,myFaces,index,step):
    x = origin[0]
    y = origin[1]
    z = origin[2]
    i = index
    max_depth = y + self.depth
    if (self.back == True):
        max_depth = self.depth * self.step_num
    
    # calculate width (no side gap)
    if (self.sizev == False):
        width = self.max_width / 2
    else:
        width = (self.max_width / 2) - (step * (((self.max_width - self.min_width) / 2) / self.step_num)) 
    
    # Vertical Rectangle
    myVertex.extend([(x,y,z),(x,y,z + self.height),(x + width,y,z + self.height),(x + width,y,z)])
    val = y + self.thickness 
    myVertex.extend([(x,val,z),(x,val,z + self.height),(x + width,val,z + self.height),(x + width,val,z)])
    
    myFaces.extend([(i+0,i+1,i+2,i+3),(i+4,i+5,i+6,i+7),(i+0,i+3,i+7,i+4)
                    ,(i+1,i+2,i+6,i+5),(i+0,i+1,i+5,i+4),(i+3,i+2,i+6,i+7)])
    # Side plane
    myVertex.extend([(x + width,max_depth,z + self.height),(x + width,max_depth,z)])
    myFaces.extend([(i+7,i+6,i+8,i+9)])
    i = i + 10
    # calculate width (side gap)
    width = width + self.side_gap
     
    # Horizontal Rectangle 
    z = z + self.height 
    myVertex.extend([(x,y - self.front_gap,z),(x,max_depth,z),(x + width,max_depth,z),(x + width,y - self.front_gap,z)])
    z = z + self.thickness 
    myVertex.extend([(x,y - self.front_gap,z),(x,max_depth,z),(x + width,max_depth,z),(x + width,y - self.front_gap,z)])
    myFaces.extend([(i+0,i+1,i+2,i+3),(i+4,i+5,i+6,i+7),(i+0,i+3,i+7,i+4)
                    ,(i+1,i+2,i+6,i+5),(i+3,i+2,i+6,i+7)])
    i = i + 8
    # remap origin
    y = y + (self.depth * self.shift)
    
    return (i,(x,y,z)) 
#------------------------------------------------------------------------------
# Create rounded step
#------------------------------------------------------------------------------
def create_round_step(self,context,origin,myVertex,myFaces,index,step):
    x = origin[0]
    y = origin[1]
    z = origin[2]
    i = index
    li = [math.radians(270),math.radians(288),math.radians(306),math.radians(324),math.radians(342),math.radians(0)]
    
    max_width = self.max_width
    max_depth = y + self.depth
    if (self.back == True):
        max_depth = (self.depth) * self.step_num


# Resize for width
    if (self.sizev == True):
        max_width = max_width - (step * ((self.max_width - self.min_width) / self.step_num))

    
    half = max_width / 2
    #------------------------------------
    # Vertical 
    #------------------------------------
    # calculate width 
    width = half - (half * self.radio)
    myRadio = half - width

    myVertex.extend([(x,y,z),(x,y,z + self.height)])
    # Round
    for e in li:
        pos_x = (math.cos(e) * myRadio) + x + width - myRadio
        pos_y = (math.sin(e) * myRadio) + y + myRadio
        
        myVertex.extend([(pos_x,pos_y,z),(pos_x,pos_y,z + self.height)])

    # back point    
    myVertex.extend([(x + width,max_depth,z),(x + width,max_depth,z + self.height)])
        
    myFaces.extend([(i,i+1,i+3,i+2),(i+2,i+3,i+5,i+4),(i+4,i+5,i+7,i+6),(i+6,i+7,i+9,i+8)
                    ,(i+8,i+9,i+11,i+10),(i+10,i+11,i+13,i+12),(i+12,i+13,i+15,i+14)])

    i = i + 16
    #------------------------------------
    # Horizontal 
    #------------------------------------
    # calculate width gap
    width = half + self.front_gap - (half * self.radio)
 
    z = z + self.height 
    # Vertical 
    myVertex.extend([(x,y - self.front_gap,z),(x,y - self.front_gap,z + self.thickness)])
    # Round
    for e in li:
        pos_x = (math.cos(e) * myRadio) + x + width - myRadio
        pos_y = (math.sin(e) * myRadio) + y + myRadio - self.front_gap
        
        myVertex.extend([(pos_x,pos_y,z),(pos_x,pos_y,z + self.thickness)])
    
    # back points    
    myVertex.extend([(pos_x,max_depth,z),(pos_x,max_depth,z + self.thickness)
                     ,(x,max_depth,z),(x,max_depth,z + self.thickness)])
        
    myFaces.extend([(i,i+1,i+3,i+2),(i+2,i+3,i+5,i+4),(i+4,i+5,i+7,i+6),(i+6,i+7,i+9,i+8)
                    ,(i+8,i+9,i+11,i+10),(i+10,i+11,i+13,i+12),(i+12,i+13,i+15,i+14)
                    ,(i,i+2,i+4,i+6,i+8,i+10,i+12,i+14,i+16),(i+1,i+3,i+5,i+7,i+9,i+11,i+13,i+15,i+17)
                    ,(i+14,i+15,i+17,i+16)])

    i = i + 18
    z = z + self.thickness
     
    # remap origin
    #y = y + (self.depth - myRadio) * self.shift
    y = y + (self.depth * self.shift)
    
    return (i,(x,y,z)) 
#------------------------------------------------------------------------------
# Create bezier curve
#------------------------------------------------------------------------------
def create_bezier(objName, points, origin):    
    curvedata = bpy.data.curves.new(name=objName, type='CURVE')   
    curvedata.dimensions = '3D'    
    
    myObject = bpy.data.objects.new(objName, curvedata)    
    myObject.location = origin
    myObject.rotation_euler[2] = math.radians(90)
    
    bpy.context.scene.objects.link(myObject)    
    
    polyline = curvedata.splines.new('BEZIER')    
    polyline.bezier_points.add(len(points)-1)    
 
 
    for idx, (knot, h1, h2) in enumerate(points):
        point = polyline.bezier_points[idx]
        point.co = knot
        point.handle_left = h1
        point.handle_right = h2
        point.handle_left_type = 'FREE'
        point.handle_right_type = 'FREE'

    return myObject 
#----------------------------------------------
# Code to run alone the script
#----------------------------------------------
if __name__ == "__main__":
    create_mesh(0)
    print("Executed")
