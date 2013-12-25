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
    "name": "Create html documentation",
    "author": "Antonio Vazquez (antonioya)",
    "location": "File > Import-Export",
    "version": (0, 2),
    "blender": (2, 6, 8),
    "description": "Create html documentation for blend files, including storyboards, images and linked assets.",
    "category": "Import-Export"}

import sys,os

#----------------------------------------------
# Add to Phyton path (once only)
#----------------------------------------------
path = sys.path
flag = False
for item in path:
    if "doc_scenes" in item:
        flag = True
if flag == False:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'doc_scenes'))
    print("doc_scenes: added to phytonpath")

#----------------------------------------------
# Import modules
#----------------------------------------------
if "bpy" in locals():
    import imp
    imp.reload(html_maker)
    print("doc_scenes: Reloaded multifiles")
else:
    from . import html_maker
    print("doc_scenes: Imported multifiles")

import bpy 

from bpy.props import *
from bpy_extras.io_utils import ExportHelper, ImportHelper
 
#----------------------------------------------------------
#    Export menu UI
#----------------------------------------------------------
 
class EXPORT_html_doc(bpy.types.Operator, ExportHelper):
    bl_idname = "io_export_h.doc_scenes"
    bl_description = 'Create html documentation (.html)'
    bl_label = "Create html"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
 
    # From ExportHelper. Filter filenames.
    filename_ext = ".htm"
    filter_glob = StringProperty(default="*.htm", options={'HIDDEN'})
 
    filepath = bpy.props.StringProperty(
        name="File Path", 
        description="File path used for creating html documentation.", 
        maxlen= 1024, default= "")
 
    include_render = bpy.props.BoolProperty(
        name = "Renders stored in slots",
        description="Include a render example in documentation. All slots will be included in the documentation."
            + " Warning: if not exist, a default OpenGl will be created.",
        default = True)

    only_render = bpy.props.BoolProperty(
        name = "Only render objects",
        description="Hide controlers for OpenGL renders.",
        default = True)
     
    include_story = bpy.props.EnumProperty(items = (('2',"Two keframes by line",""),
                                    ('1',"One keyframe by line",""),
                                    ('3',"Keyframe and Notes",""),
                                    ('0',"None","")),
                                    name="Storyboard",
                                    description="Include a OpenGL render for each keyframe.")
    
    threshold = bpy.props.IntProperty(
            name = "threshold", 
            description="threshold between keyframes in storyboard.", 
            default = 1, min = 1, max = 25)
        
    include_images = bpy.props.BoolProperty(
        name = "Images thumbnails",
        description="Include a table with all images used.",
        default = True)
    
    include_links = bpy.props.BoolProperty(
        name = "Linked files",
        description="Include a table with all linked files.",
        default = True)
    
    
    typecolor = bpy.props.EnumProperty(items = (('#336699',"Blue",""),
                                    ('#CC9900',"Orange",""),
                                    ('#336633',"Green",""),
                                    ('#FFFFCC',"Yellow",""),
                                    ('#990000',"Red",""),
                                    ('#999999',"Gray",""),
                                    ('#666666',"Dark gray",""),
                                    ('#FFFFFF',"White","")),
                                    name="Background",
                                    description="Defines the background color used to generate documentation")
    
    webserver = bpy.props.BoolProperty(
        name = "Optimize for webserver",
        description="OPtimize folder structure for deploying to webservers",
        default = False)

    include_borders = bpy.props.BoolProperty(
        name = "Table borders",
        description="Include borders in documentation tables.",
        default = False)


#----------------------------------------------------------
# Execute
#----------------------------------------------------------
    def execute(self, context):
        print("doc_scenes:", self.properties.filepath)
        #from . import simple_obj_export
        html_maker.write_html(
            self.properties.filepath, 
            self.include_render,
            self.only_render,
            self.include_story,
            self.threshold,
            self.include_images,
            self.include_links,
            self.typecolor,
            self.webserver,
            self.include_borders)
        return {'FINISHED'}
#----------------------------------------------------------
# Invoke
#----------------------------------------------------------
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
 
#----------------------------------------------------------
# Registration
#----------------------------------------------------------
def menu_func_export(self, context):
    self.layout.operator(EXPORT_html_doc.bl_idname, text="Create scene documentation (.htm)",icon='URL')
 
def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_export.append(menu_func_export)
 
def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)
 
if __name__ == "__main__":
    register()
