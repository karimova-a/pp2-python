
import pygame
import os

pygame.mixer.init()

pygame.init()


class MusicPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        self.current_song_index = 0
        self.is_playing = False
        self.is_paused = False
        self.load_song()

    def load_song(self):

        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_song_index])

    def play(self):
        
        if not self.is_playing:
            pygame.mixer.music.play()
            self.is_playing = True
            print(f"Playing: {self.playlist[self.current_song_index]}")
        elif self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            print(f"Resuming: {self.playlist[self.current_song_index]}")

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False
        print("Stopped")

    def pause(self):
        pygame.mixer.music.pause()
        self.is_paused = True
        print(f"Paused: {self.playlist[self.current_song_index]}")

    def next_song(self):
        self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
        self.load_song()
        self.play()

    def previous_song(self):
        self.current_song_index = (self.current_song_index - 1) % len(self.playlist)
        self.load_song()
        self.play()

    def handle_events(self, screen, buttons):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Play or Resume
                    self.play()
                elif event.key == pygame.K_s:  # Stop
                    self.stop()
                elif event.key == pygame.K_n:  # Next song
                    self.next_song()
                elif event.key == pygame.K_b:  # Previous song
                    self.previous_song()
                elif event.key == pygame.K_q:  # Quit
                    self.stop()
                    pygame.quit()
                    exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for button_action, button_rect in buttons.items():
                    if button_rect.collidepoint(mouse_x, mouse_y): 
                        if button_action == 'play':
                            self.play()
                        elif button_action == 'stop':
                            self.stop()
                        elif button_action == 'next':
                            self.next_song()
                        elif button_action == 'prev':
                            self.previous_song()

    def draw_buttons(self, screen, font):

    
        button_width = 150
        button_height = 50
        margin = 20
        
    
        play_button = pygame.Rect(50, 350, button_width, button_height)
        stop_button = pygame.Rect(250, 350, button_width, button_height)
        next_button = pygame.Rect(450, 350, button_width, button_height)
        prev_button = pygame.Rect(650, 350, button_width, button_height)

        
        pygame.draw.rect(screen, (255, 255, 255), play_button)
        pygame.draw.rect(screen, (255, 255, 255), stop_button)
        pygame.draw.rect(screen, (255, 255, 255), next_button)
        pygame.draw.rect(screen, (255, 255, 255), prev_button)

       
        play_text = font.render('Play', True, (0, 0, 0))
        stop_text = font.render('Stop', True, (0, 0, 0))
        next_text = font.render('Next', True, (0, 0, 0))
        prev_text = font.render('Prev', True, (0, 0, 0))

        screen.blit(play_text, (play_button.centerx - play_text.get_width() / 2, play_button.centery - play_text.get_height() / 2))
        screen.blit(stop_text, (stop_button.centerx - stop_text.get_width() / 2, stop_button.centery - stop_text.get_height() / 2))
        screen.blit(next_text, (next_button.centerx - next_text.get_width() / 2, next_button.centery - next_text.get_height() / 2))
        screen.blit(prev_text, (prev_button.centerx - prev_text.get_width() / 2, prev_button.centery - prev_text.get_height() / 2))

        
        return {
            'play': play_button, 
            'stop': stop_button, 
            'next': next_button, 
            'prev': prev_button
        }


playlist = [
    "song1.mp3",
    "song2.mp3",
    "song3.mp3"
]


player = MusicPlayer(playlist)


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Music Player")


background_image = pygame.image.load("background1.png.webp")  
background_image = pygame.transform.scale(background_image, (800, 600))  


font = pygame.font.Font(None, 36)


while True:
    screen.blit(background_image, (0, 0))
    
    
    buttons = player.draw_buttons(screen, font)
    
    
    player.handle_events(screen, buttons)
    
  
    pygame.display.update()
    
    
    pygame.time.Clock().tick(30)
