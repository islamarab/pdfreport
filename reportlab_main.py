from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import mm, inch
import reportlab.rl_config
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color, black, white, grey

from utils import to_mm, rgb, shadow
from cards import city_card


def country_card(c, x, y, w, h):
    """ ."""

    print("x", x, "y", y)
    print("w", w, "h", h)

    # parent_rect_width = w
    # parent_rect_height = h

    # # Shadow
    # c.setFillColor(shadow(0.1))
    # c.setStrokeColor(shadow(0.1))
    # c.setLineWidth(5)
    # c.roundRect(x, y, w, h, radius=10, fill=True, stroke=True)
    # c.setFillColor(shadow(0.09))
    # c.setStrokeColor(shadow(0.09))
    # c.setLineWidth(5)
    # c.roundRect(x*1.05, y*0.995, w*1, h*1, radius=10, fill=True, stroke=True)

    c.setFillColor(white)
    c.setStrokeColor(shadow(0.09))
    c.setLineWidth(1)
    # c.setStrokeColorRGB(*white)
    c.roundRect(x=x,
                y=y,
                width=w,
                height=h,
                radius=10, stroke=1, fill=1)

    c.setFillColor(grey)
    c.drawString(x=x * 1.2,
                 y=y * 1.26,
                 text="Республика Казахстан")

    row_height = 20
    row_first_rects_y = y * 1.167
    space_columns = w * 0.015
    space_rows = 25

    # Column 1
    c.setFillColor(black)
    c.setFontSize(9)
    column_first_rects_x = x + space_columns
    column_first_rects_y = row_first_rects_y
    column_first_rects_width = w * 0.15
    column_first_rects_height = row_height

    c.roundRect(x=column_first_rects_x,
                y=column_first_rects_y,
                width=column_first_rects_width,
                height=column_first_rects_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=column_first_rects_x + column_first_rects_width / 2,
                        y=column_first_rects_y + row_height / 3,
                        text="Площадь")

    row_second_rects_y = column_first_rects_y - space_rows

    c.roundRect(x=column_first_rects_x,
                y=row_second_rects_y,
                width=column_first_rects_width,
                height=column_first_rects_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=column_first_rects_x + column_first_rects_width / 2,
                        y=column_first_rects_y - 25 + row_height / 3,
                        text="Квартиры")

    row_third_rects_y = row_second_rects_y - space_rows

    c.roundRect(x=column_first_rects_x,
                y=row_third_rects_y,
                width=column_first_rects_width,
                height=column_first_rects_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=column_first_rects_x + column_first_rects_width / 2,
                        y=column_first_rects_y - 25 * 2 + row_height / 3,
                        text="Объекты")

    row_fourth_rects_y = row_third_rects_y - space_rows

    c.roundRect(x=column_first_rects_x,
                y=row_fourth_rects_y,
                width=column_first_rects_width,
                height=column_first_rects_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=column_first_rects_x + column_first_rects_width / 2,
                        y=column_first_rects_y - 25 * 3 + row_height / 3,
                        text="Инветиции")

    # Column 2
    column_second_rects_x = column_first_rects_x + column_first_rects_width + space_columns
    column_second_rects_y = row_first_rects_y
    column_second_rects_width = w * 0.64
    column_second_rects_height = row_height
    c.roundRect(x=column_second_rects_x,
                y=column_second_rects_y,
                width=column_second_rects_width,
                height=column_second_rects_height,
                radius=5, stroke=1, fill=0)
    c.roundRect(x=column_second_rects_x,
                y=row_second_rects_y,
                width=column_second_rects_width,
                height=column_second_rects_height,
                radius=5, stroke=1, fill=0)
    c.roundRect(x=column_second_rects_x,
                y=row_third_rects_y,
                width=column_second_rects_width,
                height=column_second_rects_height,
                radius=5, stroke=1, fill=0)
    c.roundRect(x=column_second_rects_x,
                y=row_fourth_rects_y,
                width=column_second_rects_width,
                height=column_second_rects_height,
                radius=5, stroke=1, fill=0)
    # Subcolumn 1
    column_second_subcolumn_first_x = column_second_rects_x + column_second_rects_width * (0.02 + 0.15 / 2)
    c.setFontSize(7)
    c.setFillColor(grey)
    c.drawCentredString(x=column_second_subcolumn_first_x,
                        y=column_second_rects_y + row_height * 1.2,
                        text="Строящиеся")
    c.setFontSize(8)
    c.setFillColorRGB(rgb(255), rgb(69), rgb(29))
    c.drawCentredString(x=column_second_subcolumn_first_x,
                        y=row_first_rects_y + row_height / 3,
                        text="22 345 м2")
    c.setFillColorRGB(rgb(255), rgb(69), rgb(29))
    c.drawCentredString(x=column_second_subcolumn_first_x,
                        y=row_second_rects_y + row_height / 3,
                        text="22 345 ед.")
    c.setFillColorRGB(rgb(255), rgb(69), rgb(29))
    c.drawCentredString(x=column_second_subcolumn_first_x,
                        y=row_third_rects_y + row_height / 3,
                        text="2 345 ед.")
    # Subcolumn 2
    column_second_subcolumn_second_x = column_second_rects_x + column_second_rects_width * (0.02 + 0.15 + 0.03)
    column_second_subcolumn_second_width = column_second_rects_width * 0.6
    c.setFillColorRGB(rgb(255), rgb(69), rgb(29))
    c.setStrokeColor(grey)
    c.line(x1=column_second_subcolumn_second_x+row_height/12,
           y1=column_second_rects_y + row_height/2,
           x2=column_second_subcolumn_second_x+column_second_subcolumn_second_width-row_height/12,
           y2=column_second_rects_y + row_height/2)
    c.circle(x_cen=column_second_subcolumn_second_x+column_second_subcolumn_second_width,
             y_cen=column_second_rects_y + row_height / 2,
             r=row_height/12,
             stroke=1, fill=0)
    c.line(x1=column_second_subcolumn_second_x+row_height/12,
           y1=column_second_rects_y + row_height/2-25,
           x2=column_second_subcolumn_second_x+column_second_subcolumn_second_width-row_height/12,
           y2=column_second_rects_y + row_height/2-25)
    c.circle(x_cen=column_second_subcolumn_second_x+column_second_subcolumn_second_width,
             y_cen=column_second_rects_y + row_height/2-25,
             r=row_height/12,
             stroke=1, fill=0)
    c.line(x1=column_second_subcolumn_second_x+row_height/12,
           y1=column_second_rects_y + row_height/2-25-25,
           x2=column_second_subcolumn_second_x+column_second_subcolumn_second_width-row_height/12,
           y2=column_second_rects_y + row_height/2-25-25)
    c.circle(x_cen=column_second_subcolumn_second_x+column_second_subcolumn_second_width,
             y_cen=column_second_rects_y + row_height/2-25-25,
             r=row_height/12,
             stroke=1, fill=0)
    c.roundRect(x=column_second_subcolumn_second_x,
                y=column_second_rects_y + row_height / 2.7,
                width=column_second_rects_width * 0.2,
                height=column_second_rects_height / 4,
                radius=column_second_rects_height * 0.15, stroke=0, fill=1)
    c.roundRect(x=column_second_subcolumn_second_x,
                y=column_second_rects_y + row_height / 2.7 - 25,
                width=column_second_rects_width * 0.3,
                height=column_second_rects_height / 4,
                radius=column_second_rects_height * 0.15, stroke=0, fill=1)
    c.roundRect(x=column_second_subcolumn_second_x,
                y=column_second_rects_y + row_height / 2.7 - 25 - 25,
                width=column_second_rects_width * 0.1,
                height=column_second_rects_height / 4,
                radius=column_second_rects_height * 0.15, stroke=0, fill=1)
    c.setFontSize(7)
    c.setFillColorRGB(rgb(57), rgb(169), rgb(231))
    c.drawCentredString(x=column_second_rects_x + column_second_rects_width * (0.02 + 0.15 + 0.03 + 0.6 / 2),
                        y=column_second_rects_y - 25 - 25 - 25 + row_height / 3,
                        text="1 821 122 345 т")
    # Subcolumn 3
    column_second_subcolumn_third_x = column_second_rects_x + \
                                      column_second_rects_width * (0.02 + 0.15 + 0.03 + 0.6 + 0.03 + 0.15 / 2)
    c.setFontSize(7)
    c.setFillColor(grey)
    c.drawCentredString(x=column_second_subcolumn_third_x,
                        y=column_second_rects_y + row_height * 1.2,
                        text="Завершено")
    c.setFontSize(8)
    c.setFillColor(black)
    c.drawCentredString(x=column_second_subcolumn_third_x,
                        y=column_second_rects_y + row_height / 3,
                        text="12 345 м2")
    c.setFillColor(black)
    c.drawCentredString(x=column_second_subcolumn_third_x,
                        y=column_second_rects_y - 25 + row_height / 3,
                        text="65 965 ед.")
    c.setFillColor(black)
    c.drawCentredString(x=column_second_subcolumn_third_x,
                        y=column_second_rects_y - 25 - 25 + row_height / 3,
                        text="5 256 ед.")

    # Column 3
    column_third_rects_x = column_second_rects_x + column_second_rects_width + space_columns
    column_third_rects_y = row_first_rects_y
    column_third_rects_width = w * 0.15
    column_third_rects_height = row_height
    c.setStrokeColor(shadow(0.09))
    c.roundRect(x=column_third_rects_x,
                y=column_third_rects_y,
                width=column_third_rects_width,
                height=column_third_rects_height,
                radius=5, stroke=1, fill=0)
    c.roundRect(x=column_third_rects_x,
                y=column_third_rects_y - 25,
                width=column_third_rects_width,
                height=column_third_rects_height,
                radius=5, stroke=1, fill=0)
    c.roundRect(x=column_third_rects_x,
                y=column_third_rects_y - 25 * 2,
                width=column_third_rects_width,
                height=column_third_rects_height,
                radius=5, stroke=1, fill=0)
    c.setFontSize(7)
    c.setFillColorRGB(rgb(57), rgb(169), rgb(231))
    c.drawCentredString(x=column_third_rects_x + column_third_rects_width / 2,
                        y=column_third_rects_y + row_height / 3,
                        text="34 690 м2")
    c.drawCentredString(x=column_third_rects_x + column_third_rects_width / 2,
                        y=column_third_rects_y - 25 + row_height / 3,
                        text="88 310 ед.")
    c.drawCentredString(x=column_third_rects_x + column_third_rects_width / 2,
                        y=column_third_rects_y - 25 * 2 + row_height / 3,
                        text="7 601 ед.")


