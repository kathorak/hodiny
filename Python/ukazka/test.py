def postavy():
    for i in range(7):
        print("trpaslík")
    print("sněhurka")

# for x in range(5):
#    print("haf")


n = int(input())
for cislo in range(n+1):
    if cislo == 13:
        pass
    else:
        print(cislo)


odpoved = int(input("Kolik programátorů je potřeba na výměnu žárovky? "))

if odpoved == 0:
    print("Správně, žádný. Je to problém hardwaru.")
else:
    print("Špatně.")

