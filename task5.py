# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


def parse_poly(_string):
    my_list = list(_string.split())
    for i in my_list:
        if "+" in my_list:
            my_list.remove("+")
        if "=" in my_list:
            my_list.remove("=")
    my_list.pop()
    return my_list


def readFromFile(_file):
    data = ""
    with open(_file) as rfile:
        data = rfile.read()
    return data


def dictToFile(mydict, file3):
    new_poly = ""
    for i in reversed(mydict.items()):
        if i[0] == 0:
            new_poly += str(i[1]) + " + "
        else:
            new_poly += str(i[1]) + "*x**" + str(i[0]) + " + "

    new_poly = new_poly[:-3]

    with open(file3, "w") as newfile:
        print(f"Записываем в файл {file3} новый полином: {new_poly}")
        newfile.write(new_poly)
    return

def makeDict(poly_list):
    poly_dict = {}
    poly_list.reverse()
    for item in poly_list:
        if item.isdigit():
            poly_dict[0] = int(item)
        else:
            poly_dict[int(item.split("**")[-1])] = int(item[0:item.find("*")])
    return poly_dict

def sum_dict(dict1, dict2):
    for key, value in dict1.items():
        dict1[key] = value + dict2.get(key, 0)
    return dict1

def main():
    poly1 = readFromFile("polynom1.txt")
    print("Полином 1:", poly1)
    poly2 = readFromFile("polynom2.txt")
    print("Полином 2:", poly2)

    print("Полином 1, преобразованный в список:", parse_poly(poly1))
    print("Полином 2, преобразованный в список:", parse_poly(poly2))

    poly_dict1 = makeDict(parse_poly(poly1))
    poly_dict2 = makeDict(parse_poly(poly2))


    print("Парсим сумму полиномов в словарь:", sum_dict(poly_dict1, poly_dict2))
    
    dictToFile(poly_dict1, "polynom3.txt")

if __name__ == "__main__":
  main()

