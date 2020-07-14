# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_watermark_plus

from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from .watermark_plus import WatermarkPlus


class WATERMARK_PLUS_OT_add_watermark(Operator):
    bl_idname = 'watermark_plus.add_watermark'
    bl_label = 'Add Watermark'
    bl_description = 'Add watermark to render'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        WatermarkPlus.add_watermark()
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return True


def register():
    register_class(WATERMARK_PLUS_OT_add_watermark)


def unregister():
    unregister_class(WATERMARK_PLUS_OT_add_watermark)
