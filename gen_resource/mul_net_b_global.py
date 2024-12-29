'''==============================================
== Global data
=============================================='''

''' Ini file '''
# kênh truyền
datarate = 1*10**6         # 10MiB theo thông số đường truyền mẫu - xem ví dụ rtp multicast
delay_normal_mean = "0.00015" # s - ky vong
delay_normal_var = "0.00005"  # s - phuong sai
ber = "0.0001"               # ber theo thông số đường truyền mẫu
# (thay doi) giam datarate 10MB -> 1MB, ber 0.00001 -> 0.0001

# output file
ini_file = '../src/mul_simulation.ini'



''' Ned file '''
# arrage object
max_host = 2         # n host communicate
max_host_per_row = 5
row_padding = 60
col_padding = 80

# output file
ned_file = '../src/mul_net.ned'



''' data file '''
# tham so audio/video data
ini_delay = 0       # (float) mô phỏng thời gian trễ khởi động tài nguyên
under_load_time  = 20 # (int) biểu thị thời gian mà mức tải < datarate của đường truyền 
over_load_time = 20 # (int) biểu thị thời gian mà mức tải > datarate dường truyền
max_time_sim = under_load_time + over_load_time  # (int) mô phỏng dữ liệu trong n giây, n nen > 1 va la so nguyen de khong loi tinh toan
frame_bits = None   # (int) tinh toan trong qua trinh sinh data
framerate = 25      # (int) số khung hình / s lấy theo thông số mẫu trong file 'alien...'

# output file
data_file = '../data/mul_net_frame_increase.mpg.gdf'
