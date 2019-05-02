import pygame
import sys
import time
import math
import webbrowser
import datetime
from database import candict  # Canteen Database
from database import food_preferences  # All food preferences

# Empty Dictionaries
distance_between_points_dict = {}
dictSort = {}
timeSort = {}

canteen_dict = candict()
all_preferences = food_preferences()


# Display NTU Campus Map (Gupta Jay)
# USER INTERFACE DESIGN - RUBRICS
def display_map():
    font_name = pygame.font.match_font('arial')  # Initialize font
    pygame.init()
    intro_screen_image = pygame.image.load("NTUMap.jpg")  # Load NTU Map
    screen = pygame.display.set_mode((875, 625))
    screen.blit(intro_screen_image, (0, 0))
    font = pygame.font.Font(font_name, 30)
    text_surface = font.render("Please select your location on the map to begin.", True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (295, 50)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    get_user_location(screen)


# Get the x,y co-ordinates of the user click (Gupta Jay)
# USE OF ABSTRACTION - RUBRICS
# USER INTERFACE DESIGN - RUBRICS
def get_user_location(screen):
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                font_name = pygame.font.match_font('arial')  # Initialize font
                pygame.init()
                pygame.display.set_caption("Location successfully captured. Please go back to the terminal!")
                font = pygame.font.Font(font_name, 35)
                text_surface = font.render(
                    "Location successfully captured. Please go back to the terminal!", True, (0, 0, 0))
                text_rect = text_surface.get_rect()
                text_rect.midtop = (430, 260)
                screen.blit(text_surface, text_rect)
                pygame.display.flip()
                time.sleep(2)
                pygame.quit()
                distance_a_b(mx, my)  # Pass parameters in function to apply distance formula

        time.sleep(0.03)
        pygame.display.update()


# Calculate the distance between the user location and all the canteens (Gupta Jay)
# USE OF PATTERN RECOGNITION - RUBRICS
def distance_a_b(x_cor, y_cor):
    no_of_canteens = len(canteen_dict)

    for i in range(1, no_of_canteens+1):
        x_coordinate = canteen_dict[i]['x-coordinate']  # Get x-coordinate from Canteen Dictionary
        y_coordinate = canteen_dict[i]['y-coordinate']  # Get y-coordinate from Canteen Dictionary
        distance_between_points = math.sqrt((x_cor - x_coordinate)**2 + (y_cor - y_coordinate)**2)  # Distance Formula
        canteen_dict[i]['Distance from user'] = distance_between_points

    search_food()  # Call function to filter out the results


# Prompts the user to enter a valid input
def valid_input():
    print("Please enter a valid input.")
    print()  # Line Break


# Filter the canteen results (Gupta Jay & Xavier Ho)
# USE OF ABSTRACTION - RUBRICS
# USE OF DECOMPOSITION - RUBRICS
# USER INTERFACE DESIGN - RUBRICS
def search_food():
    print("Location successfully captured.")
    print()  # Line Break

    while True:
        try:
            i = 1
            print("How would you like to refine your search? (Enter the INDEX NO. of the option)")
            for key, value in all_preferences.items():
                print("[", i, "]", key)
                i += 1
            print("[", len(all_preferences) + 1, "]", "Multiple")
            filter_choice = int(input())
        except ValueError:
            valid_input()
            continue
        else:
            if filter_choice not in range(1, len(all_preferences) + 2):
                valid_input()
                continue
            else:
                break

    if filter_choice == 1:
        sort_by_veghalal(search_by_veghalal())  # Pass "Dietary Preference" parameter
    elif filter_choice == 2:
        sort_by_cuisine(search_by_cuisine())  # Pass "Cuisine" parameter
    elif filter_choice == 3:
        sort_by_price_range(search_by_price_range())  # Pass "Price Range" parameter
    else:
        filter_by_multiple(multiple_choices())

    sort_distance()
    
# Return multiple choices based on user input (Iyer Rajagopal Mahadevan)
# USE OF ABSTRACTION - RUBRICS
def multiple_choices():
    while True:
        try:
            flag = 0
            multiple = input(
                "Enter the INDEX NO. of the choices you want your food to be filtered. (e.g. for filtering based on "
                "Cuisine and Price Range, INPUT: 1 3 \n")
            filter_choices = [int(choices) for choices in multiple.split()]  # Returns a list
        except ValueError:
            valid_input()
            continue
        for i in filter_choices:
            if i not in range(1, len(all_preferences) + 1):
                flag = 1
                break
        if flag == 1:
            valid_input()
            continue
        break
    return filter_choices


# Return Dietary Preferences (Gupta Jay & Xavier Ho)
# USE OF ABSTRACTION - RUBRICS
def search_by_veghalal():
    while True:
        try:
            print("Enter your dietary preferences: (Enter the INDEX NO. of the option)")
            # USE OF PATTERN RECOGNITION - RUBRICS
            for i in range(1, len(all_preferences['Dietary Preference'])+1):
                print("[", i, "]", all_preferences['Dietary Preference'][i-1])
            veg_halal = int(input())
        except ValueError:
            valid_input()
            continue
        else:
            if veg_halal not in range(1, len(all_preferences['Dietary Preference']) + 1):
                valid_input()
                continue
            else:
                break

    # USE OF PATTERN RECOGNITION - RUBRICS
    veg_halal = all_preferences['Dietary Preference'][veg_halal-1]

    return veg_halal


# Return cuisine preference (Gupta Jay & Xavier Ho)
# USE OF ABSTRACTION - RUBRICS
def search_by_cuisine():

    while True:
        try:
            print("What type of cuisine do prefer? (Enter the INDEX NO. of the option)")
            # USE OF PATTERN RECOGNITION - RUBRICS
            for i in range(1, len(all_preferences['Cuisine'])+1):
                print("[", i, "]", all_preferences['Cuisine'][i-1])
            cuisine = int(input())
        except ValueError:
            valid_input()
            continue
        else:
            if cuisine not in range(1, len(all_preferences['Cuisine']) + 1):
                valid_input()
                continue
            else:
                break

    # USE OF PATTERN RECOGNITION - RUBRICS
    cuisine = all_preferences['Cuisine'][cuisine-1]

    return cuisine


# Return price range (Gupta Jay & Xavier Ho)
# USE OF ABSTRACTION - RUBRICS
def search_by_price_range():
    while True:
        try:
            print("Enter your price range: (Enter the INDEX NO. of the option)")
            # USE OF PATTERN RECOGNITION - RUBRICS
            for i in range(1, len(all_preferences['Price'])+1):
                print("[", i, "]", all_preferences['Price'][i-1])
            price_range = int(input())
        except ValueError:
            valid_input()
            continue
        else:
            if price_range not in range(1, len(all_preferences['Price']) + 1):
                valid_input()
                continue
            else:
                break

    # USE OF PATTERN RECOGNITION - RUBRICS
    price_range = all_preferences['Price'][price_range-1]

    return price_range


# Filter by all preferences (Gupta Jay & Xavier Ho)
# ALGORITHM DESIGN - RUBRICS
def filter_by_all():
    veg_halal = search_by_veghalal()
    cuisine = search_by_cuisine()
    price_range = search_by_price_range()

    for foodpref, value in canteen_dict.items():
        if veg_halal in canteen_dict[foodpref]['Dietary Preference'] and cuisine in canteen_dict[foodpref]['Cuisine'] \
           and price_range in canteen_dict[foodpref]['Price']:
            dictSort[foodpref] = value


# Filter by dietary preferences (Gupta Jay & Xavier Ho)
# ALGORITHM DESIGN - RUBRICS
def sort_by_veghalal(veg_halal):
    for foodpref, value in canteen_dict.items():
        if veg_halal in canteen_dict[foodpref]['Dietary Preference']:
            dictSort[foodpref] = value


# Filter by cuisine (Gupta Jay & Xavier Ho)
# ALGORITHM DESIGN - RUBRICS
def sort_by_cuisine(cuisine):
    for foodpref, value in canteen_dict.items():
        if cuisine in canteen_dict[foodpref]['Cuisine']:
            dictSort[foodpref] = value


# Filter by price range (Gupta Jay & Xavier Ho)
# ALGORITHM DESIGN - RUBRICS
def sort_by_price_range(price_range):
    for foodpref, value in canteen_dict.items():
        if price_range in canteen_dict[foodpref]['Price']:
            dictSort[foodpref] = value


# Filter by multiple choices (Iyer Rajagopal Mahadevan)
# USE OF ABSTRACTION - RUBRICS
def filter_by_multiple(filter_choices):
    if 1 in filter_choices and 2 in filter_choices and 3 in filter_choices:
        filter_by_all()
    elif 1 in filter_choices and 2 in filter_choices:
        filter_by_diet_and_cuisine()
    elif 1 in filter_choices and 3 in filter_choices:
        filter_by_diet_and_price()
    elif 2 in filter_choices and 3 in filter_choices:
        filter_by_cuisine_and_price()


