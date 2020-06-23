import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, stats, sb, bullets, save_s):
#moves of ship
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
#shoting
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
#exit
	elif event.key == pygame.K_q:
		save_s.save_high_score(stats)
		sys.exit()
#check keydown of music
	elif event.key == pygame.K_1:
		stop_all_music(ai_settings)
		ai_settings.sound_1.play(-1)
	elif event.key == pygame.K_2:
		stop_all_music(ai_settings)
		ai_settings.sound_2.play(-1)
	elif event.key == pygame.K_3:
		stop_all_music(ai_settings)
		ai_settings.sound_3.play(-1)
	elif event.key == pygame.K_4:
		stop_all_music(ai_settings)
		ai_settings.sound_4.play(-1)
	elif event.key == pygame.K_5:
		stop_all_music(ai_settings)
		ai_settings.sound_5.play(-1)
	elif event.key == pygame.K_z:
		stop_all_music(ai_settings)
		pygame.mixer.music.play(-1)
	elif event.key == pygame.K_o:
		volume_increase(ai_settings)
	elif event.key == pygame.K_p:
		volume_decrease(ai_settings)
def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
def check_events(ai_settings, screen, stats, play_button, ship, sb, aliens, bullets, save_s):
	#preparing click and mouse's event
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			save_s.save_high_score(stats)
			sys.exit()
		elif event.type == pygame.KEYDOWN: #если клавиша нажата 
			check_keydown_events(event, ai_settings, screen, ship, stats, sb, bullets, save_s)
		elif event.type == pygame.KEYUP:  #если отпущенна
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN: #нажатия мыши
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, play_button, ship, sb, aliens, bullets, mouse_x, mouse_y)
def check_play_button(ai_settings, screen, stats, play_button, ship, sb, aliens, bullets, mouse_x, mouse_y):
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		ai_settings.initialize_dynamic_settings()
		pygame.mouse.set_visible(False)
		#ships live
		stats.ship_left = 3
		#game active (To move the fleet)
		stats.game_active = True
		#create fleet, ship and other
		clear_and_add(aliens, bullets, ai_settings, screen, ship)
		stats.check_game_active()
		#display (update) basic data for the first level
		sb.prep_level()
		sb.prep_score()
		sb.prep_ships()
		#standart bg music
		play_bg_music(ai_settings)
def play_bg_music(ai_settings):
	pygame.mixer.music.load(ai_settings.music)
	pygame.mixer.music.play(-1)
	pygame.mixer.music.set_volume(ai_settings.volume)
def stop_all_music(ai_settings):
	pygame.mixer.music.stop()
	ai_settings.sound_1.stop()
	ai_settings.sound_2.stop()
	ai_settings.sound_3.stop()
	ai_settings.sound_4.stop()
	ai_settings.sound_5.stop()
	#ai_settings.sound_6.stop()
	#ai_settings.sound_7.stop()
def volume_increase(ai_settings):
	#volume_increase
	ai_settings.increase_standart_volume()
	pygame.mixer.music.set_volume(ai_settings.volume)
	if ai_settings.volume > 1:
		ai_settings.volume = 1
	print(ai_settings.volume)
def volume_decrease(ai_settings):
	#volume_decrease
	ai_settings.decrease_standart_volume()
	pygame.mixer.music.set_volume(ai_settings.volume)
	if ai_settings.volume <= 0:
		ai_settings.volume = 0
	print(ai_settings.volume)


def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings, screen, ship)
			bullets.add(new_bullet)
def update_bullets(ai_settings, screen, stats, ship, sb, aliens, bullets):
	#update position bullets
	bullets.update()
	#delete old bullets
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0 or bullet.rect.top <= 0:
			bullets.remove(bullet)
	#check bulets and aliens colisions
	check_bullet_alien_collisions(ai_settings, screen, stats, ship, sb, aliens, bullets)
def check_bullet_alien_collisions(ai_settings, screen, stats, ship, sb, aliens, bullets):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
		sb.prep_score()
	if stats.game_active == False:
		stats.score = 0
		stats.level = 1
		pygame.mixer.music.stop()
	if len(aliens) == 0:
		upgrade_level(bullets, ai_settings, stats, sb, screen, ship, aliens)		
def upgrade_level(bullets, ai_settings, stats, sb, screen, ship, aliens):
	bullets.empty()
	create_fleet(ai_settings, screen, ship, aliens)
	ai_settings.increase_speed()
	stats.level += 1
	sb.prep_level()

def get_number_aliens_x(ai_settings, alien_width):
	#the number of aliens
	avaible_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(avaible_space_x / (2 * alien_width))
	return number_aliens_x
def get_number_rows(ai_settings, ship_height, alien_height):
	avaible_space_y = (ai_settings.screen_height  -  alien_height - ship_height )
	number_rows = int(avaible_space_y / (2 * alien_height) + 1)
	return number_rows
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	#create alien accommodation in a number
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height +  alien.rect.height * row_number + 10
	aliens.add(alien)
def create_fleet(ai_settings, screen, ship, aliens):
	#create fleet
	#create alien
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)   
    for row_number in range(number_rows):
	    for alien_number in range(number_aliens_x):
	    	create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
	#react
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break
def change_fleet_direction(ai_settings, aliens):
	#drop fleet and change his position 
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
def ship_hit(ai_settings, stats, screen, ship, sb, aliens, bullets):
	if stats.ship_left > 0:
		#the number of ships
		stats.ship_left -= 1
		
		clear_and_add(aliens, bullets, ai_settings, screen, ship)
		ship_hit_addition(ai_settings, stats, screen, ship, sb, aliens, bullets)		
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)
		stats.check_game_active()
def ship_hit_addition(ai_settings, stats, screen, ship, sb, aliens, bullets):
	sb.prep_ships()
	#pause
	sleep(1.0)
	print("Ships left: " + repr(stats.ship_left) + "/3")
def clear_and_add(aliens, bullets, ai_settings, screen, ship):
	ship.center_ship()
	aliens.empty()
	bullets.empty()
	#new fleet
	create_fleet(ai_settings, screen, ship, aliens)
def check_aliens_bottom(ai_settings, stats, screen, ship, sb, aliens, bullets):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings, stats, screen, ship, sb, aliens, bullets)
			break
def check_high_score(stats, sb, save_s):
	if stats.score > save_s.high_score:
		save_s.high_score = stats.score
		sb.prep_high_score()


def update_aliens(ai_settings, stats, screen, ship, sb, aliens, bullets, play_button):
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, sb, aliens, bullets)
	check_aliens_bottom(ai_settings, stats, screen, ship, sb, aliens, bullets)
def update_screen(ai_settings, screen, ship, stats, sb, aliens, bullets, play_button, save_s):
	#reload display every cycle
	screen.fill(ai_settings.bg_color)
	#bullets under other images
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	sb.show_score()
	check_high_score(stats, sb, save_s)
	aliens.draw(screen)
	if not stats.game_active:
		#view button play if game_active = False
		play_button.draw_button()
	#view last screen
	pygame.display.flip()