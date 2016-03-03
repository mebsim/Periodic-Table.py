choice = input("Welcome to the Valence Electrons Calculator. Please write the symbol of the element you want to find the number of valence electron for: ")
atomicn = 0
charge = 0
if choice == "H":
	element = "Hydrogen"
	atomicn = 1
if choice == "He":
	element = "Helium"
	atomicn = 2
if choice == "Li":
	element = "Lithium"
	atomicn = 3
if choice == "Be":
	element = "Berylium"
	atomicn = 4
if choice == "B":
	element = "Boron"
	atomicn = 5
if choice == "C":
	element = "Carbon"
	atomicn = 6
if choice == "N":
	element = "Nitrogen"
	atomicn = 7
if choice == "O":
	element = "Oxygen"
	atomicn = 8
if choice == "F":
    element = "Fluoride"
    atomicn = 9
if choice == "Ne":
    element = "Neon"
    atomicn = 10

anum = atomicn
if anum >= 2 & anum <=3:
        anum = anum - 2
if anum > 4:
        anum = 8 - anum

anum = anum * -1
charge = anum
print (atomicn)
print(element)
print(charge)
