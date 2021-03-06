# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
import html


# OTHER FORMATS
def draw_on_image(image_path, image_save_path, logo_path, font_path, text_to_draw,
                  shadowcolor='black', spacing=15, default_img=False):
    """
    Функция для написания текста на изображении
    :param image_path: str - Путь до изображения которое открываем
    :param image_save_path: str - Путь куда сохраняем
    :param font_path: str - Путь до шрифта ttf!
    :param logo_path: str - Путь до лого
    :param text_to_draw: str - Что пишем собственно говоря
    :param shadowcolor: str - Цвет обводки
    :param spacing: int - Пробелы между строками
    :param default_img: bool - Если оно не стоковое, то затемняем
    :return:
    """
    # Меняем в строке laquo raquo и пр. на нормальные unicode символы
    text_to_draw = html.unescape(text_to_draw)
    # Открываем изображение
    img = Image.open(image_path)
    # Если изображение не стоковое, а это какое-нибудь фото +
    # empty нет в пути изображения FIXME более изящно идентифицировать пустышку
    if not default_img and 'empty' not in image_path:
        img = img.point(lambda p: p * 0.6)
    # Ооткрываем лого
    logo = Image.open(logo_path)
    # Получаем размеры изображения
    img_width, img_height = img.size
    # Cплитим на линии чтобы красиво было
    lines = textwrap.wrap(text_to_draw, width=40)
    # Получаем индекс самого длинного текста в строке в списке
    longest_elem_idx = lines.index(max(lines, key=len))
    # Изначальный размер шрифта, потом будем повышать
    font_size = 10
    # Часть изображения в которой должен поместиться текст
    img_fraction = 0.95
    # Выбираем шрифт, дальше будем его повышать
    font = ImageFont.truetype(font_path, font_size)
    # Смотрим по длине первой линии
    while font.getsize(lines[longest_elem_idx])[0] < img_fraction * img_width:
        font_size += 1
        font = ImageFont.truetype(font_path, font_size)
    # Уменьшаем на 1 чтобы точно влез
    font_size -= 1
    # Ставим финальный шрифт с финальным размером
    font = ImageFont.truetype(font_path, font_size)
    # Соединяем лист строк в одну через символ новой строки для того чтобы его "нарисовать"
    splitted_text = '\n'.join(lines)
    # Готовим его к тому чтобы рисовать
    draw = ImageDraw.Draw(img)
    # Получаем размеры текста
    text_width, text_height = draw.textsize(splitted_text, font=font)
    # Рисуем цветные буквы немного большего размера для эффекта тени
    # Но это оказалось ненужно
    # if not default_img and 'empty' not in image_path:
    #     draw.multiline_text(((img_width-text_width)/2 + 2, (img_height-text_height)/1.2 + 2),
    #                         splitted_text, fill=shadowcolor, font=font, spacing=spacing, align='left')
    # Рисуем белый текст
    draw.multiline_text(((img_width-text_width)/2, (img_height-text_height)/1.2),
                        splitted_text, fill=(255, 255, 255), font=font, spacing=spacing, align='left')
    # Пастим лого
    img.paste(logo, (30, 30), logo)
    # И сохраняем его как новое
    img.save(image_save_path)


if __name__ == "__main__":
    text_to_draw = 'ТЕЛЕВЕДУЩАЯ ЕЛЕНА ЛЕТУЧАЯ РАССКАЗАЛА, ПОЧЕМУ УШЛА ИЗ «РЕВИЗОРРО»'
    draw_on_image(image_path='new_empty.jpg',
                  image_save_path='sample_with_text.jpg',
                  logo_path='new_logo.png',
                  font_path='frank_medium.otf',
                  text_to_draw=text_to_draw,
                  shadowcolor='black',
                  spacing=10,
                  default_img=True)
    draw_on_image(image_path='sample_cat_normal.jpg',
                  image_save_path='sample_normal_with_text.jpg',
                  logo_path='new_logo.png',
                  font_path='frank_medium.otf',
                  text_to_draw=text_to_draw,
                  shadowcolor='black',
                  spacing=10,
                  default_img=False)
