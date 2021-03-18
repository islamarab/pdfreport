from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.colors import Color, black, white, grey, blue

from cards_utils import __city_card


def city_card(c, x, y, w=None, h=None, data: dict = None):
    """ ."""

    assert isinstance(data, dict), "data is not Dict"

    if not w:
        w = A4[0] - x * 2

    if not h:
        # h = w * 0.32
        h = w * 0.3

    rect_radius = [
        h / 2,
        h / 18.878,
        h / 2,
        h / 18.878
    ]

    # MAIN rounded rectangle
    c.setStrokeColor(aColor=grey, alpha=0.1)
    # c.setStrokeColor(black)  # потом удалить
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
    cell_width = table_area_width * 0.22
    space_column = (table_area_width - cell_width*4) / 5

    cell_height = table_area_height * 0.15
    space_row = (table_area_height - cell_height*4) / 8

    __city_card(
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
    )


def city_card_reversed(c, x, y, w=None, h=None, data: dict = None):
    """ ."""

    assert isinstance(data, dict), "data is not Dict"

    if not w:
        w = A4[0] - x * 2

    if not h:
        # h = w * 0.32
        h = w * 0.3

    rect_radius = [
        h / 18.878,
        h / 2,
        h / 18.878,
        h / 2
    ]

    # MAIN rounded rectangle
    c.setStrokeColor(aColor=grey, alpha=0.1)
    # c.setStrokeColor(black)  # потом удалить
    c.roundRect(x=x,
                y=y,
                width=w,
                height=h,
                radius=rect_radius, stroke=1, fill=0)

    # Content area calculating
    # Content
    content_area_width = w - h
    # Title
    title_area_width = content_area_width
    title_area_height = h * 0.2
    title_area_x = x
    title_area_y = y + h - title_area_height
    # Table
    table_area_width = content_area_width
    table_area_height = h * 0.8
    table_area_x = x
    table_area_y = y

    # Circle area calculating
    circle_area_x = x + content_area_width
    circle_area_y = y
    circle_area_width = h
    circle_area_height = h

    # Spaces and cells caltulating
    cell_width = table_area_width * 0.22
    space_column = (table_area_width - cell_width*4) / 5

    cell_height = table_area_height * 0.15
    space_row = (table_area_height - cell_height*4) / 8

    __city_card(
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
    )

