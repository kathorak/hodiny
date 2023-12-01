def main():

    bludistaci = {
    "Jakub": 3,
    "Vašek": 2,
    "Ema": 2
}
    jmeno = input("Napiš jméno: ").capitalize() #převede první písmeno na velké, aby nedocházelo k chybám
    kolik_bludistaku(bludistaci, jmeno)

def kolik_bludistaku(seznam, jmeno):
    if(jmeno) in seznam:
            print(seznam[jmeno])

def pridej_jmeno(bludistaci, jmeno):
    jmeno = input("Napiš nové jméno: ").capitalize()
    bludistaci[jmeno] = 1

if __name__ == "__main__":
    main()