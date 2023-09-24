import tkinter as tk
import random

def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

def roll_button_clicked():
    try:
        num_dice = int(dice_entry.get())
        if num_dice <= 0:
            result_label.config(text="Please enter a positive number of dice.")
        else:
            dice_results = roll_dice(num_dice)
            result_label.config(text=f"Result(s) of rolling {num_dice} dice:\n{', '.join(map(str, dice_results))}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

def quit_button_clicked():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Dice Rolling App")

# Create and configure widgets
dice_label = tk.Label(root, text="Enter the number of dice to roll:")
dice_entry = tk.Entry(root)
roll_button = tk.Button(root, text="Roll Dice", command=roll_button_clicked)
quit_button = tk.Button(root, text="Quit", command=quit_button_clicked)
result_label = tk.Label(root, text="")

# Place widgets in the window
dice_label.pack()
dice_entry.pack()
roll_button.pack()
quit_button.pack()
result_label.pack()

# Start the main event loop
root.mainloop()
