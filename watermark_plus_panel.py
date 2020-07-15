# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_watermark_plus

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class WATERMARK_PLUS_PT_panel_3d_view(Panel):
    bl_idname = 'WATERMARK_PLUS_PT_panel_3d_view'
    bl_label = 'Watermark Plus'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Watermark Plus'

    def draw(self, context):
        self.layout.label(text='Add Watermark')
        operator = self.layout.operator('watermark_plus.add_watermark', icon='OUTLINER_DATA_LIGHTPROBE', text='Watermark Level 1')
        operator.level = 1
        operator = self.layout.operator('watermark_plus.add_watermark', icon='OUTLINER_DATA_LIGHTPROBE', text='Watermark Level 2')
        operator.level = 2


class WATERMARK_PLUS_PT_panel_shader_editor(Panel):
    bl_idname = 'WATERMARK_PLUS_PT_panel_shader_editor'
    bl_label = 'Watermark Plus'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Watermark Plus'

    def draw(self, context):
        self.layout.label(text='Add Watermark')
        operator = self.layout.operator('watermark_plus.add_watermark', icon='OUTLINER_DATA_LIGHTPROBE', text='Watermark Level 1')
        operator.level = 1
        operator = self.layout.operator('watermark_plus.add_watermark', icon='OUTLINER_DATA_LIGHTPROBE', text='Watermark Level 2')
        operator.level = 2


def register():
    register_class(WATERMARK_PLUS_PT_panel_3d_view)
    register_class(WATERMARK_PLUS_PT_panel_shader_editor)


def unregister():
    unregister_class(WATERMARK_PLUS_PT_panel_shader_editor)
    unregister_class(WATERMARK_PLUS_PT_panel_3d_view)
