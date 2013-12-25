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
# File: __init__.py
# Author: Antonio Vazquez (antonioya)
#----------------------------------------------------------
 
#----------------------------------------------
# Define Addon info
#----------------------------------------------
bl_info = {
    "name": "Archimesh",
    "author": "Antonio Vazquez (antonioya)",
    "location": "View3D > Add > Mesh > Archimesh",
    "version": (0,6,0),
    "blender": (2, 6, 8),
    "description": "Generate rooms, doors, kitchen cabinets, roofs, stairs and other architecture stuff.",
    "category": "Add Mesh"}

import sys,os

#----------------------------------------------
# Add to Phyton path (once only)
#----------------------------------------------
path = sys.path
flag = False
for item in path:
    if "archimesh" in item:
        flag = True
if flag == False:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'archimesh'))
    print("archimesh: added to phytonpath")

#----------------------------------------------
# Import modules
#----------------------------------------------
if "bpy" in locals():
    import imp
    imp.reload(room_maker)
    imp.reload(door_maker)
    imp.reload(roof_maker)
    imp.reload(column_maker)
    imp.reload(stairs_maker)
    imp.reload(kitchen_maker)
    print("archimesh: Reloaded multifiles")
else:
    from . import room_maker, door_maker,roof_maker,column_maker,stairs_maker,kitchen_maker
    print("archimesh: Imported multifiles")

import bpy 
from bpy.props import *

#------------------------------------------------------------------
# Reset room default values
# Rooms
#------------------------------------------------------------------
def reset_room(self):
    self.room_height=2.4
    self.wall_width=0.0
    self.inverse = False
    self.crt_mat = True
    self.wall_num=1
    self.baseboard = True
    self.base_width=0.015
    self.base_height=0.12
    self.ceiling = False
    self.floor = False
    self.merge = False
   
    self.w01=1
    self.w02=1
    self.w03=1
    self.w04=1
    self.w05=1
    self.w06=1
    self.w07=1
    self.w08=1
    self.w09=1
    self.w10=1
    self.w11=1
    self.w12=1
    self.w13=1
    self.w14=1
    self.w15=1
    self.w16=1
    self.w17=1
    self.w18=1
    self.w19=1
    self.w20=1
    self.w11=1
    self.w12=1
    self.w23=1
    self.w24=1
    self.w25=1
    
    self.a01= False
    self.a02= False
    self.a03= False
    self.a04= False
    self.a05= False
    self.a06= False
    self.a07= False
    self.a08= False
    self.a09= False
    self.a10= False
    self.a11= False
    self.a12= False
    self.a13= False
    self.a14= False
    self.a15= False
    self.a16= False
    self.a17= False
    self.a18= False
    self.a19= False
    self.a20= False
    self.a21= False
    self.a22= False
    self.a23= False
    self.a24= False
    self.a25= False
   
    self.m01= 0
    self.m02= 0
    self.m03= 0
    self.m04= 0
    self.m05= 0
    self.m06= 0
    self.m07= 0
    self.m08= 0
    self.m09= 0
    self.m10= 0
    self.m11= 0
    self.m12= 0
    self.m13= 0
    self.m14= 0
    self.m15= 0
    self.m16= 0
    self.m17= 0
    self.m18= 0
    self.m19= 0
    self.m20= 0
    self.m21= 0
    self.m22= 0
    self.m23= 0
    self.m24= 0
    self.m25= 0
       
    self.f01= 0
    self.f02= 0
    self.f03= 0
    self.f04= 0
    self.f05= 0
    self.f06= 0
    self.f07= 0
    self.f08= 0
    self.f09= 0
    self.f10= 0
    self.f11= 0
    self.f12= 0
    self.f13= 0
    self.f14= 0
    self.f15= 0
    self.f16= 0
    self.f17= 0
    self.f18= 0
    self.f19= 0
    self.f20= 0
    self.f21= 0
    self.f22= 0
    self.f23= 0
    self.f24= 0
    self.f25= 0
       
    self.r01= 0
    self.r02= 90
    self.r03= 0
    self.r04= 90
    self.r05= 0
    self.r06= 90
    self.r07= 0
    self.r08= 90
    self.r09= 0
    self.r10= 90
    self.r11= 0
    self.r12= 90
    self.r13= 0
    self.r14= 90
    self.r15= 0
    self.r16= 90
    self.r17= 0
    self.r18= 90
    self.r19= 0
    self.r20= 90
    self.r21= 0
    self.r22= 90
    self.r23= 0
    self.r24= 90
    self.r25= 0
    
    self.h01 = '0'
    self.h02 = '0'
    self.h03 = '0'
    self.h04 = '0'
    self.h05 = '0'
    self.h06 = '0'
    self.h07 = '0'
    self.h08 = '0'
    self.h09 = '0'
    self.h10 = '0'
    self.h11 = '0'
    self.h12 = '0'
    self.h13 = '0'
    self.h14 = '0'
    self.h15 = '0'
    self.h16 = '0'
    self.h17 = '0'
    self.h18 = '0'
    self.h19 = '0'
    self.h20 = '0'
    self.h21 = '0'
    self.h22 = '0'
    self.h23 = '0'
    self.h24 = '0'
    self.h25 = '0'
       
    self.reset = '0';
