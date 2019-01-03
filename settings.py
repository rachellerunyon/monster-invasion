#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 15:44:47 2018

@author: rachellerunyon
"""

class Settings():
    """A class to store all settings for Monster Invasion."""
    def __init__(self):
        
        """Initialize the game's static settings."""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (133,210,205)
        
        #arrow settings
        self.arrow_speed_factor = 1.5
        self.arrow_limit = 3
        
        #bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 2
        self.bullet_height = 16
        self.bullet_color = 58, 58, 58
        self.bullets_allowed = 3
        
        #monster settings
        self.monster_speed_factor = 1
        self.fleet_drop_speed = 10
        #How quickly the game speeds up
        self.speedup_scale = 1.1
        #how quickly the monster point vals inc
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        #fleet_irection of 1 represents right; -1 represents left.
        self.fleet_direction =1
        
    def initialize_dynamic_settings(self):
        """Initialze settings that change throughout the game"""
        self.arrow_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.monster_speed_factor = 1
        #fleet_direction of 1 represens right; -1 represents left
        self.fleet_direction = 1
        #scoring
        self.monster_points = 50
        
    def increase_speed(self):
        """Increase speed settings and monster point values"""
        self.arrow_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.monster_speed_factor *= self.speedup_scale
        self.monster_points = int(self.monster_points * self.score_scale)
        print(self.monster_points)
        