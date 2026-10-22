import turtle


# Čtverec: čtyřikrát „popojeď dopředu a otoč se o 90 stupňů".
for strana in range(50):
    turtle.forward(100)     # popojeď o 100 kroků
    turtle.left(90)  