#------------------------------------------------------------------
# Define UI class
# Rooms
#------------------------------------------------------------------
class ROOM(bpy.types.Operator):
    bl_idname = "mesh.archimesh_room"
    bl_label = "Room"
    bl_description = "Room Generator"
    bl_options = {'REGISTER', 'UNDO'}
    
    # reset function
    reset=bpy.props.EnumProperty(items = (('0',"Keep last values",""),('1',"Reset to Default","")),
                                name="",description="Reset all values to default parameters")

    # Define properties
    room_height= bpy.props.FloatProperty(name='Height',min=0.001,max= 50, default= 2.4,precision=3, description='Room height')
    wall_width= bpy.props.FloatProperty(name='Thickness',min=0.000,max= 10, default= 0.0,precision=3, description='Thickness of the walls')
    inverse = bpy.props.BoolProperty(name = "Inverse",description="Inverse normals to outside.",default = False)
    crt_mat = bpy.props.BoolProperty(name = "Create default Cycles materials",description="Create default materials for Cycles render.",default = True)

    wall_num= bpy.props.IntProperty(name='Number of Walls',min=1,max= 25, default= 1, description='Number total of walls in the room')
    
    baseboard = bpy.props.BoolProperty(name = "Create baseboard",description="Create a baseboard automatically.",default = True)
    base_width= bpy.props.FloatProperty(name='Width',min=0.001,max= 10, default= 0.015,precision=3, description='Baseboard width')
    base_height= bpy.props.FloatProperty(name='Height',min=0.05,max= 20, default= 0.12,precision=3, description='Baseboard height')
    
    ceiling = bpy.props.BoolProperty(name = "Ceiling",description="Create a ceiling.",default = False)
    floor = bpy.props.BoolProperty(name = "Floor",description="Create a floor automatically.",default = False)

    merge = bpy.props.BoolProperty(name = "Close walls",description="Close walls to create a full closed room.",default = False)
   
    w01= bpy.props.FloatProperty(name='Wall01 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w02= bpy.props.FloatProperty(name='Wall02 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w03= bpy.props.FloatProperty(name='Wall03 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w04= bpy.props.FloatProperty(name='Wall04 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w05= bpy.props.FloatProperty(name='Wall05 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w06= bpy.props.FloatProperty(name='Wall06 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w07= bpy.props.FloatProperty(name='Wall07 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w08= bpy.props.FloatProperty(name='Wall08 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w09= bpy.props.FloatProperty(name='Wall09 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w10= bpy.props.FloatProperty(name='Wall10 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w11= bpy.props.FloatProperty(name='Wall11 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w12= bpy.props.FloatProperty(name='Wall12 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w13= bpy.props.FloatProperty(name='Wall13 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w14= bpy.props.FloatProperty(name='Wall14 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w15= bpy.props.FloatProperty(name='Wall15 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w16= bpy.props.FloatProperty(name='Wall16 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w17= bpy.props.FloatProperty(name='Wall17 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w18= bpy.props.FloatProperty(name='Wall18 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w19= bpy.props.FloatProperty(name='Wall19 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w20= bpy.props.FloatProperty(name='Wall20 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w21= bpy.props.FloatProperty(name='Wall21 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w22= bpy.props.FloatProperty(name='Wall22 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w23= bpy.props.FloatProperty(name='Wall23 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w24= bpy.props.FloatProperty(name='Wall24 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    w25= bpy.props.FloatProperty(name='Wall25 size',min=-150,max= 150, default= 1,precision=3, description='Length of the wall (negative to reverse direction)')
    
    a01 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m01= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f01= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r01= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 0,precision=1, description='Wall Angle (-180 to +180)')
    
    a02 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m02= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f02= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r02= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 90,precision=1, description='Wall Angle (-180 to +180)')
    
    a03 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m03= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f03= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r03= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 0,precision=1, description='Wall Angle (-180 to +180)')
    
    a04 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m04= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f04= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r04= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 90,precision=1, description='Wall Angle (-180 to +180)')
    
    a05 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m05= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f05= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r05= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 0,precision=1, description='Wall Angle (-180 to +180)')
    
    a06 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m06= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f06= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r06= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 90,precision=1, description='Wall Angle (-180 to +180)')
    
    a07 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m07= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f07= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r07= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 0,precision=1, description='Wall Angle (-180 to +180)')
    
    a08 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m08= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f08= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r08= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 90,precision=1, description='Wall Angle (-180 to +180)')
    
    a09 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m09= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f09= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r09= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 0,precision=1, description='Wall Angle (-180 to +180)')
    
    a10 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m10= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f10= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r10= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 90,precision=1, description='Wall Angle (-180 to +180)')
    
    a11 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m11= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f11= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r11= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 0,precision=1, description='Wall Angle (-180 to +180)')
    
    a12 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m12= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f12= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r12= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 90,precision=1, description='Wall Angle (-180 to +180)')
    
    a13 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m13= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f13= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r13= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 0,precision=1, description='Wall Angle (-180 to +180)')
    
    a14 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m14= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f14= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r14= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 90,precision=1, description='Wall Angle (-180 to +180)')
    
    a15 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m15= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f15= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r15= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 0,precision=1, description='Wall Angle (-180 to +180)')
    
    a16 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m16= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f16= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r16= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 90,precision=1, description='Wall Angle (-180 to +180)')
    
    a17 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m17= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f17= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r17= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 0,precision=1, description='Wall Angle (-180 to +180)')
    
    a18 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m18= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f18= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r18= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 90,precision=1, description='Wall Angle (-180 to +180)')
    
    a19 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m19= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f19= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r19= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 0,precision=1, description='Wall Angle (-180 to +180)')
    
    a20 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m20= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f20= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r20= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 90,precision=1, description='Wall Angle (-180 to +180)')
    
    a21 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m21= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f21= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r21= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 0,precision=1, description='Wall Angle (-180 to +180)')
    
    a22 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m22= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f22= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r22= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 90,precision=1, description='Wall Angle (-180 to +180)')
    
    a23 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m23= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f23= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r23= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 0,precision=1, description='Wall Angle (-180 to +180)')
    
    a24 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m24= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f24= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r24= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 90,precision=1, description='Wall Angle (-180 to +180)')
    
    a25 = bpy.props.BoolProperty(name = "Advanced",description="Advance options.",default = False)
    m25= bpy.props.FloatProperty(name='',min=0,max= 50, default= 0,precision=3, description='Middle height variation')
    f25= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')
    r25= bpy.props.FloatProperty(name='',min=-180,max= 180, default= 0,precision=1, description='Wall Angle (-180 to +180)')

    h01=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h02=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h03=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h04=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h05=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h06=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h07=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h08=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h09=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h10=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h11=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h12=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h13=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h14=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h15=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h16=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h17=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h18=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h19=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h20=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h21=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h22=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h23=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h24=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")
    h25=bpy.props.EnumProperty(items = (('0',"Visible",""),('1',"Baseboard",""),('2',"Wall",""),('3',"Hidden","")),
                                name="",description="Wall visibility")



    #-----------------------------------------------------
    # Draw (create UI interface)
    #-----------------------------------------------------
    def draw(self, context):
        layout = self.layout
        space = bpy.context.space_data
        if (not space.local_view):
            row=layout.row()
            row.prop(self,"reset")
            row=layout.row()
            row.prop(self,'room_height')
            row.prop(self,'wall_width')
            row.prop(self,'inverse')
        
            row=layout.row()
            row.prop(self,'ceiling')
            row.prop(self,'floor')
            row.prop(self,'merge')
                    
            box=layout.box()
            # Wall number
            box.prop(self,'wall_num')
            if (self.wall_num >= 1): add_wall(self,context,box,self.a01,'01')
            if (self.wall_num >= 2): add_wall(self,context,box,self.a02,'02')
            if (self.wall_num >= 3): add_wall(self,context,box,self.a03,'03')
            if (self.wall_num >= 4): add_wall(self,context,box,self.a04,'04')
            if (self.wall_num >= 5): add_wall(self,context,box,self.a05,'05')
            if (self.wall_num >= 6): add_wall(self,context,box,self.a06,'06')
            if (self.wall_num >= 7): add_wall(self,context,box,self.a07,'07')
            if (self.wall_num >= 8): add_wall(self,context,box,self.a08,'08')
            if (self.wall_num >= 9): add_wall(self,context,box,self.a09,'09')
            if (self.wall_num >= 10): add_wall(self,context,box,self.a10,'10')
            if (self.wall_num >= 11): add_wall(self,context,box,self.a11,'11')
            if (self.wall_num >= 12): add_wall(self,context,box,self.a12,'12')
            if (self.wall_num >= 13): add_wall(self,context,box,self.a13,'13')
            if (self.wall_num >= 14): add_wall(self,context,box,self.a14,'14')
            if (self.wall_num >= 15): add_wall(self,context,box,self.a15,'15')
            if (self.wall_num >= 16): add_wall(self,context,box,self.a16,'16')
            if (self.wall_num >= 17): add_wall(self,context,box,self.a17,'17')
            if (self.wall_num >= 18): add_wall(self,context,box,self.a18,'18')
            if (self.wall_num >= 19): add_wall(self,context,box,self.a19,'19')
            if (self.wall_num >= 20): add_wall(self,context,box,self.a20,'20')
            if (self.wall_num >= 21): add_wall(self,context,box,self.a21,'21')
            if (self.wall_num >= 22): add_wall(self,context,box,self.a22,'22')
            if (self.wall_num >= 23): add_wall(self,context,box,self.a23,'23')
            if (self.wall_num >= 24): add_wall(self,context,box,self.a24,'24')
            if (self.wall_num >= 25): add_wall(self,context,box,self.a25,'25')
            
            
            box=layout.box()
            box.prop(self,'baseboard')
            if (self.baseboard==True):
                row = box.row()
                row.prop(self,'base_width')
                row.prop(self,'base_height')
    
            box=layout.box()
            box.prop(self,'crt_mat')
        else:
            row=layout.row()
            row.label("Warning: Operator does not work in local view mode", icon='ERROR')

        
    #-----------------------------------------------------
    # Execute
    #-----------------------------------------------------
    def execute(self, context):
        if (bpy.context.mode == "OBJECT"):
            if (self.reset == '1'):
                reset_room(self)
            
            
            room_maker.create_mesh(self,context)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Archimesh: Option only valid in Object mode")
            return {'CANCELLED'}

