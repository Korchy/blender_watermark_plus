# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_watermark_plus

from bpy.types import AddonPreferences
from bpy.props import StringProperty
from bpy.utils import register_class, unregister_class


class WATERMARK_PLUS_preferences(AddonPreferences):
    bl_idname = __package__

    user_watermark_path: StringProperty(
        name='User Watermark',
        subtype='FILE_PATH',
        default=''
    )

    def draw(self, context):
        self.layout.prop(self, property='user_watermark_path')


def register():
    register_class(WATERMARK_PLUS_preferences)


def unregister():
    unregister_class(WATERMARK_PLUS_preferences)
