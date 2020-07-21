# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_watermark_plus

import bpy
from bpy.props import IntProperty
from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from .watermark_plus import WatermarkPlus


class WATERMARK_PLUS_OT_add_watermark(Operator):
    bl_idname = 'watermark_plus.add_watermark'
    bl_label = 'Add Watermark'
    bl_description = 'Add watermark to render'
    bl_options = {'REGISTER', 'UNDO'}

    level: IntProperty(
        name='Level',
        subtype='UNSIGNED',
        min=1,
        max=2,
        default=1
    )

    def execute(self, context):
        # add watermark
        WatermarkPlus.add_watermark(
            context=context,
            scene=context.scene,
            bpy_data=bpy.data,
            level=self.level
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        if bpy.context.scene.node_tree and bpy.context.scene.use_nodes:
            return True
        else:
            return False


def register():
    register_class(WATERMARK_PLUS_OT_add_watermark)


def unregister():
    unregister_class(WATERMARK_PLUS_OT_add_watermark)
