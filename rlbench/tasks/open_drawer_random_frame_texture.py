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


class OpenDrawerRandomFrameTexture(Task):

    def init_task(self) -> None:
        self._options = ['bottom', 'middle', 'top']
        self._texture_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, "assets", "textures"))
        self._texture_files = os.listdir(self._texture_dir)

        self._anchors = [Dummy('waypoint_anchor_%s' % opt)
                         for opt in self._options]
        self._joints = [Joint('drawer_joint_%s' % opt)
                        for opt in self._options]
        self._waypoint1 = Dummy('waypoint1')

        self._drawer_frame_shape = Shape('drawer_frame')

    def init_episode(self, index: int) -> List[str]:

        rand_ind = random.randint(0, len(self._texture_files) - 1)
        rand_texture_file = os.path.join(self._texture_dir, self._texture_files[rand_ind])
        text_obj, texture = self.pyrep.create_texture(rand_texture_file)

        shape_components = self._drawer_frame_shape.ungroup()
        for sh in shape_components:
            sh.set_texture(texture, TextureMappingMode.PLANE)
        self.pyrep.group_objects(shape_components)
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

        self._drawer_frame_shape = Shape('drawer_frame')

