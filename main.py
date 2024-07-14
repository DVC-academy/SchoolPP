def get_min(numbers): 
  min = numbers[0]
  for num in numbers:
    if num < min:
      min = num
  return min

# Példa használat
numbers = [1, 2, 3, 4, 5]
min = get_min(numbers)
print(f"A legkisebb szám a listában: {min}")  # Kiírja: A legkisebb szám a listában: 1