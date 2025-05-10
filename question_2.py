# Егор с друзьями гуляли по городу N и нашли карту метро. В этом городе целых п веток метро, у
# каждой ветки свое расписание. Изучив расписание, они обнаружили, что по ветке і поезд начинает
# ходить в ал секунду с начала дня, И каждыи новыи поезд начинает маошоут после предыдущего
# спустя 6; секунд. Теперь им захотелось научиться в некоторые моменты времени для ветки и
# времени определять, когда они увидят поезд после прихода на станцию.
# 
# Формат входных данных
# в первои строке входных данных дано число п — количество веток в городе (1 > n ≤ 1UU).
# В следующих п строках даны числа а;, bj - первый момент, когда поезд с і-й ветки приезжает на
# станцию, и промежуток между поездами (0 < ai < bi < 10º).
# В следующей строке дано число д- количество запросов (1 ≤ 9 < 100).
# В следующих у строках даны числа ti, di — номер ветки и момент времени, 
# когда друзья придут на станцию (1 ≤ ti {n, 1 < di < 10°).
# 
# Формат выходных данных
# Для каждого запроса выведите в отдельной строке ответ на задачу.


train_schedule = {}
n_lines = int(input())

for i in range(1, n_lines+1):
    res: str = input()
    res_list = res.split(" ")
    train_schedule[i] = [int(element) for element in res_list]

n_requests = int(input())
for i in range(n_requests):
    res = input()
    res_list = res.split(" ")
    number_line = int(res_list[0])
    time_request = int(res_list[1])
    start_time = train_schedule[number_line][0]

    time_between_trains = train_schedule[number_line][1]
    resul = time_request % time_between_trains
    if start_time == resul:
        print(time_request)
    elif start_time > resul:
        print(time_request - resul + start_time)
    else:
        print(time_request - resul + start_time + time_between_trains)


    

    