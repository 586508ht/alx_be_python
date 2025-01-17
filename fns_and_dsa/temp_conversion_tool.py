# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main user interaction
def main():
    try:
        # Get temperature and unit from the user
        temp_input = input("Enter the temperature (e.g., 32F or 0C): ").strip()
        if temp_input[-1].upper() == 'F':
            # Fahrenheit to Celsius
            temp_value = float(temp_input[:-1])
            converted_temp = convert_to_celsius(temp_value)
            print(f"{temp_value}F is equivalent to {converted_temp:.2f}C.")
        elif temp_input[-1].upper() == 'C':
            # Celsius to Fahrenheit
            temp_value = float(temp_input[:-1])
            converted_temp = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}C is equivalent to {converted_temp:.2f}F.")
        else:
            raise ValueError("Invalid temperature unit. Please end the input with 'C' or 'F'.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()