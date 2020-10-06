from PIL import Image, ImageDraw, ImageFont

def genarateBar(xp, level):
    req = level * 25 + 100
    proc = xp / req * 100

    proc *= 4
    im = Image.new('RGBA', (400, 30), (0, 0, 0, 0))

    draw = ImageDraw.Draw(im)

    font = ImageFont.truetype("font.ttf", 12)
    draw.text((0, 3), f"{round(proc/4)}% To level {level+1}", (240, 240, 240), font=font)

    TINT_COLOR = (0, 0, 0)  # Black
    TRANSPARENCY = .10  # Degree of transparency, 0-100%
    OPACITY = int(255 * TRANSPARENCY)
    draw.rectangle(((0, 16), (600, 25)), fill=TINT_COLOR+(OPACITY,))


    draw.line((0, 20, proc, 20), fill=(255, 0, 61), width=5)
    im.save('image.png', quality=95)
