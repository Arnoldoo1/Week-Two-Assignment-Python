# Step 1: Create an empty list
my_list = []

# Step 2: Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert value 15 at the second position
my_list.insert(1, 15)

# Step 4: Extend the list with another list
my_list.extend([50, 60, 70])

# Step 5: Remove the last element
my_list.pop()

# Step 6: Sort the list in ascending order
my_list.sort()

# Step 7: Find and print the index of value 30
index_30 = my_list.index(30)
print(f"Sorted list: {my_list}")
print(f"Index of 30: {index_30}")
