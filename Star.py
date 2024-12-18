import turtle

# creating canvas 
turtle.Screen().bgcolor("orange")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

# turtle object creation

window = turtle.Turtle()
window.forward(100)
window.left(120)
window.forward(100)
window.left(120)
window.forward(100)
window.penup()
window.right(150)
window.forward(50)
window.pendown()
window.right(90)
window.forward(100)
window.right(120)
window.forward(100)
window.right(120)
window.forward(100)
turtle.mainloop()