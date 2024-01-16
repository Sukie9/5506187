 # Input: Number of students
    n = int(input())

    # List to store student records
    records = []

    # Input student names and grades
    for _ in range(n):
        name = input()
        score = float(input())
        records.append([name, score])

    # Find the second lowest grade
    grades = set(score for name, score in records)
    second_lowest_grade = sorted(grades)[1]

    # Collect names of students with the second lowest grade
    students_with_second_lowest_grade = [name for name, score in records if score == second_lowest_grade]

    # Sort the names alphabetically
    students_with_second_lowest_grade.sort()

    # Print the names
   
    for name in students_with_second_lowest_grade:
        print(name)