boxVolume = float(input("Enter Box Volume in Meters:"))
sugarVolume = int(input("Enter Sugar Volume in cm :"))

cubesFit = boxVolume*1e6//sugarVolume
spaceLeft = boxVolume%sugarVolume

print("You can fit:",cubesFit,"sugar cubes","\nWith", spaceLeft, "cm^3 left over" )