#-----------------------------------------------------
# Add wall parameters
#-----------------------------------------------------
def add_wall(self,context,box,var,num):
    row = box.row()
    row.prop(self,'w' + num)
    row.prop(self,'a' + num)
    if (var == True):
        srow = row.row()
        srow.prop(self,'r' + num)
        srow.prop(self,'h' + num)
        srow.prop(self,'m' + num)
        srow.prop(self,'f' + num)
 
 
#------------------------------------------------------------------
# Define UI class
# Rooms
#------------------------------------------------------------------
class ROOF(bpy.types.Operator):
    bl_idname = "mesh.archimesh_roof"
    bl_label = "Roof"
    bl_description = "Roof Generator"
    bl_options = {'REGISTER', 'UNDO'}
    
    # Define properties
    roof_width = bpy.props.IntProperty(name='Num tiles X',min=1,max= 100, default= 6, description='Tiles in X axis')
    roof_height = bpy.props.IntProperty(name='Num tiles Y',min=1,max= 100, default= 3, description='Tiles in Y axis')
    #roof_base= bpy.props.FloatProperty(name='Base thickness',min=0.002,max= 0.50, default= 0.02,precision=3, description='Thickness of base in the smallets point')
    
    roof_thick= bpy.props.FloatProperty(name='Tile thickness',min=0.000,max= 0.50, default= 0.012,precision=3, description='Thickness of the roof tile')
    roof_angle= bpy.props.FloatProperty(name='Roof slope',min=0.0,max= 70.0, default= 0.0,precision=1, description='Roof angle of slope')
    roof_scale= bpy.props.FloatProperty(name='Tile scale',min=0.001,max= 10, default= 1,precision=3, description='Scale of roof tile')
    
    crt_mat = bpy.props.BoolProperty(name = "Create default Cycles materials",description="Create default materials for Cycles render.",default = True)

    model = bpy.props.EnumProperty(items = (('1',"Model 01",""),
                                ('2',"Model 02",""),
                                ('3',"Model 03",""),
                                ('4',"Model 04","")),
                                name="Model",
                                description="Roof tile model")
    
    #-----------------------------------------------------
    # Draw (create UI interface)
    #-----------------------------------------------------
    def draw(self, context):
        layout = self.layout
        space = bpy.context.space_data
        if (not space.local_view):
            # Imperial units warning
            if (bpy.context.scene.unit_settings.system == "IMPERIAL"):
                row=layout.row()
                row.label("Warning: Imperial units not supported", icon='COLOR_RED')
            box=layout.box()
            box.prop(self,'model')
            box.prop(self,'roof_width')
            box.prop(self,'roof_height')
            box.prop(self,'roof_scale')
            
            if (self.model == "1"):
                tilesize_x = 0.184
                tilesize_y = 0.413
            
            if (self.model == "2"):
                tilesize_x = 0.103
                tilesize_y = 0.413
            
            if (self.model == "3"):
                tilesize_x = 0.184
                tilesize_y = 0.434
            
            if (self.model == "4"):
                tilesize_x = 0.231
                tilesize_y = 0.39
                
            
            x = tilesize_x * self.roof_scale * self.roof_width
            y = tilesize_y * self.roof_scale * self.roof_height
             
            buf = 'Size: {0:.2f} * {1:.2f} aprox.'.format(x,y)
            box.label(buf)
        
            box=layout.box()
            box.prop(self,'roof_thick')
            box.prop(self,'roof_angle')
    
            box=layout.box()
            box.prop(self,'crt_mat')
        else:
            row=layout.row()
            row.label("Warning: Operator does not work in local view mode", icon='ERROR')
        
    #-----------------------------------------------------
    # Execute
    #-----------------------------------------------------
    def execute(self, context):
        if (bpy.context.mode == "OBJECT"):
            roof_maker.create_mesh(self,context)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Archimesh: Option only valid in Object mode")
            return {'CANCELLED'}

#------------------------------------------------------------------
# Define UI class
# Doors
#------------------------------------------------------------------
class DOOR(bpy.types.Operator):
    bl_idname = "mesh.archimesh_door"
    bl_label = "Door"
    bl_description = "Door Generator"
    bl_options = {'REGISTER', 'UNDO'}
    
    # Define properties
    frame_width= bpy.props.FloatProperty(name='Frame width',min=0.25,max= 10, default= 1,precision=2, description='Doorframe width')
    frame_height= bpy.props.FloatProperty(name='Frame height',min=0.25,max= 10, default= 2.1,precision=2, description='Doorframe height')
    frame_thick= bpy.props.FloatProperty(name='Frame thickness',min=0.05,max= 0.50, default= 0.08,precision=2, description='Doorframe thickness')
    frame_size= bpy.props.FloatProperty(name='Frame size',min=0.05,max= 0.25, default= 0.08,precision=2, description='Doorframe size')
    crt_mat = bpy.props.BoolProperty(name = "Create default Cycles materials",description="Create default materials for Cycles render.",default = True)
    factor= bpy.props.FloatProperty(name='',min=0.2,max= 1, default= 0.5,precision=3, description='Door ratio')

    openside = bpy.props.EnumProperty(items = (('1',"Right open",""),
                                ('2',"Left open",""),
                                ('3',"Both sides","")),
                                name="Open side",
                                description="Defines the direction for opening the door")

    model = bpy.props.EnumProperty(items = (('1',"Model 01",""),
                                ('2',"Model 02",""),
                                ('3',"Model 03",""),
                                ('4',"Model 04",""),
                                ('5',"Model 05","Glass"),
                                ('6',"Model 06","Glass")),
                                name="Model",
                                description="Door model")
    
    handle = bpy.props.EnumProperty(items = (('1',"Handle 01",""),
                                ('2',"Handle 02",""),
                                ('3',"Handle 03",""),
                                ('4',"Handle 04",""),
                                ('0',"None","")),
                                name="Handle",
                                description="Handle model")
    
    #-----------------------------------------------------
    # Draw (create UI interface)
    #-----------------------------------------------------
    def draw(self, context):
        layout = self.layout
        space = bpy.context.space_data
        if (not space.local_view):
            # Imperial units warning
            if (bpy.context.scene.unit_settings.system == "IMPERIAL"):
                row=layout.row()
                row.label("Warning: Imperial units not supported", icon='COLOR_RED')
            box=layout.box()
            row=box.row()
            row.prop(self,'frame_width')
            row.prop(self,'frame_height')
            row=box.row()
            row.prop(self,'frame_thick')
            row.prop(self,'frame_size')
            
            box=layout.box()
            row=box.row()
            row.prop(self,'openside')
            if (self.openside == "3"):
                row.prop(self,"factor")
                
            layout.prop(self,'model')
            layout.prop(self,'handle')
            
            box=layout.box()
            box.prop(self,'crt_mat')
        else:
            row=layout.row()
            row.label("Warning: Operator does not work in local view mode", icon='ERROR')
        
    #-----------------------------------------------------
    # Execute
    #-----------------------------------------------------
    def execute(self, context):
        if (bpy.context.mode == "OBJECT"):
            door_maker.create_mesh(self,context)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Archimesh: Option only valid in Object mode")
            return {'CANCELLED'}

    
