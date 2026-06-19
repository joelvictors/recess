# 1. Create beverages set
beverages = set(["Tea", "Coffee", "Juice"])
print(beverages)

# 2. Add two items
beverages.update(["Soda", "Water"])
print(beverages)

# 3. Check if microwave exists
mySet = {"oven", "kettle", "microwave", "refrigerator"}

if "microwave" in mySet:
    print("Present")

# 4. Remove kettle
mySet.remove("kettle")
print(mySet)

# 5. Loop through set
for item in mySet:
    print(item)

# 6. Add list elements to set
my_set = {"Pen", "Book", "Bag", "Desk"}
my_list = ["Phone", "Laptop"]

my_set.update(my_list)
print(my_set)

# 7. Join two sets
ages = {20, 25, 30}
names = {"Joel", "Sarah", "Peter"}

combined = ages.union(names)
print(combined)