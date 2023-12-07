def main():
    bludistaci = {
        "Božetěch": 1,
        "Želmíra": 3,
        "Andělín": 2,
        "Hvězdoslava": 1
        }

def _existuje_student(bludistaci, student:str) -> str | None:
    if student.capitalize() in bludistaci.keys():
        return student.capitalize()
    else:
        return None
        
def _sklonuj(student:str, pocet:int):
    tvar = ""
    if pocet == 1:
        tvar = "bludišťáka"
    elif pocet < 5 and pocet != 0:
        tvar = "bludišťáky"
    else:
        tvar = "bludišťáků"
    print(f"{student} má {pocet} {tvar}!")

def pocet_student(bludistaci):
        student = input("Koho chceš zkontrolovat? ")
        student = _existuje_student(student)
        if not student:
            print("Student neexistuje.")
            return
        pocet = bludistaci[student]
        _sklonuj(student, pocet)

def vypis_vsechny(bludistaci):
    for student, pocet in bludistaci.items():
        print(student, pocet)

def pridej_bludistaka(bludistaci):
    student = input("Komu chceš přidat bludišťáka? ")
    student = _existuje_student(student)
    if not student:
        print("Student neexistuje.")
        return
    bludistaci[student] += 1 
    pocet = bludistaci[student]
    _sklonuj(student, pocet)

def odeber_bludistaka(bludistaci):
    student = input("Komu chceš přidat bludišťáka? ")
    student = _existuje_student(student)
    if not student:
        print("Student neexistuje.")
        return
    bludistaci[student] -= 1
    pocet = bludistaci[student]
    _sklonuj(student, pocet)

def pridej_studenta(bludistaci):
    student = input("Koho chceš přidat? ").capitalize()
    existuje = _existuje_student(student)
    if existuje:
        print("Student již existuje")
        return
    bludistaci[student] = 1 
    _sklonuj(student, 1)

def nejvyssi_pocet(bludistaci):
    best_pocet = -1
    best_student = None
    for student, pocet in bludistaci.items():
        if pocet > best_pocet:
            best_pocet = pocet
            best_student = student
    _sklonuj(best_student, best_pocet)

nejvyssi_pocet()