#------------------------------------------------------------------
# Define UI class
# Columns
#------------------------------------------------------------------
class COLUMN(bpy.types.Operator):
    bl_idname = "mesh.archimesh_column"
    bl_label = "Column"
    bl_description = "Columns Generator"
    bl_options = {'REGISTER', 'UNDO'}
    
    # Define properties
    model = bpy.props.EnumProperty(items = (('1',"Circular",""),
                                ('2',"Rectangular","")),
                                name="Model",
                                description="Type of column")
    keep_size = bpy.props.BoolProperty(name = "Keep radius equal",description="Keep all radius (top, mid and bottom) to the same size.",default = True)
    
    rad_top = bpy.props.FloatProperty(name='Top radius',min=0.001,max= 10, default= 0.15,precision=3, description='Radius of the column in the top')
    rad_mid = bpy.props.FloatProperty(name='Middle radius',min=0.001,max= 10, default= 0.15,precision=3, description='Radius of the column in the middle')
    shift= bpy.props.FloatProperty(name='',min=-1,max= 1, default= 0,precision=3, description='Middle displacement')

    rad_bottom = bpy.props.FloatProperty(name='Bottom radius',min=0.001,max= 10, default= 0.15,precision=3, description='Radius of the column in the bottom')
    
    col_height = bpy.props.FloatProperty(name='Total height',min=0.001,max= 10, default= 2.4,precision=3, description='Total height of column, including bases and tops')
    col_sx = bpy.props.FloatProperty(name='X size',min=0.001,max= 10, default= 0.30,precision=3, description='Column size for x axis')
    col_sy = bpy.props.FloatProperty(name='Y size',min=0.001,max= 10, default= 0.30,precision=3, description='Column size for y axis')
    
    cir_base = bpy.props.BoolProperty(name = "Include circular base",description="Include a base with circular form.",default = False)
    cir_base_r = bpy.props.FloatProperty(name='Radio',min=0.001,max= 10, default= 0.08,precision=3, description='Rise up radio of base')
    cir_base_z = bpy.props.FloatProperty(name='Height',min=0.001,max= 10, default= 0.05,precision=3, description='Size for z axis')
    
    cir_top = bpy.props.BoolProperty(name = "Include circular top",description="Include a top with circular form.",default = False)
    cir_top_r = bpy.props.FloatProperty(name='Radio',min=0.001,max= 10, default= 0.08,precision=3, description='Rise up radio of top')
    cir_top_z = bpy.props.FloatProperty(name='Height',min=0.001,max= 10, default= 0.05,precision=3, description='Size for z axis')
    
    box_base = bpy.props.BoolProperty(name = "Include rectangular base",description="Include a base with rectangular form.",default = True)
    box_base_x = bpy.props.FloatProperty(name='X size',min=0.001,max= 10, default= 0.40,precision=3, description='Size for x axis')
    box_base_y = bpy.props.FloatProperty(name='Y size',min=0.001,max= 10, default= 0.40,precision=3, description='Size for y axis')
    box_base_z = bpy.props.FloatProperty(name='Height',min=0.001,max= 10, default= 0.05,precision=3, description='Size for z axis')
    
    box_top = bpy.props.BoolProperty(name = "Include rectangular top",description="Include a top with rectangular form.",default = True)
    box_top_x = bpy.props.FloatProperty(name='X size',min=0.001,max= 10, default= 0.40,precision=3, description='Size for x axis')
    box_top_y = bpy.props.FloatProperty(name='Y size',min=0.001,max= 10, default= 0.40,precision=3, description='Size for y axis')
    box_top_z = bpy.props.FloatProperty(name='Height',min=0.001,max= 10, default= 0.05,precision=3, description='Size for z axis')

    arc_top = bpy.props.BoolProperty(name = "Create top arch",description="Include an arch in the top of the column.",default = False)
    arc_radio = bpy.props.FloatProperty(name='Arc Radio',min=0.001,max= 10, default= 1,precision=1, description='Radio of the arch')
    arc_width = bpy.props.FloatProperty(name='Thickness',min=0.01,max= 10, default= 0.15,precision=2, description='Thickness of the arch wall')
    arc_gap = bpy.props.FloatProperty(name='Arc gap',min=0.01,max= 10, default= 0.25,precision=2, description='Size of the gap in the arch sides')
    
    crt_mat = bpy.props.BoolProperty(name = "Create default Cycles materials",description="Create default materials for Cycles render.",default = True)
    crt_array = bpy.props.BoolProperty(name = "Create array of elements",description="Create a modifier array for all elemnst.",default = False)
    array_num_x = bpy.props.IntProperty(name='Count X',min=0,max= 100, default= 3, description='Number of elements in array')
    array_space_x = bpy.props.FloatProperty(name='Distance X',min=0.000,max= 10, default= 1,precision=3, description='Distance between elements (only arc disabled)')
    array_num_y = bpy.props.IntProperty(name='Count Y',min=0,max= 100, default= 0, description='Number of elements in array')
    array_space_y = bpy.props.FloatProperty(name='Distance Y',min=0.000,max= 10, default= 1,precision=3, description='Distance between elements (only arc disabled)')
    array_space_z = bpy.props.FloatProperty(name='Distance Z',min=-10,max= 10, default= 0,precision=3, description='Combined X/Z distance between elements (only arc disabled)')
    ramp = bpy.props.BoolProperty(name = "Deform",description="Deform top base with Z displacement.",default = True)
    array_space_factor = bpy.props.FloatProperty(name='Move Y center',min=0.00,max= 1, default= 0.0,precision=3, description='Move the center of the arch in Y axis. (0 centered)')

    
    #-----------------------------------------------------
    # Draw (create UI interface)
    #-----------------------------------------------------
    def draw(self, context):
        layout = self.layout
        space = bpy.context.space_data
        if (not space.local_view):
            # Imperial units warning
            if (bpy.context.scene.unit_settings.system == "IMPERIAL"):
                row=layout.row()
                row.label("Warning: Imperial units not supported", icon='COLOR_RED')
            box=layout.box()
            box.prop(self,'model')
            # Circular
            if (self.model == "1"):
                box.prop(self,'keep_size')
                box.prop(self,'rad_top')
                if (self.keep_size == False):
                    row = box.row()
                    row.prop(self,'rad_mid')
                    row.prop(self,'shift')
                    box.prop(self,'rad_bottom')
                    
            # Rectangular
            if (self.model == "2"):
                box.prop(self,'col_sx')
                box.prop(self,'col_sy')
                
            box.prop(self,'col_height')
                
            box=layout.box()
            box.prop(self,'box_base')
            if (self.box_base == True):
                row=box.row()
                row.prop(self,'box_base_x')
                row.prop(self,'box_base_y')
                row.prop(self,'box_base_z')
                
            box=layout.box()
            box.prop(self,'box_top')
            if (self.box_top == True):
                row=box.row()
                row.prop(self,'box_top_x')
                row.prop(self,'box_top_y')
                row.prop(self,'box_top_z')
                
            box=layout.box()
            box.prop(self,'cir_base')
            if (self.cir_base == True):
                row=box.row()
                row.prop(self,'cir_base_r')
                row.prop(self,'cir_base_z')
                
            box=layout.box()
            box.prop(self,'cir_top')
            if (self.cir_top == True):
                row=box.row()
                row.prop(self,'cir_top_r')
                row.prop(self,'cir_top_z')
                 
            box = layout.box()
            box.prop(self,'arc_top')
            if (self.arc_top == True):
                row=box.row()
                row.prop(self,'arc_radio')
                row.prop(self,'arc_width')
                row=box.row()
                row.prop(self,'arc_gap')
                row.prop(self,'array_space_factor')
            
            box = layout.box()
            box.prop(self,'crt_array')
            if (self.crt_array == True):
                row = box.row()
                row.prop(self,'array_num_x')
                row.prop(self,'array_num_y')
                if (self.arc_top == True):        
                    box.label("Use arch radio and thickness to set distances")
                  
                if (self.arc_top == False):
                    row = box.row()
                    row.prop(self,'array_space_x')
                    row.prop(self,'array_space_y')
                    row = box.row()
                    row.prop(self,'array_space_z')
                    row.prop(self,'ramp')
                    
            box = layout.box()
            box.prop(self,'crt_mat')
        else:
            row=layout.row()
            row.label("Warning: Operator does not work in local view mode", icon='ERROR')
        
    #-----------------------------------------------------
    # Execute
    #-----------------------------------------------------
    def execute(self, context):
        if (bpy.context.mode == "OBJECT"):
            column_maker.create_mesh(self,context)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Archimesh: Option only valid in Object mode")
            return {'CANCELLED'}

