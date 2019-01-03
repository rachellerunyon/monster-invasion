#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:59:26 2018

@author: rachellerunyon
"""
class GameStats():
    """Track stats for monster invasion"""
    
    def __init__(self, ai_settings):
        """initialze stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #start monster invasion in an active state.
        self.game_active = True
        #start game in an inactive state
        self.game_active = False
        #high score should never be reset
        self.high_score = 0
        
    def reset_stats(self):
        """Initialze stats that can change during the game"""
        self.arrows_left = self.ai_settings.arrow_limit
        self.score = 0
        self.level = 1