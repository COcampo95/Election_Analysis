print ("Hello World")

counties = ["Arapahoe", "Denver", "Jefferson"]
if counties [1] == "Denver": #The double equals sign, ==, is a comparison operator, or Boolean operator, which means "equal to."
    print (counties[1]) #Since the second item in the counties list, counties[1], is "equal to" 'Denver', the condition is met. "Denver" is printed to the terminal screen.


counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)

## using range for i in range(len(counties)): (newline)   print(counties[i])
