import os
from typing import List
from pyrep.objects.dummy import Dummy
from pyrep.objects.joint import Joint
from rlbench.backend.task import Task
from rlbench.backend.conditions import JointCondition
from pyrep.objects.shape import Shape
import random
from pyrep.const import TextureMappingMode

OPTIONS = ['left', 'right']


class TurnTapRandomTextures(Task):

    def init_task(self) -> None:
        self.left_start = Dummy('waypoint0')
        self.left_end = Dummy('waypoint1')
        self.right_start = Dummy('waypoint5')
        self.right_end = Dummy('waypoint6')
        self.left_joint = Joint('left_joint')
        self.right_joint = Joint('right_joint')

        self._texture_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, "assets", "textures"))
        self._texture_files = os.listdir(self._texture_dir)

        self._obj_shapes = [Shape(obj_name) for obj_name in
                            ['tap_main_visual', 'tap_right_visual', 'tap_left_visual']]

    def init_episode(self, index: int) -> List[str]:

        for obj_shape in self._obj_shapes:

            rand_ind = random.randint(0, len(self._texture_files) - 1)
            rand_texture_file = os.path.join(self._texture_dir, self._texture_files[rand_ind])
            text_obj, texture = self.pyrep.create_texture(rand_texture_file)
            obj_shape.set_texture(texture, TextureMappingMode.PLANE)
            text_obj.remove()

        option = OPTIONS[index]
        if option == 'right':
            self.left_start.set_position(self.right_start.get_position())
            self.left_start.set_orientation(self.right_start.get_orientation())
            self.left_end.set_position(self.right_end.get_position())
            self.left_end.set_orientation(self.right_end.get_orientation())
            self.register_success_conditions(
                [JointCondition(self.right_joint, 1.57)])
        else:
            self.register_success_conditions(
                [JointCondition(self.left_joint, 1.57)])

        return ['turn %s tap' % option,
                'rotate the %s tap' % option,
                'grasp the %s tap and turn it' % option]

    def variation_count(self) -> int:
        return 2
