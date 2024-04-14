#!/usr/bin/env python3


from pathlib import Path
import datetime

import settings


projectdir = f"/tmp/{settings.project}"


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


def initConfig(project: str):
    docs = {"NDA": False, "SOW": False, "ROE": False, "Approval": False, "3rd Party": False, "Other": False}
    engagement_type = {"Black Box": False, "White Box": False, "Grey Box": False}
    engagement_scope = {"Physical": False, "Remote": False, "Full-spec": False, "Wireless": False, "Web": False, "App": False, "SocEng": False, "Rogue": False, "Inside": False, "DoS": False}
    timeline = {"from": datetime.date.today(), "to": (datetime.date.today() + datetime.timedelta(days=7)), "Status Updates": {"Daily": False, "Weekly": False, "Monthly": False, "Quarterly": False}}

    with open(f"{projectdir}/config","w") as file:
        file.write(f"tester: {settings.tester}\r\n")
        file.write(f"docs: {docs}\r\n")
        file.write(f"type: {engagement_type}\r\n")
        file.write(f"scope: {engagement_scope}\r\n")
        file.write(f"timeline: {timeline}\r\n")


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

    initConfig(project)
    initAccounts()
    initInfrastructure()
    initObjectives()
    initFindings()
    initTasks()
    initTools()
    initRecommendations()

    with open(f"{projectdir}/walkthrough.txt","w") as file:
        file.write(f"{settings.project}\r\n")
        file.write(f"{settings.tester}\r\n")
        file.write("----------\r\n")
        file.write("Scanning\r\n\r\n")
        file.write("Enumeration\r\n\r\n")
        file.write("Exploitation\r\n\r\n")
        file.write("Privilege Escalation\r\n\r\n")
        file.write("Cleaning House\r\n\r\n")
        file.write("Fin")

