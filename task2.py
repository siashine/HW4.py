# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def Factor(n):
  Mas = []
  d = 2
  while d * d <= n:
    if n % d == 0:
      Mas.append(d)
      n //= d
    else:
      d += 1
  if n > 1:
    Mas.append(n)
  return Mas
print(Factor(int(input("Введите число: "))))
