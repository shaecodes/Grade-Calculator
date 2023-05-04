def main():
    while True:
        # Print the main menu
        print("===================================")
        print("   GRADE CALCULATOR  ")
        print("===================================")
        print("Welcome to the Grade Calculator.")
        print("Enter to continue. Select q to quit. ")
        print("===================================")

        # Get user input
        answer = input(">> ").lower()

        if (answer == "q"):
            # If the user selects 'q', quit the program
            print("Thanks for choosing Grade Calculator")
            break;
        else:
            # If the user presses any other key, start the calculation
            calculate()

def calculate():
    # Create empty lists to store grades and weights
    grade_values = []
    weight_list = []

    while True: 
        try: 
            # Get user input for grade and weight
            print("\n")
            grade = input("Enter grade: >> ")
            weight = input("Enter weight: >>")

            # Convert the inputs to integers
            grade = int(grade)
            weight = int(weight)

            # Validate the grade and weight inputs
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be between 0 and 100")
            if weight < 0 or weight > 100:
                raise ValueError("Weight must be between 0 and 100")

            # Add the grade and weight to the corresponding lists
            grade_values.append(grade)
            weight_list.append(weight)

            # Ask the user if they want to add more grades
            answer = input("Would you like to continue? Select q to quit: >> ").lower()
            if (answer == "q"):
                # If the user quits, check that the sum of weights is 100
                sum_of_weights = sum(weight_list)

                if (sum_of_weights != 100):
                    # If the sum of weights is not 100, display an error message and break out of the loop
                    print("===================================")
                    print("Sum of weights do not equal to 100%")
                    print("Please try again")
                    print("===================================")
                    print("\n")
                    break
        
                # Calculate the weighted average and print it to the console
                weighted_sum = sum([grade * weight for grade, weight in zip(grade_values, weight_list)])
                weighted_average = weighted_sum / sum_of_weights
                print("===================================")
                print(f"Your final weighted grade is {weighted_average}%")

                # Call the letter_grade function to print the corresponding letter grade
                letter_grade(weighted_average)
            else:
                # If the user wants to add more grades, continue the loop
                continue
        except ValueError:
            # If the user enters invalid input, display an error message and continue the loop
            print("Cannot convert to an integer. Try again")

def letter_grade(percentage):
    # Determine the letter grade based on the percentage range and print it to the console
    if percentage >= 90:
        grade_letter = 'A+'
    elif percentage >= 80:
        grade_letter = 'A'
    elif percentage >= 75:
        grade_letter = 'A-'
    elif percentage >= 70:
        grade_letter = 'B+'
    elif percentage >= 65:
        grade_letter = 'B'
    elif percentage >= 60:
        grade_letter = 'B-'
    elif percentage >= 55:
        grade_letter = 'C+'
    elif percentage >= 50:
        grade_letter = 'C'
    elif percentage >= 40:
        grade_letter = 'F1'
    elif percentage >= 30:
        grade_letter = 'F2'
    else:
        grade_letter = 'F3'
    
    # Print the letter grade to the console
    print(f'The grade letter for {percentage}% is {grade_letter}')
    print("===================================")
    

main()
