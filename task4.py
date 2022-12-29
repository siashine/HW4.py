# Задана натуральная степень k. Сформировать 
# случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint

k = 2

def generate_polystring(n):
  generated_poly = ""
  for i in range(n, -1, -1):
    rnd = randint(0,100)
    if rnd != 0:
        if len(generated_poly) > 1:
            generated_poly += " + "
        if i == 0:
            generated_poly += str(rnd)
        else:
            generated_poly += str(rnd) + "*x**" + str(i)
  generated_poly += " = 0"
  return generated_poly

def main():
  polynom = generate_polystring(k)
  print("Случайный многочлен:", polynom)
  with open("polynom.txt", "w") as file1:
    file1.write(polynom)

if __name__ == "__main__":
  main()