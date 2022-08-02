from turtle import back
import pygame
from pygame.locals import *
import sys
import pygwidgets

# CONSTANTS
BLACK = (40, 40, 40)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
FRAMES_PS = 30

# INITIALISATIONS
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pregnancy Calculator")
clock = pygame.time.Clock()

# ASSETS

# VARIABLES
text = """Welcome to the Pregnancy App"""
text2 = """This App that gives you all the details 
on how to have a successful pregnancy 
in Zimbabwe"""

intro_screen = pygwidgets.DisplayText(window, (50, 100), text, fontSize = 25, width = 300, textColor=WHITE)
intro_screen2 = pygwidgets.DisplayText(window, (75, 300), text2, textColor=WHITE, justified='center')

page_two_button = pygwidgets.TextButton(window, (150, 500), "Enter App")
page_two = False
label = "What Is Your Name: "
label_screen = pygwidgets.DisplayText(window, (0, 100), label, textColor=WHITE, fontSize=30)
input_box = pygwidgets.InputText(window, (200, 100), fontSize=30, width=150)


page_three = False
page_three_button = pygwidgets.TextButton(window, (150, 300), "Next")
back_button = pygwidgets.TextButton(window, (150, 400), "Back" )


routine = pygwidgets.TextButton(window, (50, 500), "Routine Care")
chart = pygwidgets.TextButton(window, (200, 500), "Kick Chart")

# LOOPS
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if page_two_button.handleEvent(event):
            page_two = True
        if input_box.handleEvent(event):
            input_text = input_box.getValue()
            congrats_msg = f'''Congratulations {input_text}. Your journey 
            to a successful pregnancy begins here'''
            name_text = pygwidgets.DisplayText(window, (0, 100), congrats_msg, textColor=WHITE, fontSize=25)
        if page_three_button.handleEvent(event):
            page_two = False
            page_three = True
        if back_button.handleEvent(event):
            page_two = False
            page_three = False
        if routine.handleEvent(event):
            pass
        if chart.handleEvent(event):
            pass
        
    if page_two:
        window.fill(BLACK)
        label_screen.draw()
        input_box.draw()
        page_three_button.draw()
        back_button.draw()
        pygame.display.update()
        clock.tick(FRAMES_PS)

    elif page_three:
        window.fill(BLACK)        
        name_text.draw()
        pygwidgets.DisplayText(window, (0, 300), "What would you like to do?", textColor=WHITE, fontSize=25).draw()
        routine.draw()
        chart.draw()
        pygame.display.update()
        clock.tick(FRAMES_PS)
    else:

        window.fill(BLACK)
        intro_screen.draw()
        intro_screen2.draw()
        page_two_button.draw()
        pygame.display.update()
        clock.tick(FRAMES_PS)