#------------------------------------------------------------------
# Define UI class
# Stairs
#------------------------------------------------------------------
class STAIRS(bpy.types.Operator):
    bl_idname = "mesh.archimesh_stairs"
    bl_label = "Stairs"
    bl_description = "Stairs Generator"
    bl_options = {'REGISTER', 'UNDO'}
    
    # Define properties
    model = bpy.props.EnumProperty(items = (('1',"Rectangular",""),
                                ('2',"Rounded","")),
                                name="Model",
                                description="Type of steps")
    radio = bpy.props.FloatProperty(name='',min=0.001,max= 0.500, default= 0.20,precision=3, description='Radius factor for rounded')
    curve = bpy.props.BoolProperty(name = "Include deformation handles",description="Include a curve to modify the stairs curve.",default = False)

    step_num= bpy.props.IntProperty(name='Number of steps',min=1,max= 1000, default= 3, description='Number total of steps')
    max_width = bpy.props.FloatProperty(name='Width',min=0.001,max= 10, default= 1,precision=3, description='Step maximum width')
    depth = bpy.props.FloatProperty(name='Depth',min=0.001,max= 10, default= 0.30,precision=3, description='Depth of the step')
    shift = bpy.props.FloatProperty(name='Shift',min=0.001,max= 1, default= 1,precision=3, description='Step shift in Y axis')
    thickness = bpy.props.FloatProperty(name='Thickness',min=0.001,max= 10, default= 0.03,precision=3, description='Step thickness')
    sizev = bpy.props.BoolProperty(name = "Variable width",description="Steps are not equal in width.",default = False)
    back = bpy.props.BoolProperty(name = "Close sides",description="Close all steps side to make a solid structure.",default = False)
    min_width = bpy.props.FloatProperty(name='',min=0.001,max= 10, default= 1,precision=3, description='Step minimum width')
    
    height = bpy.props.FloatProperty(name='height',min=0.001,max= 10, default= 0.14,precision=3, description='Step height')
    front_gap = bpy.props.FloatProperty(name='Front',min=0,max= 10, default= 0.03,precision=3, description='Front gap')
    side_gap = bpy.props.FloatProperty(name='Side',min=0,max= 10, default= 0,precision=3, description='Side gap')
    crt_mat = bpy.props.BoolProperty(name = "Create default Cycles materials",description="Create default materials for Cycles render.",default = True)

    
    #-----------------------------------------------------
    # Draw (create UI interface)
    #-----------------------------------------------------
    def draw(self, context):
        layout = self.layout
        space = bpy.context.space_data
        if (not space.local_view):
            # Imperial units warning
            if (bpy.context.scene.unit_settings.system == "IMPERIAL"):
                row=layout.row()
                row.label("Warning: Imperial units not supported", icon='COLOR_RED')
            
            box=layout.box()
            row = box.row()
            row.prop(self,'model')
            if (self.model == "2"):
                row.prop(self,'radio')
            
            box.prop(self,'step_num')
            row = box.row()
            row.prop(self,'max_width')
            row.prop(self,'depth')
            row.prop(self,'shift')
            row = box.row()
            row.prop(self,'back')
            row.prop(self,'sizev')
            row = box.row()
            row.prop(self,'curve')
            # all equal
            if (self.sizev == True):
                row.prop(self,'min_width')
                
            box=layout.box()
            row = box.row()
            row.prop(self,'thickness')
            row.prop(self,'height')
            row = box.row()
            row.prop(self,'front_gap')
            if (self.model == "1"):
                row.prop(self,'side_gap')
                
            box = layout.box()
            box.prop(self,'crt_mat')
        else:
            row=layout.row()
            row.label("Warning: Operator does not work in local view mode", icon='ERROR')
        
    #-----------------------------------------------------
    # Execute
    #-----------------------------------------------------
    def execute(self, context):
        if (bpy.context.mode == "OBJECT"):
            stairs_maker.create_mesh(self,context)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Archimesh: Option only valid in Object mode")
            return {'CANCELLED'}
