# File định nghĩa các biến toàn cục trước khi tạo file ini, ned, frame data

'''==============================================
== Global Data / Definitions
=============================================='''
from mul_net_b_global import (datarate, delay_normal_mean, delay_normal_var, ber,
                              ini_file,
                              framerate,
                              max_host,
                              data_file, max_time_sim)


'''==============================================
== Gen ini file
=============================================='''
def gen_mul_net_ini_file():
    # open file
    with open(ini_file, 'w') as f:
        f.write('''[General]
# mo ta mang
network = multicast_Network
total-stack = 28MiB # tong stack phan bo cho cac host khi mo phong, thay doi khi stack overflow

# mo ta host
**.Host_*.forwarding = false
**.Host_*.profileName = "inet.transportlayer.rtp.RtpAvProfile"
**.Host_*.portNumber = 5004
**.Host_*.bandwidth = 8000

# mo ta file data
**.Host_*.fileName = \"{}\"
**.payloadType = 32 #video
**.autoOutputFileNames = true #khong biet :) nhung khong co se loi khi mo phong

# mo phong delay cho chuong trinh
**.sessionEnterDelay = 10s # tre 1 khoang truoc khi bat dau phien / sau khi khoi tao cac ket noi
**.transmissionStartDelay = 10s # tre truoc khi bat dau truyen / sau khi bat dau session
**.transmissionStopDelay = {}s  # ket thuc sau n giay / tinh tu khi bat dau truyen
**.sessionLeaveDelay = 10s # sau khi ket thuc

# ??? trong vi du no ghi the :)
**.Host_*.**.commonName = "???"
'''.format(data_file, max_time_sim))