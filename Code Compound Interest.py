# Prompt the user for input
sPrincipal = float(input("Enter the starting principal: "))
sAnnual_rate = float(input("Enter the annual interest rate: "))
sCompounding = int(input("How many times per year is the interest compounded? "))
sYears = float(input("For how many years will the account earn interest? "))

# Convert the annual interest rate from percentage and calculate
sRate = sAnnual_rate / 100  

# Calculate the future value using compound interest formula
sFuture_value = sPrincipal * (1 + sRate / sCompounding) ** (sCompounding * sYears)

# Output the result with proper formatting
print(f"At the end of {int(sYears)} years, you will have ${sFuture_value:,.2f}")
