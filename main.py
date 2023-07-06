# На шахматной доске 8х8 расположены три фигуры: слон, ладья и конь.
# Требуется определить количество пустых полей доски, которые находятся под боем.
# Для простоты будем полагать, что фигуры могут «бить» через другие фигуры.

#
# В единственной строке входного файла INPUT.TXT записаны через пробел координаты расположения трех фигур:
# ферзя, ладьи и коня соответственно.
# Каждая координата состоит из одного английского символа (от A до H) и одной цифры (от 1 до 8).

import random
import math

cells=[]
for i in range(1,9):
    for j in range(1,9):
        cells.append([j, i])
while True:
    bishop_place = random.choice(cells)
    rook_place = random.choice(cells)
    knight_place = random.choice(cells)
    a = {f'{bishop_place[0]}{bishop_place[1]}', f'{rook_place[0]}{rook_place[1]}', f'{knight_place[0]}{knight_place[1]}'}
    if len(a) == 3:
        break

impact =[]

for j in range(1,9):
    impact.append([j, rook_place[1]])
for i in range(1,9):
    impact.append([rook_place[0], i])
    if 0 < bishop_place[0] + int(math.fabs(bishop_place[1] - i)) < 9:
        impact.append([bishop_place[0] + int(math.fabs(bishop_place[1] - i)), i])
    if 0 < bishop_place[0] - int(math.fabs(bishop_place[1] - i)) < 9:
        impact.append([bishop_place[0] - int(math.fabs(bishop_place[1] - i)), i])
knight_variants = [[-2,-1],[-1,-2],[-2,1],[-1,2],[1,2],[2,1],[1,-2],[2,-1]]
for k in knight_variants:
    if 0 < knight_place[0] + k[0] < 9 and 0 < knight_place[1] + k[1] < 9:
        impact.append([knight_place[0]+k[0], knight_place[1]+k[1]])
impact.append(knight_place)


print(f'Слон = {chr(bishop_place[0]+64)}{bishop_place[1]}')
print(f'Ладья = {chr(rook_place[0]+64)}{rook_place[1]}')
print(f'Конь = {chr(knight_place[0]+64)}{knight_place[1]}')
print(f"Количество пустых клеток под боем (кроме занятых самими фигурами) - {len(set(list(map(lambda x: f'{x[0]}{x[1]}', impact))))-3}")
for i in range(1,9):
    print(chr(i+64), end = '  ')
print()
for j in range(8):
    for i in cells[0+ 8*j:8 + 8*j]:
        cell = "+" if i in impact else "."
        if i == bishop_place:
            cell = 'С'
        if i == rook_place:
            cell = 'Л'
        if i == knight_place:
            cell = 'К'
        if i[0] == 'H':
            cell = f'{cell}  {i[1]}'
        print(cell, end = '  ')
    print()
    print("Пешка")
    print("Конь")
    print("Слон")