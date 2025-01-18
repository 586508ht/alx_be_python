# temp_conversion_tool.py

# Conversion factors stored in a dictionary
CONVERSION_FACTORS = {
    "FAHRENHEIT_TO_CELSIUS": 5 / 9,
    "CELSIUS_TO_FAHRENHEIT": 9 / 5,
}

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * CONVERSION_FACTORS["FAHRENHEIT_TO_CELSIUS"]

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CONVERSION_FACTORS["CELSIUS_TO_FAHRENHEIT"]) + 32

# Main function for user interaction
def main():
    try:
        # Prompt the user for a temperature input
        temperature = input("Enter the temperature to convert: ").strip()
        if not temperature.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temp_value = float(temperature)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted_temp = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted_temp:.2f}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted_temp:.2f}°F")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()