def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Input a number that is greater than 0.")
                continue
            return value
        except ValueError:
            print("Input a number that is greater than 0.")

def getMedian(sales_list):
    n = len(sales_list)
    if n == 0:
        return 0.0
    
    if n % 2 == 1:  # Odd number of elements
        return sales_list[n // 2]
    else:  # Even number of elements
        return (sales_list[n // 2 - 1] + sales_list[n // 2]) / 2

def main():
    sales = []
    
    # Data entry loop
    while True:
        price = getFloatInput("Enter property sales value: ")
        sales.append(price)
        
        # Ask if user wants to enter another value
        while True:
            another = input("Enter another value Y or N: ").upper()
            if another in ['Y', 'N']:
                break
            # No message needed per sample output
        if another == 'N':
            break
    
    # Process and display results
    if not sales:
        print("No sales data entered.")
        return
    
    sales.sort()
    
    # Display sorted properties
    for i, price in enumerate(sales, 1):
        print(f"Property {i} ${price:12,.2f}")
    
    # Calculate statistics
    minimum = min(sales)
    maximum = max(sales)
    total = sum(sales)
    average = total / len(sales)
    median = getMedian(sales)
    commission = total * 0.03
    
    # Display results
    print(f"Minimum:    ${minimum:12,.2f}")
    print(f"Maximum:    ${maximum:12,.2f}")
    print(f"Total:    ${total:12,.2f}")
    print(f"Average:    ${average:12,.2f}")
    print(f"Median:    ${median:12,.2f}")
    print(f"Commission: ${commission:12,.2f}")

# Call the main function directly
main()
