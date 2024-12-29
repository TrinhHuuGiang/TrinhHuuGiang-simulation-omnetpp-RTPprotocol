# File này dùng để sinh dữ liệu mô phỏng audio/video cho các máy tham gia mạng giao thức RTP multicast nhiều - nhiều
# Tham khảo từ các file trong mục data của example 'rtp' thuộc inet
# File được thiết kế dựa trên các thông số mẫu của 'alien.mpg.gdf'
# các khung hình được thiết kế tăng dần đến giới hạn băng thông 'datarate' theo từng giây

'''==============================================
== Definitions
=============================================='''
from mul_net_b_global import (datarate, framerate, max_host,
                         ini_delay, under_load_time, over_load_time, frame_bits,
                         data_file)

'''==============================================
== Gen data
=============================================='''

def gen_mul_net_data_file():
    # open file
    with open(data_file, 'w') as f:
        # noi dung khoi tao frame rate, ini delay
        f.write('''{:<10}\t{} {}\n'''.format(framerate, "[frames/second]", "Frame Rate"))
        f.write('''{:<10}\t{}\t{}\n'''.format(ini_delay, "[seconds]", "Initial Delay"))
        
        # noi dung cac khung hinh sau do
        # ta coi datarate la dung luong toi da truyen duoc
        # frame_bits cho moi frame co the tinh tu 'datarate' va 'framerate' va max_time_sim va max host
        # - 'datarate' => dung luong kenh
        # - chia 'max_host' => dung luong cho 1 host truyen tren kenh
        # - chia 'framerate' => dung luong 1 frame
        # - chia 'under_load_time'=> dung luong frame nho nhat
        # ta thiet ke de sau moi giay frame_bits của khung hinh tang len
        step_increase_bits = ( ( datarate // max_host ) // framerate ) // under_load_time
        frame_bits = step_increase_bits
        
        # under load time
        for i in range(under_load_time):
            for j in range(framerate):
                f.write('''{}\t\t{}\t\t{}\n'''.format(frame_bits, "[bits]", "I-Frame")) # o day chi dung I-Frame, bo qua B và P Frame
            # tang frame_bits
            frame_bits += step_increase_bits
        
        #over load time
        for i in range(over_load_time):
            for j in range(framerate):
                f.write('''{}\t\t{}\t\t{}\n'''.format(frame_bits, "[bits]", "I-Frame")) # o day chi dung I-Frame, bo qua B và P Frame
            # tang frame_bits
            frame_bits += step_increase_bits


