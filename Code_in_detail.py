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

from turtle import Turtle, Screen
import random

# Constants for turtle colors and starting positions
COLORS = ["red", "blue", "green", "yellow", "pink", "purple"]
STARTING_Y_POSITIONS = [-70, -40, -10, 20, 50, 80]

def setup_screen():
    """Initializes the game screen."""
    screen = Screen()
    screen.title("Turtle Race Game")
    screen.setup(width=500, height=400)
    return screen

def create_turtles():
    """Creates turtle players and positions them on the screen."""
    turtles = []
    for i in range(len(COLORS)):
        turtle = Turtle()
        turtle.color(COLORS[i])
        turtle.shape("turtle")
        turtle.penup()
        turtle.goto(-230, STARTING_Y_POSITIONS[i])
        turtles.append(turtle)
    return turtles

def get_user_bet(screen):
    """Prompts the user for their bet on the turtle color."""
    # Display the available colors on the screen
    screen.clear()
    screen.title("Turtle Race Game - Choose Your Bet")
    screen.setup(width=500, height=400)
    
    # Create a Turtle object to display the colors
    display_turtle = Turtle()
    display_turtle.hideturtle()
    display_turtle.penup()
    display_turtle.goto(-200, 150)
    display_turtle.write("Available Colors:", align="left", font=("Arial", 16, "bold"))
    
    y_position = 120
    for color in COLORS:
        display_turtle.goto(-200, y_position)
        display_turtle.write(color, align="left", font=("Arial", 14, "normal"))
        y_position -= 30

    # Prompt the user for their bet
    user_bet = screen.textinput("YOUR BET", "Color of the turtle you think will win:")
    
    # Clear the screen after user input
    screen.clear()
    return user_bet

def race(turtles, user_bet):
    """Runs the turtle race and determines the winner."""
    race_on = True
    while race_on:
        for turtle in turtles:
            if turtle.xcor() >= 230:
                race_on = False
                winning_color = turtle.pencolor()
                
                # Create a Turtle object to display the result
                result_turtle = Turtle()
                result_turtle.hideturtle()
                result_turtle.penup()
                result_turtle.goto(0, 0)
                
                if winning_color == user_bet:
                    result_turtle.write(f"🎉 YOU WON! {winning_color} is the winner! 🎉", align="center", font=("Arial", 16, "bold"))
                else:
                    result_turtle.write(f"😢 YOU LOST! {winning_color} is the winner! 😢", align="center", font=("Arial", 16, "bold"))
                break
            turtle.forward(random.randint(0, 10))

def main():
    """Main function to run the turtle race game."""
    screen = setup_screen()
    user_bet = get_user_bet(screen)
    
    if user_bet:
        turtles = create_turtles()
        race(turtles, user_bet)
    
    screen.exitonclick()

if __name__ == "__main__":
    main()