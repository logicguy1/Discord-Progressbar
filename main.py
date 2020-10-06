from PIL import Image, ImageDraw, ImageFont

def genarateBar(xp, level):
    req = level * 25 + 100 # the required xp for the next level update this for your use case
    proc = xp / req * 100 # The maount of procent left for the next level

    proc *= 4 # The canvas is 400 pixels long since proc is a number between 0 and 100 we * it by 4 to get the amount of pixels to draw
    im = Image.new('RGBA', (400, 30), (0, 0, 0, 0)) # Create the canvas

    draw = ImageDraw.Draw(im) # Allow us to draw on the image

    font = ImageFont.truetype("font.ttf", 12) # Load up the font
    draw.text((0, 3), f"{round(proc/4)}% To level {level+1}", (240, 240, 240), font=font) # Type the text on the leveling bar (x% To level y)

    TINT_COLOR = (0, 0, 0)  # Setup for transparency
    TRANSPARENCY = .10  # Degree of transparency, 0-100%
    OPACITY = int(255 * TRANSPARENCY)
    draw.rectangle(((0, 16), (600, 25)), fill=TINT_COLOR+(OPACITY,)) # Draw the trasparent line under the leveling bar


    draw.line((0, 20, proc, 20), fill=(255, 0, 61), width=5) # Draw the leveling bar
    im.save('image.png', quality=95) # Save the image

if __name__ == '__main__':
    genarateBar(50, 2)
