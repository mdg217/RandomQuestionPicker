import numpy as np
import sys

_file = sys.argv[1]

file = open(_file, 'r')
questions = []
raw = file.readlines()
for line in raw:
    questions.append(line[0:len(line)-1])

_range = len(questions)

while questions is not None:
    if questions is None or _range == 0:
        print("Hai ripetuto tutto Complimenti")
        break
    print("-------------------------")
    index = np.random.randint(0, _range)
    input(questions[index])
    _range -= 1
    questions.remove(questions[index])

