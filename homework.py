grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_name = sorted(students)
average_value_1 = (sum(grades[0])/len(grades[0]))
average_value_2 = (sum(grades[1])/len(grades[1]))
average_value_3 = (sum(grades[2])/len(grades[2]))
average_value_4 = (sum(grades[3])/len(grades[3]))
average_value_5 = (sum(grades[4])/len(grades[4]))
average_value = ((average_value_1),
                 (average_value_2),
                 (average_value_3),
                 (average_value_4),
                 (average_value_5))
dictionary = (dict(zip(sorted_name, average_value)))
print(dictionary)
