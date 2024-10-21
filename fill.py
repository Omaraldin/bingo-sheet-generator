from PIL import Image, ImageDraw, ImageFont
import random

def generate_bingo_numbers():
    numbers = {
        'B': random.sample(range(1, 16), 5),
        'I': random.sample(range(16, 31), 5),
        'N': random.sample(range(31, 46), 4),
        'G': random.sample(range(46, 61), 5),
        'O': random.sample(range(61, 76), 5)
    }
    numbers['N'].insert(2, ' ')
    return numbers

def draw_numbers(draw, numbers, font):
    start_x = 160
    start_y = 360
    w, h = 349.6, 425.2
    
    positions = [
        (164, 560), (250, 100), (450, 100), (650, 100), (850, 100),
        (164, 300), (250, 300), (450, 300), (650, 300), (850, 300),
        (419.1667, 500), (250, 500), (450, 500), (650, 500), (850, 500),
        (419.1667, 700), (250, 700), (450, 700), (650, 700), (850, 700),
        (419.1667, 900), (250, 900), (450, 900), (650, 900), (850, 900)
    ]
    
    #    B   I   N   G   O
    #    1   2   3   4   5
    # 1  X   X   X   X   X
    # 2  X   X   X   X   X
    # 3  X   X   X   X   X
    # 4  X   X   X   X   X
    # 5  X   X   X   X   X
    
    for i, letter in enumerate(['B', 'I', 'N', 'G', 'O']):
        for j in range(5):
            k, n = i + 1, j + 1
            number = numbers[letter][j]
            text = str(number)
            text_width = draw.textlength(text, font=font)
            x = start_x + (w * k) - (w / 2) - (text_width / 2) - 170
            y = start_y + (h * n) - (h / 2) - 170
            draw.text((x, y), text, fill="black", font=font)

def generate_bingo_cards(num_cards):
    template = Image.open("bingo-g.jpg")
    font = ImageFont.truetype("./GoogleSansDisplay-Bold.ttf", 240)
    
    for i in range(1, num_cards + 1):
        card = template.copy()
        draw = ImageDraw.Draw(card)
        numbers = generate_bingo_numbers()
        draw_numbers(draw, numbers, font)
        card.save(f"./out/bingo-{i}.jpg")
        print(f"Generated bingo-{i}.jpg")