scores={
    "Amina":{"python":82, "statistics":76, "calculus":88},
    "Maya":{"python":58, "statistics":64, "calculus":61},
    "Disha":{"python":91, "statistics":89, "calculus":94},
    "Nora":{"python":45, "statistics":52, "calculus":56}
}

results={}

for student, marks in scores.items():
    average=sum(marks.values())/len(marks)
    rounded_average=round(average)

    status="Pass" if average>=60 else "Fail"

    results[student]={
        "average":rounded_average,
        "status":status
    }

top_student=max(
    results,
    key=lambda student: results[student]["average"]
)

print("Results:", results)
print("Highest average:", top_student)