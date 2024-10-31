# Function to find numbers divisible by both 3 and 5
def find_divisible_numbers(x):
    divisible_numbers = []  # List for divisible numbers

    for i in range(1, x + 1):  
        if i % 3 == 0 and i % 5 == 0:  # Check if divisible by 3 and 5
            divisible_numbers.append(i)  # Add number to the list

    return divisible_numbers

# Main program function
def main():
    x = int(input("Enter a number x: "))
    result = find_divisible_numbers(x)
    
    if result:  
        print("Numbers from 1 to", x, "that are divisible by both 3 and 5 are:", result)
    else:
        print("There are no numbers that are divisible by both 3 and 5.")

# Run main program
if __name__ == "__main__":
    main()

