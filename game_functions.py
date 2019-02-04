#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 15:57:52 2018

@author: rachellerunyon
"""

import sys
from time import sleep
import pygame
from bullet import Bullet
from Monster import Monster

def check_keydown_events(event, ai_settings, screen,arrow,bullets):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        arrow.moving_right = True
    elif event.key == pygame.K_LEFT:
        arrow.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, arrow, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    

def check_keyup_events(event, arrow):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        arrow.moving_right = False
    elif event.key == pygame.K_LEFT:
        arrow.moving_left = False

def check_events(ai_settings,screen, stats, sb, play_button, arrow, monsters,
                 bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, arrow,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,arrow)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                              arrow, monsters, bullets, mouse_x, mouse_y)
        
def check_play_button(ai_settings, screen, stats, sb, play_button, arrow,
                      monsters, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        
        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True
        
        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_arrows()
        
        # Empty the list of aliens and bullets.
        monsters.empty()
        bullets.empty()
        
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, arrow, monsters)
        arrow.center_arrow()


def fire_bullet(ai_settings, screen, arrow,bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, arrow)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, stats, sb, arrow, monsters, bullets,
                  play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    arrow.blitme()
    monsters.draw(screen)

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, arrow, monsters, bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            # print(len(bullets))

    check_bullet_monster_collisions(ai_settings, screen, stats, sb, arrow, monsters, bullets)
    
def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_bullet_monster_collisions(ai_settings, screen, stats, sb, arrow, monsters, bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, monsters, True, True)

    if collisions:
        for monsters in collisions.values():
            stats.score += ai_settings.monster_points * len(monsters)
            sb.prep_score()

        check_high_score(stats, sb)

    if len(monsters) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        
        #inc level
        stats.level += 1
        sb.prep_level()
        
        create_fleet(ai_settings, screen, arrow, monsters)
        #start_new_level(ai_settings, monsters, bullets, sb, screen, arrow, stats)
        
def check_fleet_edges(ai_settings, monsters):
    """Respond appropriately if any aliens have reached an edge."""
    for monster in monsters.sprites():
        if monster.check_edges():
            change_fleet_direction(ai_settings, monsters)
            break

def change_fleet_direction(ai_settings, monsters):
    """Drop the entire fleet and change the fleet's direction."""
    for monster in monsters.sprites():
       monster.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
def arrow_hit(ai_settings, screen, stats, sb, arrow, monsters, bullets):
    """Respond to arrow being hit by monster."""


    if stats.arrows_left > 0:
        # Decrement ships_left.
        stats.arrows_left -= 1

        # Update scoreboards.
        sb.prep_arrows()
        # Empty the list of aliens and bullets.
        monsters.empty()
        bullets.empty()
        
         # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, arrow, monsters)
        arrow.center_arrow()

        # Pause.
        sleep(0.5)


    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        
    
        
def check_monsters_bottom(ai_settings,screen,stats,sb, arrow, monsters, bullets):
    """Check if any monsters have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for monster in monsters.sprites():
        if monster.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            arrow_hit(ai_settings,screen, stats, sb, arrow, monsters, bullets)
            break
        
def update_monsters(ai_settings,screen, stats,sb, arrow, monsters, bullets):
    """Check if the fleet is at an edge,
    and then update the positions of all monsters in the fleet."""
    check_fleet_edges(ai_settings, monsters)
    monsters.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(arrow, monsters):
        #print("Arrow hit!!!")
        arrow_hit(ai_settings,screen,stats, sb, arrow, monsters, bullets)

    # Look for aliens hitting the bottom of the screen.
    check_monsters_bottom(ai_settings, screen, stats, sb, arrow, monsters, bullets)
    
def get_number_monsters_x(ai_settings, monster_width):
    """Determine the number of monsters that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * monster_width
    number_monsters_x = int(available_space_x / (2 * monster_width))
    return number_monsters_x

def get_number_rows(ai_settings, arrow_height, monster_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                         (3 * monster_height) - arrow_height)
    number_rows = int(available_space_y / (2 * monster_height))

    return number_rows

def create_monster(ai_settings, screen, monsters,monster_number, row_number):
    # Create an monster and place it in the row.
    monster = Monster(ai_settings, screen)
    monster_width = monster.rect.width
    monster.x = monster_width + 2 * monster_width * monster_number
    monster.rect.x = monster.x
    monster.rect.y = monster.rect.height + 2 * monster.rect.height * row_number
    monsters.add(monster)
    
def create_fleet(ai_settings, screen, arrow, monsters):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    monster = Monster(ai_settings, screen)
    number_monsters_x = get_number_monsters_x(ai_settings, monster.rect.width)
    number_rows = get_number_rows(ai_settings, arrow.rect.height,
                                  monster.rect.height)

    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for monster_number in range(number_monsters_x):
            create_monster(ai_settings, screen, monsters, monster_number, row_number)

