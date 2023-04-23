exam_points = {
    "Mariusz": 30,
    "Mateusz": 55,
    "Marta": 76,
    "Roman": 30,
    "Arleta": 59,
    "Adrian": 96,
    "Monika": 91,
    "Andrzej": 22,
    "Krzysztof": 83,
    "Krystyna": 93,
    "Piotr": 44,
    "Dawid": 10,
    "Agnieszka": 15
}

#failed_students = []
#top_students = []
#best_student = ("", 0)
#print(list(number ** 3 for number in range(1, 10) if number ** 3 % 2 != 0))
sorted_names = sorted(exam_points, key=lambda x: exam_points.get(x), reverse=True)
failed_students = [name for name in sorted_names if exam_points.get(name) <= 45]
top_students = [name for name in sorted_names if exam_points.get(name) >= 91]
best_student_name = list(result for result in sorted_names)[0]
best_student = (best_student_name, exam_points.get(best_student_name))

print(failed_students)
print(top_students)
print(best_student)