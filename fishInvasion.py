#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 19:02:54 2018

@author: rachellerunyon
"""

#import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from arrow import Arrow
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Monster Invasion")
    #Make the play button
    play_button = Button(ai_settings, screen, "Play")
    #create an instance to store game stats and create a score board
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #bg_color = (133,210,205) #light blue
    #make an arrow
    #manke an arrow, a gorup of bullets,and a group of monsters
    arrow = Arrow(ai_settings, screen)
    #make a group to store bullets in
    bullets = Group()
    monsters = Group()
    gf.create_fleet(ai_settings, screen, arrow, monsters)

    
    #start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats,sb, play_button, arrow,monsters, bullets)
        if stats.game_active:
            arrow.update()
            gf.update_bullets(ai_settings, screen,stats,sb, arrow, monsters, bullets)
            gf.update_monsters(ai_settings, screen,stats, sb, arrow, monsters, bullets)
        
       
        gf.update_screen(ai_settings, screen,stats, sb, arrow, monsters,bullets, play_button)
            




 
run_game()

