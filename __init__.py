# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_watermark_plus

from . import watermark_plus_ops
from . import watermark_plus_panel
from . import watermark_plus_preferences
from .addon import Addon


bl_info = {
    'name': 'Watermark Plus',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 83, 0),
    'location': 'N-Panel - Watermark Plus',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-watermark-plus/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-watermark-plus/',
    'description': 'Easily adding watermark to render'
}


def register():
    if not Addon.dev_mode():
        watermark_plus_preferences.register()
        watermark_plus_ops.register()
        watermark_plus_panel.register()
    else:
        print('It seems you are trying to use the dev version of the ' + bl_info['name'] + ' add-on. It may work not properly. Please download and use the release version!')


def unregister():
    if not Addon.dev_mode():
        watermark_plus_panel.unregister()
        watermark_plus_ops.unregister()
        watermark_plus_preferences.unregister()


if __name__ == '__main__':
    register()
