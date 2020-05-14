# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter = ",", skip_header = 1)
print(data)

print("\nType of Data: \n\n", type(data))

census = np.concatenate((new_record,data), axis = 0)
print(census)


# --------------
#Code starts here
import numpy as np

age = census[:,0]
print(age)

max_age = max(age)
print(max_age)

min_age = min(age)
print(min_age)

age_mean = np.mean(age)
print(age_mean)

age_std = np.std(age)
print(age_std)


# --------------
#Code starts here
import numpy as np

Race = census[:,2]
print(Race)

race_0 = census[census[:,2]==0]
len_0 = len(race_0)
print(len_0)

race_1 = census[census[:,2]==1]
len_1 = len(race_1)
print(len_1)

race_2 = census[census[:,2]==2]
len_2 = len(race_2)
print(len_2)

race_3 = census[census[:,2]==3]
len_3 = len(race_3)
print(len_3)

race_4 = census[census[:,2]==4]
len_4 = len(race_4)
print(len_4)

minimum = min(len_0,len_1,len_2,len_3,len_4)
minority_race = 3
print(minority_race)



# --------------
#Code starts here
senior_citizens = census[census[:,0] > 60]
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

working_hours_sum=senior_citizens.sum(axis=0)[6]

avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here

#Creating an array based on 'education' column
high=census[census[:,1]>10]

#Finding the average pay
avg_pay_high=high[:,7].mean()

#Printing the average pay
print(avg_pay_high)

#Creating an array based on 'education' column
low=census[census[:,1]<=10]

#Finding the average pay
avg_pay_low=low[:,7].mean()

#Printing the average pay
print(avg_pay_low)
#Code ends here


