from typing import List

from pyrep.const import TextureMappingMode
from pyrep.objects.dummy import Dummy
from pyrep.objects.proximity_sensor import ProximitySensor
from pyrep.objects.shape import Shape
from rlbench.backend.conditions import NothingGrasped, DetectedCondition
from rlbench.backend.task import Task
import os
import random


MEAT = ['chicken', 'steak']


class MeatOffGrillRandomFullBodyTexture(Task):

    def init_task(self) -> None:
        self._steak = Shape('steak')
        self._chicken = Shape('chicken')
        self._success_sensor = ProximitySensor('success')
        self.register_graspable_objects([self._chicken, self._steak])
        self._w1 = Dummy('waypoint1')
        self._w1z= self._w1.get_position()[2]

        self._texture_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, "assets", "textures"))
        self._texture_files = os.listdir(self._texture_dir)
        self._grill_shape = Shape('grill_visual')

    def init_episode(self, index: int) -> List[str]:

        rand_ind = random.randint(0, len(self._texture_files) - 1)
        rand_texture_file = os.path.join(self._texture_dir, self._texture_files[rand_ind])
        text_obj, texture = self.pyrep.create_texture(rand_texture_file)

        ungrouped_simple_shapes = self._grill_shape.ungroup()
        for shape in ungrouped_simple_shapes:
            shape.set_texture(texture, TextureMappingMode.PLANE)
        self.pyrep.group_objects(ungrouped_simple_shapes)
        text_obj.remove()

        conditions = [NothingGrasped(self.robot.gripper)]
        if index == 0:
            x, y, _ = self._chicken.get_position()
            self._w1.set_position([x, y, self._w1z])
            conditions.append(
                DetectedCondition(self._chicken, self._success_sensor))
        else:
            x, y, _ = self._steak.get_position()
            self._w1.set_position([x, y, self._w1z])
            conditions.append(
                DetectedCondition(self._steak, self._success_sensor))
        self.register_success_conditions(conditions)
        return ['take the %s off the grill' % MEAT[index],
                'pick up the %s and place it next to the grill' % MEAT[index],
                'remove the %s from the grill and set it down to the side'
                % MEAT[index]]

    def variation_count(self) -> int:
        return 2
