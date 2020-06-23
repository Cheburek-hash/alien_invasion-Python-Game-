import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from save_stats import Savescore, Giveses
from ships_live import Shipss

#run game :d
def run_game():
    pygame.init()
    ai_settings = Settings()
    print (ai_settings.screen_width)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Inwasion")
    #create ship
    ship = Ship(ai_settings, screen)
    #ships live
    shipss = Shipss(ai_settings, screen)
    #create stats
    stats = GameStats(ai_settings)
    #save score
    ses_2 = Giveses()
    save_s = Savescore(stats, ses_2)
    #create button Play
    play_button = Button(ai_settings, screen, "Play")
    #create score
    sb = Scoreboard(ai_settings, screen, stats, save_s, shipss)
    #create group for bullets
    bullets = Group()
    #create group for alien
    aliens = Group()
    #create fleet for aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #main loop
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, sb, aliens, bullets, save_s)
        ship.update()
        gf.update_bullets(ai_settings, screen, stats, ship, sb, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, sb, aliens, bullets, play_button)        
        gf.update_screen(ai_settings, screen, ship, stats, sb, aliens, bullets, play_button, save_s)



run_game()
