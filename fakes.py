from faker import Faker
import pandas as pd

sample = Faker()

num = int(input("Place in the number of data you want: "))
data = [sample.profile() for n in range(num)]
my_data_frame = pd.DataFrame(data)

# print(my_data_frame)
with open('file.txt', 'w') as write_file:
    data_frame = str(my_data_frame)
    write_file.write(data_frame)