marks=[93,84,82,83,77,95]
subjects=['Tamil','English','Maths','Physics','Chemistry','Computer Science']
n=len(marks)
total=sum(marks)
high=max(marks)
low=min(marks)
average=total/n
print(subjects[:1],marks[:1])
print(subjects[1:2],marks[1:2])
print(subjects[2:3],marks[2:3])
print(subjects[3:4],marks[3:4])
print(subjects[4:5],marks[4:5])
print(subjects[5:6],marks[5:6])

print("Total Marks :",total)
print("Average Marks :",average)
print("Highest Mark :",high)
print("Lowest Mark :",low)
