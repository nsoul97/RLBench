import os.path
from typing import List, Tuple
import numpy as np
from pyrep.objects.dummy import Dummy
from pyrep.objects.joint import Joint
from rlbench.backend.conditions import JointCondition
from rlbench.backend.task import Task
from pyrep.objects.shape import Shape
from pyrep.const import TextureMappingMode
import random


class OpenDrawerRandomFullBodyTexture(Task):

    def init_task(self) -> None:
        self._options = ['bottom', 'middle', 'top']
        self._texture_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, "assets", "textures"))
        self._texture_files = os.listdir(self._texture_dir)

        self._anchors = [Dummy('waypoint_anchor_%s' % opt)
                         for opt in self._options]
        self._joints = [Joint('drawer_joint_%s' % opt)
                        for opt in self._options]
        self._waypoint1 = Dummy('waypoint1')

        self._obj_shapes = [Shape(obj_name) for obj_name in
                            ['drawer_frame', 'drawer_bottom', 'drawer_middle', 'drawer_top']]

    def init_episode(self, index: int) -> List[str]:

        rand_ind = random.randint(0, len(self._texture_files) - 1)
        rand_texture_file = os.path.join(self._texture_dir, self._texture_files[rand_ind])
        text_obj, texture = self.pyrep.create_texture(rand_texture_file)

        for obj_shape in self._obj_shapes:
            mass = obj_shape.get_mass()
            shape_components = obj_shape.ungroup()
            obj_name = obj_shape.get_name()
            for i, sh in enumerate(shape_components):
                if obj_name != 'drawer_frame':
                    pass
                    if i == 5 or i == 7:
                        sh.set_texture(texture, TextureMappingMode.CUBE)
                    elif i == 6:
                        sh.set_texture(texture, TextureMappingMode.CYLINDER)
                    else:
                        sh.set_texture(texture, TextureMappingMode.PLANE)
                else:
                    sh.set_texture(texture, TextureMappingMode.PLANE)

            obj_shape = self.pyrep.group_objects(shape_components)
            obj_shape.set_mass(mass)

        text_obj.remove()

        option = self._options[index]
        self._waypoint1.set_position(self._anchors[index].get_position())
        self.register_success_conditions(
            [JointCondition(self._joints[index], 0.15)])
        return ['open the %s drawer' % option,
                'grip the %s handle and pull the %s drawer open' % (
                    option, option),
                'slide the %s drawer open' % option]

    def variation_count(self) -> int:
        return 3

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        return [0, 0, - np.pi / 8], [0, 0, np.pi / 8]

    def cleanup(self) -> None:
        self.unload()
        self.load()

        self._anchors = [Dummy('waypoint_anchor_%s' % opt)
                         for opt in self._options]
        self._joints = [Joint('drawer_joint_%s' % opt)
                        for opt in self._options]
        self._waypoint1 = Dummy('waypoint1')

        self._obj_shapes = [Shape(obj_name) for obj_name in
                            ['drawer_frame', 'drawer_bottom', 'drawer_middle', 'drawer_top']]