'''for i in range(int(input())):
    a = int(input())
    b = bin(a-1)[2:]
    if '111' in b:
        b = b[b.rfind('1')-2:]
        print(int(b, base=2))
    else:
        print(-1)'''


'''for i in range(int(input())):
    a = int(input())
    b = input()
    for j in range(0, a-a%2, 2):
        c1 = a[j]+a[j+1]
        c2 = a[j+2]+a[j+3]
        if c2 in c1 and len(c1)>len(c2):
            ans = 'no'
            break
        elif '''

'''m = []
s = 0
for i in range(4):
    m.append([int(el) for el in input().split()])
for i in range(4):
    s += (m[i][2] - m[i][0]) * (m[i][3] - m[i][1])'''

'''def calculate_area(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return width * height

def intersection_area(x1, y1, x2, y2, x3, y3, x4, y4):
    x_left = max(x1, x3)
    y_bottom = max(y1, y3)
    x_right = min(x2, x4)
    y_top = min(y2, y4)

    if (x_right < x_left) or (y_top < y_bottom):
        return 0
    else:
        return calculate_area(x_left, y_bottom, x_right, y_top)

ingredient1 = list(map(int, input().split()))
ingredient2 = list(map(int, input().split()))
ingredient3 = list(map(int, input().split()))
ingredient4 = list(map(int, input().split()))

# Находим координаты левого нижнего и правого верхнего угла области
x1 = min(ingredient1[0], ingredient2[0], ingredient3[0], ingredient4[0])
y1 = min(ingredient1[1], ingredient2[1], ingredient3[1], ingredient4[1])
x2 = max(ingredient1[2], ingredient2[2], ingredient3[2], ingredient4[2])
y2 = max(ingredient1[3], ingredient2[3], ingredient3[3], ingredient4[3])

total_area = calculate_area(x1, y1, x2, y2)

# Проверяем каждый ингредиент и пересекаем его с областью
total_area -= intersection_area(x1, y1, x2, y2, ingredient1[0], ingredient1[1], ingredient1[2], ingredient1[3])
total_area -= intersection_area(x1, y1, x2, y2, ingredient2[0], ingredient2[1], ingredient2[2], ingredient2[3])
total_area -= intersection_area(x1, y1, x2, y2, ingredient3[0], ingredient3[1], ingredient3[2], ingredient3[3])
total_area -= intersection_area(x1, y1, x2, y2, ingredient4[0], ingredient4[1], ingredient4[2], ingredient4[3])

print(total_area)'''


def calculate_charge(n, a, b, times):
    charge = 100.0
    minutes_in_day = 24 * 60

    for i in range(n):
        current_time = times[i].split(":")
        current_hour = int(current_time[0])
        current_minute = int(current_time[1])

    current_minute_of_day = current_hour * 60 + current_minute
    next_charge_minute = (current_minute_of_day + a) % minutes_in_day

    if current_minute_of_day <= next_charge_minute:
        charge -= (b - a) / minutes_in_day
    else:
        charge -= a / minutes_in_day
        charge += b / minutes_in_day

    return charge


n, a, b = map(int, input().split())
times = []
for i in range(n):
    times.append(input())

remaining_charge = calculate_charge(n, a, b, times)
print(remaining_charge)
