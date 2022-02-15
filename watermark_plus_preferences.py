# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_watermark_plus

from bpy.types import AddonPreferences
from bpy.props import StringProperty, BoolProperty
from bpy.utils import register_class, unregister_class
from .watermark_plus_panel import register_3d_view, unregister_3d_view


class WATERMARK_PLUS_preferences(AddonPreferences):
    bl_idname = __package__

    user_watermark_path: StringProperty(
        name='User Watermark',
        subtype='FILE_PATH',
        default=''
    )

    panel_viewport: BoolProperty(
        name='Panel in a 3D Viewport area',
        default=True,
        update=lambda self, context: self._panel_viewport_update(
            self=self
        )
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, property='user_watermark_path')
        layout.prop(self, property='panel_viewport')

    @staticmethod
    def _panel_viewport_update(self):
        if self.panel_viewport:
            register_3d_view()
        else:
            unregister_3d_view()


def register():
    register_class(WATERMARK_PLUS_preferences)


def unregister():
    unregister_class(WATERMARK_PLUS_preferences)
