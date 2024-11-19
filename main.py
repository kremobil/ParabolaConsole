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
a = float(matched_regex.group(1))
horizontal_offset_regex = re.compile(r"\(x\s*([\+\-]\s*\d+)\)")

matched_horizontal_offset = horizontal_offset_regex.match(matched_regex.group(2))
if matched_horizontal_offset:
    p = float(matched_horizontal_offset.group(1).replace(' ', ''))
else:
    p = 0

if matched_regex.group(4):
    q = float(matched_regex.group(4).replace(' ', ''))
else:
    q = 0

print(f"p = {p}")
print(f"q = {q}")

print(f"y = {a}x² + {2*p*a}x + {p*p*a+q}")

