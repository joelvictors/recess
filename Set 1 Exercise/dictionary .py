# Dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# 1. Print shoe size
print(Shoes["size"])

# 2. Change Nick to Adidas
Shoes["brand"] = "Adidas"
print(Shoes)

# 3. Add type:sneakers
Shoes["type"] = "sneakers"
print(Shoes)

# 4. Return keys
print(Shoes.keys())

# 5. Return values
print(Shoes.values())

# 6. Check if size exists
if "size" in Shoes:
    print("Key exists")

# 7. Loop through dictionary
for key, value in Shoes.items():
    print(key, value)

# 8. Remove color
Shoes.pop("color")
print(Shoes)

# 9. Empty dictionary
Shoes.clear()
print(Shoes)

# 10. Copy a dictionary
student = {
    "name": "Joel",
    "course": "Computer Science"
}

student_copy = student.copy()
print(student_copy)

# 11. Nested dictionaries
students = {
    "student1": {
        "name": "Joel",
        "age": 22
    },
    "student2": {
        "name": "Sarah",
        "age": 21
    }
}

print(students)