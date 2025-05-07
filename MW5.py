
def main():
    # Initialize variables with Hungarian notation
    fOriginalDeposit = 0.0
    fInterestRate = 0.0
    iNumMonths = 0
    fGoalAmount = 0.0
    
    # Get original deposit with validation
    while True:
        try:
            sInput = input("What is the Original Deposit (positive value): ")
            fOriginalDeposit = float(sInput)
            if fOriginalDeposit <= 0:
                print("Input must a positive numeric value")
                continue
            break
        except ValueError:
            print("Input must a positive numeric value")
    
    # Get interest rate with validation
    while True:
        try:
            sInput = input("What is the Interest Rate (positive value): ")
            fInterestRate = float(sInput)
            if fInterestRate <= 0:
                print("Input must a positive numeric value")
                continue
            break
        except ValueError:
            print("Input must a positive numeric value")
    
    # Get number of months with validation
    while True:
        try:
            sInput = input("What is the Number of Months (positive value): ")
            iNumMonths = int(sInput)
            if iNumMonths <= 0:
                print("Input must a positive numeric value")
                continue
            break
        except ValueError:
            print("Input must a positive numeric value")
    
    # Get goal amount with validation
    while True:
        try:
            sInput = input("What is the Goal Amount (can enter 0 but not negative)): ")
            fGoalAmount = float(sInput)
            if fGoalAmount < 0:
                print("Input must 0 or greater")
                continue
            break
        except ValueError:
            print("Input must 0 or greater")
    
    # Convert annual interest rate to monthly decimal rate
    fMonthlyRate = (fInterestRate / 100) / 12
    
    # Initialize account balance with original deposit
    fAccountBalance = fOriginalDeposit
    
    # Loop to show monthly compounding for the specified number of months
    print("\nMonthly compounding results:")
    for iMonth in range(1, iNumMonths + 1):
        fInterest = fAccountBalance * fMonthlyRate
        fAccountBalance += fInterest
        print(f"Month: {iMonth} Account Balance is: $ {fAccountBalance:,.2f}")
    
    # Calculate how many months needed to reach goal (if goal > 0)
    if fGoalAmount > 0:
        fAccountBalance = fOriginalDeposit
        iMonthsToGoal = 0
        
        while fAccountBalance < fGoalAmount:
            fInterest = fAccountBalance * fMonthlyRate
            fAccountBalance += fInterest
            iMonthsToGoal += 1
        
        print(f"\nIt will take: {iMonthsToGoal:,} months to reach the goal of $ {fGoalAmount:,.2f}")

if __name__ == "__main__":
    main()
