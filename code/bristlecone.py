#!/usr/bin/env python3


import os
import curses
from pathlib import Path

import settings
from bristle_init import projectSetup


def main():
    projectSetup(settings.project)

if __name__ == '__main__':
    main()
