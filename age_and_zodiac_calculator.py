## Testing previously learned skills
def calculate():
    return current_year - user_byear

user_byear = None
age = None
user_day = None
user_month = None
month_index = None
int_day = None
int_byear = None
current_year = 2024
yes_responses = ["yes", "y", "ye", "ya", "yep", "yeah", "yess", "ys", "yea"]
no_responses = ["no", "n", "nah", "nope", "nop", "na", "nuh"]
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_map = {
    "january": 0, "jan": 0,
    "february": 1, "feb": 1,
    "march": 2, "mar": 2,
    "april": 3, "apr": 3,
    "may": 4,
    "june": 5, "jun": 5,
    "july": 6, "jul": 6,
    "august": 7, "aug": 7,
    "september": 8, "sep": 8,
    "october": 9, "oct": 9,
    "november": 10, "nov": 10,
    "december": 11, "dec": 11
}

print("Hello, this is an age and zodiac calculator.")

while True:
    user_byear = input("What year you born? ")
  #  int_byear = int(user_byear)
    
    if user_byear.isdigit():
        user_byear = int(user_byear)
        int_byear = int(user_byear)
        
        if int_byear >= current_year:
            print("Nice try! Enter a real birth year.")
            continue

        elif int_byear in range(2019, current_year):
            print("No way you're that young!")
            continue
        elif int_byear in range(0, 1777):
            print("Ha! Yeah right!")
            continue
        
        else:
            age = calculate()
            print(f"You're {age} years old.")
        break
    else:
        print("Error: Please enter a valid year (numbers only).")

while True:
    user_decision = input("Do you want to know your Zodiac Sign? (Y)es or (N)o? ").lower()

    if user_decision in no_responses:
        print("Thanks for using this calculator!")
        print("Goodbye")
        break

    elif user_decision in yes_responses:
        break

    else:
        print("Error: (Y)es or (N)o")
        continue

while True:
    user_month = input("What month were you born? ").lower()
    if user_month not in month_map:
        print("Error: Invalid month. Please try again.")
        continue
    else:
        break

while True:
    try:
        user_day = input("What day were you born? ")
        int_day = int(user_day)  # Attempt to convert the input to an integer
        month_index = month_map[user_month]

        # Check if the day is valid for the given month
        if int_day < 1 or int_day > days_in_month[month_index]:
            print("Error: Invalid day for the given month. Please try again.")
            continue
    except ValueError:
        print("Error: Day must be a number.")  # This should trigger on invalid input
        continue
            
    
    if user_month in month_map:
        month_index = month_map[user_month]
        
    if (month_index == 0 and int_day <= 19) or (month_index == 11 and int_day >= 22):
        print(f"You're a {age} year old Capricorn")


    #if month_map[0] in user_month and int_day <= 19:
   #     print(f"You're a {age} year old Capricorn")


    else:
        print("Not implemented yet! Sorry!")
        

    break