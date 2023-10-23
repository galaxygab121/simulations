import tkinter as tk
import random
import time

# Constants
POPULATION = 200
INITIAL_INFECTED = 5
INFECTION_PROBABILITY = 0.3
RECOVERY_TIME = 14
MORTALITY_RATE = 0.02  # 2% mortality rate

# Create a tkinter window
root = tk.Tk()
root.title("COVID-19 Simulation")

# Create canvas for visualization
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Create a class to represent people
class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.infected = False
        self.days_infected = 0
        self.alive = True
        self.shape = canvas.create_oval(x-5, y-5, x+5, y+5, fill="green")

    def move(self):
        if self.alive:
            new_x = self.x + random.randint(-1, 1)
            new_y = self.y + random.randint(-1, 1)
            canvas.move(self.shape, new_x - self.x, new_y - self.y)
            self.x, self.y = new_x, new_y

    def infect(self):
        if self.alive and not self.infected and random.random() < INFECTION_PROBABILITY:
            self.infected = True
            canvas.itemconfig(self.shape, fill="red")

    def update(self):
        if self.infected:
            self.days_infected += 1
            if self.days_infected == RECOVERY_TIME:
                if random.random() < MORTALITY_RATE:
                    self.alive = False
                    canvas.itemconfig(self.shape, fill="black")
                else:
                    canvas.itemconfig(self.shape, fill="blue")
                self.infected = False

# Create a list of people
people = [Person(random.randint(0, 800), random.randint(0, 600)) for _ in range(POPULATION)]

# Infect some people initially
for i in range(INITIAL_INFECTED):
    people[i].infect()

# Create a function to update the simulation
def update_simulation():
    for person in people:
        person.move()
        person.infect()
        person.update()
    root.after(100, update_simulation)

# Create buttons and labels
start_button = tk.Button(root, text="Start Simulation", command=update_simulation)
start_button.pack()

# Start the tkinter main loop
root.mainloop()
