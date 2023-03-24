# Let's create a file with the mock dataset
# Example - create a program which allows to generate any number of lines following the structure:
#  * hour:minute
#  * value from 0 to 100
#  * value from 0.1 to 1.0
# Each value should be separated with ";" (time;value1,value2)

from datetime import datetime as dt, timedelta as td
from random import randint, uniform

# To be fancy, we can even name the file with the current date,
# however in this example we will stick with an already used name

#now = dt.now()
#file_name = f"data_{now.strftime('%Y%m%d')}.txt"


for _ in range(10):
    with open(data_20230323.txt, "a", encoding="utf-8") as file:
        for _ in range(2):
            time = now - td(hours=randint(-24, 24), minutes=randint(-60, 60))
            # time = f"{randint(0,23):2d}:{randint(0,59):2d}".replace(" ", "0")
            first_value = str(randint(0, 100))
            second_value = str(round(uniform(0.1, 1.0), 2))
            row = time.strftime("%H:%M") + ";" + first_value + ";" + second_value + "\n"
            file.write(row)

# Using nested loops allows us to optimize the program, as it takes less memory to run it

# Now, we would like to EXTRACT some of the data (and TRANSFORM it a little)
# Example - from the mock dataset, create a new file with additional column, which contains
# operation: value1 * value2, and in the first column there is only hour left

with open("data_20230323.txt", "r", encoding="utf-8") as file:
    with open("data_20230323_processing.txt", "a", encoding="utf-8") as output:
        for line in file:
            tmp = line.replace("\n", "").split(";")
            row = tmp[0][:2] + ";" \
                  + tmp[1] + ";" + tmp[2] \
                  + ";" + str(round(float(tmp[1]) * float(tmp[2]), 2)) + "\n"
            output.write(row)

# If we didn't want to create a new file, but instead overwrite the file,
# we would use mode "w" instead of r and would not open (create) a second file
# (+ some minor changes in syntax)


# Now, we would like to LOAD some data in desired form, which will be easier to analyse
# Example - from the new file, find the greatest value from the last column for each hour

result = {}

with open("data_20230323_processing.txt", "r", encoding="utf-8") as file:
    for line in file:
        tmp = line.replace("\n", "").split(";")
        key = tmp[0]
        value = tmp[3]

        if key not in result.keys():
            result[key] = value
        elif result[key] < value:
            result[key] = value

# With that, we have loaded only the desired data to our program in the format that we wanted (dict)
# and we can check the results:

for i in result:
    print(i, result[i])




