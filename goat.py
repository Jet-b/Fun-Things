import PIL
import PIL.Image



pic = PIL.Image.open("goat.png")

try:
    with open("goat.txt", "w") as f:


        for x in range(pic.width):
            for y in range(pic.height):
                z, r, g, b = pic.getpixel((x, y))
                f.write(f"({x}, {y}) : ({r} {g} {b})\n")
            print(x)
except FileNotFoundError:
    try:
        with open("goat.txt", "w") as f:


            for x in range(pic.width):
                for y in range(pic.height):
                    z, r, g, b = pic.getpixel((x, y))
                    f.write(f"({x}, {y}) : ({r} {g} {b})\n")
    except FileNotFoundError:
        print("File not found and could not be created.")