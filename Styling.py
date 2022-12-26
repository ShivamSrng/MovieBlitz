import colorama
from colorama import Fore
from colorama import Back
from colorama import Style

spacing, left_space = 100, 10


def init():
    colorama.init(autoreset=True)


def lines(*attribs):
    aligner_hl = "{:^" + str(spacing) + "}"
    set_color = Fore.__getattribute__(attribs[0])
    set_style = Style.BRIGHT
    if len(attribs) == 3:
        back_color = Back.__getattribute__(attribs[1])
        print(set_color + back_color + set_style + aligner_hl.format("-" * attribs[2]))
    else:
        print(set_color + set_style + aligner_hl.format("-" * attribs[1]))


def centeredText(*attribs):
    aligner_hl = "{:^" + str(spacing) + "}"
    set_color = Fore.__getattribute__(attribs[0])
    set_style = Style.BRIGHT
    if len(attribs) == 3:
        back_color = Back.__getattribute__(attribs[1])
        print(set_color + back_color + set_style + aligner_hl.format(attribs[2]))
    else:
        print(set_color + set_style + aligner_hl.format("-" * attribs[1]))


def normalText(*attribs):
    aligner_txt = "{:<" + str(spacing) + "}"
    set_color = Fore.__getattribute__(attribs[0])
    set_style = Style.BRIGHT
    if len(attribs) == 3:
        back_color = Back.__getattribute__(attribs[1])
        print(set_color + back_color + set_style + aligner_txt.format(" " * left_space + attribs[2]))
    else:
        print(set_color + set_style + aligner_txt.format(attribs[1]))


def emptyLine(*attribs):
    normalText(*attribs, " ")
