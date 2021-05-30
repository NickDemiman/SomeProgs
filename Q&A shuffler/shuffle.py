from random import shuffle,seed

# answers
file = open("src/answers.md","r",errors="ignore")

lines = file.readlines()
file.close()

new_lines = []

# отсеиваем пустые строки
for line in lines:
    if line != "\n":
        new_lines.append(line)

# перемешиваем список
seed()
shuffle(new_lines)

# записываем результат в новый файл
file = open("new/new_answers.md","w")
for line in new_lines:
    file.write(line)
    file.write("\n")

file.close()

#questions
file = open("src/questions.md", "r", errors="ignore")

lines = file.readlines()
file.close()

new_lines = []

# отсеиваем пустые строки
for line in lines:
    if line != "\n":
        new_lines.append(" ".join(line.split()[2:]))

# перемешиваем список
seed()
shuffle(new_lines)

file = open("new/new_questions.md","w")
for line in new_lines:
    file.write(line)
    file.write("\n\n")

file.close()