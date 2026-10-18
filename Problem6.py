marks=[88,74,93,-5,61,47,105,82,59]

valid_marks=[mark for mark in marks if 0<=mark<=100]

grade_counts={'A':0,'B':0,'C':0,'F':0}

for m in valid_marks:
    if m>=80:
        grade_counts['A']+=1
    elif m>=70:
        grade_counts['B']+=1
    elif m>=60:
        grade_counts['C']+=1
    else:
        grade_counts['F']+=1

average=sum(valid_marks)/len(valid_marks)

print(f"Valid marks:{valid_marks}")
print(f"Grade counts:{grade_counts}")
print(f"Average:{average:.2f}")