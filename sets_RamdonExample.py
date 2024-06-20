# Example

#create a set
fruits = {'apple','banana','orange'}

# Add elements to set
fruits.add('mango')
fruits.add('apple') # Duplicate value , Ignored

# Remove an element from set
fruits.remove('banana')

# check f an element exists in the set
print('apple' in fruits) # Output : True
print('grape' in fruits) # output: False

# Ierate over the set
for fruit in fruits:
    print(fruit)
    
# Perform set operations
set1 = {1,2,3}
set2 = {2,3,4}

union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)

# Display the results
print("Union:", union) # output: {1,2,3,4}
print("intersection:", intersection) # output: {2,3}
print("Difference:", difference) #Output: {1}