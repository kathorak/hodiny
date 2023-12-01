with open("H:\\Python\\ukazka\\ukladani\\data.txt", "r") as file:
    print(file.read())
#abych nezapomínala zavírat soubor používám tuhle syntax

#"r" = čtení, "w" = přepisování, "a" = připisování

with open("H:\\Python\\ukazka\\ukladani\\data.txt", "a") as file:
    file.write("\nBye")
