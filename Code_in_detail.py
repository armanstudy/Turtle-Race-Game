"""
*******************************************************
*                                                     *
*               🐢 Turtle Race Game 🐢               *
*                                                     *
*  Welcome to the Turtle Race Game!                  *
*  This is a fun and interactive Python project       *
*  where you can bet on your favorite turtle and      *
*  watch them race to the finish line.                *
*                                                     *
*  🏁 A perfect project for beginners to learn Python!*
*  Learn about loops, functions, and libraries        *
*  while having fun with colorful graphics.           *
*                                                     *
*  Enjoy the race and may the best turtle win! 🏆     *
*******************************************************
"""

# Importing necessary libraries
from turtle import Turtle, Screen  # Turtle for graphics, Screen for the game window
import random  # Random for generating random movements for turtles

# Constants for turtle colors and their starting positions
COLORS = ["red", "blue", "green", "yellow", "pink", "purple"]
STARTING_Y_POSITIONS = [-70, -40, -10, 20, 50, 80]

def setup_screen():
    """
    Initializes the game screen.
    - Sets the title of the window.
    - Configures the screen size.
    """
    screen = Screen()
    screen.title("Turtle Race Game")  # Title of the game window
    screen.setup(width=500, height=400)  # Set the width and height of the window
    return screen

def create_turtles():
    """
    Creates turtle players and positions them at the starting line.
    - Each turtle is assigned a unique color from the COLORS list.
    - Turtles are positioned vertically based on STARTING_Y_POSITIONS.
    """
    turtles = []
    for i in range(len(COLORS)):
        turtle = Turtle()  # Create a new turtle object
        turtle.color(COLORS[i])  # Assign a color to the turtle
        turtle.shape("turtle")  # Set the shape of the turtle to "turtle"
        turtle.penup()  # Lift the pen to avoid drawing lines while moving
        turtle.goto(-230, STARTING_Y_POSITIONS[i])  # Position the turtle at the starting line
        turtles.append(turtle)  # Add the turtle to the list of turtles
    return turtles

def get_user_bet(screen):
    """
    Prompts the user to place a bet on which turtle will win the race.
    - Displays the available colors on the screen for reference.
    - Uses a text input dialog to get the user's bet.
    - Clears the screen after the user enters their bet.
    """
    # Clear the screen and set up the title for the betting phase
    screen.clear()
    screen.title("Turtle Race Game - Choose Your Bet")
    screen.setup(width=500, height=400)
    
    # Create a Turtle object to display the available colors
    display_turtle = Turtle()
    display_turtle.hideturtle()  # Hide the turtle cursor
    display_turtle.penup()  # Lift the pen to avoid drawing lines
    display_turtle.goto(-200, 150)  # Position the text at the top of the screen
    display_turtle.write("Available Colors:", align="left", font=("Arial", 16, "bold"))
    
    # Display each color below the "Available Colors" heading
    y_position = 120
    for color in COLORS:
        display_turtle.goto(-200, y_position)
        display_turtle.write(color, align="left", font=("Arial", 14, "normal"))
        y_position -= 30

    # Prompt the user to enter their bet
    user_bet = screen.textinput("YOUR BET", "Color of the turtle you think will win:")
    
    # Clear the screen after the user enters their bet
    screen.clear()
    return user_bet

def race(turtles, user_bet):
    """
    Runs the turtle race and determines the winner.
    - Moves each turtle forward by a random distance in each iteration.
    - Checks if any turtle has crossed the finish line.
    - Displays the result of the race (win/lose) based on the user's bet.
    """
    race_on = True  # Flag to keep the race running
    while race_on:
        for turtle in turtles:
            # Check if the turtle has crossed the finish line
            if turtle.xcor() >= 230:  # Finish line is at x = 230
                race_on = False  # Stop the race
                winning_color = turtle.pencolor()  # Get the color of the winning turtle
                
                # Create a Turtle object to display the result
                result_turtle = Turtle()
                result_turtle.hideturtle()
                result_turtle.penup()
                result_turtle.goto(0, 0)  # Position the result text at the center
                
                # Display the result based on the user's bet
                if winning_color == user_bet:
                    result_turtle.write(f"🎉 YOU WON! {winning_color} is the winner! 🎉", align="center", font=("Arial", 16, "bold"))
                else:
                    result_turtle.write(f"😢 YOU LOST! {winning_color} is the winner! 😢", align="center", font=("Arial", 16, "bold"))
                break
            # Move the turtle forward by a random distance
            turtle.forward(random.randint(0, 10))

def main():
    """
    Main function to run the Turtle Race Game.
    - Sets up the screen.
    - Prompts the user to place a bet.
    - Creates the turtles and starts the race.
    - Waits for the user to close the game window.
    """
    screen = setup_screen()  # Initialize the game screen
    user_bet = get_user_bet(screen)  # Get the user's bet
    
    if user_bet:  # Proceed only if the user enters a valid bet
        turtles = create_turtles()  # Create and position the turtles
        race(turtles, user_bet)  # Start the race
    
    screen.exitonclick()  # Wait for the user to click on the screen to close the game

# Entry point of the program
if __name__ == "__main__":
    main()