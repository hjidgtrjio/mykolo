num1 = int(input("Napiste cislo 1: "))
num2 = int(input("Napiste cislo 2: "))
num3 = int(input("Napiste cislo 3: "))
#nacteni od uzivatele jsou "Napiste cislo"
# int je pretypovani, kde se string meni na intiger
if (num1 ==10 or num1 == 20):
    print("Ahoj")
elif 20 < num2 < 50:
    print("Privet")
elif 50 < num3 < 100:
    print ("Halo")
else:
    print("Napiste cislo od 0 do 50")
# 3 podminky jsou if, elif, else
#print je "vypsat"

#prikazy pro git
#git add
# git commit -m "zprava"
# git push