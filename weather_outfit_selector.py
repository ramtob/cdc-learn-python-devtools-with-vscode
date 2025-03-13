def weather_outfit_selector():
    print("Welcome to the Weather-Driven Outfit Selector!")

    while True:
        try:
            temperature = int(input("Enter the current temperature in Celsius: "))  
            break
        except ValueError:
            print("Invalid temperature. Please enter a valid number.")  

    while True:
        weather = input("Is it sunny, rainy, cloudy, or snowy today? ").lower()
        if weather in ['sunny', 'rainy', 'cloudy', 'snowy']:
            break
        else:       
            print("Invalid weather type. Please enter 'sunny', 'rainy', 'cloudy', or 'snowy'.")

    if temperature > 25 and weather == 'sunny':  
        outfit = "T-shirt and shorts"
    elif temperature <= 25 and weather == 'sunny':
        outfit = "Light jacket and jeans"
    elif temperature <= 15 and weather == 'rainy':
        outfit = "Raincoat and boots"
    elif temperature <= 5 and weather == 'snowy': 
        outfit = "Heavy winter coat and snow boots"
    else:
        outfit = "Heavy jacket and scarf"

    print(f"Suggested outfit: {outfit}")

    while True:
        preference = input("Do you prefer casual or formal? ").lower()
        if preference in ['casual', 'formal']:
            break
        else:
            print("Invalid preference. Please enter 'casual' or 'formal'.") 

    if preference == 'formal':
        outfit = outfit.replace("T-shirt", "Button-up shirt").replace("shorts", "Formal pants")

    print(f"Suggested outfit based on your preference: {outfit}")

weather_outfit_selector()