def main(c):

    pdfmetrics.registerFont(TTFont("Roboto", "assets\\fonts\\Roboto-Medium.ttf"))
    c.setFont("Roboto", 12)

    # c.drawImage(r"assets\\images\\background_image.png", x=0, y=0)

    c.setFillColor(black)
    c.drawString(100, 820, "Информация о строящихся объектах")

    c.setFillColorRGB(rgb(255), rgb(69), rgb(29))
    c.drawString(100, 780, "в разрезе регионов РК")

    country_card(c, A4[0] * 0.07, 540, A4[0] * 0.86, 160)

    city_data = {
        "city_name": "Нур-Султан",
        "table": [
            ["Строящиеся", "Завершено", "Всего"],
            ["Площадь", "12 345 м2", "22 345 м2", "34 690 м2"],
            ["Квартиры", "22 345 ед.", "65 965 ед.", "88 310 ед."],
            ["Объекты", "2 345 ед.", "5 256 ед.", "7 601 ед."],
            ["Инвестиции", "1 821 122 345 Т"]
        ],
        "proportion_of_the_total_area": 12.6
    }
    city_card(c=c, x=A4[0] * 0.07, y=300, data=city_data)

    c.showPage()


if __name__ == "__main__":
    c = canvas.Canvas(filename="reports\\hello.pdf")

    # print(to_mm(A4[0]), to_mm(A4[1]))
    print(A4)
    # print("card rect", A4[0]*0.1, A4[0]*0.8, A4[0]*0.1)
    print("card rect", A4[0] * 0.07, A4[0] * 0.86, A4[0] * 0.07)
    main(c)
    c.save()
