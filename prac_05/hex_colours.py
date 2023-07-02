CODE_TO_COLOUR = {"red": "#ff0000", "green": "#00ff00", "blue": "#0000ff", "orange": "#ffa500",
                  "yellow": "#ffff00", "white": "#ffffff", "pink": "#ffb5c5", "purple": "#9b30ff",
                  "black": "#000000", "aqua": "#00ffff"}

colour = input("Enter a colour: ").lower()
while colour != "":
    try:
        print(colour, "is", CODE_TO_COLOUR[colour])
    except KeyError:
        print("Invalid colour name")
    colour = input("Enter a colour: ").lower()
