from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap


def draw_on_image(image_path, image_save_path, font_path, text_to_draw,
                  shadowcolor='black', spacing=15, font_size=70):
    """
    Рисуем на изображении буквы
    :param image_path: str - Путь до изображения которое открываем
    :param image_save_path: str - Путь куда сохраняем
    :param font_path: str - Путь до шрифта ttf!
    :param text_to_draw: str - Что пишем собственно говоря
    :param shadowcolor: str - Цвет обводки
    :param spacing: int - Пробелы между строками
    :param font_size: int - Размер шрифта
    :return:
    """

    # Открываем изображение
    img = Image.open(image_path)
    # Получаем размеры
    img_width, img_height = img.size
    # Выбираем шрифт
    font = ImageFont.truetype(font_path, font_size)
    # Cплитим на линии чтобы красиво было
    lines = textwrap.wrap(text_to_draw, width=30)
    # И соединяем с символом новой строки
    splitted_text = '\n'.join(lines)
    # Готовим его к тому чтобы рисовать
    draw = ImageDraw.Draw(img)
    # Получаем размеры текста
    text_width, text_height = draw.textsize(splitted_text, font=font)
    # Рисуем цветные буквы немного большего размера
    draw.multiline_text(((img_width-text_width)/2 + 2, (img_height-text_height)/2 + 2),
                        splitted_text, fill=shadowcolor, font=font, spacing=spacing, align='center')
    # Рисуем белый текст
    draw.multiline_text(((img_width-text_width)/2, (img_height-text_height)/2),
                        splitted_text, fill=(255, 255, 255), font=font, spacing=spacing, align='center')
    # И сохраняем его как новое
    img.save(image_save_path)


if __name__ == "__main__":
    draw_on_image(image_path='sample.jpg',
                  image_save_path='sample_with_text.jpg',
                  font_path='reforma_grotesk_bold.ttf',
                  text_to_draw='АНДРЕЙ ВОРОБЬЕВ ВЫСТУПИТ С ЕЖЕГОДНЫМ ОБРАЩЕНИЕМ К ЖИТЕЛЯМ ПОДМОСКОВЬЯ 14 ФЕВРАЛЯ',
                  shadowcolor='green',
                  spacing=20,
                  font_size=60)