#------------------------------------------------------------------
# Define UI class
# Kitchens
#------------------------------------------------------------------
class KITCHEN(bpy.types.Operator):
    bl_idname = "mesh.archimesh_kitchen"
    bl_label = "Cabinets"
    bl_description = "Cabinet Generator"
    bl_options = {'REGISTER', 'UNDO'}
    
    # Define properties
    type_cabinet = bpy.props.EnumProperty(items = (('1',"Floor",""),
                                ('2',"Wall","")),
                                name="Type",
                                description="Type of cabinets")
    oldtype = type_cabinet
     
    thickness= bpy.props.FloatProperty(name='Thickness',min=0.001,max= 5, default= 0.018,precision=3, description='Board thickness')
    depth= bpy.props.FloatProperty(name='Depth',min=0.001,max= 50, default= 0.59,precision=3, description='Default cabinet depth')
    height= bpy.props.FloatProperty(name='Height',min=0.001,max= 50, default= 0.70,precision=3, description='Default cabinet height')
    handle = bpy.props.EnumProperty(items = (('1',"Model 1",""),
                                ('2',"Model 2",""),
                                ('3',"Model 3",""),
                                ('4',"Model 4",""),
                                ('5',"Model 5",""),
                                ('6',"Model 6",""),
                                ('7',"Model 7",""),
                                ('8',"Model 8",""),
                                ('9',"None","")),
                                name="Handle",
                                description="Type of handle")
    handle_x = bpy.props.FloatProperty(name='',min=0.001,max= 10, default= 0.05,precision=3, description='Displacement in X relative position (limited to door size)')
    handle_z = bpy.props.FloatProperty(name='',min=0.001,max= 10, default= 0.05,precision=3, description='Displacement in Z relative position (limited to door size)')
    
    baseboard = bpy.props.BoolProperty(name = "Baseboard",description="Create a baseboard automatically",default = True)
    baseheight = bpy.props.FloatProperty(name='height',min=0.001,max= 10, default= 0.16,precision=3, description='Baseboard height')
    basefactor = bpy.props.FloatProperty(name='sink',min=0,max= 1, default= 0.90,precision=3, description='Baseboard sink')

    countertop = bpy.props.BoolProperty(name = "Countertop",description="Create a countertop automatically (only default cabinet height)",default = True)
    counterheight = bpy.props.FloatProperty(name='height',min=0.001,max= 10, default= 0.02,precision=3, description='Countertop height')
    counterextend = bpy.props.FloatProperty(name='extend',min=0.001,max= 10, default= 0.03,precision=3, description='Countertop extent')
 
    fitZ = bpy.props.BoolProperty(name = "Floor origin in Z=0",description="Use Z=0 axis as vertical origin floor position",default = True)
    moveZ = bpy.props.FloatProperty(name='Z position',min=0.001,max= 10, default= 1.5,precision=3, description='Wall cabinet Z position from floor')

    cabinet_num= bpy.props.IntProperty(name='Number of Cabinets',min=1,max= 10, default= 1, description='Number total of cabinets in the Kitchen')
    # Cabinet width    
    sX01 = bpy.props.FloatProperty(name='width',min=0.001,max= 10, default= 0.60,precision=3, description='Cabinet width')
    sX02 = bpy.props.FloatProperty(name='width',min=0.001,max= 10, default= 0.60,precision=3, description='Cabinet width')
    sX03 = bpy.props.FloatProperty(name='width',min=0.001,max= 10, default= 0.60,precision=3, description='Cabinet width')
    sX04 = bpy.props.FloatProperty(name='width',min=0.001,max= 10, default= 0.60,precision=3, description='Cabinet width')
    sX05 = bpy.props.FloatProperty(name='width',min=0.001,max= 10, default= 0.60,precision=3, description='Cabinet width')
    sX06 = bpy.props.FloatProperty(name='width',min=0.001,max= 10, default= 0.60,precision=3, description='Cabinet width')
    sX07 = bpy.props.FloatProperty(name='width',min=0.001,max= 10, default= 0.60,precision=3, description='Cabinet width')
    sX08 = bpy.props.FloatProperty(name='width',min=0.001,max= 10, default= 0.60,precision=3, description='Cabinet width')
    sX09 = bpy.props.FloatProperty(name='width',min=0.001,max= 10, default= 0.60,precision=3, description='Cabinet width')
    sX10 = bpy.props.FloatProperty(name='width',min=0.001,max= 10, default= 0.60,precision=3, description='Cabinet width')
        
    wY01 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify y size')
    wY02 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify y size')
    wY03 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify y size')
    wY04 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify y size')
    wY05 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify y size')
    wY06 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify y size')
    wY07 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify y size')
    wY08 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify y size')
    wY09 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify y size')
    wY10 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify y size')

    wZ01 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify z size')
    wZ02 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify z size')
    wZ03 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify z size')
    wZ04 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify z size')
    wZ05 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify z size')
    wZ06 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify z size')
    wZ07 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify z size')
    wZ08 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify z size')
    wZ09 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify z size')
    wZ10 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Modify z size')
        
    # Cabinet position shift   
    pX01 = bpy.props.FloatProperty(name='',min=0,max= 10, default= 0,precision=3, description='Position x shift')
    pX02 = bpy.props.FloatProperty(name='',min=0,max= 10, default= 0,precision=3, description='Position x shift')
    pX03 = bpy.props.FloatProperty(name='',min=0,max= 10, default= 0,precision=3, description='Position x shift')
    pX04 = bpy.props.FloatProperty(name='',min=0,max= 10, default= 0,precision=3, description='Position x shift')
    pX05 = bpy.props.FloatProperty(name='',min=0,max= 10, default= 0,precision=3, description='Position x shift')
    pX06 = bpy.props.FloatProperty(name='',min=0,max= 10, default= 0,precision=3, description='Position x shift')
    pX07 = bpy.props.FloatProperty(name='',min=0,max= 10, default= 0,precision=3, description='Position x shift')
    pX08 = bpy.props.FloatProperty(name='',min=0,max= 10, default= 0,precision=3, description='Position x shift')
    pX09 = bpy.props.FloatProperty(name='',min=0,max= 10, default= 0,precision=3, description='Position x shift')
    pX10 = bpy.props.FloatProperty(name='',min=0,max= 10, default= 0,precision=3, description='Position x shift')

    pY01 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position y shift')
    pY02 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position y shift')
    pY03 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position y shift')
    pY04 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position y shift')
    pY05 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position y shift')
    pY06 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position y shift')
    pY07 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position y shift')
    pY08 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position y shift')
    pY09 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position y shift')
    pY10 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position y shift')

    pZ01 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position z shift')
    pZ02 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position z shift')
    pZ03 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position z shift')
    pZ04 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position z shift')
    pZ05 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position z shift')
    pZ06 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position z shift')
    pZ07 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position z shift')
    pZ08 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position z shift')
    pZ09 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position z shift')
    pZ10 = bpy.props.FloatProperty(name='',min=-10,max= 10, default= 0,precision=3, description='Position z shift')
        
    # Door type
    dType01 = bpy.props.EnumProperty(items = (('1',"Single R",""),
                                    ('2',"Single L",""),
                                    ('3',"Single T",""),
                                    ('4',"Glass R",""),
                                    ('5',"Glass L",""),
                                    ('6',"Glass T",""),
                                    ('7',"Drawers",""),
                                    ('8',"Double",""),
                                    ('11',"Double Glass",""),
                                    ('10',"Corner R",""),
                                    ('9',"Corner L",""),
                                    ('99',"None","")),
                        name="Door",
                        description="Type of front door or drawers")
    dType02 = bpy.props.EnumProperty(items = (('1',"Single R",""),
                                    ('2',"Single L",""),
                                    ('3',"Single T",""),
                                    ('4',"Glass R",""),
                                    ('5',"Glass L",""),
                                    ('6',"Glass T",""),
                                    ('7',"Drawers",""),
                                    ('8',"Double",""),
                                    ('11',"Double Glass",""),
                                    ('10',"Corner R",""),
                                    ('9',"Corner L",""),
                                    ('99',"None","")),
                        name="Door",
                        description="Type of front door or drawers")
    dType03 = bpy.props.EnumProperty(items = (('1',"Single R",""),
                                    ('2',"Single L",""),
                                    ('3',"Single T",""),
                                    ('4',"Glass R",""),
                                    ('5',"Glass L",""),
                                    ('6',"Glass T",""),
                                    ('7',"Drawers",""),
                                    ('8',"Double",""),
                                    ('11',"Double Glass",""),
                                    ('10',"Corner R",""),
                                    ('9',"Corner L",""),
                                    ('99',"None","")),
                        name="Door",
                        description="Type of front door or drawers")
    dType04 = bpy.props.EnumProperty(items = (('1',"Single R",""),
                                    ('2',"Single L",""),
                                    ('3',"Single T",""),
                                    ('4',"Glass R",""),
                                    ('5',"Glass L",""),
                                    ('6',"Glass T",""),
                                    ('7',"Drawers",""),
                                    ('8',"Double",""),
                                    ('11',"Double Glass",""),
                                    ('10',"Corner R",""),
                                    ('9',"Corner L",""),
                                    ('99',"None","")),
                        name="Door",
                        description="Type of front door or drawers")
    dType05 = bpy.props.EnumProperty(items = (('1',"Single R",""),
                                    ('2',"Single L",""),
                                    ('3',"Single T",""),
                                    ('4',"Glass R",""),
                                    ('5',"Glass L",""),
                                    ('6',"Glass T",""),
                                    ('7',"Drawers",""),
                                    ('8',"Double",""),
                                    ('11',"Double Glass",""),
                                    ('10',"Corner R",""),
                                    ('9',"Corner L",""),
                                    ('99',"None","")),
                        name="Door",
                        description="Type of front door or drawers")
    dType06 = bpy.props.EnumProperty(items = (('1',"Single R",""),
                                    ('2',"Single L",""),
                                    ('3',"Single T",""),
                                    ('4',"Glass R",""),
                                    ('5',"Glass L",""),
                                    ('6',"Glass T",""),
                                    ('7',"Drawers",""),
                                    ('8',"Double",""),
                                    ('11',"Double Glass",""),
                                    ('10',"Corner R",""),
                                    ('9',"Corner L",""),
                                    ('99',"None","")),
                        name="Door",
                        description="Type of front door or drawers")
    dType07 = bpy.props.EnumProperty(items = (('1',"Single R",""),
                                    ('2',"Single L",""),
                                    ('3',"Single T",""),
                                    ('4',"Glass R",""),
                                    ('5',"Glass L",""),
                                    ('6',"Glass T",""),
                                    ('7',"Drawers",""),
                                    ('8',"Double",""),
                                    ('11',"Double Glass",""),
                                    ('10',"Corner R",""),
                                    ('9',"Corner L",""),
                                    ('99',"None","")),
                        name="Door",
                        description="Type of front door or drawers")
    dType08 = bpy.props.EnumProperty(items = (('1',"Single R",""),
                                    ('2',"Single L",""),
                                    ('3',"Single T",""),
                                    ('4',"Glass R",""),
                                    ('5',"Glass L",""),
                                    ('6',"Glass T",""),
                                    ('7',"Drawers",""),
                                    ('8',"Double",""),
                                    ('11',"Double Glass",""),
                                    ('10',"Corner R",""),
                                    ('9',"Corner L",""),
                                    ('99',"None","")),
                        name="Door",
                        description="Type of front door or drawers")
    dType09 = bpy.props.EnumProperty(items = (('1',"Single R",""),
                                    ('2',"Single L",""),
                                    ('3',"Single T",""),
                                    ('4',"Glass R",""),
                                    ('5',"Glass L",""),
                                    ('6',"Glass T",""),
                                    ('7',"Drawers",""),
                                    ('8',"Double",""),
                                    ('11',"Double Glass",""),
                                    ('9',"Corner L",""),
                                    ('10',"Corner R",""),
                                    ('99',"None","")),
                        name="Door",
                        description="Type of front door or drawers")
    dType10 = bpy.props.EnumProperty(items = (('1',"Single R",""),
                                    ('2',"Single L",""),
                                    ('3',"Single T",""),
                                    ('4',"Glass R",""),
                                    ('5',"Glass L",""),
                                    ('6',"Glass T",""),
                                    ('7',"Drawers",""),
                                    ('8',"Double",""),
                                    ('11',"Double Glass",""),
                                    ('10',"Corner R",""),
                                    ('9',"Corner L",""),
                                    ('99',"None","")),
                        name="Door",
                        description="Type of front door or drawers")

    # Shelves
    sNum01 = bpy.props.IntProperty(name='Shelves',min=0,max= 10, default= 1, description='Number total of shelves')
    sNum02 = bpy.props.IntProperty(name='Shelves',min=0,max= 10, default= 1, description='Number total of shelves')
    sNum03 = bpy.props.IntProperty(name='Shelves',min=0,max= 10, default= 1, description='Number total of shelves')
    sNum04 = bpy.props.IntProperty(name='Shelves',min=0,max= 10, default= 1, description='Number total of shelves')
    sNum05 = bpy.props.IntProperty(name='Shelves',min=0,max= 10, default= 1, description='Number total of shelves')
    sNum06 = bpy.props.IntProperty(name='Shelves',min=0,max= 10, default= 1, description='Number total of shelves')
    sNum07 = bpy.props.IntProperty(name='Shelves',min=0,max= 10, default= 1, description='Number total of shelves')
    sNum08 = bpy.props.IntProperty(name='Shelves',min=0,max= 10, default= 1, description='Number total of shelves')
    sNum09 = bpy.props.IntProperty(name='Shelves',min=0,max= 10, default= 1, description='Number total of shelves')
    sNum10 = bpy.props.IntProperty(name='Shelves',min=0,max= 10, default= 1, description='Number total of shelves')
    
    # Drawers
    dNum01 = bpy.props.IntProperty(name='Num',min=1,max= 10, default= 3, description='Number total of drawers')
    dNum02 = bpy.props.IntProperty(name='Num',min=1,max= 10, default= 3, description='Number total of drawers')
    dNum03 = bpy.props.IntProperty(name='Num',min=1,max= 10, default= 3, description='Number total of drawers')
    dNum04 = bpy.props.IntProperty(name='Num',min=1,max= 10, default= 3, description='Number total of drawers')
    dNum05 = bpy.props.IntProperty(name='Num',min=1,max= 10, default= 3, description='Number total of drawers')
    dNum06 = bpy.props.IntProperty(name='Num',min=1,max= 10, default= 3, description='Number total of drawers')
    dNum07 = bpy.props.IntProperty(name='Num',min=1,max= 10, default= 3, description='Number total of drawers')
    dNum08 = bpy.props.IntProperty(name='Num',min=1,max= 10, default= 3, description='Number total of drawers')
    dNum09 = bpy.props.IntProperty(name='Num',min=1,max= 10, default= 3, description='Number total of drawers')
    dNum10 = bpy.props.IntProperty(name='Num',min=1,max= 10, default= 3, description='Number total of drawers')

    # Glass Factor
    gF01 = bpy.props.FloatProperty(name='',min=0.001,max= 1, default= 0.1,precision=3, description='Glass ratio')
    gF02 = bpy.props.FloatProperty(name='',min=0.001,max= 1, default= 0.1,precision=3, description='Glass ratio')
    gF03 = bpy.props.FloatProperty(name='',min=0.001,max= 1, default= 0.1,precision=3, description='Glass ratio')
    gF04 = bpy.props.FloatProperty(name='',min=0.001,max= 1, default= 0.1,precision=3, description='Glass ratio')
    gF05 = bpy.props.FloatProperty(name='',min=0.001,max= 1, default= 0.1,precision=3, description='Glass ratio')
    gF06 = bpy.props.FloatProperty(name='',min=0.001,max= 1, default= 0.1,precision=3, description='Glass ratio')
    gF07 = bpy.props.FloatProperty(name='',min=0.001,max= 1, default= 0.1,precision=3, description='Glass ratio')
    gF08 = bpy.props.FloatProperty(name='',min=0.001,max= 1, default= 0.1,precision=3, description='Glass ratio')
    gF09 = bpy.props.FloatProperty(name='',min=0.001,max= 1, default= 0.1,precision=3, description='Glass ratio')
    gF10 = bpy.props.FloatProperty(name='',min=0.001,max= 1, default= 0.1,precision=3, description='Glass ratio')

    # Handle flag
    hand01 = bpy.props.BoolProperty(name = "Handle",description="Create a handle",default = True)
    hand02 = bpy.props.BoolProperty(name = "Handle",description="Create a handle",default = True)
    hand03 = bpy.props.BoolProperty(name = "Handle",description="Create a handle",default = True)
    hand04 = bpy.props.BoolProperty(name = "Handle",description="Create a handle",default = True)
    hand05 = bpy.props.BoolProperty(name = "Handle",description="Create a handle",default = True)
    hand06 = bpy.props.BoolProperty(name = "Handle",description="Create a handle",default = True)
    hand07 = bpy.props.BoolProperty(name = "Handle",description="Create a handle",default = True)
    hand08 = bpy.props.BoolProperty(name = "Handle",description="Create a handle",default = True)
    hand09 = bpy.props.BoolProperty(name = "Handle",description="Create a handle",default = True)
    hand10 = bpy.props.BoolProperty(name = "Handle",description="Create a handle",default = True)

    # Left baseboard
    bL01 = bpy.props.BoolProperty(name = "Left Baseboard",description="Create a left baseboard",default = False)
    bL02 = bpy.props.BoolProperty(name = "Left Baseboard",description="Create a left baseboard",default = False)
    bL03 = bpy.props.BoolProperty(name = "Left Baseboard",description="Create a left baseboard",default = False)
    bL04 = bpy.props.BoolProperty(name = "Left Baseboard",description="Create a left baseboard",default = False)
    bL05 = bpy.props.BoolProperty(name = "Left Baseboard",description="Create a left baseboard",default = False)
    bL06 = bpy.props.BoolProperty(name = "Left Baseboard",description="Create a left baseboard",default = False)
    bL07 = bpy.props.BoolProperty(name = "Left Baseboard",description="Create a left baseboard",default = False)
    bL08 = bpy.props.BoolProperty(name = "Left Baseboard",description="Create a left baseboard",default = False)
    bL09 = bpy.props.BoolProperty(name = "Left Baseboard",description="Create a left baseboard",default = False)
    bL10 = bpy.props.BoolProperty(name = "Left Baseboard",description="Create a left baseboard",default = False)

    # Right baseboard
    bR01 = bpy.props.BoolProperty(name = "Right Baseboard",description="Create a left baseboard",default = False)
    bR02 = bpy.props.BoolProperty(name = "Right Baseboard",description="Create a left baseboard",default = False)
    bR03 = bpy.props.BoolProperty(name = "Right Baseboard",description="Create a left baseboard",default = False)
    bR04 = bpy.props.BoolProperty(name = "Right Baseboard",description="Create a left baseboard",default = False)
    bR05 = bpy.props.BoolProperty(name = "Right Baseboard",description="Create a left baseboard",default = False)
    bR06 = bpy.props.BoolProperty(name = "Right Baseboard",description="Create a left baseboard",default = False)
    bR07 = bpy.props.BoolProperty(name = "Right Baseboard",description="Create a left baseboard",default = False)
    bR08 = bpy.props.BoolProperty(name = "Right Baseboard",description="Create a left baseboard",default = False)
    bR09 = bpy.props.BoolProperty(name = "Right Baseboard",description="Create a left baseboard",default = False)
    bR10 = bpy.props.BoolProperty(name = "Right Baseboard",description="Create a left baseboard",default = False)

    # Fill countertop spaces
    tC01 = bpy.props.BoolProperty(name = "Countertop fill",description="Fill empty spaces with countertop",default = True)
    tC02 = bpy.props.BoolProperty(name = "Countertop fill",description="Fill empty spaces with countertop",default = True)
    tC03 = bpy.props.BoolProperty(name = "Countertop fill",description="Fill empty spaces with countertop",default = True)
    tC04 = bpy.props.BoolProperty(name = "Countertop fill",description="Fill empty spaces with countertop",default = True)
    tC05 = bpy.props.BoolProperty(name = "Countertop fill",description="Fill empty spaces with countertop",default = True)
    tC06 = bpy.props.BoolProperty(name = "Countertop fill",description="Fill empty spaces with countertop",default = True)
    tC07 = bpy.props.BoolProperty(name = "Countertop fill",description="Fill empty spaces with countertop",default = True)
    tC08 = bpy.props.BoolProperty(name = "Countertop fill",description="Fill empty spaces with countertop",default = True)
    tC09 = bpy.props.BoolProperty(name = "Countertop fill",description="Fill empty spaces with countertop",default = True)
    tC10 = bpy.props.BoolProperty(name = "Countertop fill",description="Fill empty spaces with countertop",default = True)


    # Materials        
    crt_mat = bpy.props.BoolProperty(name = "Create default Cycles materials",description="Create default materials for Cycles render.",default = True)

    #-----------------------------------------------------
    # Draw (create UI interface)
    #-----------------------------------------------------
    def draw(self, context):
        layout = self.layout
        space = bpy.context.space_data
        if (not space.local_view):
            # Imperial units warning
            if (bpy.context.scene.unit_settings.system == "IMPERIAL"):
                row=layout.row()
                row.label("Warning: Imperial units not supported", icon='COLOR_RED')
            
            box=layout.box()
            row=box.row()
            row.prop(self,'type_cabinet')
                
            row.prop(self,'thickness')
            row=box.row()
            row.prop(self,'depth')
            row.prop(self,'height')
            row=box.row()
            row.prop(self,'handle')
            if (self.handle != "9"):
                row.prop(self,'handle_x')
                row.prop(self,'handle_z')
            
            if (self.type_cabinet == "1"):
                row=box.row()
                row.prop(self,"countertop")
                if (self.countertop):
                    row.prop(self,"counterheight")
                    row.prop(self,"counterextend")
                row=box.row()
                row.prop(self,'baseboard')
                if (self.baseboard):
                    row.prop(self,'baseheight')
                    row.prop(self,'basefactor')
                
            row=box.row()
            row.prop(self,'fitZ')
            if (self.type_cabinet == "2"):
                row.prop(self,'moveZ')
    
            # Cabinet number
            row=layout.row()
            row.prop(self,'cabinet_num')
            if (self.cabinet_num >= 1): add_cabinet(self,'01',self.dType01)
            if (self.cabinet_num >= 2): add_cabinet(self,'02',self.dType02)
            if (self.cabinet_num >= 3): add_cabinet(self,'03',self.dType03)
            if (self.cabinet_num >= 4): add_cabinet(self,'04',self.dType04)
            if (self.cabinet_num >= 5): add_cabinet(self,'05',self.dType05)
            if (self.cabinet_num >= 6): add_cabinet(self,'06',self.dType06)
            if (self.cabinet_num >= 7): add_cabinet(self,'07',self.dType07)
            if (self.cabinet_num >= 8): add_cabinet(self,'08',self.dType08)
            if (self.cabinet_num >= 9): add_cabinet(self,'09',self.dType09)
            if (self.cabinet_num >= 10): add_cabinet(self,'10',self.dType10)
            
    
            box=layout.box()
            box.prop(self,'crt_mat')
        else:
            row=layout.row()
            row.label("Warning: Operator does not work in local view mode", icon='ERROR')
        
    #-----------------------------------------------------
    # Execute
    #-----------------------------------------------------
    def execute(self, context):
        if (bpy.context.mode == "OBJECT"):
            # Set default values
            if (self.oldtype != self.type_cabinet):
                if (self.type_cabinet == "1"): # Floor
                    self.depth= 0.59
                    self.height= 0.70
                    
                if (self.type_cabinet == "2"): # Wall
                    self.depth= 0.35
                    self.height= 0.70
                    1
                self.oldtype = self.type_cabinet
            # Create cabinets    
            kitchen_maker.create_mesh(self,context)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Archimesh: Option only valid in Object mode")
            return {'CANCELLED'}
