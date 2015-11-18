f = open("geneSequence.txt", "r")

sequence = f.read()

print(sequence)

gc = 0

for i in sequence:
    if i == "G" or i == "C":
        gc += 1

gcContent = gc/len(sequence) * 100

print("GC content = " + str(gcContent)[0:5] + "%")
