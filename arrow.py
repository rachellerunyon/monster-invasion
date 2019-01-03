#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 15:45:50 2018

@author: rachellerunyon
"""
import pygame
from pygame.sprite import Sprite
class Arrow(Sprite):
    def __init__(self, ai_settings, screen):
        #inittialize the arrow and set its startign position
        super(Arrow, self).  __init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.moving_left = False
        """Initialize the arrow and set its starting position."""
        #load the arrow image and get its rect
        self.image = pygame.image.load('/Users/rachellerunyon/Desktop/Sword2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #start each new arrow at bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #movement flag
        self.moving_right = False
        
    def update(self):
        """Update the arrows position based on the movement flag."""
        #update the arrow's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left  > 0:
            self.center -= self.ai_settings.ship_speed_factor
       
           
            
    def blitme(self):
        """draw the arrow at its correct location"""
        self.screen.blit(self.image, self.rect)
        
    def center_arrow(self):
        """center the arrow on the screen"""
        self.center = self.screen_rect.centerx
        #update rect object from self.center
        self.rect.centerx = self.center
        self.rect.centerx +=1
        self.rect.centerx -= 1