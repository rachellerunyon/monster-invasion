#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 20:05:33 2018

@author: rachellerunyon
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the arrows's current position"""
        super(Bullet, self).__init__()
        self.screen = screen
        
        #create a cullet rect at (0,0) and then set correct position
        self.rect = pygame.rect(0, 0, ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.recttop = ship.rect.top
        
        #store that bullets position as a decimal val
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

def update(self):
    """move the bullet up the screen"""
    #update the decimal position of the bullet
    self.y -= self.speed_factor
    #update the rect position
    self.rect.y = self.y
    
def draw_bullet(self):
    """draw the bullet to the screen"""
    pygame.draw.rect(self.screen, self.color, self.rect)
        
        