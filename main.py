import re

expression = input("podaj wzór funkcji kwadratowej:\nf(x) = ")

expression_regex = re.compile(r"(-?\d+)?(x|\(x\s*[\+\-]\s*\d+\))(\^2|²)\s*([\+\-]\s*\d+)?")

while not expression_regex.match(expression):
    message = "Wzrór funckji jest nieprawidłowy skorzystaj z jednego z podanych wzorów np.:"
    print('\033[31m')
    print(" Błąd ".center(len(message), "-"))
    print(message)
    print("-3(x + 4)^2 + 5")
    print("2x² - 4")
    print('\033[0m')


    expression = input("podaj wzór funkcji kwadratowej:\nf(x) = ")

matched_regex = expression_regex.match(expression)
print(matched_regex.groups())
