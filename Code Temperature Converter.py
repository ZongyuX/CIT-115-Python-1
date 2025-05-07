# Zongyu Xie's Temperature Converter

# Named Constants
fFAHRENHEIT_MAX = 212.0
fCELSIUS_MAX = 100.0
fFAHRENHEIT_FACTOR = 9.0/5.0
fCELSIUS_FACTOR = 5.0/9.0

# Get temperature input
print("Zongyu Xie's Temp Converter:")
fTemp = float(input("Enter a temperature: "))
sScale = input("Is the temp F for Fahrenheit or C for Celsius? ").upper()

# Validate input
if sScale not in ('F', 'C'):
    print("You must enter a F or C")
    raise SystemExit

# Calculate conversion
if sScale == 'F':
    if fTemp > fFAHRENHEIT_MAX:
        print("Temp can not be > 212")
        raise SystemExit
    fConvertedTemp = fCELSIUS_FACTOR * (fTemp - 32)
    sOutputMessage = "The Celsius equivalent is: ".format(fConvertedTemp)
else:
    if fTemp > fCELSIUS_MAX:
        print("Temp can not be > 100")
        raise SystemExit
    fConvertedTemp = (fFAHRENHEIT_FACTOR * fTemp) + 32
    sOutputMessage = "The Fahrenheit equivalent is: ".format(fConvertedTemp)

# Output result
print("The Fahrenheit equivalent is: ", format(fConvertedTemp,",.1f"))