#-----------------------------------------------------
# Add cabinet parameters
#-----------------------------------------------------
def add_cabinet(self,num,doorType):
    layout = self.layout
    box=layout.box()
    row = box.row()
    row.label("Cabinet " + str(num))
    row.prop(self,'sX' + num)

    row = box.row()
    row.prop(self,'wY' + num)
    row.prop(self,'wZ' + num)
    
    row = box.row()
    row.prop(self,'pX' + num)
    row.prop(self,'pY' + num)
    row.prop(self,'pZ' + num)

    row = box.row()
    row.prop(self,'dType' + num)
    if (doorType == "7"): # Drawers
        row.prop(self,'dNum' + num) # drawers number
    else:    
        row.prop(self,'sNum' + num) # shelves number
    # Glass ratio
    if (doorType == "4" or doorType == "5" or doorType == "6" or doorType == "11"):
        row.prop(self,'gF' + num) # shelves number
    # Handle
    row = box.row()
    if (self.handle != "9"):
        row.prop(self,'hand' + num)
    if (self.baseboard and self.type_cabinet == "1"): 
        row.prop(self,'bL' + num)
        row.prop(self,'bR' + num)

    if (self.countertop and self.type_cabinet == "1"):
        row = box.row()
        row.prop(self,'tC' + num)
    
