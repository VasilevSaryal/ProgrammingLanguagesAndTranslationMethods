fio_list = """1. Васильев Сарыал Иннокентьевич
2 Платонов Симон Владимирович
3 Кыппыгыров Сарыал Васильевич
4. ФИИТ-16
5. Атласов Сарыал Чеевич
6. Чабыева Дайаана Иннокетьевна
7. Эверстов Владимир Васильевич
8 Васильев Арсен Владимирович
9 Новиков Сарыал Иннокентьевич
10 Просто Сарыал"""


def three():
    print(fio_list)
    names = list()
    second_names = list()
    answer = 0  # Если имя и отчество одинаковые
    for field in fio_list.split(sep="\n"):
        words = field.split()
        if len(words) < 3:
            continue
        names.append(words[2])
        if len(words) == 4:
            second_names.append(words[3])
            if len(names) > 1 and len(second_names) > 1:
                if words[2] in names[:len(names)-1] or words[3] in second_names[:len(second_names)-1]:
                    answer += 1
                continue
        if len(names) > 1:
            if words[2] in names[:len(names) - 2]:
                answer += 1
    print("Число тезок: ", 0 if answer == 0 else answer + 1)
