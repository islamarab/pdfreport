from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.colors import Color, black, white, grey, blue

from utils import to_mm, rgb, shadow, percent


def __city_card(
        c,
        w,
        h,
        circle_area_x,
        circle_area_y,
        circle_area_width,
        circle_area_height,
        content_area_width,
        title_area_width,
        title_area_height,
        title_area_x,
        title_area_y,
        table_area_width,
        table_area_height,
        table_area_x,
        table_area_y,
        cell_width,
        space_column,
        cell_height,
        space_row,
        data
):

    # Circle
    c.setStrokeColor(grey)
    c.setLineWidth(circle_area_width / 2 * 0.9 - circle_area_width / 2 * 0.7)
    c.arc(x1=circle_area_x + circle_area_width * 0.1,
          y1=circle_area_y + circle_area_width * 0.1,
          x2=circle_area_x + circle_area_width * 0.9,
          y2=circle_area_y + circle_area_width * 0.9,
          startAng=90,
          extent=-361)
    c.setStrokeColorRGB(rgb(255), rgb(69), rgb(29))
    c.arc(x1=circle_area_x + circle_area_width * 0.1,
          y1=circle_area_y + circle_area_width * 0.1,
          x2=circle_area_x + circle_area_width * 0.9,
          y2=circle_area_y + circle_area_width * 0.9,
          startAng=90,
          extent=-361 * float(data['proportion_of_the_total_area']) / 100)
    c.setFontSize(size=h/6.006, leading=None)
    c.setFillColorRGB(rgb(255), rgb(69), rgb(29))
    c.drawCentredString(x=circle_area_x + circle_area_width/2,
                        y=circle_area_y + circle_area_height/2,
                        text=f"{data['proportion_of_the_total_area']}%",
                        mode=None, charSpace=0, direction=None, wordSpace=None)
    c.setFontSize(size=h/14.683, leading=None)
    c.setFillColor(grey)
    c.drawCentredString(x=circle_area_x + circle_area_width/2,
                        y=circle_area_y + circle_area_height/2.5,
                        text="Доля от общей",
                        mode=None, charSpace=0, direction=None, wordSpace=None)

    c.setFontSize(size=h/14.683, leading=None)
    c.setFillColor(grey)
    c.drawCentredString(x=circle_area_x + circle_area_width/2,
                        y=circle_area_y + circle_area_height/3,
                        text="площади по РК",
                        mode=None, charSpace=0, direction=None, wordSpace=None)

    # Title area
    title_x = title_area_x + space_column*2
    title_y = title_area_y + title_area_height / 5
    c.setFillColor(grey)
    c.setFontSize(size=h/10.165, leading=None)
    c.drawString(x=title_x,
                 y=title_y,
                 text=data['city_name'],
                 mode=None, charSpace=0, direction=None, wordSpace=None)

    # Row 1
    first_row_x = table_area_x + space_column
    first_row_y = table_area_y + space_row*6 + cell_height*4
    c.setFontSize(size=h/18.878, leading=None)
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
    c.setFontSize(size=h/13.215, leading=None)
    c.setLineWidth(1)

    # c.roundRect(x=second_row_x,
    #             y=second_row_y,
    #             width=cell_width,
    #             height=cell_height,
    #             radius=5, stroke=1, fill=0)
    c.drawString(x=second_row_x + space_column*1,
                 y=second_row_y + cell_height/3,
                 text=data['table'][1][0])

    c.setStrokeColor(aColor=grey, alpha=0.1)
    c.setFontSize(size=h/16.518, leading=None)
    c.setFillColorRGB(rgb(255), rgb(69), rgb(29))
    c.roundRect(x=second_row_x + cell_width*1 + space_column*1,
                y=second_row_y,
                width=cell_width,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=second_row_x + cell_width*1 + space_column*1 + cell_width/2,
                        y=second_row_y + cell_height/3,
                        text=data['table'][1][1])

    c.setFillColor(black)
    c.roundRect(x=second_row_x + cell_width*2 + space_column*2,
                y=second_row_y,
                width=cell_width,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=second_row_x + cell_width*2 + space_column*2 + cell_width/2,
                        y=second_row_y + cell_height/3,
                        text=data['table'][1][2])

    c.setFillColorRGB(rgb(57), rgb(169), rgb(231))
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
    c.setFillColor(grey)
    c.setFontSize(size=h/13.215, leading=None)
    c.setLineWidth(1)
    # c.roundRect(x=third_row_x,
    #             y=third_row_y,
    #             width=cell_width,
    #             height=cell_height,
    #             radius=5, stroke=1, fill=0)
    c.drawString(x=third_row_x + space_column*1,
                 y=third_row_y + cell_height/3,
                 text=data['table'][2][0])

    c.setStrokeColor(aColor=grey, alpha=0.1)
    c.setFontSize(size=h/16.518, leading=None)
    c.setFillColorRGB(rgb(255), rgb(69), rgb(29))
    c.roundRect(x=third_row_x + cell_width*1 + space_column*1,
                y=third_row_y,
                width=cell_width,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=third_row_x + cell_width*1 + space_column*1 + cell_width/2,
                        y=third_row_y + cell_height/3,
                        text=data['table'][2][1])

    c.setFillColor(black)
    c.roundRect(x=third_row_x + cell_width*2 + space_column*2,
                y=third_row_y,
                width=cell_width,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=third_row_x + cell_width*2 + space_column*2 + cell_width/2,
                        y=third_row_y + cell_height/3,
                        text=data['table'][2][2])

    c.setFillColorRGB(rgb(57), rgb(169), rgb(231))
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
    c.setFillColor(grey)
    c.setFontSize(size=h/13.215, leading=None)
    c.setLineWidth(1)
    # c.roundRect(x=fourth_row_x,
    #             y=fourth_row_y,
    #             width=cell_width,
    #             height=cell_height,
    #             radius=5, stroke=1, fill=0)
    c.drawString(x=fourth_row_x + space_column*1,
                 y=fourth_row_y + cell_height/3,
                 text=data['table'][3][0])

    c.setStrokeColor(aColor=grey, alpha=0.1)
    c.setFontSize(size=h/16.518, leading=None)
    c.setFillColorRGB(rgb(255), rgb(69), rgb(29))
    c.roundRect(x=fourth_row_x + cell_width*1 + space_column*1,
                y=fourth_row_y,
                width=cell_width,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=fourth_row_x + cell_width*1 + space_column*1 + cell_width/2,
                        y=fourth_row_y + cell_height/3,
                        text=data['table'][3][1])

    c.setFillColor(black)
    c.roundRect(x=fourth_row_x + cell_width*2 + space_column*2,
                y=fourth_row_y,
                width=cell_width,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=fourth_row_x + cell_width*2 + space_column*2 + cell_width/2,
                        y=fourth_row_y + cell_height/3,
                        text=data['table'][3][2])

    c.setFillColorRGB(rgb(57), rgb(169), rgb(231))
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
    c.setFillColor(grey)
    c.setFontSize(size=h/13.215, leading=None)
    c.setLineWidth(1)
    # c.roundRect(x=fifth_row_x,
    #             y=fifth_row_y,
    #             width=cell_width,
    #             height=cell_height,
    #             radius=5, stroke=1, fill=0)
    c.drawString(x=fifth_row_x + space_column*1,
                 y=fifth_row_y + cell_height/3,
                 text=data['table'][4][0])

    c.setStrokeColor(aColor=grey, alpha=0.1)
    c.setFontSize(size=h/16.518, leading=None)
    c.setFillColorRGB(rgb(57), rgb(169), rgb(231))
    c.roundRect(x=fifth_row_x + cell_width*1 + space_column*1,
                y=fifth_row_y,
                width=cell_width*2+space_column,
                height=cell_height,
                radius=5, stroke=1, fill=0)
    c.drawCentredString(x=fifth_row_x + cell_width*1 + space_column*1 + (cell_width*2+space_column)/2,
                        y=fifth_row_y + cell_height/3,
                        text=data['table'][4][1])
