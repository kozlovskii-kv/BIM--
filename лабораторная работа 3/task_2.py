# TODO Напишите функцию find_common_participants
def find_common_participants(participants_1, participants_2, argument=","):
    participants_first = participants_1.split(argument)
    participants_second = participants_2.split(argument)

    total_participants = list(set(participants_first).intersection(participants_second))
    total_participants.sort()

    return total_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)