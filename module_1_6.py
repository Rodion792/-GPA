grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
sorted_students = sorted(students)
print(sorted_students)
conclusion0 = sum(grades[0])/len(grades[0])
conclusion1 = sum(grades[1])/len(grades[1])
conclusion2 = sum(grades[2])/len(grades[2])
conclusion3 = sum(grades[3])/len(grades[3])
conclusion4 = sum(grades[4])/len(grades[4])
result = {sorted_students[0]: conclusion0, sorted_students[1]: conclusion1, sorted_students[2]: conclusion2, sorted_students[3]: conclusion3, sorted_students[4]: conclusion4}
print(result)