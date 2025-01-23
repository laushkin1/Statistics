import re
import matplotlib.pyplot as plt
from datetime import datetime

# Symbols that should be in a line
symbol_map = {
    1: "\U0001F4BB",  # 💻 - Programming
    2: "\U0001F4DA",  # 📚 - Studying
    3: "\U0001F4F1"   # 📱 - Procrastinating
}

# Functions for line check 
def check_symbols(line: str) -> int:
    for key, symbol in symbol_map.items():
        if symbol in line:
            return key
    return 0

def check_x(line: str) -> bool:
    if re.search(r'\[x\]', line):
        return True
    return False

def check_time(line: str) -> float:
    time_match = re.search(r'\b(\d{1,2}:\d{2})-(\d{1,2}:\d{2})\b', line)
    if time_match:
        if datetime.strptime(time_match.group(1), "%H:%M") < datetime.strptime(time_match.group(2), "%H:%M"):
            total_hour = (datetime.strptime(time_match.group(2), "%H:%M") - datetime.strptime(time_match.group(1), "%H:%M")).total_seconds() / 3600
            return total_hour
    return 0.0

def check_date(line: str) -> bool:
    return bool(re.search(r'\b\d{2}.\d{2}.\d{4}\b', line))

def check_line(line: str) -> bool:
    if check_x(line) and check_time(line):
        return True
    return False


# Percentage for each entry
programing_percent = 0
studying_percent = 0
procrastinating_percent = 0
else_percent = 0

with open('file.txt') as file:
    for line in file:
        if check_date(line):
            print()
            print(line, end="")
        if check_line(line):
            print(line, end="")
            percent = check_symbols(line)
            if percent == 1:
                programing_percent += check_time(line)
            elif percent == 2:
                studying_percent += check_time(line)
            elif percent == 3:
                procrastinating_percent += check_time(line)
            else:
                else_percent += check_time(line)
print('\n')


# Create a diagram
labels = ['Programming', 'Studying', 'Procrastinating', 'Else']
sizes = [programing_percent, studying_percent, procrastinating_percent, else_percent]
colors = ['#0087ff', '#54f10f', '#f10f0f', '#f2eb17']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'black'})
plt.title('Statistics of life')
plt.show()

