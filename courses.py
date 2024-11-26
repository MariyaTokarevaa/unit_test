courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]

durations = [14, 20, 12, 20]


def sort_by_duration(courses: list, durations: list) -> list:
    courses_list = []
    for course, duration in zip(courses, durations):
        course_dict = {"title": course, "duration": duration}
        courses_list.append(course_dict)

    durations_dict = {}
    for id, course in enumerate(courses_list):
        key = course["duration"]
        durations_dict.setdefault(key, [])
        durations_dict[key].append(id)

    durations_dict = dict(sorted(durations_dict.items()))

    result_list = []
    for duration, ids in durations_dict.items():
        for id in ids:
            result_list.append(f'{courses_list[id]["title"]} - {duration} месяцев')
    return result_list


def get_min_max_course(courses: list, durations: list) -> str:
    courses_list = []

    for course, duration in zip(courses, durations):
        course_dict = {"title": course, "duration": duration}
        courses_list.append(course_dict)

    maxes = []
    minis = []
    for id, duration in enumerate(durations):
        if duration == max(durations):
            maxes.append(id)
        elif duration == min(durations):
            minis.append(id)

    courses_max = [x["title"] for id, x in enumerate(courses_list) if id in maxes]
    courses_min = [x["title"] for id, x in enumerate(courses_list) if id in minis]

    return f'Самый короткий курс(ы): {", ".join(courses_min)} - {min(durations)} месяца(ев) \n' \
           f'Самый длинный курс(ы): {", ".join(courses_max)} - {max(durations)} месяца(ев)'

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]


def get_unique_mentors(mentors: list) -> str:
    all_list = []
    [all_list.extend(x) for x in mentors]
    all_names_list = [x.split(" ")[0].strip() for x in all_list]
    all_names_set = set(all_names_list)
    all_names_sorted = sorted(list(all_names_set))
    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'


if __name__ == '__main__':
    print(sort_by_duration(courses, durations))
    print(get_min_max_course(courses, durations))
    print(get_unique_mentors(mentors))