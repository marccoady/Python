fruit = ["apples","oranges","bananas"]
print(fruit[1])

# len(fruit)

print(fruit[-1])

print(fruit[-2])

fruit.append("kiwi")
print(fruit)

fruit.insert(2, "passion fruit")
print(fruit)

print(sorted(fruit))

print(fruit)

fruit.sort()

print(fruit)

fruit.reverse()
print(fruit)

del fruit[1]
print(fruit)

favorite_fruit = fruit.pop()
print(favorite_fruit)

fresh_fruit = fruit.pop(1)
print(fresh_fruit)

fruit.remove('bananas')
print(fruit)