#----------------------------------------------------------
# Registration
#----------------------------------------------------------
class INFO_MT_mesh_custom_menu_add(bpy.types.Menu):
    bl_idname = "INFO_MT_mesh_custom_menu_add"
    bl_label = "Archimesh"
    
    def draw(self, context):
        layout = self.layout
        self.layout.operator("mesh.archimesh_room", text="Add Room",icon="PLUGIN");
        self.layout.operator("mesh.archimesh_door", text="Add Door",icon="PLUGIN")
        self.layout.operator("mesh.archimesh_kitchen", text="Add Cabinet",icon="PLUGIN")
        self.layout.operator("mesh.archimesh_column", text="Add Column",icon="PLUGIN")
        self.layout.operator("mesh.archimesh_stairs", text="Add Stairs",icon="PLUGIN")
        self.layout.operator("mesh.archimesh_roof", text="Add Roof",icon="PLUGIN")


#--------------------------------------------------------------
# Register all operators and panels
#--------------------------------------------------------------
# Define menu
def menu_func(self, context):
    self.layout.menu("INFO_MT_mesh_custom_menu_add", icon="PLUGIN")

def register():
    bpy.utils.register_class(INFO_MT_mesh_custom_menu_add)
    bpy.utils.register_class(ROOM)
    bpy.utils.register_class(DOOR)
    bpy.utils.register_class(ROOF)
    bpy.utils.register_class(COLUMN)
    bpy.utils.register_class(STAIRS)
    bpy.utils.register_class(KITCHEN)
    bpy.types.INFO_MT_mesh_add.append(menu_func)
    
def unregister():
    bpy.utils.unregister_class(INFO_MT_mesh_custom_menu_add)
    bpy.utils.unregister_class(ROOM)
    bpy.utils.unregister_class(DOOR)
    bpy.utils.unregister_class(ROOF)
    bpy.utils.unregister_class(COLUMN)
    bpy.utils.unregister_class(STAIRS)
    bpy.utils.unregister_class(KITCHEN)
    bpy.types.INFO_MT_mesh_add.remove(menu_func)
    
if __name__ == '__main__':
    register()

