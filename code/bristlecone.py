#!/usr/bin/env python3


import os
import datetime
from pathlib import Path
import curses
from curses import A_REVERSE, wrapper


project = "Testing"
tester = "Ursa"
docs = {"NDA": False, "SOW": False, "ROE": False, "Approval": False, "3rd Party": False, "Other": False}
engagement_type = {"Black Box": False, "White Box": False, "Grey Box": False}
engagement_scope = {"Physical": False, "Remote": False, "Full-spec": False, "Wireless": False, "Web": False, "App": False, "SocEng": False, "Rogue": False, "Inside": False, "DoS": False}
timeline = {"from": datetime.date.today(), "to": (datetime.date.today() + datetime.timedelta(days=7)), "Status Updates": {"Daily": False, "Weekly": False, "Monthly": False, "Quarterly": False}}
projectdir = f"/tmp/{project}"
menu = ["Start a new project", "Open an existing project", "Recompile a project", "Open compiled report", "Exit"]


# Initialization functions
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

def examTitlePage():
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

def foreword():
    with open(f"{projectdir}/writeup/writeup.tex", "a") as f:
        f.write("\\section{High-level Summary}\n")
        f.write("\\begin{wrapfigure}[10]{r}{0.4\\textwidth}\n")
        f.write("\\begin{tcolorbox}[colback=white, colframe=TCColor, title=A quick note]\n")
        f.write("Testers look for insecure settings or data out of place, which may not fit snugly into one standard's regulation.\n")
        f.write("\\end{tcolorbox}\n")
        f.write("\\end{wrapfigure}\n")
        f.write("\\paragraph{High-level Summary}Ursa was tasked with performing an internal penetration test on the Offensive Security (refered to as OffSec in this report) exam environment. The focus of this test is to identify systems inside the OSCP.exam domain, find any vulnerabilities in the lab machines inside the domain as well as three standalone hosts, attack those vulnerabilities to gain privileged access to the hosts, and report all findings back to OffSec.\n")
        f.write("\\paragraph{Recommendations}Ursa recommends that OffSec follow OWASP's \\href{https://github.com/OWASP/ASVS/tree/v4.0.3#latest-stable-version---403}{Application Security Verification Standard} to correct all web app-related vulnerabilities, correct all vulnerabilities identified in this report, and take advantage of MITRE \\href{https://attack.mitre.org/}{ATT\\&CK} and \\href{https://shield.mitre.org/resources/downloads/Introduction_to_MITRE_Shield.pdf}{SHIELD} frameworks to progressively increase the security posture of the organization.\n")
        f.write("\\begin{tcolorbox}[colback=white, colframe=TColor, title=Regarding Security Standards]\n")
        f.write("There are plenty of standards and regulations that a tester can reference when conducting an engagement; listing the ones most often used would be outside the scope of this document, though some effort will be made to educate the technical personnel reading the later sections of this report. The two most common institutions that publish standards which your leadership can use to augment current security practices are \\href{https://www.nist.gov/}{The National Institute of Standards and Technology (NIST)} and \\href{https://www.iso.org/home.html}{The International Organization for Standardization}.\n")
        f.write("\\end{tcolorbox}\n")
        f.write("\\pagebreak\n\n")
        f.write("\\section{Methodologies}\n")
        f.write("\\paragraph{}Ursa used a hybridized methodology which adopted important management principles from the PMBOK project management method, and tied the various project phases to individual steps of the penetration test. There were multiple instances during the test that required a planning phase, such as tying users to their respective groups to create a roadmap that Ursa could use to gain access to a domain admin account. There are also instances of enumeration where iteration of penetration testing steps is necessary, such as individual testing of multiple services.\n")
        f.write("\\subsection*{Information Gathering}\n")
        f.write("\\paragraph{}This step encompasses the action of instituting the foundational documents for the engagement, including the scope, rules of engagement, project schedule, types of tests performed, and approval from both parties. Investigating any information offered and undergoing passive reconnaisance on the hosts, apps, users, and methods that are known about at the start of the engagement are also completed in this step.\n")
        f.write("\\begin{center}\n")
        f.write("\\begin{tcolorbox}[colback=white, colframe=TColor, title=Scope of Work, text width=0.91\\textwidth]\n")
        f.write("The following hosts have been designated in-scope by OffSec:\n")
        f.write("\\vspace{5pt}\n")
        f.write("\\begin{center}\n")
        f.write("\\begin{tabular}{| l | c | c |}\n")
        f.write("\\hline\n")
        file = open(f"{projectdir}/infra.csv","r")
        lines = file.read().splitlines()
        file.close()
        f.write(lines[0].replace(", "," & ")+"\\\\\n")
        f.write("\\hline\n")
        for line in lines[1:]:
            f.write(line.replace(", "," & ")+"\\\\\n")
        f.write("\\hline\n")
        f.write("\\end{tabular}\n")
        f.write("\\end{center}\n")
        f.write("\\end{tcolorbox}\n")
        f.write("\\end{center}\n")
        f.write("\\subsection*{Enumeration}\n")
        f.write("\\paragraph{Host Enumeration}Sometimes, the tester is given a domain or a IP range to test, and must identify the individual hosts; that's not the case in this scenario.\n")
        f.write("\\paragraph*{Service Enumeration}This portion of the enumeration step is almost always conducted; the open (and sometimes filtered) ports are noted along with their service name and version. This is important information since it gives the attacker a more in-depth understanding of the services they're working to infiltrate. This is one of the most important steps of the test, and comprises around 80\\% of the content in a report. After grabbing the service information, the tester must iterate the enumeration phase for each running service to gather more information about the host.\n")
        f.write("\\subsection*{Exploitation}\n")
        f.write("\\paragraph{}When a vulnerability is made readily apparent, the phase changes temporarily to the exploitation phase, and the vulnerability is tested. Oftentimes the enumeration and exploitation phases will cycle, similar to the monitor \\& control phases in project management methodologies, until one vulnerability is successfully exploited. In this test, Ursa was able to exploit 4 out of the 6 systems.\n")
        f.write("\\subsection*{Maintaining Access}\n")
        f.write("\\paragraph{}In most cases, the penetration tester will have a way to cement their presence on the domain, or on the host(s) they're testing. This is important in case the tester needs to access the system at a later date; some exploits leave the host in a state where the original exploit is unrepeatable, and will not allow access via that avenue again. Ursa utilized Meterpreter on the first Active Directory host, and kept user credentials and hashes from the other machines. Unfortunately, in this exam environment, many hosts would revert without warning, and as a result, would terminate any ongoing sessions and remove all progress.\n")
        f.write("\\subsection*{Privilege Escalation}\n")
        f.write("\\paragraph{}After the initial access onto a host, another round of enumeration is taken to identify vulnerabilities directly related to escalating the current user to another account, either horizontally as another user with different permissions, or vertically, as a more privileged user or admin that could control the computer entirely. This step follows the same loop as earlier, but the focus on vulnerability type changes drastically. Once the tester has achieved access to the root or admin account(s), the host is considered compromised entirely and the test is mostly complete. In Active Directly environments, the equivalent would be Administrator access to the Domain Controller, or access to a user in the Domain Admins group. Ursa was successful in accessing a root user on a standalone machine, and multiple Administrator-level users on the Active Directory hosts.\n")
        f.write("\\subsection*{Cleaning House}\n")
        f.write("\\paragraph{}The final step of a penetration test is to clean up any interaction with the computer and remove all applications, settings, files, or other data that wasn't there before the tester's involvement. Ursa deleted all privilege escalation utilities on the computers and all temporary files in the users' home directories and the /tmp directory (C:/Users/Public on Windows machines).\n")
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


