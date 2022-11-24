from typing import List
from pyrep.objects.shape import Shape
from pyrep.objects.proximity_sensor import ProximitySensor
from rlbench.backend.task import Task
from pyrep.objects.object import Object
from pyrep.objects.dummy import Dummy
from rlbench.backend.conditions import DetectedCondition
import os
import random
from pyrep.const import TextureMappingMode

DIRT_NUM = 5


class SweepToDustpanOfSizeRandomFullBodyEntitiesTextures(Task):

    def init_task(self) -> None:
        self._dustpan_sizes = ['tall', 'short']

        broom = Shape('broom')
        self.register_graspable_objects([broom])

        self._waypoint_paths = {
            0: [Dummy('point1a'),
                Dummy('point1b'),
                Dummy('point1c')],

            1: [Dummy('point2a'),
                Dummy('point2b'),
                Dummy('point2c')]
        }

        self._broom_shape = Shape('sweep_to_dustpan_broom_visual')
        self._broom_holder_shape = Shape('broom_holder')
        self._tall_dustpan_shapes = [Shape(obj_name) for obj_name in ['dustpan_tall', 'Dustpan_3', 'Dustpan_5']]
        self._short_dustpan_shapes = [Shape(obj_name) for obj_name in ['dustpan_short', 'Dustpan_4', 'Dustpan_6']]
        self._dirt_shapes = [Shape(obj_name) for obj_name in ['dirt0', 'dirt1', 'dirt2', 'dirt3', 'dirt4']]

        self._texture_dir = "/home/soul/Development/Stanford/Fall 2022/CS 330: Deep Multi-Task and Meta Learning/" \
                            "Project/RLBench/tests/unit/assets/textures"
        self._texture_files = os.listdir(self._texture_dir)

    def init_episode(self, index: int) -> List[str]:

        rand_ind = random.randint(0, len(self._texture_files) - 1)
        rand_texture_file = os.path.join(self._texture_dir, self._texture_files[rand_ind])
        text_obj, texture = self.pyrep.create_texture(rand_texture_file)
        for shape in self._dirt_shapes:
            shape.set_texture(texture, TextureMappingMode.CUBE)
        text_obj.remove()

        rand_ind = random.randint(0, len(self._texture_files) - 1)
        rand_texture_file = os.path.join(self._texture_dir, self._texture_files[rand_ind])
        text_obj, texture = self.pyrep.create_texture(rand_texture_file)
        self._broom_shape.set_texture(texture, TextureMappingMode.PLANE)
        text_obj.remove()

        rand_ind = random.randint(0, len(self._texture_files) - 1)
        rand_texture_file = os.path.join(self._texture_dir, self._texture_files[rand_ind])
        text_obj, texture = self.pyrep.create_texture(rand_texture_file)
        self._broom_holder_shape.set_texture(texture, TextureMappingMode.CUBE)
        text_obj.remove()

        rand_ind = random.randint(0, len(self._texture_files) - 1)
        rand_texture_file = os.path.join(self._texture_dir, self._texture_files[rand_ind])
        text_obj, texture = self.pyrep.create_texture(rand_texture_file)
        for shape in self._tall_dustpan_shapes[:-1]:
            shape.set_texture(texture, TextureMappingMode.PLANE)
        self._tall_dustpan_shapes[-1].set_texture(texture, TextureMappingMode.CYLINDER)
        text_obj.remove()

        rand_ind = random.randint(0, len(self._texture_files) - 1)
        rand_texture_file = os.path.join(self._texture_dir, self._texture_files[rand_ind])
        text_obj, texture = self.pyrep.create_texture(rand_texture_file)
        for shape in self._short_dustpan_shapes[:-1]:
            shape.set_texture(texture, TextureMappingMode.PLANE)
        self._short_dustpan_shapes[-1].set_texture(texture, TextureMappingMode.CYLINDER)
        text_obj.remove()


        self._variation_index = index
        dustpan_size = self._dustpan_sizes[self._variation_index]

        success_sensor = ProximitySensor(f'success_{dustpan_size}')
        dirts = [Shape('dirt' + str(i)) for i in range(DIRT_NUM)]
        conditions = [DetectedCondition(dirt, success_sensor) for dirt in dirts]
        self.register_success_conditions(conditions)

        target_waypoints = self._waypoint_paths[self._variation_index]
        self._waypoints = [Dummy('waypoint%d'%(i))
                           for i in range(2, 5)]

        for i in range(len(target_waypoints)):
            self._waypoints[i].set_pose(target_waypoints[i].get_pose())
        self.register_stop_at_waypoint(2+i+1)

        return ['sweep dirt to the %s dustpan' % (dustpan_size),
                'sweep the dirt up into the %s dustpan' % (dustpan_size),
                'use the broom to brush the dirt into the %s dustpan' % (dustpan_size),
                'clean up the dirt with the %s pan' % (dustpan_size)]

    def variation_count(self) -> int:
        return 2

    # def boundary_root(self) -> Object:
    #     return Shape('boundary_root')
