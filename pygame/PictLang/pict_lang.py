import pygame, sys

pygame.init()

# --- DEFINITIONS ---
''' Foseme = unit used to create words in pictlang (corresponds to phonemes in spoken language)
    Message = The message which the user wishes to send to the reader
    Signal = the list of fosemes which is read by the picter in order to send the message'''
# Code written by Tashi Visschedijk

# set display
pygame.display.set_caption('Picter')
screen = pygame.display.set_mode((300,300))

# picting surface
pict_rect = pygame.Rect(0, 0, 300, 300)
pict_surf = pygame.Surface((300,300))

# input text
text = 'RGB'
font = pygame.font.SysFont(None, 40)
text_img = font.render(text, True, (255,255,255))
text_rect = text_img.get_rect()
text_rect.topleft = (20, 20)
cursor = pygame.Rect(text_rect.topright, (3, text_rect.height))


# FOSEMES
#prime
R = (255,0,0)
G = (0,255,0) 
B = (0,0,255)
#secondary
M = (255,0,255)
Y = (255,255,0)
C = (0,255,255) 
#break letters
w = (255,255,255)
b = (0,0,0)

# PRESET MESSAGES
all_fosemes = [R, G, B, M, Y, C, w, b]
message1 = [R, Y, G, B]
message2 = [B, b, R, G, w, b]
message3 = [Y, Y, G, b]

# FUNCTIONS
#converts the inputted string into a signal the pict function can read
def convert_input(input):
    letters_list = list(input) #defines a list comprised of each letter from the input
    #print(letters_list) #DEBUG prints the list of letters gathered
    signal = [] #create an empty list to hold the signal sequence
    for letter in letters_list: #run through for each letter individually
        if letter == 'R': #check if letter is R
            signal.append(R) #if so, add R to the signal
        if letter == 'G':
            signal.append(G)
        if letter == 'B':
            signal.append(B)
        if letter == 'M':
            signal.append(M)
        if letter == 'Y':
            signal.append(Y)
        if letter == 'C':
            signal.append(C)
        if letter == 'w' or letter == '.':
            signal.append(w)
        if letter == 'b' or letter == ';' or letter == ' ':
            signal.append(b)
    #print(signal) #DEBUG print the converted signal sequence
    return signal

#gets direct input from the user through the terminal (not preferred)
def get_input():
    message = input("Input message: ")
    #print(message) #DEBUG
    signal = convert_input(message) #convert the inputted string into a signal readable by the pict function
    return signal

#draw the signal sequence onto the screen to be read as a message by the user
def pict(pict_list):
    for colour in pict_list:
        pict_surf.fill(colour)
        screen.blit(pict_surf, (0,0))
        pygame.display.update()
        pygame.time.delay(200)

SEND_MESSAGE = False   
while True:
    for event in pygame.event.get(): # Check for user input
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RETURN:
                SEND_MESSAGE = True
            elif event.key == pygame.K_BACKSPACE:
                if len(text) > 0:
                    text = text[:-1]
            else:
                text += event.unicode
    
    text_img = font.render(text, True, (255,255,255))
    text_rect.size=text_img.get_size()
    cursor.topleft = text_rect.topright

    if SEND_MESSAGE == True:
        #message = get_input()
        message = convert_input(text)
        pict(message)
        SEND_MESSAGE = False

    #draw to the screen
    screen.fill('BLACK')
    screen.blit(text_img, (10, 10))
    pygame.display.update()