# В ВУЗе Никите задали домашнее задание по программированию, которое 
# он никак не мог решить, поэтому он попросил вас решить следующую задачу.
# Дана строка s длины 2n, состоящая из "(" и ")". Со строкой можно 
# проделывать две операции:
# • Выбрать пару (і, j) такую, что 1 ≤ і < j ≤ 2n и поменять символы 
# si и sj местами за а монет.
# • Заменить произвольный символ строки на "(" или ")" за b монет.
# Требуется сделать строку s правильной скобочной последовательностью за минимальное
# количество монет.
# Строка является правильной скобочной последовательностью, если выполнено одно из трех
# условий
# • Строка пустая.
# • Строку можно представить в виде (S), где S - правильная скобочная последовательность.
# • Строку можно представить в виде S1S2, где S1, S2 - правильные скобочные
# послеловательности.
# 
# Формат входных данных
# В первой строке входных данных дано три числа n, а, b (1 ≤ n ≤ 5 * 10^5, 1 ≤ a,b ≤ 10^9).
# Во второй строке дана строка s длины 2n, состоящая из символов "(" и ")".


poh: str = input()
lst_raw = poh.split(" ")
lst = [int(el) for el in lst_raw]

n_pairs = lst[0]
swap_price = lst[1]
invert_price = lst[2]

strin = input()

unpair_op = 0
unpair_cl = 0
for ch in strin:
    if ch == '(':
        unpair_op += 1
    else:
        if unpair_op > 0:
            unpair_op -= 1
        else:
            unpair_cl += 1

wrong = unpair_op + unpair_cl

if invert_price <= swap_price/2:
    # Выгодно все инвертить
    if unpair_cl % 2 != 0:
        num_invert_cl = unpair_cl // 2 + 1
        num_invert_op = unpair_op // 2 + 1
    else:
        num_invert_cl = unpair_cl // 2
        num_invert_op = unpair_op // 2

    cost = (num_invert_cl + num_invert_op) * invert_price

else:
    swaps = min(unpair_op, unpair_cl)
    differ = abs(unpair_op - unpair_cl)
    if differ % 2 != 0:
        inverts = differ // 2 + 1
    else:
        inverts = differ // 2
    cost = swaps * swap_price + inverts * invert_price


print(cost)
