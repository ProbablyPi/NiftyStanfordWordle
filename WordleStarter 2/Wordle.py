# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, MISSING_COLOR, CORRECT_COLOR, PRESENT_COLOR


def wordle():
    number = random.randint(0, len(FIVE_LETTER_WORDS))

    def enter_action(s):
        lost = False
        answer = list(FIVE_LETTER_WORDS[number].lower())

        inputlist = []
        inputstring = ""
        A = gw.get_square_letter(gw.get_current_row(), 0).lower()
        B = gw.get_square_letter(gw.get_current_row(), 1).lower()
        C = gw.get_square_letter(gw.get_current_row(), 2).lower()
        D = gw.get_square_letter(gw.get_current_row(), 3).lower()
        E = gw.get_square_letter(gw.get_current_row(), 4).lower()
        inputlist.append(A)
        inputlist.append(B)
        inputlist.append(C)
        inputlist.append(D)
        inputlist.append(E)
        inputstring = inputstring.join(inputlist).lower()

        if E == "" or FIVE_LETTER_WORDS.count(inputstring) == 0:
            gw.show_message("Word not in dictionary")

        elif not lost:
            for i in range(0, 5):
                gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                if (not (gw.get_key_color(inputstring[i].upper()) == "#CCBB66")) or (
                        not (gw.get_key_color(inputstring[i].upper()) == "#66BB66")):
                    gw.set_key_color(inputstring[i].upper(), MISSING_COLOR)

            for green in range(0, 5):
                if inputlist[green].lower() == answer[green].lower():
                    gw.set_square_color(gw.get_current_row(), green, CORRECT_COLOR)
                    gw.set_key_color(inputstring[green].upper(), CORRECT_COLOR)
                    inputlist[green] = "!greened"
                    answer[green] = "?green"

            for yellow in range(0, 5):
                if answer.count(inputlist[yellow].lower()) > 0:
                    if not (gw.get_key_color(inputstring[yellow].upper()) == "#66BB66"):
                        gw.set_key_color(inputstring[yellow].upper(), PRESENT_COLOR)
                    gw.set_square_color(gw.get_current_row(), yellow, PRESENT_COLOR)
                    answer[answer.index(inputlist[yellow])] = "?yellow"
                    inputlist[yellow] = "!yellowed"
            gw.show_message(gw.get_key_color(inputstring[yellow].upper()))

            if gw.get_square_color(gw.get_current_row(), 0) == CORRECT_COLOR and gw.get_square_color(
                    gw.get_current_row(), 1) == CORRECT_COLOR and gw.get_square_color(gw.get_current_row(),
                                                                                      2) == CORRECT_COLOR and gw.get_square_color(
                gw.get_current_row(), 3) == CORRECT_COLOR and gw.get_square_color(gw.get_current_row(),
                                                                                  4) == CORRECT_COLOR:
                gw.show_message("You Win!")
            if gw.get_current_row() < 5:
                gw.set_current_row(gw.get_current_row() + 1)
            else:
                gw.show_message("You lost")
            if gw.get_square_color(gw.get_current_row(), 0) == CORRECT_COLOR and gw.get_square_color(
                    gw.get_current_row(), 1) == CORRECT_COLOR and gw.get_square_color(gw.get_current_row(),
                                                                                      2) == CORRECT_COLOR and gw.get_square_color(
                gw.get_current_row(), 3) == CORRECT_COLOR and gw.get_square_color(gw.get_current_row(),
                                                                                  4) == CORRECT_COLOR:
                gw.show_message("You Win!")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()
