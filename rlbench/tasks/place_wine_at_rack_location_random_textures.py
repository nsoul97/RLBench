from typing import List, Tuple
import os
from pyrep.const import TextureMappingMode
import numpy as np
from pyrep.objects.shape import Shape
from pyrep.objects.proximity_sensor import ProximitySensor
from rlbench.backend.task import Task
from pyrep.objects.dummy import Dummy
from rlbench.backend.conditions import DetectedCondition, NothingGrasped
import random


class PlaceWineAtRackLocationRandomTextures(Task):

    def init_task(self):
        self.wine_bottle = Shape('wine_bottle')
        self.register_graspable_objects([self.wine_bottle])

        self.locations = ['middle', 'left', 'right']

        self.register_waypoint_ability_start(3, self._move_to_rack)
        
        self.register_waypoint_ability_start(5, self._is_last)
        self.register_waypoint_ability_start(6, self._is_last)
        self.register_waypoint_ability_start(7, self._is_last)
        self.register_waypoint_ability_start(8, self._is_last)

        self._rack_shapes = [Shape(obj_name) for obj_name in
                             ['rack_bottom_visual', 'rack_top_visual']]
        self._bottle_shape = Shape('wine_bottle_visual')

        self._texture_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, "assets", "textures"))
        self._texture_files = os.listdir(self._texture_dir)

    def init_episode(self, index: int) -> List[str]:

        for shape in self._rack_shapes:
            rand_ind = random.randint(0, len(self._texture_files) - 1)
            rand_texture_file = os.path.join(self._texture_dir, self._texture_files[rand_ind])
            text_obj, texture = self.pyrep.create_texture(rand_texture_file)
            shape.set_texture(texture, TextureMappingMode.PLANE)
            text_obj.remove()

        ungrouped_simple_shapes = self._bottle_shape.ungroup()
        for shape in ungrouped_simple_shapes:
            rand_ind = random.randint(0, len(self._texture_files) - 1)
            rand_texture_file = os.path.join(self._texture_dir, self._texture_files[rand_ind])
            text_obj, texture = self.pyrep.create_texture(rand_texture_file)
            shape.set_texture(texture, TextureMappingMode.CYLINDER)
            text_obj.remove()
        self.pyrep.group_objects(ungrouped_simple_shapes)

        self._variation_index = index
        location = self.locations[self._variation_index]
        self.register_success_conditions(
            [DetectedCondition(self.wine_bottle, 
                ProximitySensor(f'success_{location}')),
            NothingGrasped(self.robot.gripper)])

        return ['stack the wine bottle to the %s of the rack' % (location),
                'slide the bottle onto the %s part of the rack' % (location),
                'put the wine on the %s' % (location),
                'leave the wine on the %s section of the shelf' % (location),
                'grasp the bottle and put it away on the %s' % (location)]
    
    def _move_to_rack(self, _):
        next1, next2 = Dummy('waypoint3'), Dummy('waypoint4')
        left1, left2 = Dummy('waypoint5'), Dummy('waypoint6')
        right1, right2 = Dummy('waypoint7'), Dummy('waypoint8')
        
        if self._variation_index == 1:
            next1.set_position(left1.get_position())
            next1.set_orientation(left1.get_orientation())

            next2.set_position(left2.get_position())
            next2.set_orientation(left2.get_orientation())
        elif self._variation_index == 2:
            next1.set_position(right1.get_position())
            next1.set_orientation(right1.get_orientation())

            next2.set_position(right2.get_position())
            next2.set_orientation(right2.get_orientation())


    def _is_last(self, waypoint):
        waypoint.skip = True

    def variation_count(self) -> int:
        return 3

    def base_rotation_bounds(self) -> Tuple[List[float], List[float]]:
        return [0, 0, -np.pi / 4.], [0, 0, np.pi / 4.]
