import matplotlib.pyplot as plt
print("Tamil:93 \nEnglish:84 \nMaths:82 \nPhysics:83 \nChemistry:77 \nComputer Science:95")
subjects=('Tamil','English','Maths','Physics','Chemistry','Computer Science')
marks=[93,84,82,83,77,95]
y_positions=range(len(subjects))
plt.bar(y_positions,marks)
plt.xticks(y_positions,subjects)
plt.title("SUTHARSAN 'S  HSE+2 MARKS")
plt.ylabel("MARKS")
plt.xlabel("SUBJECTS")
plt.show()