# More Utility Functions
def compileProject(stdscr):
    docHeader()
    examTitlePage()
    foreword()
    simpleContent()
    os.system(f"pdflatex -output-directory={projectdir}/writeup {projectdir}/writeup/writeup.tex")
    stdscr.clear()
    stdscr.addstr("Compiling Project to TeX.\n")
    stdscr.addstr("Press any key.")
    stdscr.refresh()
    key = stdscr.getch()
    if key in [curses.KEY_EXIT, 27]:
        printMenu(stdscr, 0)

def openReport(stdscr):
    os.system(f"zathura {projectdir}/writeup/writeup.pdf")
    stdscr.clear()
    stdscr.addstr("Opening Report.\n")
    stdscr.addstr("Press any key.")
    stdscr.refresh()
    stdscr.getch()


# Main UI Functions
def mainUI(stdscr):
    stdscr.clear()
    editor = curses.newwin(curses.LINES - 15, curses.COLS - 33, 0, 0)
    editor.box()
    editor.addstr(1, editor.getmaxyx()[1] // 2 - 1, "Notes", A_REVERSE)
    i = 3
    file = open(f"{projectdir}/walkthrough.txt","r")
    lines = file.read().splitlines()
    file.close()
    for line in lines:
        editor.addstr(i, 2, line)
        i += 1

    infrastructure = curses.newwin(21, 30, 0, curses.COLS - 30)
    accounts = curses.newwin(15, 30, curses.LINES - 30, curses.COLS - 30)

    findings = curses.newwin(14, curses.COLS // 3 - 1, curses.LINES - 14, 0)
    #reccomendations = curses.newwin(14, 30, curses.LINES - 14, 0)
    
    objectives = curses.newwin(14, curses.COLS // 3 - 2, curses.LINES - 14, curses.COLS // 3 + 1)
    task = curses.newwin(14, curses.COLS // 3 - 1, curses.LINES - 14, curses.COLS // 3 * 2 + 1)
    #tool = curses.newwin(14, curses.COLS // 3 - 1, curses.LINES - 14, curses.COLS // 3 * 2)

    objectives.box()
    task.box()
    #tool.box()
    findings.box()
    infrastructure.box()
    accounts.box()
    infrastructure.addstr(1, infrastructure.getmaxyx()[1] // 2 - 7, "Infrastructure", A_REVERSE)
    i = 3
    file = open(f"{projectdir}/infra.csv","r")
    lines = file.read().splitlines()
    file.close()
    for line in lines[1:]:
        infrastructure.addstr(i, 2, line.split(", ")[0] + " | " + line.split(", ")[1])
        infrastructure.addstr(i + 1, 2, line.split(", ")[2])
        i += 3

    accounts.addstr(1, accounts.getmaxyx()[1] // 2 - 4, "Accounts", A_REVERSE)
    i = 3
    file = open(f"{projectdir}/accounts.csv","r")
    lines = file.read().splitlines()
    file.close()
    for line in lines[1:]:
        accounts.addstr(i, 2, line.split(", ")[2] + ":" + line.split(", ")[3])
        accounts.addstr(i + 1, 2, line.split(", ")[1] + " -> " + line.split(", ")[0])
        i += 3
    findings.addstr(1, findings.getmaxyx()[1] // 2 - 5, "Findings", A_REVERSE)
    objectives.addstr(1, objectives.getmaxyx()[1] // 2 - 5, "Objectives", A_REVERSE)
    task.addstr(1, task.getmaxyx()[1] // 2 - 2, "Tasks", A_REVERSE)
    #tool.addstr(1, tool.getmaxyx()[1] // 2 - 2, "Tools", A_REVERSE)
    infrastructure.refresh()
    accounts.refresh()
    findings.refresh()
    objectives.refresh()
    task.refresh()
    #tool.refresh()
    editor.refresh()
    infrastructure.getch()


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
            elif current_row == 3:
                openReport(stdscr)
            elif current_row == len(menu) - 1:
                break
        printMenu(stdscr, current_row)
        curses.doupdate()


def main():
    wrapper(ui)

if __name__ == '__main__':
    main()
