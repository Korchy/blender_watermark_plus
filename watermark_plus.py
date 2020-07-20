# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_watermark_plus

import os


class WatermarkPlus:

    _watermark_image = 'watermark_plus.png'

    @classmethod
    def add_watermark(cls, scene, bpy_data, level=1):
        # add watermark to render
        if level == 2:
            watermark_nodegroup, image_node = cls._watermark_lv2(scene=scene, bpy_data=bpy_data)
        else:   # level = 1
            watermark_nodegroup, image_node = cls._watermark_lv1(scene=scene, bpy_data=bpy_data)
        # locate watermark nodegroup under the Composite node and reconnect input Composite node link
        composite_node = cls._composite_node(scene=scene)
        if composite_node:
            # location
            watermark_nodegroup.location = (composite_node.location.x, composite_node.location.y - 200)
            image_node.location = (composite_node.location.x - 250, composite_node.location.y - 400)
            # connect
            link_to_composite = next(iter(composite_node.inputs['Image'].links), None)
            if link_to_composite:
                from_node_to_composite = link_to_composite.from_socket
                if from_node_to_composite != watermark_nodegroup.outputs['Image']:
                    scene.node_tree.links.new(from_node_to_composite, watermark_nodegroup.inputs['Render Layers'])
            scene.node_tree.links.new(watermark_nodegroup.outputs['Image'], composite_node.inputs['Image'])
        viewer_node = cls._viewer_node(scene=scene)
        # connect to Viewer node
        if viewer_node:
            scene.node_tree.links.new(watermark_nodegroup.outputs['Image'], viewer_node.inputs['Image'])
        # add sample watermark image
        watermark_img = cls._load_watermark_img(bpy_data=bpy_data)
        if watermark_img:
            image_node.image = watermark_img

    @classmethod
    def _load_watermark_img(cls, bpy_data):
        # load sample watermark img
        watermark_img = bpy_data.images.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), cls._watermark_image))
        return watermark_img

    @classmethod
    def _watermark_lv1(cls, scene, bpy_data):
        # add watermark level 1
        # NODES
        node_tree1 = bpy_data.node_groups.get('Watermark Level 1')
        if not node_tree1:
            node_tree1 = bpy_data.node_groups.new('Watermark Level 1', 'CompositorNodeTree')
            # INPUTS
            node_tree1.inputs.new('NodeSocketColor', 'Render Layers')
            node_tree1.inputs.new('NodeSocketColor', 'Watermark Image')
            node_tree1.inputs.new('NodeSocketFloat', 'Scale')
            node_tree1.inputs.new('NodeSocketFloatAngle', 'Rotation (deg)')
            node_tree1.inputs.new('NodeSocketFloat', 'Offset X')
            node_tree1.inputs.new('NodeSocketFloat', 'Offset Y')
            node_tree1.inputs.new('NodeSocketFloat', 'Intensity')
            node_tree1.inputs.new('NodeSocketFloat', 'White')
            node_tree1.inputs.new('NodeSocketFloat', 'Black')
            node_tree1.inputs.new('NodeSocketFloat', 'White/Black')
            # OUTPUTS
            node_tree1.outputs.new('NodeSocketColor', 'Image')
            # NODES
            area_influence_1 = node_tree1.nodes.new('NodeFrame')
            area_influence_1.color = (0.0, 0.7469902038574219, 1.0)
            area_influence_1.hide = False
            area_influence_1.label = 'area influence'
            area_influence_1.label_size = 20
            area_influence_1.location = (-14.266263961791992, 246.41172790527344)
            area_influence_1.mute = False
            area_influence_1.name = 'area influence'
            area_influence_1.shrink = True
            area_influence_1.use_custom_color = True
            area_influence_1.width = 380.0

            colorramp_1 = node_tree1.nodes.new('CompositorNodeValToRGB')
            colorramp_1.parent = node_tree1.nodes.get('area influence')
            colorramp_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            colorramp_1.color_ramp.color_mode = 'RGB'
            if 0 >= len(colorramp_1.color_ramp.elements):
                colorramp_1.color_ramp.elements.new(0.20725402235984802)
            colorramp_1.color_ramp.elements[0].alpha = 1.0
            colorramp_1.color_ramp.elements[0].color = (0.0, 0.0, 0.0, 1.0)
            colorramp_1.color_ramp.elements[0].position = 0.20725402235984802
            if 1 >= len(colorramp_1.color_ramp.elements):
                colorramp_1.color_ramp.elements.new(0.24870474636554718)
            colorramp_1.color_ramp.elements[1].alpha = 1.0
            colorramp_1.color_ramp.elements[1].color = (1.0, 1.0, 1.0, 1.0)
            colorramp_1.color_ramp.elements[1].position = 0.24870474636554718
            colorramp_1.color_ramp.hue_interpolation = 'NEAR'
            colorramp_1.color_ramp.interpolation = 'EASE'
            colorramp_1.hide = False
            colorramp_1.location = (-191.0001678466797, 123.82817077636719)
            colorramp_1.mute = False
            colorramp_1.name = 'ColorRamp'
            colorramp_1.use_custom_color = False
            colorramp_1.width = 320.0
            colorramp_1.inputs[0].default_value = 0.5
            colorramp_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            colorramp_1.outputs[1].default_value = 0.0

            reroute_1 = node_tree1.nodes.new('NodeReroute')
            reroute_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            reroute_1.hide = False
            reroute_1.location = (49.12303161621094, 22.004796981811523)
            reroute_1.mute = False
            reroute_1.name = 'Reroute'
            reroute_1.use_custom_color = False
            reroute_1.width = 16.0

            group_output_1 = node_tree1.nodes.new('NodeGroupOutput')
            group_output_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            group_output_1.hide = False
            group_output_1.is_active_output = True
            group_output_1.location = (1308.7017822265625, -57.550865173339844)
            group_output_1.mute = False
            group_output_1.name = 'Group Output'
            group_output_1.use_custom_color = False
            group_output_1.width = 140.0
            group_output_1.inputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_1.blend_type = 'VALUE'
            mix_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_1.hide = True
            mix_1.location = (552.4007568359375, -66.55184936523438)
            mix_1.mute = False
            mix_1.name = 'Mix'
            mix_1.use_alpha = True
            mix_1.use_clamp = False
            mix_1.use_custom_color = False
            mix_1.width = 153.52993774414062
            mix_1.inputs[0].default_value = 1.0
            mix_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            invert_001_1 = node_tree1.nodes.new('CompositorNodeInvert')
            invert_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            invert_001_1.hide = True
            invert_001_1.invert_alpha = False
            invert_001_1.invert_rgb = True
            invert_001_1.location = (245.9341278076172, -113.9513168334961)
            invert_001_1.mute = False
            invert_001_1.name = 'Invert.001'
            invert_001_1.use_custom_color = False
            invert_001_1.width = 140.0
            invert_001_1.inputs[0].default_value = 1.0
            invert_001_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            invert_001_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_001_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_001_1.blend_type = 'VALUE'
            mix_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_001_1.hide = True
            mix_001_1.location = (552.4007568359375, -113.13603973388672)
            mix_001_1.mute = False
            mix_001_1.name = 'Mix.001'
            mix_001_1.use_alpha = True
            mix_001_1.use_clamp = False
            mix_001_1.use_custom_color = False
            mix_001_1.width = 153.52993774414062
            mix_001_1.inputs[0].default_value = 1.0
            mix_001_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_001_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_001_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_003_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_003_1.blend_type = 'MIX'
            mix_003_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_003_1.hide = True
            mix_003_1.location = (757.84326171875, -110.664794921875)
            mix_003_1.mute = False
            mix_003_1.name = 'Mix.003'
            mix_003_1.use_alpha = False
            mix_003_1.use_clamp = False
            mix_003_1.use_custom_color = False
            mix_003_1.width = 140.0
            mix_003_1.inputs[0].default_value = 2.0
            mix_003_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_003_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_003_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_002_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_002_1.blend_type = 'MIX'
            mix_002_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_002_1.hide = True
            mix_002_1.location = (755.5724487304688, -67.10868072509766)
            mix_002_1.mute = False
            mix_002_1.name = 'Mix.002'
            mix_002_1.use_alpha = False
            mix_002_1.use_clamp = False
            mix_002_1.use_custom_color = False
            mix_002_1.width = 140.0
            mix_002_1.inputs[0].default_value = 1.0
            mix_002_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_002_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_002_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_004_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_004_1.blend_type = 'MIX'
            mix_004_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_004_1.hide = True
            mix_004_1.location = (925.0614013671875, -89.7184066772461)
            mix_004_1.mute = False
            mix_004_1.name = 'Mix.004'
            mix_004_1.use_alpha = False
            mix_004_1.use_clamp = False
            mix_004_1.use_custom_color = False
            mix_004_1.width = 140.0
            mix_004_1.inputs[0].default_value = 0.5
            mix_004_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_004_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_004_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_005_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_005_1.blend_type = 'MIX'
            mix_005_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_005_1.hide = True
            mix_005_1.location = (1115.6046142578125, -89.73394775390625)
            mix_005_1.mute = False
            mix_005_1.name = 'Mix.005'
            mix_005_1.use_alpha = False
            mix_005_1.use_clamp = False
            mix_005_1.use_custom_color = False
            mix_005_1.width = 140.0
            mix_005_1.inputs[0].default_value = 1.0
            mix_005_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_005_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_005_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            translate_1 = node_tree1.nodes.new('CompositorNodeTranslate')
            translate_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            translate_1.hide = True
            translate_1.location = (-485.753662109375, -411.6445617675781)
            translate_1.mute = False
            translate_1.name = 'Translate'
            translate_1.use_custom_color = False
            translate_1.use_relative = False
            translate_1.width = 140.0
            translate_1.wrap_axis = 'BOTH'
            translate_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            translate_1.inputs[1].default_value = 0.0
            translate_1.inputs[2].default_value = 0.0
            translate_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            transform_1 = node_tree1.nodes.new('CompositorNodeTransform')
            transform_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            transform_1.filter_type = 'NEAREST'
            transform_1.hide = False
            transform_1.location = (-216.620361328125, -329.40924072265625)
            transform_1.mute = False
            transform_1.name = 'Transform'
            transform_1.use_custom_color = False
            transform_1.width = 140.0
            transform_1.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            transform_1.inputs[1].default_value = 0.0
            transform_1.inputs[2].default_value = 0.0
            transform_1.inputs[3].default_value = 0.0
            transform_1.inputs[4].default_value = 1.0
            transform_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            invert_1 = node_tree1.nodes.new('CompositorNodeInvert')
            invert_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            invert_1.hide = True
            invert_1.invert_alpha = False
            invert_1.invert_rgb = True
            invert_1.location = (356.48980712890625, -67.36713409423828)
            invert_1.mute = False
            invert_1.name = 'Invert'
            invert_1.use_custom_color = False
            invert_1.width = 140.0
            invert_1.inputs[0].default_value = 1.0
            invert_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            invert_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            group_input_1 = node_tree1.nodes.new('NodeGroupInput')
            group_input_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            group_input_1.hide = False
            group_input_1.location = (-925.753662109375, 181.09393310546875)
            group_input_1.mute = False
            group_input_1.name = 'Group Input'
            group_input_1.use_custom_color = False
            group_input_1.width = 140.0
            group_input_1.outputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
            group_input_1.outputs[1].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            group_input_1.outputs[2].default_value = 0.0
            group_input_1.outputs[3].default_value = 0.0
            group_input_1.outputs[4].default_value = 0.0
            group_input_1.outputs[5].default_value = 0.0
            group_input_1.outputs[6].default_value = 0.0
            group_input_1.outputs[7].default_value = 0.0
            group_input_1.outputs[8].default_value = 0.0
            group_input_1.outputs[9].default_value = 0.0

            invert_002_1 = node_tree1.nodes.new('CompositorNodeInvert')
            invert_002_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            invert_002_1.hide = True
            invert_002_1.invert_alpha = False
            invert_002_1.invert_rgb = True
            invert_002_1.location = (-669.486572265625, -401.89971923828125)
            invert_002_1.mute = False
            invert_002_1.name = 'Invert.002'
            invert_002_1.use_custom_color = False
            invert_002_1.width = 140.0
            invert_002_1.inputs[0].default_value = 1.0
            invert_002_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            invert_002_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            # LINKS
            node_tree1.links.new(invert_1.outputs[0], mix_1.inputs[2])
            node_tree1.links.new(invert_001_1.outputs[0], mix_001_1.inputs[0])
            node_tree1.links.new(mix_004_1.outputs[0], mix_005_1.inputs[2])
            node_tree1.links.new(mix_1.outputs[0], mix_002_1.inputs[2])
            node_tree1.links.new(mix_001_1.outputs[0], mix_003_1.inputs[2])
            node_tree1.links.new(mix_003_1.outputs[0], mix_004_1.inputs[2])
            node_tree1.links.new(mix_002_1.outputs[0], mix_004_1.inputs[1])
            node_tree1.links.new(transform_1.outputs[0], mix_001_1.inputs[2])
            node_tree1.links.new(transform_1.outputs[0], invert_1.inputs[1])
            node_tree1.links.new(group_input_1.outputs[0], reroute_1.inputs[0])
            node_tree1.links.new(reroute_1.outputs[0], mix_1.inputs[1])
            node_tree1.links.new(reroute_1.outputs[0], mix_002_1.inputs[1])
            node_tree1.links.new(reroute_1.outputs[0], mix_001_1.inputs[1])
            node_tree1.links.new(reroute_1.outputs[0], mix_003_1.inputs[1])
            node_tree1.links.new(colorramp_1.outputs[0], mix_1.inputs[0])
            node_tree1.links.new(colorramp_1.outputs[0], invert_001_1.inputs[1])
            node_tree1.links.new(group_input_1.outputs[4], transform_1.inputs[1])
            node_tree1.links.new(group_input_1.outputs[5], transform_1.inputs[2])
            node_tree1.links.new(group_input_1.outputs[2], transform_1.inputs[4])
            node_tree1.links.new(group_input_1.outputs[7], mix_002_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[8], mix_003_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[9], mix_004_1.inputs[0])
            node_tree1.links.new(mix_005_1.outputs[0], group_output_1.inputs[0])
            node_tree1.links.new(reroute_1.outputs[0], mix_005_1.inputs[1])
            node_tree1.links.new(group_input_1.outputs[6], mix_005_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[1], invert_002_1.inputs[1])
            node_tree1.links.new(translate_1.outputs[0], transform_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[0], colorramp_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[3], transform_1.inputs[3])
            node_tree1.links.new(invert_002_1.outputs[0], translate_1.inputs[0])

        watermark_lv1_0 = scene.node_tree.nodes.new('CompositorNodeGroup')
        watermark_lv1_0.node_tree = bpy_data.node_groups.get('Watermark Level 1')
        watermark_lv1_0.color = (1.0, 0.0, 0.8082889914512634)
        watermark_lv1_0.hide = False
        watermark_lv1_0.label = 'Watermark'
        watermark_lv1_0.location = (0.0, 0.0)
        watermark_lv1_0.mute = False
        watermark_lv1_0.name = 'Watermark_lv1'
        watermark_lv1_0.use_custom_color = False
        watermark_lv1_0.width = 301.3756103515625
        watermark_lv1_0.inputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
        watermark_lv1_0.inputs[1].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
        watermark_lv1_0.inputs[2].default_value = 0.5
        watermark_lv1_0.inputs[3].default_value = 0.7853981852531433
        watermark_lv1_0.inputs[4].default_value = 0.0
        watermark_lv1_0.inputs[5].default_value = 0.0
        watermark_lv1_0.inputs[6].default_value = 0.5
        watermark_lv1_0.inputs[7].default_value = 1.0
        watermark_lv1_0.inputs[8].default_value = 1.0
        watermark_lv1_0.inputs[9].default_value = 0.5
        watermark_lv1_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

        image_001_0 = scene.node_tree.nodes.new('CompositorNodeImage')
        image_001_0.color = (0.0, 1.0, 1.0)
        image_001_0.frame_duration = 1
        image_001_0.frame_offset = -1
        image_001_0.frame_start = 1
        image_001_0.hide = False
        image_001_0.location = (-294.5710144042969, -111.08281707763672)
        image_001_0.mute = False
        image_001_0.name = 'Image.001'
        image_001_0.use_auto_refresh = True
        image_001_0.use_custom_color = False
        image_001_0.use_cyclic = False
        image_001_0.use_straight_alpha_output = False
        image_001_0.width = 230.5516815185547
        image_001_0.outputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
        image_001_0.outputs[1].default_value = 0.0

        # LINKS
        scene.node_tree.links.new(image_001_0.outputs[0], watermark_lv1_0.inputs[1])

        return watermark_lv1_0, image_001_0

    @classmethod
    def _watermark_lv2(cls, scene, bpy_data):
        # add watermark level 2
        # NODES
        image_001_0 = scene.node_tree.nodes.new('CompositorNodeImage')
        image_001_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        image_001_0.frame_duration = 1
        image_001_0.frame_offset = -1
        image_001_0.frame_start = 1
        image_001_0.hide = False
        image_001_0.location = (-280.0, -200.0)
        image_001_0.mute = False
        image_001_0.name = 'Image.001'
        image_001_0.use_auto_refresh = False
        image_001_0.use_custom_color = False
        image_001_0.use_cyclic = False
        image_001_0.use_straight_alpha_output = False
        image_001_0.width = 210.0883026123047
        image_001_0.outputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
        image_001_0.outputs[1].default_value = 0.0

        node_tree1 = bpy_data.node_groups.get('Watermark Level 2')
        if not node_tree1:
            node_tree1 = bpy_data.node_groups.new('Watermark Level 2', 'CompositorNodeTree')
            # INPUTS
            node_tree1.inputs.new('NodeSocketColor', 'Render Layers')
            node_tree1.inputs.new('NodeSocketColor', 'Watermark Image')
            node_tree1.inputs.new('NodeSocketFloat', 'Scale')
            node_tree1.inputs.new('NodeSocketFloat', 'Rotation (deg)')
            node_tree1.inputs.new('NodeSocketFloat', 'Offset X')
            node_tree1.inputs.new('NodeSocketFloat', 'Offset Y')
            node_tree1.inputs.new('NodeSocketFloat', 'Intensity')
            node_tree1.inputs.new('NodeSocketFloat', 'Blur')
            node_tree1.inputs.new('NodeSocketShader', '# Additional params')
            node_tree1.inputs.new('NodeSocketFloat', 'Intensity 0-25% ')
            node_tree1.inputs.new('NodeSocketFloat', 'Intensity 25-50%')
            node_tree1.inputs.new('NodeSocketFloat', 'Intensity 50-75%')
            node_tree1.inputs.new('NodeSocketFloat', 'Intensity 75-98%')
            node_tree1.inputs.new('NodeSocketFloat', 'Intensity 98-100%')
            node_tree1.inputs.new('NodeSocketFloat', 'Multiply Effect')
            node_tree1.inputs.new('NodeSocketFloat', 'Blur Mask')
            # OUTPUTS
            node_tree1.outputs.new('NodeSocketColor', 'Image')
            node_tree1.outputs.new('NodeSocketShader', '# Additional params')
            node_tree1.outputs.new('NodeSocketColor', '0-25')
            node_tree1.outputs.new('NodeSocketColor', '25-50')
            node_tree1.outputs.new('NodeSocketColor', '50-75')
            node_tree1.outputs.new('NodeSocketColor', '75-98')
            node_tree1.outputs.new('NodeSocketColor', '98-100')
            # NODES
            frame_1 = node_tree1.nodes.new('NodeFrame')
            frame_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            frame_1.hide = False
            frame_1.label = 'mask'
            frame_1.label_size = 20
            frame_1.location = (-248.23880004882812, 338.5074462890625)
            frame_1.mute = False
            frame_1.name = 'Frame'
            frame_1.shrink = True
            frame_1.use_custom_color = False
            frame_1.width = 1304.2984619140625

            frame_003_1 = node_tree1.nodes.new('NodeFrame')
            frame_003_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            frame_003_1.hide = False
            frame_003_1.label = 'Multipli effect'
            frame_003_1.label_size = 20
            frame_003_1.location = (2196.178955078125, -248.23880004882812)
            frame_003_1.mute = False
            frame_003_1.name = 'Frame.003'
            frame_003_1.shrink = True
            frame_003_1.use_custom_color = False
            frame_003_1.width = 440.0

            frame_004_1 = node_tree1.nodes.new('NodeFrame')
            frame_004_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            frame_004_1.hide = False
            frame_004_1.label = 'Power'
            frame_004_1.label_size = 20
            frame_004_1.location = (2647.522216796875, -383.64178466796875)
            frame_004_1.mute = False
            frame_004_1.name = 'Frame.004'
            frame_004_1.shrink = True
            frame_004_1.use_custom_color = False
            frame_004_1.width = 372.477783203125

            frame_002_1 = node_tree1.nodes.new('NodeFrame')
            frame_002_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            frame_002_1.hide = False
            frame_002_1.label = 'Add'
            frame_002_1.label_size = 20
            frame_002_1.location = (977.5521850585938, 180.5373077392578)
            frame_002_1.mute = False
            frame_002_1.name = 'Frame.002'
            frame_002_1.shrink = True
            frame_002_1.use_custom_color = False
            frame_002_1.width = 758.63525390625

            frame_001_1 = node_tree1.nodes.new('NodeFrame')
            frame_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            frame_001_1.hide = False
            frame_001_1.label = 'blur'
            frame_001_1.label_size = 20
            frame_001_1.location = (60.0, -240.0)
            frame_001_1.mute = False
            frame_001_1.name = 'Frame.001'
            frame_001_1.shrink = True
            frame_001_1.use_custom_color = False
            frame_001_1.width = 372.8358154296875

            transform_1 = node_tree1.nodes.new('NodeFrame')
            transform_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            transform_1.hide = False
            transform_1.label = 'transform'
            transform_1.label_size = 20
            transform_1.location = (-880.0, -220.0)
            transform_1.mute = False
            transform_1.name = 'transform'
            transform_1.shrink = True
            transform_1.use_custom_color = False
            transform_1.width = 900.0

            colorramp_004_1 = node_tree1.nodes.new('CompositorNodeValToRGB')
            colorramp_004_1.parent = node_tree1.nodes.get('Frame')
            colorramp_004_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            colorramp_004_1.color_ramp.color_mode = 'RGB'
            if 0 >= len(colorramp_004_1.color_ramp.elements):
                colorramp_004_1.color_ramp.elements.new(0.004310344811528921)
            colorramp_004_1.color_ramp.elements[0].alpha = 1.0
            colorramp_004_1.color_ramp.elements[0].color = (1.0, 1.0, 1.0, 1.0)
            colorramp_004_1.color_ramp.elements[0].position = 0.004310344811528921
            if 1 >= len(colorramp_004_1.color_ramp.elements):
                colorramp_004_1.color_ramp.elements.new(0.9800000190734863)
            colorramp_004_1.color_ramp.elements[1].alpha = 1.0
            colorramp_004_1.color_ramp.elements[1].color = (0.0, 0.0, 0.0, 1.0)
            colorramp_004_1.color_ramp.elements[1].position = 0.9800000190734863
            colorramp_004_1.color_ramp.hue_interpolation = 'NEAR'
            colorramp_004_1.color_ramp.interpolation = 'CONSTANT'
            colorramp_004_1.hide = True
            colorramp_004_1.label = '98-100'
            colorramp_004_1.location = (-404.71636962890625, 23.64178466796875)
            colorramp_004_1.mute = False
            colorramp_004_1.name = 'ColorRamp.004'
            colorramp_004_1.use_custom_color = False
            colorramp_004_1.width = 240.0
            colorramp_004_1.inputs[0].default_value = 0.5
            colorramp_004_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            colorramp_004_1.outputs[1].default_value = 0.0

            colorramp_1 = node_tree1.nodes.new('CompositorNodeValToRGB')
            colorramp_1.parent = node_tree1.nodes.get('Frame')
            colorramp_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            colorramp_1.color_ramp.color_mode = 'RGB'
            if 0 >= len(colorramp_1.color_ramp.elements):
                colorramp_1.color_ramp.elements.new(0.0)
            colorramp_1.color_ramp.elements[0].alpha = 1.0
            colorramp_1.color_ramp.elements[0].color = (0.0, 0.0, 0.0, 1.0)
            colorramp_1.color_ramp.elements[0].position = 0.0
            if 1 >= len(colorramp_1.color_ramp.elements):
                colorramp_1.color_ramp.elements.new(0.25)
            colorramp_1.color_ramp.elements[1].alpha = 1.0
            colorramp_1.color_ramp.elements[1].color = (1.0, 1.0, 1.0, 1.0)
            colorramp_1.color_ramp.elements[1].position = 0.25
            colorramp_1.color_ramp.hue_interpolation = 'NEAR'
            colorramp_1.color_ramp.interpolation = 'CONSTANT'
            colorramp_1.hide = True
            colorramp_1.label = '0-25'
            colorramp_1.location = (-404.71636962890625, -21.4925537109375)
            colorramp_1.mute = False
            colorramp_1.name = 'ColorRamp'
            colorramp_1.use_custom_color = False
            colorramp_1.width = 240.0
            colorramp_1.inputs[0].default_value = 0.5
            colorramp_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            colorramp_1.outputs[1].default_value = 0.0

            colorramp_001_1 = node_tree1.nodes.new('CompositorNodeValToRGB')
            colorramp_001_1.parent = node_tree1.nodes.get('Frame')
            colorramp_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            colorramp_001_1.color_ramp.color_mode = 'RGB'
            if 0 >= len(colorramp_001_1.color_ramp.elements):
                colorramp_001_1.color_ramp.elements.new(0.24899999797344208)
            colorramp_001_1.color_ramp.elements[0].alpha = 1.0
            colorramp_001_1.color_ramp.elements[0].color = (1.0, 1.0, 1.0, 1.0)
            colorramp_001_1.color_ramp.elements[0].position = 0.24899999797344208
            if 1 >= len(colorramp_001_1.color_ramp.elements):
                colorramp_001_1.color_ramp.elements.new(0.25)
            colorramp_001_1.color_ramp.elements[1].alpha = 1.0
            colorramp_001_1.color_ramp.elements[1].color = (0.0, 0.0, 0.0, 1.0)
            colorramp_001_1.color_ramp.elements[1].position = 0.25
            if 2 >= len(colorramp_001_1.color_ramp.elements):
                colorramp_001_1.color_ramp.elements.new(0.5)
            colorramp_001_1.color_ramp.elements[2].alpha = 1.0
            colorramp_001_1.color_ramp.elements[2].color = (1.0, 1.0, 1.0, 1.0)
            colorramp_001_1.color_ramp.elements[2].position = 0.5
            colorramp_001_1.color_ramp.hue_interpolation = 'NEAR'
            colorramp_001_1.color_ramp.interpolation = 'CONSTANT'
            colorramp_001_1.hide = True
            colorramp_001_1.label = '25-50'
            colorramp_001_1.location = (-404.71636962890625, -66.62686157226562)
            colorramp_001_1.mute = False
            colorramp_001_1.name = 'ColorRamp.001'
            colorramp_001_1.use_custom_color = False
            colorramp_001_1.width = 240.0
            colorramp_001_1.inputs[0].default_value = 0.5
            colorramp_001_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            colorramp_001_1.outputs[1].default_value = 0.0

            separate_hsva_1 = node_tree1.nodes.new('CompositorNodeSepHSVA')
            separate_hsva_1.parent = node_tree1.nodes.get('Frame')
            separate_hsva_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            separate_hsva_1.hide = True
            separate_hsva_1.location = (-630.3880615234375, -66.62686157226562)
            separate_hsva_1.mute = False
            separate_hsva_1.name = 'Separate HSVA'
            separate_hsva_1.use_custom_color = False
            separate_hsva_1.width = 140.0
            separate_hsva_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            separate_hsva_1.outputs[0].default_value = 0.0
            separate_hsva_1.outputs[1].default_value = 0.0
            separate_hsva_1.outputs[2].default_value = 0.0
            separate_hsva_1.outputs[3].default_value = 0.0

            colorramp_002_1 = node_tree1.nodes.new('CompositorNodeValToRGB')
            colorramp_002_1.parent = node_tree1.nodes.get('Frame')
            colorramp_002_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            colorramp_002_1.color_ramp.color_mode = 'RGB'
            if 0 >= len(colorramp_002_1.color_ramp.elements):
                colorramp_002_1.color_ramp.elements.new(0.49000000953674316)
            colorramp_002_1.color_ramp.elements[0].alpha = 1.0
            colorramp_002_1.color_ramp.elements[0].color = (1.0, 1.0, 1.0, 1.0)
            colorramp_002_1.color_ramp.elements[0].position = 0.49000000953674316
            if 1 >= len(colorramp_002_1.color_ramp.elements):
                colorramp_002_1.color_ramp.elements.new(0.5)
            colorramp_002_1.color_ramp.elements[1].alpha = 1.0
            colorramp_002_1.color_ramp.elements[1].color = (0.0, 0.0, 0.0, 1.0)
            colorramp_002_1.color_ramp.elements[1].position = 0.5
            if 2 >= len(colorramp_002_1.color_ramp.elements):
                colorramp_002_1.color_ramp.elements.new(0.75)
            colorramp_002_1.color_ramp.elements[2].alpha = 1.0
            colorramp_002_1.color_ramp.elements[2].color = (1.0, 1.0, 1.0, 1.0)
            colorramp_002_1.color_ramp.elements[2].position = 0.75
            colorramp_002_1.color_ramp.hue_interpolation = 'NEAR'
            colorramp_002_1.color_ramp.interpolation = 'CONSTANT'
            colorramp_002_1.hide = True
            colorramp_002_1.label = '50-75'
            colorramp_002_1.location = (-404.71636962890625, -111.76119995117188)
            colorramp_002_1.mute = False
            colorramp_002_1.name = 'ColorRamp.002'
            colorramp_002_1.use_custom_color = False
            colorramp_002_1.width = 240.0
            colorramp_002_1.inputs[0].default_value = 0.5
            colorramp_002_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            colorramp_002_1.outputs[1].default_value = 0.0

            colorramp_003_1 = node_tree1.nodes.new('CompositorNodeValToRGB')
            colorramp_003_1.parent = node_tree1.nodes.get('Frame')
            colorramp_003_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            colorramp_003_1.color_ramp.color_mode = 'RGB'
            if 0 >= len(colorramp_003_1.color_ramp.elements):
                colorramp_003_1.color_ramp.elements.new(0.7490000128746033)
            colorramp_003_1.color_ramp.elements[0].alpha = 1.0
            colorramp_003_1.color_ramp.elements[0].color = (1.0, 1.0, 1.0, 1.0)
            colorramp_003_1.color_ramp.elements[0].position = 0.7490000128746033
            if 1 >= len(colorramp_003_1.color_ramp.elements):
                colorramp_003_1.color_ramp.elements.new(0.75)
            colorramp_003_1.color_ramp.elements[1].alpha = 1.0
            colorramp_003_1.color_ramp.elements[1].color = (0.0, 0.0, 0.0, 1.0)
            colorramp_003_1.color_ramp.elements[1].position = 0.75
            if 2 >= len(colorramp_003_1.color_ramp.elements):
                colorramp_003_1.color_ramp.elements.new(1.0)
            colorramp_003_1.color_ramp.elements[2].alpha = 1.0
            colorramp_003_1.color_ramp.elements[2].color = (1.0, 1.0, 1.0, 1.0)
            colorramp_003_1.color_ramp.elements[2].position = 1.0
            colorramp_003_1.color_ramp.hue_interpolation = 'NEAR'
            colorramp_003_1.color_ramp.interpolation = 'CONSTANT'
            colorramp_003_1.hide = True
            colorramp_003_1.label = '75-98'
            colorramp_003_1.location = (-404.71636962890625, -156.89552307128906)
            colorramp_003_1.mute = False
            colorramp_003_1.name = 'ColorRamp.003'
            colorramp_003_1.use_custom_color = False
            colorramp_003_1.width = 240.0
            colorramp_003_1.inputs[0].default_value = 0.5
            colorramp_003_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            colorramp_003_1.outputs[1].default_value = 0.0

            math_008_1 = node_tree1.nodes.new('CompositorNodeMath')
            math_008_1.parent = node_tree1.nodes.get('Frame')
            math_008_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            math_008_1.hide = True
            math_008_1.location = (-135.40298461914062, -90.26864624023438)
            math_008_1.mute = False
            math_008_1.name = 'Math.008'
            math_008_1.operation = 'ADD'
            math_008_1.use_clamp = False
            math_008_1.use_custom_color = False
            math_008_1.width = 136.99957275390625
            math_008_1.inputs[0].default_value = 0.0
            math_008_1.inputs[1].default_value = -100.0
            math_008_1.inputs[2].default_value = 0.0
            math_008_1.outputs[0].default_value = 0.0

            math_009_1 = node_tree1.nodes.new('CompositorNodeMath')
            math_009_1.parent = node_tree1.nodes.get('Frame')
            math_009_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            math_009_1.hide = True
            math_009_1.location = (-135.40298461914062, -45.134307861328125)
            math_009_1.mute = False
            math_009_1.name = 'Math.009'
            math_009_1.operation = 'ADD'
            math_009_1.use_clamp = False
            math_009_1.use_custom_color = False
            math_009_1.width = 136.99957275390625
            math_009_1.inputs[0].default_value = 0.0
            math_009_1.inputs[1].default_value = -100.0
            math_009_1.inputs[2].default_value = 0.0
            math_009_1.outputs[0].default_value = 0.0

            math_006_1 = node_tree1.nodes.new('CompositorNodeMath')
            math_006_1.parent = node_tree1.nodes.get('Frame')
            math_006_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            math_006_1.hide = True
            math_006_1.location = (-135.40298461914062, -180.5373077392578)
            math_006_1.mute = False
            math_006_1.name = 'Math.006'
            math_006_1.operation = 'ADD'
            math_006_1.use_clamp = False
            math_006_1.use_custom_color = False
            math_006_1.width = 136.99957275390625
            math_006_1.inputs[0].default_value = 0.0
            math_006_1.inputs[1].default_value = -100.0
            math_006_1.inputs[2].default_value = 0.0
            math_006_1.outputs[0].default_value = 0.0

            math_007_1 = node_tree1.nodes.new('CompositorNodeMath')
            math_007_1.parent = node_tree1.nodes.get('Frame')
            math_007_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            math_007_1.hide = True
            math_007_1.location = (-135.40298461914062, -135.40296936035156)
            math_007_1.mute = False
            math_007_1.name = 'Math.007'
            math_007_1.operation = 'ADD'
            math_007_1.use_clamp = False
            math_007_1.use_custom_color = False
            math_007_1.width = 136.99957275390625
            math_007_1.inputs[0].default_value = 0.0
            math_007_1.inputs[1].default_value = -100.0
            math_007_1.inputs[2].default_value = 0.0
            math_007_1.outputs[0].default_value = 0.0

            invert_011_1 = node_tree1.nodes.new('CompositorNodeInvert')
            invert_011_1.parent = node_tree1.nodes.get('Frame')
            invert_011_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            invert_011_1.hide = True
            invert_011_1.invert_alpha = True
            invert_011_1.invert_rgb = True
            invert_011_1.location = (473.9104309082031, -67.70147705078125)
            invert_011_1.mute = False
            invert_011_1.name = 'Invert.011'
            invert_011_1.use_custom_color = False
            invert_011_1.width = 140.0
            invert_011_1.inputs[0].default_value = 1.0
            invert_011_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            invert_011_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            invert_010_1 = node_tree1.nodes.new('CompositorNodeInvert')
            invert_010_1.parent = node_tree1.nodes.get('Frame')
            invert_010_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            invert_010_1.hide = True
            invert_010_1.invert_alpha = True
            invert_010_1.invert_rgb = True
            invert_010_1.location = (473.9104309082031, -22.567169189453125)
            invert_010_1.mute = False
            invert_010_1.name = 'Invert.010'
            invert_010_1.use_custom_color = False
            invert_010_1.width = 140.0
            invert_010_1.inputs[0].default_value = 1.0
            invert_010_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            invert_010_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            invert_009_1 = node_tree1.nodes.new('CompositorNodeInvert')
            invert_009_1.parent = node_tree1.nodes.get('Frame')
            invert_009_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            invert_009_1.hide = True
            invert_009_1.invert_alpha = True
            invert_009_1.invert_rgb = True
            invert_009_1.location = (473.9104309082031, 22.567169189453125)
            invert_009_1.mute = False
            invert_009_1.name = 'Invert.009'
            invert_009_1.use_custom_color = False
            invert_009_1.width = 140.0
            invert_009_1.inputs[0].default_value = 1.0
            invert_009_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            invert_009_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            invert_013_1 = node_tree1.nodes.new('CompositorNodeInvert')
            invert_013_1.parent = node_tree1.nodes.get('Frame')
            invert_013_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            invert_013_1.hide = True
            invert_013_1.invert_alpha = True
            invert_013_1.invert_rgb = True
            invert_013_1.location = (473.9104309082031, -157.9701385498047)
            invert_013_1.mute = False
            invert_013_1.name = 'Invert.013'
            invert_013_1.use_custom_color = False
            invert_013_1.width = 140.0
            invert_013_1.inputs[0].default_value = 1.0
            invert_013_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            invert_013_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            invert_012_1 = node_tree1.nodes.new('CompositorNodeInvert')
            invert_012_1.parent = node_tree1.nodes.get('Frame')
            invert_012_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            invert_012_1.hide = True
            invert_012_1.invert_alpha = True
            invert_012_1.invert_rgb = True
            invert_012_1.location = (473.9104309082031, -112.8358154296875)
            invert_012_1.mute = False
            invert_012_1.name = 'Invert.012'
            invert_012_1.use_custom_color = False
            invert_012_1.width = 140.0
            invert_012_1.inputs[0].default_value = 1.0
            invert_012_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            invert_012_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            blur_005_1 = node_tree1.nodes.new('CompositorNodeBlur')
            blur_005_1.parent = node_tree1.nodes.get('Frame')
            blur_005_1.aspect_correction = 'NONE'
            blur_005_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            blur_005_1.factor = 0.0
            blur_005_1.factor_x = 0.0
            blur_005_1.factor_y = 0.0
            blur_005_1.filter_type = 'FAST_GAUSS'
            blur_005_1.hide = True
            blur_005_1.location = (315.9403076171875, -157.9701385498047)
            blur_005_1.mute = False
            blur_005_1.name = 'Blur.005'
            blur_005_1.size_x = 10
            blur_005_1.size_y = 10
            blur_005_1.use_bokeh = False
            blur_005_1.use_custom_color = False
            blur_005_1.use_extended_bounds = False
            blur_005_1.use_gamma_correction = False
            blur_005_1.use_relative = False
            blur_005_1.use_variable_size = False
            blur_005_1.width = 140.0
            blur_005_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            blur_005_1.inputs[1].default_value = 1.0
            blur_005_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            blur_004_1 = node_tree1.nodes.new('CompositorNodeBlur')
            blur_004_1.parent = node_tree1.nodes.get('Frame')
            blur_004_1.aspect_correction = 'NONE'
            blur_004_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            blur_004_1.factor = 0.0
            blur_004_1.factor_x = 0.0
            blur_004_1.factor_y = 0.0
            blur_004_1.filter_type = 'FAST_GAUSS'
            blur_004_1.hide = True
            blur_004_1.location = (315.9403076171875, -112.8358154296875)
            blur_004_1.mute = False
            blur_004_1.name = 'Blur.004'
            blur_004_1.size_x = 10
            blur_004_1.size_y = 10
            blur_004_1.use_bokeh = False
            blur_004_1.use_custom_color = False
            blur_004_1.use_extended_bounds = False
            blur_004_1.use_gamma_correction = False
            blur_004_1.use_relative = False
            blur_004_1.use_variable_size = False
            blur_004_1.width = 140.0
            blur_004_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            blur_004_1.inputs[1].default_value = 1.0
            blur_004_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            blur_003_1 = node_tree1.nodes.new('CompositorNodeBlur')
            blur_003_1.parent = node_tree1.nodes.get('Frame')
            blur_003_1.aspect_correction = 'NONE'
            blur_003_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            blur_003_1.factor = 0.0
            blur_003_1.factor_x = 0.0
            blur_003_1.factor_y = 0.0
            blur_003_1.filter_type = 'FAST_GAUSS'
            blur_003_1.hide = True
            blur_003_1.location = (315.9403076171875, -67.70147705078125)
            blur_003_1.mute = False
            blur_003_1.name = 'Blur.003'
            blur_003_1.size_x = 10
            blur_003_1.size_y = 10
            blur_003_1.use_bokeh = False
            blur_003_1.use_custom_color = False
            blur_003_1.use_extended_bounds = False
            blur_003_1.use_gamma_correction = False
            blur_003_1.use_relative = False
            blur_003_1.use_variable_size = False
            blur_003_1.width = 140.0
            blur_003_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            blur_003_1.inputs[1].default_value = 1.0
            blur_003_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            blur_002_1 = node_tree1.nodes.new('CompositorNodeBlur')
            blur_002_1.parent = node_tree1.nodes.get('Frame')
            blur_002_1.aspect_correction = 'NONE'
            blur_002_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            blur_002_1.factor = 0.0
            blur_002_1.factor_x = 0.0
            blur_002_1.factor_y = 0.0
            blur_002_1.filter_type = 'FAST_GAUSS'
            blur_002_1.hide = True
            blur_002_1.location = (315.9403076171875, -22.567169189453125)
            blur_002_1.mute = False
            blur_002_1.name = 'Blur.002'
            blur_002_1.size_x = 10
            blur_002_1.size_y = 10
            blur_002_1.use_bokeh = False
            blur_002_1.use_custom_color = False
            blur_002_1.use_extended_bounds = False
            blur_002_1.use_gamma_correction = False
            blur_002_1.use_relative = False
            blur_002_1.use_variable_size = False
            blur_002_1.width = 140.0
            blur_002_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            blur_002_1.inputs[1].default_value = 1.0
            blur_002_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            blur_001_1 = node_tree1.nodes.new('CompositorNodeBlur')
            blur_001_1.parent = node_tree1.nodes.get('Frame')
            blur_001_1.aspect_correction = 'NONE'
            blur_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            blur_001_1.factor = 0.0
            blur_001_1.factor_x = 0.0
            blur_001_1.factor_y = 0.0
            blur_001_1.filter_type = 'FAST_GAUSS'
            blur_001_1.hide = True
            blur_001_1.location = (315.9403076171875, 22.567169189453125)
            blur_001_1.mute = False
            blur_001_1.name = 'Blur.001'
            blur_001_1.size_x = 10
            blur_001_1.size_y = 10
            blur_001_1.use_bokeh = False
            blur_001_1.use_custom_color = False
            blur_001_1.use_extended_bounds = False
            blur_001_1.use_gamma_correction = False
            blur_001_1.use_relative = False
            blur_001_1.use_variable_size = False
            blur_001_1.width = 140.0
            blur_001_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            blur_001_1.inputs[1].default_value = 1.0
            blur_001_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            rgb_curves_009_1 = node_tree1.nodes.new('CompositorNodeCurveRGB')
            rgb_curves_009_1.parent = node_tree1.nodes.get('Frame')
            rgb_curves_009_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            rgb_curves_009_1.hide = True
            rgb_curves_009_1.location = (45.13432312011719, -157.9701385498047)
            rgb_curves_009_1.mapping.black_level = (0.0, 0.0, 0.0)
            rgb_curves_009_1.mapping.clip_max_x = 1.0
            rgb_curves_009_1.mapping.clip_max_y = 1.0
            rgb_curves_009_1.mapping.clip_min_x = 0.0
            rgb_curves_009_1.mapping.clip_min_y = 0.0
            if 0 >= len(rgb_curves_009_1.mapping.curves[0].points):
                rgb_curves_009_1.mapping.curves[0].points.new(0.0, 0.0)
            rgb_curves_009_1.mapping.curves[0].points[0].handle_type = 'AUTO'
            rgb_curves_009_1.mapping.curves[0].points[0].location = (0.0, 0.0)
            rgb_curves_009_1.mapping.curves[0].points[0].select = False
            if 1 >= len(rgb_curves_009_1.mapping.curves[0].points):
                rgb_curves_009_1.mapping.curves[0].points.new(1.0, 1.0)
            rgb_curves_009_1.mapping.curves[0].points[1].handle_type = 'AUTO'
            rgb_curves_009_1.mapping.curves[0].points[1].location = (1.0, 1.0)
            rgb_curves_009_1.mapping.curves[0].points[1].select = False
            if 0 >= len(rgb_curves_009_1.mapping.curves[1].points):
                rgb_curves_009_1.mapping.curves[1].points.new(0.0, 0.0)
            rgb_curves_009_1.mapping.curves[1].points[0].handle_type = 'AUTO'
            rgb_curves_009_1.mapping.curves[1].points[0].location = (0.0, 0.0)
            rgb_curves_009_1.mapping.curves[1].points[0].select = False
            if 1 >= len(rgb_curves_009_1.mapping.curves[1].points):
                rgb_curves_009_1.mapping.curves[1].points.new(1.0, 1.0)
            rgb_curves_009_1.mapping.curves[1].points[1].handle_type = 'AUTO'
            rgb_curves_009_1.mapping.curves[1].points[1].location = (1.0, 1.0)
            rgb_curves_009_1.mapping.curves[1].points[1].select = False
            if 0 >= len(rgb_curves_009_1.mapping.curves[2].points):
                rgb_curves_009_1.mapping.curves[2].points.new(0.0, 0.0)
            rgb_curves_009_1.mapping.curves[2].points[0].handle_type = 'AUTO'
            rgb_curves_009_1.mapping.curves[2].points[0].location = (0.0, 0.0)
            rgb_curves_009_1.mapping.curves[2].points[0].select = False
            if 1 >= len(rgb_curves_009_1.mapping.curves[2].points):
                rgb_curves_009_1.mapping.curves[2].points.new(1.0, 1.0)
            rgb_curves_009_1.mapping.curves[2].points[1].handle_type = 'AUTO'
            rgb_curves_009_1.mapping.curves[2].points[1].location = (1.0, 1.0)
            rgb_curves_009_1.mapping.curves[2].points[1].select = False
            if 0 >= len(rgb_curves_009_1.mapping.curves[3].points):
                rgb_curves_009_1.mapping.curves[3].points.new(0.0, 0.0)
            rgb_curves_009_1.mapping.curves[3].points[0].handle_type = 'AUTO'
            rgb_curves_009_1.mapping.curves[3].points[0].location = (0.0, 0.0)
            rgb_curves_009_1.mapping.curves[3].points[0].select = False
            if 1 >= len(rgb_curves_009_1.mapping.curves[3].points):
                rgb_curves_009_1.mapping.curves[3].points.new(1.0, 1.0)
            rgb_curves_009_1.mapping.curves[3].points[1].handle_type = 'AUTO'
            rgb_curves_009_1.mapping.curves[3].points[1].location = (1.0, 1.0)
            rgb_curves_009_1.mapping.curves[3].points[1].select = False
            rgb_curves_009_1.mapping.extend = 'EXTRAPOLATED'
            rgb_curves_009_1.mapping.tone = 'STANDARD'
            rgb_curves_009_1.mapping.use_clip = True
            rgb_curves_009_1.mapping.white_level = (1.0, 1.0, 1.0)
            rgb_curves_009_1.mute = False
            rgb_curves_009_1.name = 'RGB Curves.009'
            rgb_curves_009_1.use_custom_color = False
            rgb_curves_009_1.width = 202.78076171875
            rgb_curves_009_1.inputs[0].default_value = 1.0
            rgb_curves_009_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            rgb_curves_009_1.inputs[2].default_value = (0.0, 0.0, 0.0, 1.0)
            rgb_curves_009_1.inputs[3].default_value = (1.0, 1.0, 1.0, 1.0)
            rgb_curves_009_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            rgb_curves_006_1 = node_tree1.nodes.new('CompositorNodeCurveRGB')
            rgb_curves_006_1.parent = node_tree1.nodes.get('Frame')
            rgb_curves_006_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            rgb_curves_006_1.hide = True
            rgb_curves_006_1.location = (45.13432312011719, -112.8358154296875)
            rgb_curves_006_1.mapping.black_level = (0.0, 0.0, 0.0)
            rgb_curves_006_1.mapping.clip_max_x = 1.0
            rgb_curves_006_1.mapping.clip_max_y = 1.0
            rgb_curves_006_1.mapping.clip_min_x = 0.0
            rgb_curves_006_1.mapping.clip_min_y = 0.0
            if 0 >= len(rgb_curves_006_1.mapping.curves[0].points):
                rgb_curves_006_1.mapping.curves[0].points.new(0.0, 0.0)
            rgb_curves_006_1.mapping.curves[0].points[0].handle_type = 'AUTO'
            rgb_curves_006_1.mapping.curves[0].points[0].location = (0.0, 0.0)
            rgb_curves_006_1.mapping.curves[0].points[0].select = False
            if 1 >= len(rgb_curves_006_1.mapping.curves[0].points):
                rgb_curves_006_1.mapping.curves[0].points.new(1.0, 1.0)
            rgb_curves_006_1.mapping.curves[0].points[1].handle_type = 'AUTO'
            rgb_curves_006_1.mapping.curves[0].points[1].location = (1.0, 1.0)
            rgb_curves_006_1.mapping.curves[0].points[1].select = False
            if 0 >= len(rgb_curves_006_1.mapping.curves[1].points):
                rgb_curves_006_1.mapping.curves[1].points.new(0.0, 0.0)
            rgb_curves_006_1.mapping.curves[1].points[0].handle_type = 'AUTO'
            rgb_curves_006_1.mapping.curves[1].points[0].location = (0.0, 0.0)
            rgb_curves_006_1.mapping.curves[1].points[0].select = False
            if 1 >= len(rgb_curves_006_1.mapping.curves[1].points):
                rgb_curves_006_1.mapping.curves[1].points.new(1.0, 1.0)
            rgb_curves_006_1.mapping.curves[1].points[1].handle_type = 'AUTO'
            rgb_curves_006_1.mapping.curves[1].points[1].location = (1.0, 1.0)
            rgb_curves_006_1.mapping.curves[1].points[1].select = False
            if 0 >= len(rgb_curves_006_1.mapping.curves[2].points):
                rgb_curves_006_1.mapping.curves[2].points.new(0.0, 0.0)
            rgb_curves_006_1.mapping.curves[2].points[0].handle_type = 'AUTO'
            rgb_curves_006_1.mapping.curves[2].points[0].location = (0.0, 0.0)
            rgb_curves_006_1.mapping.curves[2].points[0].select = False
            if 1 >= len(rgb_curves_006_1.mapping.curves[2].points):
                rgb_curves_006_1.mapping.curves[2].points.new(1.0, 1.0)
            rgb_curves_006_1.mapping.curves[2].points[1].handle_type = 'AUTO'
            rgb_curves_006_1.mapping.curves[2].points[1].location = (1.0, 1.0)
            rgb_curves_006_1.mapping.curves[2].points[1].select = False
            if 0 >= len(rgb_curves_006_1.mapping.curves[3].points):
                rgb_curves_006_1.mapping.curves[3].points.new(0.0, 0.0)
            rgb_curves_006_1.mapping.curves[3].points[0].handle_type = 'AUTO'
            rgb_curves_006_1.mapping.curves[3].points[0].location = (0.0, 0.0)
            rgb_curves_006_1.mapping.curves[3].points[0].select = False
            if 1 >= len(rgb_curves_006_1.mapping.curves[3].points):
                rgb_curves_006_1.mapping.curves[3].points.new(1.0, 1.0)
            rgb_curves_006_1.mapping.curves[3].points[1].handle_type = 'AUTO'
            rgb_curves_006_1.mapping.curves[3].points[1].location = (1.0, 1.0)
            rgb_curves_006_1.mapping.curves[3].points[1].select = False
            rgb_curves_006_1.mapping.extend = 'EXTRAPOLATED'
            rgb_curves_006_1.mapping.tone = 'STANDARD'
            rgb_curves_006_1.mapping.use_clip = True
            rgb_curves_006_1.mapping.white_level = (1.0, 1.0, 1.0)
            rgb_curves_006_1.mute = False
            rgb_curves_006_1.name = 'RGB Curves.006'
            rgb_curves_006_1.use_custom_color = False
            rgb_curves_006_1.width = 202.78076171875
            rgb_curves_006_1.inputs[0].default_value = 1.0
            rgb_curves_006_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            rgb_curves_006_1.inputs[2].default_value = (0.0, 0.0, 0.0, 1.0)
            rgb_curves_006_1.inputs[3].default_value = (1.0, 1.0, 1.0, 1.0)
            rgb_curves_006_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            rgb_curves_008_1 = node_tree1.nodes.new('CompositorNodeCurveRGB')
            rgb_curves_008_1.parent = node_tree1.nodes.get('Frame')
            rgb_curves_008_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            rgb_curves_008_1.hide = True
            rgb_curves_008_1.location = (45.13432312011719, -67.70147705078125)
            rgb_curves_008_1.mapping.black_level = (0.0, 0.0, 0.0)
            rgb_curves_008_1.mapping.clip_max_x = 1.0
            rgb_curves_008_1.mapping.clip_max_y = 1.0
            rgb_curves_008_1.mapping.clip_min_x = 0.0
            rgb_curves_008_1.mapping.clip_min_y = 0.0
            if 0 >= len(rgb_curves_008_1.mapping.curves[0].points):
                rgb_curves_008_1.mapping.curves[0].points.new(0.0, 0.0)
            rgb_curves_008_1.mapping.curves[0].points[0].handle_type = 'AUTO'
            rgb_curves_008_1.mapping.curves[0].points[0].location = (0.0, 0.0)
            rgb_curves_008_1.mapping.curves[0].points[0].select = False
            if 1 >= len(rgb_curves_008_1.mapping.curves[0].points):
                rgb_curves_008_1.mapping.curves[0].points.new(1.0, 1.0)
            rgb_curves_008_1.mapping.curves[0].points[1].handle_type = 'AUTO'
            rgb_curves_008_1.mapping.curves[0].points[1].location = (1.0, 1.0)
            rgb_curves_008_1.mapping.curves[0].points[1].select = False
            if 0 >= len(rgb_curves_008_1.mapping.curves[1].points):
                rgb_curves_008_1.mapping.curves[1].points.new(0.0, 0.0)
            rgb_curves_008_1.mapping.curves[1].points[0].handle_type = 'AUTO'
            rgb_curves_008_1.mapping.curves[1].points[0].location = (0.0, 0.0)
            rgb_curves_008_1.mapping.curves[1].points[0].select = False
            if 1 >= len(rgb_curves_008_1.mapping.curves[1].points):
                rgb_curves_008_1.mapping.curves[1].points.new(1.0, 1.0)
            rgb_curves_008_1.mapping.curves[1].points[1].handle_type = 'AUTO'
            rgb_curves_008_1.mapping.curves[1].points[1].location = (1.0, 1.0)
            rgb_curves_008_1.mapping.curves[1].points[1].select = False
            if 0 >= len(rgb_curves_008_1.mapping.curves[2].points):
                rgb_curves_008_1.mapping.curves[2].points.new(0.0, 0.0)
            rgb_curves_008_1.mapping.curves[2].points[0].handle_type = 'AUTO'
            rgb_curves_008_1.mapping.curves[2].points[0].location = (0.0, 0.0)
            rgb_curves_008_1.mapping.curves[2].points[0].select = False
            if 1 >= len(rgb_curves_008_1.mapping.curves[2].points):
                rgb_curves_008_1.mapping.curves[2].points.new(1.0, 1.0)
            rgb_curves_008_1.mapping.curves[2].points[1].handle_type = 'AUTO'
            rgb_curves_008_1.mapping.curves[2].points[1].location = (1.0, 1.0)
            rgb_curves_008_1.mapping.curves[2].points[1].select = False
            if 0 >= len(rgb_curves_008_1.mapping.curves[3].points):
                rgb_curves_008_1.mapping.curves[3].points.new(0.0, 0.0)
            rgb_curves_008_1.mapping.curves[3].points[0].handle_type = 'AUTO'
            rgb_curves_008_1.mapping.curves[3].points[0].location = (0.0, 0.0)
            rgb_curves_008_1.mapping.curves[3].points[0].select = False
            if 1 >= len(rgb_curves_008_1.mapping.curves[3].points):
                rgb_curves_008_1.mapping.curves[3].points.new(1.0, 1.0)
            rgb_curves_008_1.mapping.curves[3].points[1].handle_type = 'AUTO'
            rgb_curves_008_1.mapping.curves[3].points[1].location = (1.0, 1.0)
            rgb_curves_008_1.mapping.curves[3].points[1].select = False
            rgb_curves_008_1.mapping.extend = 'EXTRAPOLATED'
            rgb_curves_008_1.mapping.tone = 'STANDARD'
            rgb_curves_008_1.mapping.use_clip = True
            rgb_curves_008_1.mapping.white_level = (1.0, 1.0, 1.0)
            rgb_curves_008_1.mute = False
            rgb_curves_008_1.name = 'RGB Curves.008'
            rgb_curves_008_1.use_custom_color = False
            rgb_curves_008_1.width = 202.78076171875
            rgb_curves_008_1.inputs[0].default_value = 1.0
            rgb_curves_008_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            rgb_curves_008_1.inputs[2].default_value = (0.0, 0.0, 0.0, 1.0)
            rgb_curves_008_1.inputs[3].default_value = (1.0, 1.0, 1.0, 1.0)
            rgb_curves_008_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            rgb_curves_007_1 = node_tree1.nodes.new('CompositorNodeCurveRGB')
            rgb_curves_007_1.parent = node_tree1.nodes.get('Frame')
            rgb_curves_007_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            rgb_curves_007_1.hide = True
            rgb_curves_007_1.location = (45.13432312011719, -22.567169189453125)
            rgb_curves_007_1.mapping.black_level = (0.0, 0.0, 0.0)
            rgb_curves_007_1.mapping.clip_max_x = 1.0
            rgb_curves_007_1.mapping.clip_max_y = 1.0
            rgb_curves_007_1.mapping.clip_min_x = 0.0
            rgb_curves_007_1.mapping.clip_min_y = 0.0
            if 0 >= len(rgb_curves_007_1.mapping.curves[0].points):
                rgb_curves_007_1.mapping.curves[0].points.new(0.0, 0.0)
            rgb_curves_007_1.mapping.curves[0].points[0].handle_type = 'AUTO'
            rgb_curves_007_1.mapping.curves[0].points[0].location = (0.0, 0.0)
            rgb_curves_007_1.mapping.curves[0].points[0].select = False
            if 1 >= len(rgb_curves_007_1.mapping.curves[0].points):
                rgb_curves_007_1.mapping.curves[0].points.new(1.0, 1.0)
            rgb_curves_007_1.mapping.curves[0].points[1].handle_type = 'AUTO'
            rgb_curves_007_1.mapping.curves[0].points[1].location = (1.0, 1.0)
            rgb_curves_007_1.mapping.curves[0].points[1].select = False
            if 0 >= len(rgb_curves_007_1.mapping.curves[1].points):
                rgb_curves_007_1.mapping.curves[1].points.new(0.0, 0.0)
            rgb_curves_007_1.mapping.curves[1].points[0].handle_type = 'AUTO'
            rgb_curves_007_1.mapping.curves[1].points[0].location = (0.0, 0.0)
            rgb_curves_007_1.mapping.curves[1].points[0].select = False
            if 1 >= len(rgb_curves_007_1.mapping.curves[1].points):
                rgb_curves_007_1.mapping.curves[1].points.new(1.0, 1.0)
            rgb_curves_007_1.mapping.curves[1].points[1].handle_type = 'AUTO'
            rgb_curves_007_1.mapping.curves[1].points[1].location = (1.0, 1.0)
            rgb_curves_007_1.mapping.curves[1].points[1].select = False
            if 0 >= len(rgb_curves_007_1.mapping.curves[2].points):
                rgb_curves_007_1.mapping.curves[2].points.new(0.0, 0.0)
            rgb_curves_007_1.mapping.curves[2].points[0].handle_type = 'AUTO'
            rgb_curves_007_1.mapping.curves[2].points[0].location = (0.0, 0.0)
            rgb_curves_007_1.mapping.curves[2].points[0].select = False
            if 1 >= len(rgb_curves_007_1.mapping.curves[2].points):
                rgb_curves_007_1.mapping.curves[2].points.new(1.0, 1.0)
            rgb_curves_007_1.mapping.curves[2].points[1].handle_type = 'AUTO'
            rgb_curves_007_1.mapping.curves[2].points[1].location = (1.0, 1.0)
            rgb_curves_007_1.mapping.curves[2].points[1].select = False
            if 0 >= len(rgb_curves_007_1.mapping.curves[3].points):
                rgb_curves_007_1.mapping.curves[3].points.new(0.0, 0.0)
            rgb_curves_007_1.mapping.curves[3].points[0].handle_type = 'AUTO'
            rgb_curves_007_1.mapping.curves[3].points[0].location = (0.0, 0.0)
            rgb_curves_007_1.mapping.curves[3].points[0].select = False
            if 1 >= len(rgb_curves_007_1.mapping.curves[3].points):
                rgb_curves_007_1.mapping.curves[3].points.new(1.0, 1.0)
            rgb_curves_007_1.mapping.curves[3].points[1].handle_type = 'AUTO'
            rgb_curves_007_1.mapping.curves[3].points[1].location = (1.0, 1.0)
            rgb_curves_007_1.mapping.curves[3].points[1].select = False
            rgb_curves_007_1.mapping.extend = 'EXTRAPOLATED'
            rgb_curves_007_1.mapping.tone = 'STANDARD'
            rgb_curves_007_1.mapping.use_clip = True
            rgb_curves_007_1.mapping.white_level = (1.0, 1.0, 1.0)
            rgb_curves_007_1.mute = False
            rgb_curves_007_1.name = 'RGB Curves.007'
            rgb_curves_007_1.use_custom_color = False
            rgb_curves_007_1.width = 202.78076171875
            rgb_curves_007_1.inputs[0].default_value = 1.0
            rgb_curves_007_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            rgb_curves_007_1.inputs[2].default_value = (0.0, 0.0, 0.0, 1.0)
            rgb_curves_007_1.inputs[3].default_value = (1.0, 1.0, 1.0, 1.0)
            rgb_curves_007_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            rgb_curves_1 = node_tree1.nodes.new('CompositorNodeCurveRGB')
            rgb_curves_1.parent = node_tree1.nodes.get('Frame')
            rgb_curves_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            rgb_curves_1.hide = True
            rgb_curves_1.location = (45.13432312011719, 22.567169189453125)
            rgb_curves_1.mapping.black_level = (0.0, 0.0, 0.0)
            rgb_curves_1.mapping.clip_max_x = 1.0
            rgb_curves_1.mapping.clip_max_y = 1.0
            rgb_curves_1.mapping.clip_min_x = 0.0
            rgb_curves_1.mapping.clip_min_y = 0.0
            if 0 >= len(rgb_curves_1.mapping.curves[0].points):
                rgb_curves_1.mapping.curves[0].points.new(0.0, 0.0)
            rgb_curves_1.mapping.curves[0].points[0].handle_type = 'AUTO'
            rgb_curves_1.mapping.curves[0].points[0].location = (0.0, 0.0)
            rgb_curves_1.mapping.curves[0].points[0].select = False
            if 1 >= len(rgb_curves_1.mapping.curves[0].points):
                rgb_curves_1.mapping.curves[0].points.new(1.0, 1.0)
            rgb_curves_1.mapping.curves[0].points[1].handle_type = 'AUTO'
            rgb_curves_1.mapping.curves[0].points[1].location = (1.0, 1.0)
            rgb_curves_1.mapping.curves[0].points[1].select = False
            if 0 >= len(rgb_curves_1.mapping.curves[1].points):
                rgb_curves_1.mapping.curves[1].points.new(0.0, 0.0)
            rgb_curves_1.mapping.curves[1].points[0].handle_type = 'AUTO'
            rgb_curves_1.mapping.curves[1].points[0].location = (0.0, 0.0)
            rgb_curves_1.mapping.curves[1].points[0].select = False
            if 1 >= len(rgb_curves_1.mapping.curves[1].points):
                rgb_curves_1.mapping.curves[1].points.new(1.0, 1.0)
            rgb_curves_1.mapping.curves[1].points[1].handle_type = 'AUTO'
            rgb_curves_1.mapping.curves[1].points[1].location = (1.0, 1.0)
            rgb_curves_1.mapping.curves[1].points[1].select = False
            if 0 >= len(rgb_curves_1.mapping.curves[2].points):
                rgb_curves_1.mapping.curves[2].points.new(0.0, 0.0)
            rgb_curves_1.mapping.curves[2].points[0].handle_type = 'AUTO'
            rgb_curves_1.mapping.curves[2].points[0].location = (0.0, 0.0)
            rgb_curves_1.mapping.curves[2].points[0].select = False
            if 1 >= len(rgb_curves_1.mapping.curves[2].points):
                rgb_curves_1.mapping.curves[2].points.new(1.0, 1.0)
            rgb_curves_1.mapping.curves[2].points[1].handle_type = 'AUTO'
            rgb_curves_1.mapping.curves[2].points[1].location = (1.0, 1.0)
            rgb_curves_1.mapping.curves[2].points[1].select = False
            if 0 >= len(rgb_curves_1.mapping.curves[3].points):
                rgb_curves_1.mapping.curves[3].points.new(0.0, 0.0)
            rgb_curves_1.mapping.curves[3].points[0].handle_type = 'AUTO'
            rgb_curves_1.mapping.curves[3].points[0].location = (0.0, 0.0)
            rgb_curves_1.mapping.curves[3].points[0].select = False
            if 1 >= len(rgb_curves_1.mapping.curves[3].points):
                rgb_curves_1.mapping.curves[3].points.new(1.0, 1.0)
            rgb_curves_1.mapping.curves[3].points[1].handle_type = 'AUTO'
            rgb_curves_1.mapping.curves[3].points[1].location = (1.0, 1.0)
            rgb_curves_1.mapping.curves[3].points[1].select = False
            rgb_curves_1.mapping.extend = 'EXTRAPOLATED'
            rgb_curves_1.mapping.tone = 'STANDARD'
            rgb_curves_1.mapping.use_clip = True
            rgb_curves_1.mapping.white_level = (1.0, 1.0, 1.0)
            rgb_curves_1.mute = False
            rgb_curves_1.name = 'RGB Curves'
            rgb_curves_1.use_custom_color = False
            rgb_curves_1.width = 202.78076171875
            rgb_curves_1.inputs[0].default_value = 1.0
            rgb_curves_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            rgb_curves_1.inputs[2].default_value = (0.0, 0.0, 0.0, 1.0)
            rgb_curves_1.inputs[3].default_value = (1.0, 1.0, 1.0, 1.0)
            rgb_curves_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            math_010_1 = node_tree1.nodes.new('CompositorNodeMath')
            math_010_1.parent = node_tree1.nodes.get('Frame')
            math_010_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            math_010_1.hide = True
            math_010_1.location = (-135.40298461914062, 0.0)
            math_010_1.mute = False
            math_010_1.name = 'Math.010'
            math_010_1.operation = 'ADD'
            math_010_1.use_clamp = False
            math_010_1.use_custom_color = False
            math_010_1.width = 129.8437957763672
            math_010_1.inputs[0].default_value = 90.0
            math_010_1.inputs[1].default_value = -100.0
            math_010_1.inputs[2].default_value = 0.0
            math_010_1.outputs[0].default_value = 0.0

            math_005_1 = node_tree1.nodes.new('CompositorNodeMath')
            math_005_1.parent = node_tree1.nodes.get('Frame')
            math_005_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            math_005_1.hide = True
            math_005_1.location = (67.70149230957031, -248.23880004882812)
            math_005_1.mute = False
            math_005_1.name = 'Math.005'
            math_005_1.operation = 'MULTIPLY'
            math_005_1.use_clamp = False
            math_005_1.use_custom_color = False
            math_005_1.width = 140.0
            math_005_1.inputs[0].default_value = 0.0
            math_005_1.inputs[1].default_value = 0.10000000149011612
            math_005_1.inputs[2].default_value = 0.0
            math_005_1.outputs[0].default_value = 0.0

            alpha_over_004_1 = node_tree1.nodes.new('CompositorNodeAlphaOver')
            alpha_over_004_1.parent = node_tree1.nodes.get('Frame.002')
            alpha_over_004_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            alpha_over_004_1.hide = True
            alpha_over_004_1.location = (122.44781494140625, -20.537307739257812)
            alpha_over_004_1.mute = False
            alpha_over_004_1.name = 'Alpha Over.004'
            alpha_over_004_1.premul = 0.0
            alpha_over_004_1.use_custom_color = False
            alpha_over_004_1.use_premultiply = False
            alpha_over_004_1.width = 142.16607666015625
            alpha_over_004_1.inputs[0].default_value = 1.0
            alpha_over_004_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            alpha_over_004_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            alpha_over_004_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            invert_006_1 = node_tree1.nodes.new('CompositorNodeInvert')
            invert_006_1.parent = node_tree1.nodes.get('Frame.002')
            invert_006_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            invert_006_1.hide = True
            invert_006_1.invert_alpha = False
            invert_006_1.invert_rgb = True
            invert_006_1.location = (122.44781494140625, -100.53730773925781)
            invert_006_1.mute = False
            invert_006_1.name = 'Invert.006'
            invert_006_1.use_custom_color = False
            invert_006_1.width = 140.0
            invert_006_1.inputs[0].default_value = 1.0
            invert_006_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            invert_006_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_001_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_001_1.parent = node_tree1.nodes.get('Frame.002')
            mix_001_1.blend_type = 'MULTIPLY'
            mix_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_001_1.hide = True
            mix_001_1.location = (300.0, -220.0)
            mix_001_1.mute = False
            mix_001_1.name = 'Mix.001'
            mix_001_1.use_alpha = False
            mix_001_1.use_clamp = False
            mix_001_1.use_custom_color = False
            mix_001_1.width = 140.0
            mix_001_1.inputs[0].default_value = 1.0
            mix_001_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_001_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_001_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_005_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_005_1.parent = node_tree1.nodes.get('Frame.002')
            mix_005_1.blend_type = 'DIVIDE'
            mix_005_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_005_1.hide = True
            mix_005_1.location = (300.0, -140.0)
            mix_005_1.mute = False
            mix_005_1.name = 'Mix.005'
            mix_005_1.use_alpha = False
            mix_005_1.use_clamp = False
            mix_005_1.use_custom_color = False
            mix_005_1.width = 140.0
            mix_005_1.inputs[0].default_value = 1.0
            mix_005_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_005_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_005_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_006_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_006_1.parent = node_tree1.nodes.get('Frame.002')
            mix_006_1.blend_type = 'SCREEN'
            mix_006_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_006_1.hide = True
            mix_006_1.location = (300.0, -100.0)
            mix_006_1.mute = False
            mix_006_1.name = 'Mix.006'
            mix_006_1.use_alpha = True
            mix_006_1.use_clamp = False
            mix_006_1.use_custom_color = False
            mix_006_1.width = 140.0
            mix_006_1.inputs[0].default_value = 1.0
            mix_006_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_006_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_006_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_009_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_009_1.parent = node_tree1.nodes.get('Frame.002')
            mix_009_1.blend_type = 'DIVIDE'
            mix_009_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_009_1.hide = True
            mix_009_1.location = (300.0, -60.0)
            mix_009_1.mute = False
            mix_009_1.name = 'Mix.009'
            mix_009_1.use_alpha = False
            mix_009_1.use_clamp = False
            mix_009_1.use_custom_color = False
            mix_009_1.width = 140.0
            mix_009_1.inputs[0].default_value = 1.0
            mix_009_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_009_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_009_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_004_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_004_1.parent = node_tree1.nodes.get('Frame.002')
            mix_004_1.blend_type = 'DIVIDE'
            mix_004_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_004_1.hide = True
            mix_004_1.location = (300.0, -180.0)
            mix_004_1.mute = False
            mix_004_1.name = 'Mix.004'
            mix_004_1.use_alpha = False
            mix_004_1.use_clamp = False
            mix_004_1.use_custom_color = False
            mix_004_1.width = 140.0
            mix_004_1.inputs[0].default_value = 1.0
            mix_004_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_004_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_004_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            alpha_over_003_1 = node_tree1.nodes.new('CompositorNodeAlphaOver')
            alpha_over_003_1.parent = node_tree1.nodes.get('Frame.002')
            alpha_over_003_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            alpha_over_003_1.hide = True
            alpha_over_003_1.location = (-57.55218505859375, -200.5373077392578)
            alpha_over_003_1.mute = False
            alpha_over_003_1.name = 'Alpha Over.003'
            alpha_over_003_1.premul = 0.0
            alpha_over_003_1.use_custom_color = False
            alpha_over_003_1.use_premultiply = False
            alpha_over_003_1.width = 142.16607666015625
            alpha_over_003_1.inputs[0].default_value = 1.0
            alpha_over_003_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            alpha_over_003_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            alpha_over_003_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            alpha_over_002_1 = node_tree1.nodes.new('CompositorNodeAlphaOver')
            alpha_over_002_1.parent = node_tree1.nodes.get('Frame.002')
            alpha_over_002_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            alpha_over_002_1.hide = True
            alpha_over_002_1.location = (-57.55218505859375, -160.5373077392578)
            alpha_over_002_1.mute = False
            alpha_over_002_1.name = 'Alpha Over.002'
            alpha_over_002_1.premul = 0.0
            alpha_over_002_1.use_custom_color = False
            alpha_over_002_1.use_premultiply = False
            alpha_over_002_1.width = 142.16607666015625
            alpha_over_002_1.inputs[0].default_value = 1.0
            alpha_over_002_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            alpha_over_002_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            alpha_over_002_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            alpha_over_001_1 = node_tree1.nodes.new('CompositorNodeAlphaOver')
            alpha_over_001_1.parent = node_tree1.nodes.get('Frame.002')
            alpha_over_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            alpha_over_001_1.hide = True
            alpha_over_001_1.location = (-57.55218505859375, -120.53730773925781)
            alpha_over_001_1.mute = False
            alpha_over_001_1.name = 'Alpha Over.001'
            alpha_over_001_1.premul = 0.0
            alpha_over_001_1.use_custom_color = False
            alpha_over_001_1.use_premultiply = False
            alpha_over_001_1.width = 142.16607666015625
            alpha_over_001_1.inputs[0].default_value = 1.0
            alpha_over_001_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            alpha_over_001_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            alpha_over_001_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            alpha_over_1 = node_tree1.nodes.new('CompositorNodeAlphaOver')
            alpha_over_1.parent = node_tree1.nodes.get('Frame.002')
            alpha_over_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            alpha_over_1.hide = True
            alpha_over_1.location = (-57.55218505859375, -80.53730773925781)
            alpha_over_1.mute = False
            alpha_over_1.name = 'Alpha Over'
            alpha_over_1.premul = 0.0
            alpha_over_1.use_custom_color = False
            alpha_over_1.use_premultiply = False
            alpha_over_1.width = 142.16607666015625
            alpha_over_1.inputs[0].default_value = 1.0
            alpha_over_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            alpha_over_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            alpha_over_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            invert_005_1 = node_tree1.nodes.new('CompositorNodeInvert')
            invert_005_1.parent = node_tree1.nodes.get('Frame.002')
            invert_005_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            invert_005_1.hide = True
            invert_005_1.invert_alpha = True
            invert_005_1.invert_rgb = True
            invert_005_1.location = (-57.55218505859375, -20.537307739257812)
            invert_005_1.mute = False
            invert_005_1.name = 'Invert.005'
            invert_005_1.use_custom_color = False
            invert_005_1.width = 140.0
            invert_005_1.inputs[0].default_value = 1.0
            invert_005_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            invert_005_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            node_tree2 = bpy_data.node_groups.get('NodeGroup')
            if not node_tree2:
                node_tree2 = bpy_data.node_groups.new('NodeGroup', 'CompositorNodeTree')
                # INPUTS
                node_tree2.inputs.new('NodeSocketColor', 'Color')
                # OUTPUTS
                node_tree2.outputs.new('NodeSocketColor', 'Image')
                # NODES
                group_input_2 = node_tree2.nodes.new('NodeGroupInput')
                group_input_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                group_input_2.hide = False
                group_input_2.location = (-278.985107421875, -0.0)
                group_input_2.mute = False
                group_input_2.name = 'Group Input'
                group_input_2.use_custom_color = False
                group_input_2.width = 140.0
                group_input_2.outputs[0].default_value = (1.0, 1.0, 1.0, 1.0)

                group_output_2 = node_tree2.nodes.new('NodeGroupOutput')
                group_output_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                group_output_2.hide = False
                group_output_2.is_active_output = True
                group_output_2.location = (278.9849853515625, -0.0)
                group_output_2.mute = False
                group_output_2.name = 'Group Output'
                group_output_2.use_custom_color = False
                group_output_2.width = 140.0
                group_output_2.inputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

                invert_2 = node_tree2.nodes.new('CompositorNodeInvert')
                invert_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                invert_2.hide = False
                invert_2.invert_alpha = False
                invert_2.invert_rgb = True
                invert_2.location = (-78.985107421875, 0.0)
                invert_2.mute = False
                invert_2.name = 'Invert'
                invert_2.use_custom_color = False
                invert_2.width = 140.0
                invert_2.inputs[0].default_value = 1.0
                invert_2.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
                invert_2.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

                set_alpha_2 = node_tree2.nodes.new('CompositorNodeSetAlpha')
                set_alpha_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                set_alpha_2.hide = False
                set_alpha_2.location = (100.0, -20.0)
                set_alpha_2.mute = False
                set_alpha_2.name = 'Set Alpha'
                set_alpha_2.use_custom_color = False
                set_alpha_2.width = 140.0
                set_alpha_2.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
                set_alpha_2.inputs[1].default_value = 1.0
                set_alpha_2.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

                # LINKS
                node_tree2.links.new(set_alpha_2.outputs[0], group_output_2.inputs[0])
                node_tree2.links.new(group_input_2.outputs[0], invert_2.inputs[1])
                node_tree2.links.new(invert_2.outputs[0], set_alpha_2.inputs[1])

            group_1 = node_tree1.nodes.new('CompositorNodeGroup')
            group_1.node_tree = bpy_data.node_groups.get('NodeGroup')
            group_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            group_1.hide = True
            group_1.location = (1647.4029541015625, 0.0)
            group_1.mute = False
            group_1.name = 'Group'
            group_1.use_custom_color = False
            group_1.width = 140.0
            group_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            group_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            group_001_1 = node_tree1.nodes.new('CompositorNodeGroup')
            group_001_1.node_tree = bpy_data.node_groups.get('NodeGroup')
            group_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            group_001_1.hide = True
            group_001_1.location = (1647.4029541015625, -45.13432693481445)
            group_001_1.mute = False
            group_001_1.name = 'Group.001'
            group_001_1.use_custom_color = False
            group_001_1.width = 140.0
            group_001_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            group_001_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            group_002_1 = node_tree1.nodes.new('CompositorNodeGroup')
            group_002_1.node_tree = bpy_data.node_groups.get('NodeGroup')
            group_002_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            group_002_1.hide = True
            group_002_1.location = (1647.4029541015625, -90.2686538696289)
            group_002_1.mute = False
            group_002_1.name = 'Group.002'
            group_002_1.use_custom_color = False
            group_002_1.width = 140.0
            group_002_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            group_002_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            group_003_1 = node_tree1.nodes.new('CompositorNodeGroup')
            group_003_1.node_tree = bpy_data.node_groups.get('NodeGroup')
            group_003_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            group_003_1.hide = True
            group_003_1.location = (1647.4029541015625, -135.40298461914062)
            group_003_1.mute = False
            group_003_1.name = 'Group.003'
            group_003_1.use_custom_color = False
            group_003_1.width = 140.0
            group_003_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            group_003_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            group_004_1 = node_tree1.nodes.new('CompositorNodeGroup')
            group_004_1.node_tree = bpy_data.node_groups.get('NodeGroup')
            group_004_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            group_004_1.hide = True
            group_004_1.location = (1647.4029541015625, -180.5373077392578)
            group_004_1.mute = False
            group_004_1.name = 'Group.004'
            group_004_1.use_custom_color = False
            group_004_1.width = 140.0
            group_004_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            group_004_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            group_output_1 = node_tree1.nodes.new('NodeGroupOutput')
            group_output_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            group_output_1.hide = False
            group_output_1.is_active_output = True
            group_output_1.location = (3240.0, -120.0)
            group_output_1.mute = False
            group_output_1.name = 'Group Output'
            group_output_1.use_custom_color = False
            group_output_1.width = 140.0
            group_output_1.inputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
            group_output_1.inputs[2].default_value = (0.0, 0.0, 0.0, 0.0)
            group_output_1.inputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
            group_output_1.inputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
            group_output_1.inputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
            group_output_1.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_010_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_010_1.parent = node_tree1.nodes.get('Frame.002')
            mix_010_1.blend_type = 'VALUE'
            mix_010_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_010_1.hide = True
            mix_010_1.location = (500.0, -100.0)
            mix_010_1.mute = False
            mix_010_1.name = 'Mix.010'
            mix_010_1.use_alpha = False
            mix_010_1.use_clamp = False
            mix_010_1.use_custom_color = False
            mix_010_1.width = 141.0830078125
            mix_010_1.inputs[0].default_value = 0.25
            mix_010_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_010_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_010_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_003_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_003_1.parent = node_tree1.nodes.get('Frame.002')
            mix_003_1.blend_type = 'VALUE'
            mix_003_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_003_1.hide = True
            mix_003_1.location = (500.0, -140.0)
            mix_003_1.mute = False
            mix_003_1.name = 'Mix.003'
            mix_003_1.use_alpha = False
            mix_003_1.use_clamp = False
            mix_003_1.use_custom_color = False
            mix_003_1.width = 141.0830078125
            mix_003_1.inputs[0].default_value = 0.25
            mix_003_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_003_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_003_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_007_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_007_1.parent = node_tree1.nodes.get('Frame.002')
            mix_007_1.blend_type = 'VALUE'
            mix_007_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_007_1.hide = True
            mix_007_1.location = (500.0, -180.0)
            mix_007_1.mute = False
            mix_007_1.name = 'Mix.007'
            mix_007_1.use_alpha = False
            mix_007_1.use_clamp = False
            mix_007_1.use_custom_color = False
            mix_007_1.width = 141.0830078125
            mix_007_1.inputs[0].default_value = 0.25
            mix_007_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_007_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_007_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_008_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_008_1.parent = node_tree1.nodes.get('Frame.002')
            mix_008_1.blend_type = 'VALUE'
            mix_008_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_008_1.hide = True
            mix_008_1.location = (500.0, -220.0)
            mix_008_1.mute = False
            mix_008_1.name = 'Mix.008'
            mix_008_1.use_alpha = False
            mix_008_1.use_clamp = False
            mix_008_1.use_custom_color = False
            mix_008_1.width = 141.0830078125
            mix_008_1.inputs[0].default_value = 0.25
            mix_008_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_008_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_008_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            math_003_1 = node_tree1.nodes.new('CompositorNodeMath')
            math_003_1.parent = node_tree1.nodes.get('Frame.003')
            math_003_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            math_003_1.hide = True
            math_003_1.location = (-136.178955078125, -111.76119995117188)
            math_003_1.mute = False
            math_003_1.name = 'Math.003'
            math_003_1.operation = 'MULTIPLY'
            math_003_1.use_clamp = False
            math_003_1.use_custom_color = False
            math_003_1.width = 140.0
            math_003_1.inputs[0].default_value = 1.0
            math_003_1.inputs[1].default_value = 0.10000000149011612
            math_003_1.inputs[2].default_value = 0.0
            math_003_1.outputs[0].default_value = 0.0

            mix_011_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_011_1.parent = node_tree1.nodes.get('Frame.003')
            mix_011_1.blend_type = 'MULTIPLY'
            mix_011_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_011_1.hide = True
            mix_011_1.location = (103.821044921875, -111.76119995117188)
            mix_011_1.mute = False
            mix_011_1.name = 'Mix.011'
            mix_011_1.use_alpha = True
            mix_011_1.use_clamp = False
            mix_011_1.use_custom_color = False
            mix_011_1.width = 140.0
            mix_011_1.inputs[0].default_value = 0.0
            mix_011_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_011_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_011_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            mix_012_1 = node_tree1.nodes.new('CompositorNodeMixRGB')
            mix_012_1.parent = node_tree1.nodes.get('Frame.004')
            mix_012_1.blend_type = 'MIX'
            mix_012_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            mix_012_1.hide = True
            mix_012_1.location = (192.477783203125, -76.35821533203125)
            mix_012_1.mute = False
            mix_012_1.name = 'Mix.012'
            mix_012_1.use_alpha = True
            mix_012_1.use_clamp = False
            mix_012_1.use_custom_color = False
            mix_012_1.width = 140.0
            mix_012_1.inputs[0].default_value = 1.0
            mix_012_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_012_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            mix_012_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            math_004_1 = node_tree1.nodes.new('CompositorNodeMath')
            math_004_1.parent = node_tree1.nodes.get('Frame.004')
            math_004_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            math_004_1.hide = True
            math_004_1.location = (20.0, -40.0)
            math_004_1.mute = False
            math_004_1.name = 'Math.004'
            math_004_1.operation = 'MULTIPLY'
            math_004_1.use_clamp = False
            math_004_1.use_custom_color = False
            math_004_1.width = 140.0
            math_004_1.inputs[0].default_value = 0.0
            math_004_1.inputs[1].default_value = 0.10000000149011612
            math_004_1.inputs[2].default_value = 0.0
            math_004_1.outputs[0].default_value = 0.0

            group_input_1 = node_tree1.nodes.new('NodeGroupInput')
            group_input_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            group_input_1.hide = False
            group_input_1.location = (-1680.0, 20.0)
            group_input_1.mute = False
            group_input_1.name = 'Group Input'
            group_input_1.use_custom_color = False
            group_input_1.width = 140.0
            group_input_1.outputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
            group_input_1.outputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
            group_input_1.outputs[2].default_value = 0.0
            group_input_1.outputs[3].default_value = 0.0
            group_input_1.outputs[4].default_value = 0.0
            group_input_1.outputs[5].default_value = 0.0
            group_input_1.outputs[6].default_value = 0.0
            group_input_1.outputs[7].default_value = 0.0
            group_input_1.outputs[9].default_value = 0.0
            group_input_1.outputs[10].default_value = 0.0
            group_input_1.outputs[11].default_value = 0.0
            group_input_1.outputs[12].default_value = 0.0
            group_input_1.outputs[13].default_value = 0.0
            group_input_1.outputs[14].default_value = 0.0
            group_input_1.outputs[15].default_value = 0.0

            blur_1 = node_tree1.nodes.new('CompositorNodeBlur')
            blur_1.parent = node_tree1.nodes.get('Frame.001')
            blur_1.aspect_correction = 'NONE'
            blur_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            blur_1.factor = 0.0
            blur_1.factor_x = 0.0
            blur_1.factor_y = 0.0
            blur_1.filter_type = 'FAST_GAUSS'
            blur_1.hide = False
            blur_1.location = (112.8358154296875, 0.0)
            blur_1.mute = False
            blur_1.name = 'Blur'
            blur_1.size_x = 1
            blur_1.size_y = 1
            blur_1.use_bokeh = False
            blur_1.use_custom_color = False
            blur_1.use_extended_bounds = False
            blur_1.use_gamma_correction = False
            blur_1.use_relative = False
            blur_1.use_variable_size = False
            blur_1.width = 140.0
            blur_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            blur_1.inputs[1].default_value = 0.0
            blur_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            math_002_1 = node_tree1.nodes.new('CompositorNodeMath')
            math_002_1.parent = node_tree1.nodes.get('Frame.001')
            math_002_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            math_002_1.hide = True
            math_002_1.location = (-60.0, -140.0)
            math_002_1.mute = False
            math_002_1.name = 'Math.002'
            math_002_1.operation = 'MULTIPLY'
            math_002_1.use_clamp = False
            math_002_1.use_custom_color = False
            math_002_1.width = 140.0
            math_002_1.inputs[0].default_value = 0.0
            math_002_1.inputs[1].default_value = 0.10000000149011612
            math_002_1.inputs[2].default_value = 0.0
            math_002_1.outputs[0].default_value = 0.0

            math_001_1 = node_tree1.nodes.new('CompositorNodeMath')
            math_001_1.parent = node_tree1.nodes.get('transform')
            math_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            math_001_1.hide = True
            math_001_1.location = (-180.53732299804688, -135.40298461914062)
            math_001_1.mute = False
            math_001_1.name = 'Math.001'
            math_001_1.operation = 'MULTIPLY'
            math_001_1.use_clamp = False
            math_001_1.use_custom_color = False
            math_001_1.width = 140.0
            math_001_1.inputs[0].default_value = 0.0
            math_001_1.inputs[1].default_value = 100.0
            math_001_1.inputs[2].default_value = 0.0
            math_001_1.outputs[0].default_value = 0.0

            math_1 = node_tree1.nodes.new('CompositorNodeMath')
            math_1.parent = node_tree1.nodes.get('transform')
            math_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            math_1.hide = True
            math_1.location = (-182.14923095703125, -78.5074462890625)
            math_1.mute = False
            math_1.name = 'Math'
            math_1.operation = 'MULTIPLY'
            math_1.use_clamp = False
            math_1.use_custom_color = False
            math_1.width = 140.0
            math_1.inputs[0].default_value = 0.0
            math_1.inputs[1].default_value = 100.0
            math_1.inputs[2].default_value = 0.0
            math_1.outputs[0].default_value = 0.0

            node_tree2 = bpy_data.node_groups.get('Degrees to Radians')
            if not node_tree2:
                node_tree2 = bpy_data.node_groups.new('Degrees to Radians', 'CompositorNodeTree')
                # INPUTS
                node_tree2.inputs.new('NodeSocketFloat', 'Degrees')
                # OUTPUTS
                node_tree2.outputs.new('NodeSocketFloat', 'Radians')
                # NODES
                group_output_2 = node_tree2.nodes.new('NodeGroupOutput')
                group_output_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                group_output_2.hide = False
                group_output_2.is_active_output = True
                group_output_2.location = (220.0, -20.0)
                group_output_2.mute = False
                group_output_2.name = 'Group Output'
                group_output_2.use_custom_color = False
                group_output_2.width = 140.0
                group_output_2.inputs[0].default_value = 0.0

                math_012_2 = node_tree2.nodes.new('CompositorNodeMath')
                math_012_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                math_012_2.hide = False
                math_012_2.location = (20.0, 0.0)
                math_012_2.mute = False
                math_012_2.name = 'Math.012'
                math_012_2.operation = 'DIVIDE'
                math_012_2.use_clamp = False
                math_012_2.use_custom_color = False
                math_012_2.width = 140.0
                math_012_2.inputs[0].default_value = 0.0
                math_012_2.inputs[1].default_value = 180.0
                math_012_2.inputs[2].default_value = 0.0
                math_012_2.outputs[0].default_value = 0.0

                math_011_2 = node_tree2.nodes.new('CompositorNodeMath')
                math_011_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                math_011_2.hide = False
                math_011_2.location = (-180.0, 0.0)
                math_011_2.mute = False
                math_011_2.name = 'Math.011'
                math_011_2.operation = 'MULTIPLY'
                math_011_2.use_clamp = False
                math_011_2.use_custom_color = False
                math_011_2.width = 140.0
                math_011_2.inputs[0].default_value = 0.0
                math_011_2.inputs[1].default_value = 3.1414999961853027
                math_011_2.inputs[2].default_value = 0.0
                math_011_2.outputs[0].default_value = 0.0

                group_input_2 = node_tree2.nodes.new('NodeGroupInput')
                group_input_2.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
                group_input_2.hide = False
                group_input_2.location = (-380.0, -80.0)
                group_input_2.mute = False
                group_input_2.name = 'Group Input'
                group_input_2.use_custom_color = False
                group_input_2.width = 140.0
                group_input_2.outputs[0].default_value = 0.0

                # LINKS
                node_tree2.links.new(math_011_2.outputs[0], math_012_2.inputs[0])
                node_tree2.links.new(group_input_2.outputs[0], math_011_2.inputs[0])
                node_tree2.links.new(math_012_2.outputs[0], group_output_2.inputs[0])

            group_006_1 = node_tree1.nodes.new('CompositorNodeGroup')
            group_006_1.node_tree = bpy_data.node_groups.get('Degrees to Radians')
            group_006_1.parent = node_tree1.nodes.get('transform')
            group_006_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            group_006_1.hide = False
            group_006_1.location = (-300.0, -200.0)
            group_006_1.mute = False
            group_006_1.name = 'Group.006'
            group_006_1.use_custom_color = False
            group_006_1.width = 216.5218505859375
            group_006_1.inputs[0].default_value = 0.0
            group_006_1.outputs[0].default_value = 0.0

            transform_1 = node_tree1.nodes.new('CompositorNodeTransform')
            transform_1.parent = node_tree1.nodes.get('transform')
            transform_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            transform_1.filter_type = 'NEAREST'
            transform_1.hide = False
            transform_1.location = (100.0, -40.0)
            transform_1.mute = False
            transform_1.name = 'Transform'
            transform_1.use_custom_color = False
            transform_1.width = 140.0
            transform_1.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
            transform_1.inputs[1].default_value = 0.0
            transform_1.inputs[2].default_value = 0.0
            transform_1.inputs[3].default_value = 0.0
            transform_1.inputs[4].default_value = 1.399999976158142
            transform_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            translate_1 = node_tree1.nodes.new('CompositorNodeTranslate')
            translate_1.parent = node_tree1.nodes.get('transform')
            translate_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            translate_1.hide = True
            translate_1.location = (-180.0, -20.0)
            translate_1.mute = False
            translate_1.name = 'Translate'
            translate_1.use_custom_color = False
            translate_1.use_relative = False
            translate_1.width = 140.0
            translate_1.wrap_axis = 'BOTH'
            translate_1.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
            translate_1.inputs[1].default_value = 0.0
            translate_1.inputs[2].default_value = 0.0
            translate_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            math_011_1 = node_tree1.nodes.new('CompositorNodeMath')
            math_011_1.parent = node_tree1.nodes.get('transform')
            math_011_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            math_011_1.hide = True
            math_011_1.location = (20.0, -280.0)
            math_011_1.mute = False
            math_011_1.name = 'Math.011'
            math_011_1.operation = 'LESS_THAN'
            math_011_1.use_clamp = False
            math_011_1.use_custom_color = False
            math_011_1.width = 140.0
            math_011_1.inputs[0].default_value = 0.5
            math_011_1.inputs[1].default_value = 0.0
            math_011_1.inputs[2].default_value = 0.0
            math_011_1.outputs[0].default_value = 0.0

            set_alpha_001_1 = node_tree1.nodes.new('CompositorNodeSetAlpha')
            set_alpha_001_1.parent = node_tree1.nodes.get('transform')
            set_alpha_001_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            set_alpha_001_1.hide = True
            set_alpha_001_1.location = (200.0, -280.0)
            set_alpha_001_1.mute = False
            set_alpha_001_1.name = 'Set Alpha.001'
            set_alpha_001_1.use_custom_color = False
            set_alpha_001_1.width = 140.0
            set_alpha_001_1.inputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
            set_alpha_001_1.inputs[1].default_value = 1.0
            set_alpha_001_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            alpha_over_005_1 = node_tree1.nodes.new('CompositorNodeAlphaOver')
            alpha_over_005_1.parent = node_tree1.nodes.get('transform')
            alpha_over_005_1.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
            alpha_over_005_1.hide = True
            alpha_over_005_1.location = (400.0, -280.0)
            alpha_over_005_1.mute = False
            alpha_over_005_1.name = 'Alpha Over.005'
            alpha_over_005_1.premul = 0.0
            alpha_over_005_1.use_custom_color = False
            alpha_over_005_1.use_premultiply = False
            alpha_over_005_1.width = 140.0
            alpha_over_005_1.inputs[0].default_value = 1.0
            alpha_over_005_1.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
            alpha_over_005_1.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
            alpha_over_005_1.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)

            # LINKS
            node_tree1.links.new(colorramp_1.outputs[0], rgb_curves_007_1.inputs[1])
            node_tree1.links.new(colorramp_001_1.outputs[0], rgb_curves_008_1.inputs[1])
            node_tree1.links.new(blur_1.outputs[0], alpha_over_001_1.inputs[2])
            node_tree1.links.new(blur_1.outputs[0], alpha_over_002_1.inputs[2])
            node_tree1.links.new(colorramp_003_1.outputs[0], rgb_curves_009_1.inputs[1])
            node_tree1.links.new(blur_1.outputs[0], alpha_over_003_1.inputs[2])
            node_tree1.links.new(alpha_over_003_1.outputs[0], mix_001_1.inputs[2])
            node_tree1.links.new(group_input_1.outputs[0], mix_001_1.inputs[1])
            node_tree1.links.new(alpha_over_002_1.outputs[0], mix_004_1.inputs[2])
            node_tree1.links.new(group_input_1.outputs[0], mix_004_1.inputs[1])
            node_tree1.links.new(alpha_over_001_1.outputs[0], mix_005_1.inputs[2])
            node_tree1.links.new(group_input_1.outputs[0], mix_005_1.inputs[1])
            node_tree1.links.new(alpha_over_1.outputs[0], invert_006_1.inputs[1])
            node_tree1.links.new(group_input_1.outputs[0], mix_006_1.inputs[1])
            node_tree1.links.new(mix_003_1.outputs[0], mix_007_1.inputs[1])
            node_tree1.links.new(mix_005_1.outputs[0], mix_003_1.inputs[2])
            node_tree1.links.new(mix_004_1.outputs[0], mix_007_1.inputs[2])
            node_tree1.links.new(mix_007_1.outputs[0], mix_008_1.inputs[1])
            node_tree1.links.new(mix_001_1.outputs[0], mix_008_1.inputs[2])
            node_tree1.links.new(blur_1.outputs[0], invert_005_1.inputs[1])
            node_tree1.links.new(alpha_over_004_1.outputs[0], mix_009_1.inputs[2])
            node_tree1.links.new(group_input_1.outputs[0], mix_009_1.inputs[1])
            node_tree1.links.new(mix_009_1.outputs[0], mix_010_1.inputs[1])
            node_tree1.links.new(mix_006_1.outputs[0], mix_010_1.inputs[2])
            node_tree1.links.new(mix_010_1.outputs[0], mix_003_1.inputs[1])
            node_tree1.links.new(mix_008_1.outputs[0], mix_011_1.inputs[1])
            node_tree1.links.new(invert_005_1.outputs[0], alpha_over_004_1.inputs[2])
            node_tree1.links.new(blur_1.outputs[0], alpha_over_1.inputs[2])
            node_tree1.links.new(mix_008_1.outputs[0], mix_011_1.inputs[2])
            node_tree1.links.new(mix_011_1.outputs[0], mix_012_1.inputs[2])
            node_tree1.links.new(mix_012_1.outputs[0], group_output_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[0], mix_012_1.inputs[1])
            node_tree1.links.new(group_input_1.outputs[4], math_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[5], math_001_1.inputs[0])
            node_tree1.links.new(math_1.outputs[0], transform_1.inputs[1])
            node_tree1.links.new(math_001_1.outputs[0], transform_1.inputs[2])
            node_tree1.links.new(group_input_1.outputs[3], group_006_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[7], math_002_1.inputs[0])
            node_tree1.links.new(math_003_1.outputs[0], mix_011_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[14], math_003_1.inputs[0])
            node_tree1.links.new(math_004_1.outputs[0], mix_012_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[6], math_004_1.inputs[0])
            node_tree1.links.new(math_002_1.outputs[0], blur_1.inputs[1])
            node_tree1.links.new(math_005_1.outputs[0], blur_001_1.inputs[1])
            node_tree1.links.new(math_005_1.outputs[0], blur_002_1.inputs[1])
            node_tree1.links.new(math_005_1.outputs[0], blur_003_1.inputs[1])
            node_tree1.links.new(math_005_1.outputs[0], blur_004_1.inputs[1])
            node_tree1.links.new(math_005_1.outputs[0], blur_005_1.inputs[1])
            node_tree1.links.new(group_input_1.outputs[15], math_005_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[0], separate_hsva_1.inputs[0])
            node_tree1.links.new(separate_hsva_1.outputs[2], colorramp_1.inputs[0])
            node_tree1.links.new(separate_hsva_1.outputs[2], colorramp_001_1.inputs[0])
            node_tree1.links.new(separate_hsva_1.outputs[2], colorramp_002_1.inputs[0])
            node_tree1.links.new(separate_hsva_1.outputs[2], colorramp_003_1.inputs[0])
            node_tree1.links.new(blur_005_1.outputs[0], invert_013_1.inputs[1])
            node_tree1.links.new(blur_004_1.outputs[0], invert_012_1.inputs[1])
            node_tree1.links.new(blur_003_1.outputs[0], invert_011_1.inputs[1])
            node_tree1.links.new(blur_002_1.outputs[0], invert_010_1.inputs[1])
            node_tree1.links.new(blur_001_1.outputs[0], invert_009_1.inputs[1])
            node_tree1.links.new(invert_009_1.outputs[0], alpha_over_004_1.inputs[1])
            node_tree1.links.new(invert_010_1.outputs[0], alpha_over_1.inputs[0])
            node_tree1.links.new(invert_011_1.outputs[0], alpha_over_001_1.inputs[0])
            node_tree1.links.new(invert_012_1.outputs[0], alpha_over_002_1.inputs[0])
            node_tree1.links.new(invert_013_1.outputs[0], alpha_over_003_1.inputs[0])
            node_tree1.links.new(separate_hsva_1.outputs[2], colorramp_004_1.inputs[0])
            node_tree1.links.new(colorramp_004_1.outputs[0], rgb_curves_1.inputs[1])
            node_tree1.links.new(rgb_curves_1.outputs[0], blur_001_1.inputs[0])
            node_tree1.links.new(rgb_curves_006_1.outputs[0], blur_004_1.inputs[0])
            node_tree1.links.new(rgb_curves_007_1.outputs[0], blur_002_1.inputs[0])
            node_tree1.links.new(colorramp_002_1.outputs[0], rgb_curves_006_1.inputs[1])
            node_tree1.links.new(rgb_curves_008_1.outputs[0], blur_003_1.inputs[0])
            node_tree1.links.new(rgb_curves_009_1.outputs[0], blur_005_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[9], math_009_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[10], math_008_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[11], math_007_1.inputs[0])
            node_tree1.links.new(group_input_1.outputs[12], math_006_1.inputs[0])
            node_tree1.links.new(math_006_1.outputs[0], rgb_curves_009_1.inputs[2])
            node_tree1.links.new(math_007_1.outputs[0], rgb_curves_006_1.inputs[2])
            node_tree1.links.new(math_008_1.outputs[0], rgb_curves_008_1.inputs[2])
            node_tree1.links.new(math_009_1.outputs[0], rgb_curves_007_1.inputs[2])
            node_tree1.links.new(math_010_1.outputs[0], rgb_curves_1.inputs[2])
            node_tree1.links.new(invert_006_1.outputs[0], mix_006_1.inputs[2])
            node_tree1.links.new(group_input_1.outputs[13], math_010_1.inputs[0])
            node_tree1.links.new(colorramp_004_1.outputs[0], group_004_1.inputs[0])
            node_tree1.links.new(colorramp_001_1.outputs[0], group_001_1.inputs[0])
            node_tree1.links.new(colorramp_002_1.outputs[0], group_002_1.inputs[0])
            node_tree1.links.new(colorramp_003_1.outputs[0], group_003_1.inputs[0])
            node_tree1.links.new(group_1.outputs[0], group_output_1.inputs[2])
            node_tree1.links.new(colorramp_1.outputs[0], group_1.inputs[0])
            node_tree1.links.new(group_001_1.outputs[0], group_output_1.inputs[3])
            node_tree1.links.new(group_002_1.outputs[0], group_output_1.inputs[4])
            node_tree1.links.new(group_003_1.outputs[0], group_output_1.inputs[5])
            node_tree1.links.new(group_004_1.outputs[0], group_output_1.inputs[6])
            node_tree1.links.new(group_input_1.outputs[2], transform_1.inputs[4])
            node_tree1.links.new(transform_1.outputs[0], alpha_over_005_1.inputs[2])
            node_tree1.links.new(group_input_1.outputs[1], translate_1.inputs[0])
            node_tree1.links.new(translate_1.outputs[0], transform_1.inputs[0])
            node_tree1.links.new(group_006_1.outputs[0], transform_1.inputs[3])
            node_tree1.links.new(group_input_1.outputs[8], group_output_1.inputs[1])
            node_tree1.links.new(group_input_1.outputs[0], math_011_1.inputs[0])
            node_tree1.links.new(set_alpha_001_1.outputs[0], alpha_over_005_1.inputs[1])
            node_tree1.links.new(math_011_1.outputs[0], set_alpha_001_1.inputs[1])
            node_tree1.links.new(alpha_over_005_1.outputs[0], blur_1.inputs[0])

        watermark_0 = scene.node_tree.nodes.new('CompositorNodeGroup')
        watermark_0.node_tree = bpy_data.node_groups.get('Watermark Level 2')
        watermark_0.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
        watermark_0.hide = False
        watermark_0.location = (0.0, 0.0)
        watermark_0.mute = False
        watermark_0.name = 'Watermark'
        watermark_0.use_custom_color = False
        watermark_0.width = 230.7401123046875
        watermark_0.inputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
        watermark_0.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
        watermark_0.inputs[2].default_value = 0.5
        watermark_0.inputs[3].default_value = 45.0
        watermark_0.inputs[4].default_value = 0.0
        watermark_0.inputs[5].default_value = 0.0
        watermark_0.inputs[6].default_value = 99.0
        watermark_0.inputs[7].default_value = 1.0
        watermark_0.inputs[9].default_value = 94.0
        watermark_0.inputs[10].default_value = 94.0
        watermark_0.inputs[11].default_value = 95.0
        watermark_0.inputs[12].default_value = 90.0
        watermark_0.inputs[13].default_value = 96.0
        watermark_0.inputs[14].default_value = 0.0
        watermark_0.inputs[15].default_value = 2.0
        watermark_0.outputs[0].default_value = (0.0, 0.0, 0.0, 0.0)
        watermark_0.outputs[2].default_value = (0.0, 0.0, 0.0, 0.0)
        watermark_0.outputs[3].default_value = (0.0, 0.0, 0.0, 0.0)
        watermark_0.outputs[4].default_value = (0.0, 0.0, 0.0, 0.0)
        watermark_0.outputs[5].default_value = (0.0, 0.0, 0.0, 0.0)
        watermark_0.outputs[6].default_value = (0.0, 0.0, 0.0, 0.0)

        # LINKS
        scene.node_tree.links.new(image_001_0.outputs[0], watermark_0.inputs[1])

        return watermark_0, image_001_0

    @staticmethod
    def _composite_node(scene):
        # get composite node
        return next((node for node in scene.node_tree.nodes if node.bl_idname == 'CompositorNodeComposite'), None)

    @staticmethod
    def _viewer_node(scene):
        # get viewer node
        return next((node for node in scene.node_tree.nodes if node.bl_idname == 'CompositorNodeViewer'), None)
