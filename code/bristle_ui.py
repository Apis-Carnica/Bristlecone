#!/usr/bin/env python3


import curses
from curses import wrapper
import time
import settings
from bristle_init import projectSetup


menu = ["Start a new project", "Open an existing project", "Recompile a project", "Exit"]


def newProject(stdscr):
    projectSetup(settings.project)
    stdscr.clear()
    stdscr.addstr("Setting up your project...")
    stdscr.addstr("Press any key.")
    stdscr.refresh()
    stdscr.getch()


def printMenu(stdscr, selected):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = width // 2 - len(row) // 2
        y = height // 2 - len(menu) // 2 + idx
        if idx == selected:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, row)
    stdscr.noutrefresh()


def ui(stdscr):
    stdscr.clear()
    curses.curs_set(0)

    current_row = 0
    printMenu(stdscr, current_row)
    curses.doupdate()

    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10,13]:
            if current_row == 0:
                newProject(stdscr)
            elif current_row == 1:
                openProject(stdscr)
            elif current_row == 2:
                recompile(stdscr)
            elif current_row == len(menu) - 1:
                break
        printMenu(stdscr, current_row)
        curses.doupdate()

