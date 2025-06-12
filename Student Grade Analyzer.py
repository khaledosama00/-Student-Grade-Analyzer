grades = []

for i in range(5):
    grade = float(input(f"Enter grade for student {i+1}: "))
    grades.append(grade)

low_grade = min(grades)
high_grade = max(grades)
average = sum(grades) / len(grades)

print("Lowest grade:", low_grade)
print("Highest grade:", high_grade)
print("Average grade:", average)

passed = []
failed = []

for i in range(5):
    if grades[i] >= 50:
        passed.append(f"Student {i+1} (Grade: {grades[i]})")
    else:
        failed.append(f"Student {i+1} (Grade: {grades[i]})")

print("\nSuccessful students:")
for student in passed:
    print(student)

print("\nFailed students:")
for student in failed:
    print(student)


