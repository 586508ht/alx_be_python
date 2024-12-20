# pattern_drawing.py

def main():
    try:
        # Prompt the user for the size of the pattern
        size = int(input("Enter the size of the pattern: "))

        if size <= 0:
            print("Please enter a positive integer.")
            return

        # Use nested loops to draw the pattern
        row = 0
        while row < size:
            for col in range(size):
                print("*", end="")
            print()  # Move to the next line after each row
            row += 1
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Run the main function
if __name__ == "__main__":
    main()
