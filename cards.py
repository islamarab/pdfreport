from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import mm, inch
import reportlab.rl_config
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color, black, white, grey, blue

from utils import to_mm, rgb, shadow, percent


def city_card(c, x, y, w=None, h=None, data: dict = None):
    """ ."""

    print(x, y)

    assert isinstance(data, dict), "data is not Dict"

    if not w:
        w = A4[0] - x * 2
        print("w", w, "A4[0]", A4[0])

    if not h:
        h = w * 0.32

    rect_radius = [h / 2, 7, h / 2, 7]

    # MAIN rounded rectangle
    c.setStrokeColor(shadow(0.09))
    c.setStrokeColor(black)  # потом удалить
    c.roundRect(x=x,
                y=y,
                width=w,
                height=h,
                radius=rect_radius, stroke=1, fill=0)

    # Circle area calculating
    circle_area_x = x
    circle_area_y = y
    circle_area_width = h
    circle_area_height = h

    # Content area calculating
    # Content
    content_area_width = w - circle_area_width
    # Title
    title_area_width = content_area_width
    title_area_height = h * 0.2
    title_area_x = x + circle_area_width
    title_area_y = y + h - title_area_height

    # Table
    table_area_width = content_area_width
    table_area_height = h * 0.8
    table_area_x = x + circle_area_width
    table_area_y = y

    # Spaces and cells caltulating
    space_column = table_area_width * 0.04
    space_row = table_area_height * 0.05
    cell_width = table_area_width * 0.2
    cell_height = table_area_height * 0.15

    # Circle
    c.setStrokeColor(grey)
    c.setLineWidth(circle_area_width / 2 * 0.9 - circle_area_width / 2 * 0.7)
    c.arc(x1=x + circle_area_width * 0.1,
          y1=y + circle_area_width * 0.1,
          x2=x + circle_area_width * 0.9,
          y2=y + circle_area_width * 0.9,
          startAng=90,
          extent=-361)
    c.setStrokeColorRGB(rgb(255), rgb(69), rgb(29))
    c.arc(x1=x + circle_area_width * 0.1,
          y1=y + circle_area_width * 0.1,
          x2=x + circle_area_width * 0.9,
          y2=y + circle_area_width * 0.9,
          startAng=90,
          extent=-361 * float(data['proportion_of_the_total_area']) / 100)
    c.setFontSize(22)
    c.setFillColorRGB(rgb(255), rgb(69), rgb(29))
    c.drawCentredString(x=circle_area_x + circle_area_width/2,
                        y=circle_area_y + circle_area_height/2,
                        text=f"{data['proportion_of_the_total_area']}%",
                        mode=None, charSpace=0, direction=None, wordSpace=None)
    c.setFontSize(9)
    c.setFillColor(grey)
    c.drawCentredString(x=circle_area_x + circle_area_width/2,
                        y=circle_area_y + circle_area_height/2.5,
                        text="Доля от общей",
                        mode=None, charSpace=0, direction=None, wordSpace=None)

    c.setFontSize(9)
    c.setFillColor(grey)
    c.drawCentredString(x=circle_area_x + circle_area_width/2,
                        y=circle_area_y + circle_area_height/3,
                        text="площади по РК",
                        mode=None, charSpace=0, direction=None, wordSpace=None)

    # Title area
    title_x = x + circle_area_width + space_column
    title_y = title_area_y + title_area_height / 3
    c.setFillColor(grey)
    c.setFontSize(size=13, leading=None)
    c.drawString(x=title_x,
                 y=title_y,
                 text=data['city_name'],
                 mode=None, charSpace=0, direction=None, wordSpace=None)

    # Row 1
    first_row_x = table_area_x + space_column
    first_row_y = table_area_y + space_row*6 + cell_height*4
    c.setFontSize(size=7, leading=None)
    c.drawCentredString(x=first_row_x + cell_width*1 + space_column*1 + cell_width/2,
                        y=first_row_y,
                        text=data['table'][0][0])
    c.drawCentredString(x=first_row_x + cell_width*2 + space_column*2 + cell_width/2,
                        y=first_row_y,
                        text=data['table'][0][1])
    c.drawCentredString(x=first_row_x + cell_width*3 + space_column*3 + cell_width/2,
                        y=first_row_y,
                        text=data['table'][0][2])

    # Row 2
    second_row_x = table_area_x + space_column
    second_row_y = table_area_y + space_row*5 + cell_height*3
    c.setStrokeColor(grey)
    c.setFontSize(10)
    c.setLineWidth(1)
    # c.roundRect(x=second_row_x,
    #             y=second_row_y,
    #             width=cell_width,
    #             height=cell_height,
    #             radius=5, stroke=1, fill=0)
    c.drawString(x=second_row_x,
                        y=second_row_y + cell_height/3,
                        text=data['table'][1][0])
    c.roundRect(x=second_row_x + cell_width*1 + space_column*1,
                y=second_row_y,
                width=cell_width,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=second_row_x + cell_width*1 + space_column*1 + cell_width/2,
                        y=second_row_y + cell_height/3,
                        text=data['table'][1][1])
    c.roundRect(x=second_row_x + cell_width*2 + space_column*2,
                y=second_row_y,
                width=cell_width,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=second_row_x + cell_width*2 + space_column*2 + cell_width/2,
                        y=second_row_y + cell_height/3,
                        text=data['table'][1][2])
    c.roundRect(x=second_row_x + cell_width*3 + space_column*3,
                y=second_row_y,
                width=cell_width,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=second_row_x + cell_width*3 + space_column*3 + cell_width/2,
                        y=second_row_y + cell_height/3,
                        text=data['table'][1][3])

    # Row 3
    third_row_x = table_area_x + space_column
    third_row_y = table_area_y + space_row*4 + cell_height*2
    c.setStrokeColor(grey)
    c.setFontSize(10)
    c.setLineWidth(1)
    # c.roundRect(x=third_row_x,
    #             y=third_row_y,
    #             width=cell_width,
    #             height=cell_height,
    #             radius=5, stroke=1, fill=0)
    c.drawString(x=third_row_x,
                        y=third_row_y + cell_height/3,
                        text=data['table'][2][0])
    c.roundRect(x=third_row_x + cell_width*1 + space_column*1,
                y=third_row_y,
                width=cell_width,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=third_row_x + cell_width*1 + space_column*1 + cell_width/2,
                        y=third_row_y + cell_height/3,
                        text=data['table'][2][1])
    c.roundRect(x=third_row_x + cell_width*2 + space_column*2,
                y=third_row_y,
                width=cell_width,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=third_row_x + cell_width*2 + space_column*2 + cell_width/2,
                        y=third_row_y + cell_height/3,
                        text=data['table'][2][2])
    c.roundRect(x=third_row_x + cell_width*3 + space_column*3,
                y=third_row_y,
                width=cell_width,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=third_row_x + cell_width*3 + space_column*3 + cell_width/2,
                        y=third_row_y + cell_height/3,
                        text=data['table'][2][3])

    # Row 4
    fourth_row_x = table_area_x + space_column
    fourth_row_y = table_area_y + space_row*3 + cell_height*1
    c.setStrokeColor(grey)
    c.setFontSize(10)
    c.setLineWidth(1)
    # c.roundRect(x=fourth_row_x,
    #             y=fourth_row_y,
    #             width=cell_width,
    #             height=cell_height,
    #             radius=5, stroke=1, fill=0)
    c.drawString(x=fourth_row_x,
                        y=fourth_row_y + cell_height/3,
                        text=data['table'][3][0])
    c.roundRect(x=fourth_row_x + cell_width*1 + space_column*1,
                y=fourth_row_y,
                width=cell_width,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=fourth_row_x + cell_width*1 + space_column*1 + cell_width/2,
                        y=fourth_row_y + cell_height/3,
                        text=data['table'][3][1])
    c.roundRect(x=fourth_row_x + cell_width*2 + space_column*2,
                y=fourth_row_y,
                width=cell_width,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=fourth_row_x + cell_width*2 + space_column*2 + cell_width/2,
                        y=fourth_row_y + cell_height/3,
                        text=data['table'][3][2])
    c.roundRect(x=fourth_row_x + cell_width*3 + space_column*3,
                y=fourth_row_y,
                width=cell_width,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=fourth_row_x + cell_width*3 + space_column*3 + cell_width/2,
                        y=fourth_row_y + cell_height/3,
                        text=data['table'][3][3])

    # Row 5
    fifth_row_x = table_area_x + space_column
    fifth_row_y = table_area_y + space_row*2 + cell_height*0
    c.setStrokeColor(grey)
    c.setFontSize(10)
    c.setLineWidth(1)
    # c.roundRect(x=fifth_row_x,
    #             y=fifth_row_y,
    #             width=cell_width,
    #             height=cell_height,
    #             radius=5, stroke=1, fill=0)
    c.drawString(x=fifth_row_x,
                        y=fifth_row_y + cell_height/3,
                        text=data['table'][4][0])
    c.roundRect(x=fifth_row_x + cell_width*1 + space_column*1,
                y=fifth_row_y,
                width=cell_width*2+space_column,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=fifth_row_x + cell_width*1 + space_column*1 + (cell_width*2+space_column)/2,
                        y=fifth_row_y + cell_height/3,
                        text=data['table'][4][1])
