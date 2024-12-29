'''==============================================
== Definitions
=============================================='''
from mul_net_c_ned import gen_mul_net_ned_file
from mul_net_c_frame_increase_data import gen_mul_net_data_file
from mul_net_c_ini import gen_mul_net_ini_file

'''==============================================
== Gen Ned/ ini/ Data
=============================================='''
if __name__ == "__main__":
    gen_mul_net_ned_file()
    gen_mul_net_data_file()
    gen_mul_net_ini_file()