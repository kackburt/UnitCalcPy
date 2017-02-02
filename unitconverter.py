
#-*- coding: utf-8 -*-

# The unit converter:
print("Welcome to the unit converter!")
print("This application is designed to convert kilometers into miles.")
userinput = float(raw_input("Please enter a kilometer value: "))
kmtomiles = userinput * 0.621371
print("Your result: " + str(userinput) + " km equals " + str(kmtomiles) + " miles.")

nextcalc = str(raw_input("Do you want to convert again? (y/n): "))
while nextcalc == str("y"):
    userinput = float(raw_input("Please enter a kilometer value: "))
    kmtomiles = userinput * 0.621371
    print("Your result: " + str(userinput) + " km equals " + str(kmtomiles) + " miles.")
    nextcalc = str(raw_input("Do you want to convert again? (y/n): "))
else:
    print("Thank you for using the unit calculator! Goodbye!")