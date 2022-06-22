import matplotlib.pyplot as plt
print("Tamil:93 \nEnglish:84 \nMaths:82 \nPhysics:83 \nChemistry:77 \nComputer Science:95")

subjects=('Tamil','English','Maths','Physics','Chemistry','Computer Science')
marks=[93,84,82,83,77,95]
plt.pie(marks,labels=subjects,autopct='%1.f%%',counterclock=False,startangle=105)
plt.title("SUTHARSAN'S HSE +2 MARKS ")
plt.show()
