class Bludistaci:
    # def __init__(self, slovnik:dict[str, int]):  #? konstruktor, který ještě nechci používat
    #     self._bludistaci = slovnik

    _bludistaci = {
        "Božetěch": 1,
        "Želmíra": 3,
        "Andělín": 2,
        "Hvězdoslava": 1
    }

    def _existuje_student(self, student:str) -> str | None:
        if student.capitalize() in self._bludistaci.keys():
            return student.capitalize()
        else:
            return None
        

    def _sklonuj(self, student:str, pocet:int):
        tvar = ""
        if pocet == 1:
            tvar = "bludišťáka"
        elif pocet < 5 and pocet != 0:
            tvar = "bludišťáky"
        else:
            tvar = "bludišťáků"
        print(f"{student} má {pocet} {tvar}!")


    def pocet_student(self):
        student = input("Koho chceš zkontrolovat? ")
        student = self._existuje_student(student)
        if not student:
            print("Student neexistuje.")
            return
        pocet = self._bludistaci[student]
        self._sklonuj(student, pocet)

    def vypis_vsechny(self):
        for student, pocet in self._bludistaci.items():
            print(student, pocet)

    def pridej_bludistaka(self):
        student = input("Komu chceš přidat bludišťáka? ")
        student = self._existuje_student(student)
        if not student:
            print("Student neexistuje.")
            return
        self._bludistaci[student] += 1 #přidá 1 ke stávající hodnotě
        pocet = self._bludistaci[student]
        self._sklonuj(student, pocet)

    def odeber_bludistaka(self):
        student = input("Komu chceš přidat bludišťáka? ")
        student = self._existuje_student(student)
        if not student:
            print("Student neexistuje.")
            return
        self._bludistaci[student] -= 1 #odebere 1 od stávající hodnoty
        pocet = self._bludistaci[student]
        self._sklonuj(student, pocet)

    def pridej_studenta(self):
        student = input("Koho chceš přidat? ").capitalize()
        existuje = self._existuje_student(student)
        if existuje:
            print("Student již existuje")
            return
        self._bludistaci[student] = 1 
        self._sklonuj(student, 1)

    def nejvyssi_pocet(self):
        best_pocet = -1
        best_student = None
        for student, pocet in self._bludistaci.items():
            if pocet > best_pocet:
                best_pocet = pocet
                best_student = student
        self._sklonuj(best_student, best_pocet)

b = Bludistaci() #volám funkci kOnStRuKtOrU
