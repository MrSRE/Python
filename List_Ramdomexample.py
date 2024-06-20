# List 
# create a list of number
numbers = [1,2,3,4,5]

# Access and Modify elements
print(numbers[0]) # output: 1
numbers[2] = 10
print(numbers) # output : [1,2,10,4,5]

# Add elements to list
numbers.append(6)
print(numbers) # Output : [1,2,10,4,5,6]

# Remove elements from the list
numbers.remove(2)
print(numbers) # Output: [1,10,4,5,6]

#Iterate over the list
for num in numbers:
    print(num)

