def food_preferences():
    all_preferences = {'Dietary Preference': ['Vegetarian', 'Halal', 'Non-Halal'],
                       'Cuisine': ['Malay', 'Vegetarian', 'Indian', 'Chinese', 'Western', 'Italian', 'Korean',
                                   'Japanese', 'Vietnamese', 'Fast Food'],
                       'Price': ['$2-$5', '$5-$8', '$8-$12']
                    }
    return all_preferences


# MASTER CANTEEN DATABASE (Gupta Jay, Xavier Ho & Iyer Rajagopal Mahadevan)
def candict():
    canteen_dict = {1: {'Name': 'Canteen 1',
                        'x-coordinate': 429,
                        'y-coordinate': 428,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Halal', 'Vegetarian', 'Non-Halal'],
                        'Cuisine': ['Vegetarian', 'Indian', 'Chinese', 'Western', 'Fast Food'],
                        'Price': ['$2-$5', '$5-$8'],
                        'Timing': ['7', '24']},

                    2: {'Name': 'Canteen 2',
                        'x-coordinate': 463,
                        'y-coordinate': 370,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Halal', 'Non-Halal'],
                        'Cuisine': ['Malay', 'Chinese', 'Western', 'Japanese', 'Korean'],
                        'Price': ['$2-$5', '$5-$8', '$8-$12'],
                        'Timing': ['7', '24']},

                    3: {'Name': 'Canteen 9',
                        'x-coordinate': 574,
                        'y-coordinate': 260,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Vegetarian', 'Halal', 'Non-Halal'],
                        'Cuisine': ['Malay', 'Chinese', 'Western', 'Fast Food'],
                        'Price': ['$2-$5'],
                        'Timing': ['7', '24']},

                    4: {'Name': 'Canteen 11',
                        'x-coordinate': 669,
                        'y-coordinate': 220,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Vegetarian', 'Non-Halal'],
                        'Cuisine': ['Malay', 'Chinese', 'Western', 'Indian'],
                        'Price': ['$5-$8'],
                        'Timing': ['7', '21']},

                    5: {'Name': 'Canteen 13',
                        'x-coordinate': 431,
                        'y-coordinate': 160,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Vegetarian', 'Halal', 'Non-Halal'],
                        'Cuisine': ['Malay', 'Chinese', 'Western'],
                        'Price': ['$2-$5', '$5-$8'],
                        'Timing': ['7', '21']},

                    6: {'Name': 'Canteen 14',
                        'x-coordinate': 497,
                        'y-coordinate': 162,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Vegetarian', 'Non-Halal'],
                        'Cuisine': ['Malay', 'Chinese', 'Western', 'Fast Food', 'Korean'],
                        'Price': ['$5-$8'],
                        'Timing': ['7', '21']},

                    7: {'Name': 'Canteen 16',
                        'x-coordinate': 393,
                        'y-coordinate': 200,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Vegetarian', 'Halal', 'Non-Halal'],
                        'Cuisine': ['Malay', 'Chinese', 'Western', 'Indian'],
                        'Price': ['$5-$8'],
                        'Timing': ['7', '21']},

                    8: {'Name': 'Ananda Kitchen',
                        'x-coordinate': 682,
                        'y-coordinate': 277,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Non-Halal'],
                        'Cuisine': ['Indian'],
                        'Price': ['$5-$8', '$8-$12'],
                        'Timing': ['12', '22']},

                    
