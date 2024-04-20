#!/usr/bin/env python3


import os
import datetime
from pathlib import Path
import curses
from curses import wrapper


global project
project = "Testing"

global tester
tester = "Ursa"

global docs
docs = {"NDA": False, "SOW": False, "ROE": False, "Approval": False, "3rd Party": False, "Other": False}

global engagement_type
engagement_type = {"Black Box": False, "White Box": False, "Grey Box": False}

global engagement_scope
engagement_scope = {"Physical": False, "Remote": False, "Full-spec": False, "Wireless": False, "Web": False, "App": False, "SocEng": False, "Rogue": False, "Inside": False, "DoS": False}

global timeline
timeline = {"from": datetime.date.today(), "to": (datetime.date.today() + datetime.timedelta(days=7)), "Status Updates": {"Daily": False, "Weekly": False, "Monthly": False, "Quarterly": False}}

global texname
texname = "Exam_en.tex"

global projectdir
projectdir = f"/tmp/{project}"


# Creation of the writeup.tex file
def docHeader():
    with open("/tmp/Testing/writeup/writeup.tex", "w") as f:
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage[utf8]{inputenc}\n")
        f.write("\\usepackage{tikz}   % https://mirrors.rit.edu/CTAN/graphics/pgf/base/doc/pgfmanual.pdf\n")
        f.write("\\usepackage{tcolorbox}  % https://ctan.math.washington.edu/tex-archive/macros/latex/contrib/tcolorbox/tcolorbox.pdf\n")
        f.write("\\usepackage{wrapfig}    % https://www.overleaf.com/learn/latex/Wrapping_text_around_figures\n")
        f.write("\\setcounter{secnumdepth}{0} % https://tex.stackexchange.com/questions/116670/section-numbering\n")
        f.write("\\usepackage{enumitem,amssymb} % https://tex.stackexchange.com/questions/2291/how-do-i-change-the-enumerate-list-format-to-use-letters-instead-of-the-defaul\n")
        f.write("\\usepackage{graphicx} % https://en.wikibooks.org/wiki/LaTeX/Importing_Graphics\n")
        f.write("\\graphicspath{{./resources}}\n")
        f.write("\\usepackage[sfdefault,book]{FiraSans} %% option 'sfdefault' activates Fira Sans as the default text font\n")
        f.write("\\usepackage[T1]{fontenc}\n")
        f.write("\\renewcommand*\\oldstylenums[1]{{\\firaoldstyle #1}}\n")
        f.write("\\usepackage{listings} % https://en.wikibooks.org/wiki/LaTeX/Source_Code_Listings\n")
        f.write("\\usepackage{hyperref} % https://en.wikibooks.org/wiki/LaTeX/Hyperlinks\n")
        f.write("\\usepackage{xcolor} % https://en.wikibooks.org/wiki/LaTeX/Colors\n")
        f.write("\\definecolor{ELColor}{HTML}{81B29A} % Green\n")
        f.write("\\definecolor{TCColor}{HTML}{F2CC8F} % Yellow\n")
        f.write("\\definecolor{WColor}{HTML}{E07A5F}  % Red\n")
        f.write("\\definecolor{TColor}{HTML}{3D405B}  % Dark Blue\n")
        f.write("\\definecolor{NFColor}{HTML}{F4F1DE} % Cream\n\n")
        f.write("\\author{Ursa}\n\n")


def titlePage():
    with open(f"{projectdir}/writeup/writeup.tex", "a") as f:
        f.write("\\begin{document}\n")
        f.write("% Title Page\n")
        f.write("\\begin{center}\n")
        f.write("\\begin{tikzpicture}[scale=0.35]\n")
        f.write("\\color{WColor}\\draw[ultra thick, rounded corners=3pt] (-2,0) -- (-4,-3) -- (-5,-2.5) -- (-5,2.5) -- (-2,4) -- (-2,0);\n")
        f.write("\\color{WColor}\\draw[ultra thick, rounded corners=3pt] (-1,0) -- (-2,-4) -- (0,-5) -- (2,-4) -- (1,0) -- (1,4.5) -- (0,5) -- (-1,4.5) -- (-1,0);\n")
        f.write("\\color{WColor}\\draw[ultra thick, rounded corners=3pt] (2,0) -- (4,-3) -- (5,-2.5) -- (5,2.5) -- (2,4) -- (2,0);\n")
        f.write("\\end{tikzpicture}\n\n")
        f.write("\\Huge{\\color{TColor}{OSCP Penetration Test Report}}\n\n")
        f.write("\\Large{\\color{TColor}{Ursa -- ursa@artiotech.org}}\\\\\n")
        f.write("\\Large{\\color{TColor}{OSID: 5472386}}\n")
        f.write("\\end{center}\n")
        f.write("\\color{TColor}\n")
        f.write("\\vfill\n")
        f.write("\\tableofcontents\n")
        f.write("\\vfill\n")
        f.write("\\pagebreak\n\n")


