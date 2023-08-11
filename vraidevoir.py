nonb = input("Antre yon nonb komanse nan 1 rive nan 10: ")

while True:
    nonb = int( input("Tanpri, tape yon nonb :"))
    for i in range(1,11):
        print(i,"x",nonb,"=",i*nonb)

    repons = input("eske ou vle jenere yon lot tab si wi tape w ou sinon tape n :")
    if repons == "w" :
        continue
    elif repons == "n":
        break
    else:
        print("erreur")
