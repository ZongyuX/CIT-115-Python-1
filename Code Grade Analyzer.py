
# Get student name
strName = str(input("Name of person that we are calculating the grades for: "))

# Get test scores with validation
iTest1 = 0
while iTest1 <= 0:
    try:
        iTest1 = int(input("Test 1: "))
    except ValueError:
        print("Input must be a numeric value")

iTest2 = 0
while iTest2 <= 0:
    try:
        iTest2 = int(input("Test 2: "))
    except ValueError:
        print("Input must be a numeric value")

iTest3 = 0
while iTest3 <= 0:
    try:
        iTest3 = int(input("Test 3: "))
    except ValueError:
        print("Input must be a numeric value")

iTest4 = 0
while iTest4 <= 0:
    try:
        iTest4 = int(input("Test 4: "))
    except ValueError:
        print("Input must be a numeric value")

# Get drop lowest option with validation
strDropLowest = ""
while strDropLowest not in ['Y', 'N']:
    strDropLowest = input("Do you wish to Drop the Lowest Grade Y or N? ").upper()
    if strDropLowest not in ['Y', 'N']:
        print("Enter Y or N to Drop the Lowest Grade.")

# Calculate average
if strDropLowest == 'Y':
    # Find lowest score without using min() or lists
    iLowest = iTest1
    if iTest2 < iLowest:
        iLowest = iTest2
    if iTest3 < iLowest:
        iLowest = iTest3
    if iTest4 < iLowest:
        iLowest = iTest4
    
    # Calculate average of other three tests
    fAverage = float((iTest1 + iTest2 + iTest3 + iTest4 - iLowest) / 3)
else:
    # Calculate average of all four tests
    fAverage = float((iTest1 + iTest2 + iTest3 + iTest4) / 4)

# Determine letter grade
if fAverage >= 97.0:
    strGrade = "A+"
elif fAverage >= 94.0:
    strGrade = "A"
elif fAverage >= 90.0:
    strGrade = "A-"
elif fAverage >= 87.0:
    strGrade = "B+"
elif fAverage >= 84.0:
    strGrade = "B"
elif fAverage >= 80.0:
    strGrade = "B-"
elif fAverage >= 77.0:
    strGrade = "C+"
elif fAverage >= 74.0:
    strGrade = "C"
elif fAverage >= 70.0:
    strGrade = "C-"
elif fAverage >= 67.0:
    strGrade = "D+"
elif fAverage >= 64.0:
    strGrade = "D"
elif fAverage >= 60.0:
    strGrade = "D-"
else:
    strGrade = "F"

# Output results
print(f"{strName} test average is: {format(fAverage, '0.1f')}")
print(f"Letter Grade for the test is: {strGrade}")
