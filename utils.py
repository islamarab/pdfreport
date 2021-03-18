""" Module for ."""

from reportlab.lib.units import mm, inch
from reportlab.lib.colors import Color, black, white, grey


def to_mm(num):
    num = float(num)
    return num / mm


def rgb(num):
    num = float(num)
    return num / 255


def shadow(alpha):
    return Color(0, 0, 0, alpha=alpha)


def percent(a, b):
    """ ."""

    return a*100/b