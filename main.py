import calendar
from PIL import Image, ImageDraw, ImageFont

width, height = 8000, 6000

transparentColor = (255, 255, 255, 0)
primaryColor = (0, 0, 0)
secondaryColor = (0, 0, 0)
highlightColor = (249, 17, 16)

image = Image.new("RGBA", (width, height), transparentColor)
draw = ImageDraw.Draw(image)

normal_font = ImageFont.truetype("/assets/fonts/Roboto-Medium.ttf", 250)
title_font = ImageFont.truetype("/assets/fonts/Roboto-Medium.ttf", 500)

x_offset = 500
padding = 100
y_offset = padding
title_padding = 200

year = 2023
month = 5
selected_date = 21

month_names = list(calendar.month_name)[1:]
month_name = month_names[month-1]
year_text = str(year)

title_text = f"{month_name}, {year_text}"
title_width, title_height = title_font.getsize(title_text)
title_x = (width - title_width) // 2
title_y = y_offset
draw.text((title_x, title_y), title_text, fill=primaryColor, font=title_font)

days_of_week = list(calendar.day_abbr)
cell_size = 1000
days_cell_height = 500
date_cell_height = 500

y_offset += title_height + title_padding
for col, day in enumerate(days_of_week):
    x = x_offset + col * cell_size
    y = y_offset
    day_width, day_heigh = normal_font.getsize(day)
    x_centered = x + (cell_size - day_width) // 2
    y_centered = y + (days_cell_height - day_heigh) // 2
    draw.text((x_centered, y_centered), day, fill=secondaryColor, font=normal_font)

cal = calendar.monthcalendar(year, month)
y_offset += cell_size

heart_image = Image.open("/assets/images/heart-outline.png") 

for row, week in enumerate(cal):
    for col, day in enumerate(week):
        if day != 0:
            x = x_offset + col * cell_size
            y = y_offset + row * date_cell_height
            day_text = str(day)
            day_width, day_heigh = normal_font.getsize(day_text)
            x_centered = x + (cell_size - day_width) // 2
            y_centered = y + (date_cell_height - day_heigh) // 2

            if day == selected_date:
                resized_heart = heart_image.resize((date_cell_height, date_cell_height), Image.ANTIALIAS)
                img_x = x + (cell_size // 2) - (date_cell_height // 2)
                img_y = y + 85
                image.paste(resized_heart, (img_x, img_y), mask=resized_heart)

                draw.text((x_centered, y_centered), day_text, fill=highlightColor, font=normal_font)
            else:
                draw.text((x_centered, y_centered), day_text, fill=secondaryColor, font=normal_font)

image.save("calendar.png", "PNG")
