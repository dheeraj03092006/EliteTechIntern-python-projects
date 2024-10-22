import tkinter as tk
import random

# Function to clear the dice face
def clear_dice():
    canvas.delete("all")

# Function to draw dots and square dice based on the dice number
def draw_dice(number):
    clear_dice()
    
    # Draw a square around the dice face
    canvas.create_rectangle(30, 30, 270, 270, outline="black", width=5)
    
    # Dice dot positions (center and corners)
    dot_positions = {
        1: [(150, 150)],  # Center dot
        2: [(70, 70), (230, 230)],  # Diagonal corners
        3: [(70, 70), (150, 150), (230, 230)],  # Two corners + center
        4: [(70, 70), (230, 70), (70, 230), (230, 230)],  # 4 corners
        5: [(70, 70), (230, 70), (70, 230), (230, 230), (150, 150)],  # 4 corners + center
        6: [(70, 70), (70, 150), (70, 230), (230, 70), (230, 150), (230, 230)]  # Two columns
    }

    # Draw dots at the correct positions for the given number
    for pos in dot_positions[number]:
        canvas.create_oval(pos[0] - 20, pos[1] - 20, pos[0] + 20, pos[1] + 20, fill="black")

# Function to simulate rolling the dice and show the final face
def roll_dice():
    dice_result = random.randint(1, 6)
    draw_dice(dice_result)

# Creating the main window
root = tk.Tk()
root.title("Dice Roll Simulator")
root.geometry("300x300")

# Create a canvas to draw the dice face (with square corners and dots)
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack(pady=20)

# Adding a button to roll the dice
roll_button = tk.Button(root, text="Roll the Dice", font=("Helvetica", 14), command=roll_dice)
roll_button.pack(pady=10)

# Running the main event loop
root.mainloop()
