#!/usr/bin/env python3


import os
from curses import wrapper
from pathlib import Path

import settings
from bristle_init import projectSetup
from bristle_ui import ui


def main():
    wrapper(ui)

if __name__ == '__main__':
    main()
