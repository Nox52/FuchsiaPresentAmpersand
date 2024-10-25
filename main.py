from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")

top_text = input("Введите верхний текст мема: ")
bottom_text = input("Введите нижний текст мема: ")
print(top_text, bottom_text)

print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")

image_number = int(input("Введите номер картинки: "))

if image_number == 1:
    image_file = "png/Кот в ресторане.png"
elif image_number == 2:
    image_file = "png/Кот в очках.png"

image = Image.open(image_file)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("calibri", size=70)

width, height = image.size

text = draw.textbbox((0, 0), top_text, font)
text_width = text[2]

draw.text(((width - text_width) / 2, 15), top_text, font=font, fill="black")

text = draw.textbbox((0, 0), bottom_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width) / 2, height - text_height - 15), bottom_text, font=font, fill="black")

image.save("meme.jpg")