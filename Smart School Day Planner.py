#A Python program that asks the user three questions. It classifies the day using if-elif-else. It uses AND to check sunny weather and homework done together. It uses OR to check rainy or cloudy weather. It uses NOT to catch homework not done. It combines all three operators to print the best plan for the day.

weather = input("Weather (sunny,rainy or cloudy):")
homework = input("Is homework done (yes or no):")
weekend =  input("Is it weekend (yes or no):")

if weather == "sunny" and homework == "yes":
    print("Plan: Perfect day to go play outside(free time) :).")
elif weather == "rainy" or weather == "cloudy":
    print("Plan: Stay indoors and play video game or revise :).")
elif not homework == "yes":
    print("Plan: You must stay inside and continue finishing your homework :/.")