def simpleContent():
    with open(f"{projectdir}/writeup/writeup.tex", "a") as f:
        f.write("\\section{Introduction}\n")
        f.write("This is a test.\n\n")
        f.write("\\section{Scanning}\n")
        f.write("This is a test.\n\n")
        f.write("\\section{Enumeration}\n")
        f.write("This is a test.\n\n")
        f.write("\\section{Exploitation}\n")
        f.write("This is a test.\n\n")
        f.write("\\section{Privilege Escalation}\n")
        f.write("This is a test.\n\n")
        f.write("\\section{Cleaning House}\n")
        f.write("This is a test.\n\n")
        f.write("\\end{document}\n")




def initTasks():
    with open(f"{projectdir}/tasks.csv","w") as file:
        file.write("Member, Description, Complete?\r\n")


def initTools():
    with open(f"{projectdir}/tools.csv","w") as file:
        file.write("Date, Type, Name, Deploy Location\r\n")


def initRecommendations():
    with open(f"{projectdir}/recs.csv","w") as file:
        file.write("Finding, Recommendation\r\n")


def initFindings():
    with open(f"{projectdir}/findings.csv","w") as file:
        file.write("Finding, Description, Affected Users/Infra\r\n")


def initObjectives():
    with open(f"{projectdir}/objectives.csv","w") as file:
        file.write("Goal, Description\r\n")


def initInfrastructure():
    with open(f"{projectdir}/infra.csv","w") as file:
        file.write("IP, Hostname, Description\r\n")


def initAccounts():
    with open(f"{projectdir}/accounts.csv","w") as file:
        file.write("Service, IP/Domain, Username, Password\r\n")


def projectSetup(project: str):
    """
    The project directory will be set up in ~/Documents/ by default. You can change it if needed.
    This function will make a few folders and files to use:
        dirs: resources, writeup, scans
        files: config, accounts, infrastructure, objectives, tasks, tools, findings, recommendations, walkthrough
    """
    Path(projectdir).mkdir(parents=True, exist_ok=True)
    Path(projectdir + '/resources').mkdir(parents=True, exist_ok=True)
    Path(projectdir + '/writeup').mkdir(parents=True, exist_ok=True)
    Path(projectdir + '/scans').mkdir(parents=True, exist_ok=True)

    initAccounts()
    initInfrastructure()
    initObjectives()
    initFindings()
    initTasks()
    initTools()
    initRecommendations()

    with open(f"{projectdir}/walkthrough.txt","w") as file:
        file.write(f"{project}\r\n")
        file.write(f"{tester}\r\n")
        file.write("----------\r\n")
        file.write("Scanning\r\n\r\n")
        file.write("Enumeration\r\n\r\n")
        file.write("Exploitation\r\n\r\n")
        file.write("Privilege Escalation\r\n\r\n")
        file.write("Cleaning House\r\n\r\n")
        file.write("Fin")












menu = ["Start a new project", "Open an existing project", "Recompile a project", "Exit"]


def compileProject(stdscr):
    docHeader()
    titlePage()
    simpleContent()
    os.system(f"pdflatex -output-directory={projectdir}/writeup {projectdir}/writeup/writeup.tex")
    stdscr.clear()
    stdscr.addstr("Compiling Project to TeX.\n")
    stdscr.addstr("Press any key.")
    stdscr.refresh()
    key = stdscr.getch()
    if key in [curses.KEY_EXIT, 27]:
        printMenu(stdscr, 0)

def mainUI(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    stdscr.addstr("Main UI\n")
    stdscr.refresh()
    stdscr.getch()


def newProject(stdscr):
    projectSetup(project)
    stdscr.clear()
    stdscr.addstr("New Project Created.\n")
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
                mainUI(stdscr)
                #openProject(stdscr)
            elif current_row == 2:
                compileProject(stdscr)
                #recompile(stdscr)
            elif current_row == len(menu) - 1:
                break
        printMenu(stdscr, current_row)
        curses.doupdate()


def main():
    wrapper(ui)

if __name__ == '__main__':
    main()
