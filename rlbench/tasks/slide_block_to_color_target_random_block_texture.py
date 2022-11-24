from typing import List
from pyrep.objects.shape import Shape
from pyrep.objects.dummy import Dummy
from pyrep.objects.proximity_sensor import ProximitySensor
from rlbench.backend.task import Task
from rlbench.backend.conditions import DetectedCondition
import numpy as np
from pyrep.const import TextureMappingMode
import random
import os

class SlideBlockToColorTargetRandomBlockTexture(Task):

    def init_task(self) -> None:
        self.block = Shape('block')
        self.target_colors = ['green', 'blue', 'pink', 'yellow']

        self._waypoint_paths = {
            0: [Dummy('point1a'),
                Dummy('point1b')],

            1: [Dummy('point2a'),
                Dummy('point2b'),
                Dummy('point2c'),
                Dummy('point2d'),
                Dummy('point2e')],

            2: [Dummy('point3a'),
                Dummy('point3b')],

            3: [Dummy('point4a'),
                Dummy('point4b'),
                Dummy('point4c'),
                Dummy('point4d'),
                Dummy('point4e')]
        }

        self._texture_dir = "/home/soul/Development/Stanford/Fall 2022/CS 330: Deep Multi-Task and Meta Learning/" \
                            "Project/RLBench/tests/unit/assets/textures"
        self._texture_files = os.listdir(self._texture_dir)

    def init_episode(self, index: int) -> List[str]:

        rand_ind = random.randint(0, len(self._texture_files) - 1)
        rand_texture_file = os.path.join(self._texture_dir, self._texture_files[rand_ind])
        text_obj, texture = self.pyrep.create_texture(rand_texture_file)
        self.block.set_texture(texture, TextureMappingMode.PLANE)
        text_obj.remove()

        self._variation_index = index

        self.register_success_conditions([
            DetectedCondition(Shape('block'), 
                ProximitySensor(f'success{self._variation_index+1}'))])


        target_color = self.target_colors[self._variation_index]
        target_waypoints = self._waypoint_paths[self._variation_index]

        self._waypoints = [Dummy('waypoint%d'%(i))
                           for i in range(5)]

        for i in range(len(target_waypoints)):
            self._waypoints[i].set_pose(target_waypoints[i].get_pose())
        self.register_stop_at_waypoint(i+1)

        return ['slide the block to %s target' % (target_color),
                'slide the block onto the %s square' % (target_color),
                'push the block until it is sitting on top of the %s target' % (target_color),
                'slide the block towards the %s plane' % (target_color),
                'cover the %s target with the block by pushing the block in its direction' % (target_color)]

    def variation_count(self) -> int:
        return 4
