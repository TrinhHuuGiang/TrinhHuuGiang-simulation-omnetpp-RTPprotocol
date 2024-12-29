import pandas as pd
import matplotlib.pyplot as plt

# Đọc file CSV
file_path = 'router_drop.csv'
data = pd.read_csv(file_path)


# Đổi tên các cột
data.rename(columns={data.columns[0]: 'Time', data.columns[1]: 'PacketBytes'}, inplace=True)


# Đếm packet loss
min_time = int(data['Time'].iloc[0])  + 1
count = 0
list_time_loss = []

for value in data['Time']:
    if value < min_time:
        count +=1
    else:
        list_time_loss.append([min_time,count])
        min_time +=1
        count = 0
# if count != 0: list_time_loss.append([min_time,count])

# Tách trục x và y
times = [item[0] for item in list_time_loss]
counts = [item[1] for item in list_time_loss]

# Vẽ đồ thị
plt.figure()
plt.plot(times, counts, marker='o', color='blue', linestyle='-')
plt.xlabel('time (s)')
plt.ylabel('number Packet Loss')
plt.title('Router packet loss')
plt.grid(True)
plt.show()
