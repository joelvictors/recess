# Given tuple
phones = ("samsung", "iphone", "tecno", "redmi")

# 1. Output favorite phone brand
print(phones[0])

# 2. Print 2nd last item
print(phones[-2])

# 3. Change iphone to itel
temp = list(phones)
temp[1] = "itel"
phones = tuple(temp)
print(phones)

# 4. Add Huawei
temp = list(phones)
temp.append("Huawei")
phones = tuple(temp)
print(phones)

# 5. Loop through tuple
for phone in phones:
    print(phone)

# 6. Delete first item
temp = list(phones)
temp.pop(0)
phones = tuple(temp)
print(phones)

# 7. Tuple of Ugandan cities
cities = tuple(["Kampala", "Jinja", "Mbarara", "Gulu"])
print(cities)

# 8. Unpack tuple
city1, city2, city3, city4 = cities
print(city1, city2, city3, city4)

# 9. Print 2nd, 3rd and 4th cities
print(cities[1:4])

# 10. Join two tuples
first = ("Joel",)
second = ("Victors",)
joined = first + second
print(joined)

# 11. Multiply colors tuple
colors = ("red", "blue", "green")
print(colors * 3)

# 12. Count number of times 8 appears
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))