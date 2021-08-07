print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))
x_diff = x2 - x1
y_diff = y2 - y1
b = (x1 * y2 - x2 * y1)


print("\nУравнение прямой, проходящей через эти точку:")
if x_diff == 0:
    print('Прямая параллельна оси Y x = ', x1)
elif y_diff == 0:
    print('Прямая параллельна оси X y = ', y1)
elif b > 0:
    print("y =", y_diff / x_diff, " *  x -", b / x_diff)
else:
    print("y =", y_diff / x_diff, " *  x +", abs(b / x_diff))
