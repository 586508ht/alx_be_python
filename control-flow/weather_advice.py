# weather_advice.py

def main():
    # Prompt the user for the current weather condition
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

    # Provide clothing recommendations based on the weather input
    if weather == "sunny":
        message = ("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        message = ("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        message = ("Make sure to wear a warm coat and a scarf.")
    else:
        message = ("Sorry, I don't have recommendations for this weather.")

    print (message)

# Run the main function
if __name__ == "__main__":
    main()
