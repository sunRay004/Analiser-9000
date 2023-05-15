import re

with open("Text.txt", "r") as activeFile:
    all_lines = activeFile.readlines()

titles = []
sequences = []

for line in all_lines:
    if "." in line[0]:
        titles.append(line.rstrip("\n"))
        all_lines.remove(line)

for lines in all_lines:
    sequences.append(lines.rstrip("\n"))

print(titles)
print(sequences)