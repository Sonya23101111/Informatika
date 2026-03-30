def find_common_participants(group1, group2, separator=','): #разделяем строки на списки с разделителем запятая
    participants_1 = group1.split(separator)
    participants_2 = group2.split(separator)
    common = []
    for participant in participants_1: # находим общих участников
        if participant in participants_2 and participant is not common:
            common.append(participant)

    return sorted(common) # возвращаем отсортированный список общих участников

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


common_participants = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator='|'
)
print(common_participants)
