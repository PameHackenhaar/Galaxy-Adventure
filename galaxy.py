
import os
import pygame
import random
import sys
from faces import Face
from pygame.locals import *
from pygame.color import THECOLORS
from word import Word

EXEC_DIR = os.path.dirname(__file__)  

if sys.platform == "darwin":
    image_dir = os.walk("assets_words")
else:
    image_dir = os.walk(os.path.join(EXEC_DIR, "assets_words"))

pygame.init()
pygame.display.set_caption("GALAXY ADVENTURE")

screen = pygame.display.set_mode((700, 600))
font = pygame.font.SysFont("Monteserrat", 60)
clock = pygame.time.Clock()
image_list = []
right = False
wrong = False
entered_text = []
screen_x, screen_y = screen.get_size()
backgound = pygame.image.load("assets_back/BACK_GAME.png")

for root, dir, files in image_dir:
    for file in files:
        if ".DS_Store" not in file:
            image_list.append(file)

the_word = Word(random.choice(image_list))

ignored_keys = ('escape', 'return', 'backspace', 'enter', 'space', 'right shift'\
                ,'left shift', 'left meta', 'right meta', 'f1', 'f2', 'f3', 'f4', 'f5'\
                ,'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'caps lock')

happy = Face("happy")

sad = Face("sad")

happy_group = pygame.sprite.GroupSingle()

sad_group = pygame.sprite.GroupSingle()

rightsound = pygame.mixer.Sound("assets_sounds/RIGHT.wav")

wrongsound = pygame.mixer.Sound("assets_sounds/WRONG.wav")

def main():
   
    global the_word
    global entered_text
    global ignored_keys
    global wrong
    global right
    global hyphen

    running = True
    pygame.key.set_repeat(0,0)
    pygame.mixer.music.load("assets_sounds/BACKMUSIC.mp3")
    pygame.mixer.music.play(-1)

    while running:
        screen.blit(backgound, (0, 0))
        cursor = 0
        letter_position = dict()
        key = pygame.key.get_pressed()
        mods = pygame.key.get_mods()
        screen.fill(THECOLORS["white"])
        screen.blit(backgound, (0, 0))
        the_word.draw(screen, (screen_x/2 - the_word.width/2), 50)

        num_lines = len(the_word.letters)  
        underline_width = 40                     
        text_total_width = (num_lines * underline_width) + ((num_lines - 1) * 20) 
        line_x1 = screen_x/2 - text_total_width/2
        
        letter_beginning_list = []

        letter_beginning = screen_x/2 - text_total_width/2

        black = (0, 0, 0)
        white = (255, 255, 255)
        
        letter_keys = range(0, the_word.length)

        for letter in the_word.letters:
            letter_size = font.size(letter)
            letter_beginning_list.append([letter_beginning + (underline_width/2 - letter_size[0]/2), letter])
            correct_letter = font.render(letter, 1, (0, 0, 0))
            letter_size = font.size(letter)                       
            if letter == "-":
                screen.blit(correct_letter, [letter_beginning + (underline_width/2 - letter_size[0]/2), 400])             
            letter_beginning += underline_width + 20 
            
            line_x2 = line_x1 + underline_width 
            pygame.draw.line(screen, THECOLORS["black"], (line_x1, 460), (line_x2, 460), 2)
            line_x1 += underline_width + 20 
            line_x2 += underline_width + 20 

        letter_dict = dict(zip(letter_keys, letter_beginning_list))

        if sad.lifespan == 0:
            sad_group.empty()
            wrong = False
        sad_group.update()
        
        if happy.lifespan == 0:
            happy_group.empty()
            right = False
            the_word = Word(random.choice(image_list))
            happy.reset()
        happy_group.update()

        if right:
            clock.tick(10)
            happy_group.draw(screen)
            entered_text = []
        if wrong:
            clock.tick(10)
            sad_group.draw(screen)
            entered_text = []

        if key[pygame.K_ESCAPE]:
            sys.exit()
        elif (mods & KMOD_META):
            if key[pygame.K_q]:
                sys.exit()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                key_value = pygame.key.name(event.key)
                if key_value == "backspace":
                    if entered_text:
                        entered_text.pop()

                if key_value not in ignored_keys:
                    entered_text.append(key_value)
                    print(entered_text)
                
                if key_value == "return":
                    hyphen_pos = [i for i,x in enumerate(the_word.letters) if x == "-"]
                    print(hyphen_pos)
                    if hyphen_pos:
                        del(the_word.letters[int(hyphen_pos[0])])

                    if entered_text == the_word.letters:
                        pygame.mixer.Sound.play(rightsound)
                        happy_group.add(happy)
                        right = True
                        
                    else:
                        sad.reset()
                        pygame.mixer.Sound.play(wrongsound)
                        sad_group.add(sad)
                        wrong = True

        for letter in entered_text:                                          
            if not letter == "backspace":
                if letter_dict.get(cursor)[1] == "-":
                    cursor += 1

                correct_letter = font.render(letter, 1, (0, 0, 0))
                letter_size = font.size(letter)                        
                screen.blit(correct_letter, [letter_dict.get(cursor)[0], 400])             
                cursor += 1
        
        pygame.display.update()                                              
        clock.tick(15)
        
if __name__ == "__main__":
    main()

