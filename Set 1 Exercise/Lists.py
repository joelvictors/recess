# 1. Create a list and output the 2nd item
names = ["Joel", "Sarah", "Peter", "Mary", "John"]
print(names[1])

# 2. Change the first item
names[0] = "Victor"
print(names)

# 3. Add a sixth item
names.append("Grace")
print(names)

# 4. Add Bathel as the 3rd item
names.insert(2, "Bathel")
print(names)

# 5. Remove the 4th item
names.pop(3)
print(names)

# 6. Print the last item using negative indexing
print(names[-1])

# 7. New list with 7 items and print 3rd, 4th, 5th items
items = ["A", "B", "C", "D", "E", "F", "G"]
print(items[2:5])

# 8. Copy a list of countries
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda"]
countries_copy = countries.copy()
print(countries_copy)

# 9. Loop through countries
for country in countries:
    print(country)

# 10. Sort animals ascending and descending
animals = ["zebra", "lion", "cat", "elephant", "antelope"]
animals.sort()
print("Ascending:", animals)

animals.sort(reverse=True)
print("Descending:", animals)

# 11. Print animals containing letter a
for animal in animals:
    if "a" in animal:
        print(animal)

# 12. Join two lists
first_names = ["Joel"]
second_names = ["Alinda"]
full_names = first_names + second_names
print(full_names)