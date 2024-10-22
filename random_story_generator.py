import random

# Lists of different elements for the story
characters = ["a wizard", "an astronaut", "a pirate", "a knight", "a detective", "a superhero", "a scientist", "an adventurer"]
secondary_characters = ["a talking dog", "a wise old man", "an alien", "a ghost", "a dragon", "a robot", "a witch", "a princess"]
places = ["in a magical forest", "on a distant planet", "in a haunted mansion", "in an ancient castle", "in a futuristic city", "in a mysterious cave", "on a pirate ship", "at the bottom of the ocean"]
time_of_day = ["during the night", "at sunrise", "in the middle of the day", "at dusk", "at midnight", "in the afternoon"]
weather = ["on a stormy night", "on a rainy day", "under a bright sun", "with strong winds", "during a heavy snowfall", "in the fog"]
actions = ["found a mysterious map", "discovered a hidden portal", "fought with a dragon", "solved a great mystery", "rescued a lost child", "broke a magical curse", "stumbled upon a time machine", "uncovered a dark secret"]
objects = ["a magical sword", "a talking cat", "an ancient book", "a cursed treasure", "a glowing crystal", "a mystical amulet", "an enchanted mirror", "a strange artifact"]
plot_twists = ["but then everything changed", "only to discover it was all a dream", "and uncovered a hidden truth", "but realized they were not alone", "but suddenly vanished", "and found themselves in a different time", "but the object was cursed", "but they were betrayed by a friend"]
outcomes = ["and saved the day", "but lost everything", "and became a hero", "but vanished mysteriously", "and made a new friend", "and was never seen again", "but had to make a difficult choice", "and found happiness in the end"]

# Function to generate a random story
def generate_story():
    character = random.choice(characters)
    secondary_character = random.choice(secondary_characters)
    place = random.choice(places)
    time = random.choice(time_of_day)
    weather_condition = random.choice(weather)
    action = random.choice(actions)
    obj = random.choice(objects)
    plot_twist = random.choice(plot_twists)
    outcome = random.choice(outcomes)

    # Create the random story
    story = (f"One day, {character} and {secondary_character} were {place} {time} {weather_condition}. "
             f"There, they {action} with {obj} {plot_twist}, {outcome}.")
    
    return story

# Generate and print a random story
print("Welcome to the Random Story Generator!")
print(generate_story())
