#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:14:52 2018

@author: rachellerunyon
"""

import pygame
from pygame.sprite import Sprite

class Monster(Sprite):
    """A class to represent a single monster in the fleet """
    def __init__(self, ai_settings, screen):
        """Initialize the monster and set its starting position."""
        super(Monster, self). __init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #load the monster image and set its rect attribute
        self.image = pygame.image.load('/Users/rachellerunyon/Desktop/monster3.bmp')
        self.rect = self.image.get_rect()
        
        #start each new monster near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #store the monsters exact position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True is monster us at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        """Move the monster right or left"""
        self.x += (self.ai_settings.monster_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the monster at its current location"""
        self.screen.blit(self.image, self.rect)
   