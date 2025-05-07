import math

def main():
    """
    Main function that orchestrates the paint job cost estimation program.
    Handles all user input, calculations, and output display/file creation.
    """
    try:
        # Get all required float inputs using getFloatInput function
        fSquareFeet = getFloatInput("Enter wall space in square feet: ")
        fPaintPrice = getFloatInput("Enter paint price per gallon: ")
        fFeetPerGallon = getFloatInput("Enter feet per gallon: ")
        fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
        fLaborChargePerHour = getFloatInput("Labor charge per hour: ")
        
        # Get state and customer last name
        sState = input("State job is in: ")
        sLastName = input("Customer Last Name: ")
        
        # Perform all calculations using separate functions
        iGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
        fLaborHours = getLaborHours(fLaborHoursPerGallon, iGallons)
        fLaborCharges = getLaborCost(fLaborHours, fLaborChargePerHour)
        fPaintCharges = getPaintCost(iGallons, fPaintPrice)
        fTaxRate = getSalesTax(sState)
        fTax = (fPaintCharges + fLaborCharges) * fTaxRate
        fTotalCost = fPaintCharges + fLaborCharges + fTax
        
        # Display results and create output file
        showCostEstimate(sLastName, iGallons, fLaborHours, fPaintCharges, 
                        fLaborCharges, fTax, fTotalCost)
        
    except Exception as err:
        print("An error occurred: " + str(err))

def getFloatInput(sPrompt):
    """
    Gets and validates a positive float input from the user.
    Continues prompting until valid input is received.
    """
    while True:
        try:
            sInput = input(sPrompt)
            fValue = float(sInput)
            
            if fValue <= 0:
                print("Error: Value must be positive and non-zero. Please try again.")
                continue
                
            return fValue
            
        except ValueError:
            print("Error: Please enter a valid number. Try again.")

def getGallonsOfPaint(fSquareFeet, fFeetPerGallon):
    """
    Calculates gallons of paint needed, rounded up to nearest whole gallon.
    """
    return math.ceil(fSquareFeet / fFeetPerGallon)

def getLaborHours(fLaborHoursPerGallon, iGallons):
    """
    Calculates total labor hours required for the job.
    """
    return fLaborHoursPerGallon * iGallons

def getLaborCost(fLaborHours, fLaborChargePerHour):
    """
    Calculates total labor cost for the paint job.
    """
    return fLaborHours * fLaborChargePerHour

def getPaintCost(iGallons, fPaintPrice):
    """
    Calculates total paint cost for the job.
    """
    return iGallons * fPaintPrice

def getSalesTax(sState):
    """
    Determines sales tax rate based on state.
    """
    sState = sState.upper()
    
    if sState == "CT":
        return 0.06
    elif sState == "MA":
        return 0.0625
    elif sState == "ME":
        return 0.085
    elif sState == "NH":
        return 0.0
    elif sState == "RI":
        return 0.07
    elif sState == "VT":
        return 0.06
    else:
        return 0.0

def showCostEstimate(sLastName, iGallons, fLaborHours, fPaintCharges, 
                    fLaborCharges, fTax, fTotalCost):
    """
    Displays the cost estimate to screen and saves to a file.
    """
    # Display results to screen
    print("\nGallons of paint: ", iGallons)
    print("Hours of labor: ", f"{fLaborHours:.1f}")
    print("Paint charges: $", f"{fPaintCharges:.2f}")
    print("Labor charges: $", f"{fLaborCharges:,.2f}")
    print("Tax: $", f"{fTax:,.2f}")
    print("Total cost: $", f"{fTotalCost:,.2f}")
    
    # Create output filename
    sFilename = f"{sLastName}_PaintJobOutput.txt"
    
    # Write results to file
    try:
        with open(sFilename, 'w') as fileOutput:
            fileOutput.write(f"Gallons of paint: {iGallons}\n")
            fileOutput.write(f"Hours of labor: {fLaborHours:.1f}\n")
            fileOutput.write(f"Paint charges: ${fPaintCharges:.2f}\n")
            fileOutput.write(f"Labor charges: ${fLaborCharges:,.2f}\n")
            fileOutput.write(f"Tax: ${fTax:,.2f}\n")
            fileOutput.write(f"Total cost: ${fTotalCost:,.2f}\n")
        
        print(f"File: {sFilename} was created.")
        
    except IOError as err:
        print(f"Error creating file: {err}")

# Program starts here
main()
