from subprocess import call
from timeit import default_timer as timer

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def callFaster(s1, s2):
	call(["../fasterLev", s1, s2])


s1 = "efgh" * 15
s2 = "abcd" * 15

print("doing python")
starta = timer()
levenshtein(s1, s2)
enda = timer()

print("doing faster c++")
start = timer()
callFaster(s1, s2)
end = timer()


print("Python time:\t\t\t", (enda-starta))
print("c++ faster time:\t\t", (end-start))
