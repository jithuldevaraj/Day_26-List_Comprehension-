# numbers = [1,2,3,4]
# new_numbers = [n+5 for n in numbers if n > 1]
# print(new_numbers)
import csv

#---------------------------------------------------------------------------------------------------------------------#

# name = "Jithu"
# new_name =[letter for letter in name]
# print(new_name)

#---------------------------------------------------------------------------------------------------------------------#

# new_num = [num * 2 for num in range(1,5)]
# print(new_num)

#---------------------------------------------------------------------------------------------------------------------#

user_preferences = {
    "hobbies": [],
    "favorite_foods": []
}

# Later in the code...
user_preferences["hobbies"].append("coding")
user_preferences["favorite_foods"].extend(["pizza", "tacos"])

print(user_preferences)
# Output: {'hobbies': ['coding'], 'favorite_foods': ['pizza', 'tacos']}

#---------------------------------------------------------------------------------------------------------------------#

# 1. Filtering (Passing students only)
passed_students = {name: score for (name, score) in student_scores.items() if score >= 60}
# Output: {'Alice': 85, 'Charlie': 92, 'Diana': 74, 'Fiona': 88}

# 2. Modifying Values (Applying a $50 discount)
discounted_prices = {item: (price - 50) for (item, price) in product_prices_usd.items()}
# Output: {'laptop': 1150.0, 'smartphone': 750.0, 'headphones': 100.0, 'monitor': 250.0, 'mouse': -25.0}


#---------------------------------------------------------------------------------------------------------------------#