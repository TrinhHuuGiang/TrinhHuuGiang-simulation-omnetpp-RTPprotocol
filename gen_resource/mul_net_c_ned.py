# File này dùng để sinh mã vẽ mô hình mạng multicast để mô phỏng giao thức RTP
# file đích "mul_net.ned" trong mục src

'''==============================================
== Definitions
=============================================='''
from mul_net_b_global import (datarate, delay_normal_mean, delay_normal_var, ber,
                              max_host, max_host_per_row, row_padding, col_padding,
                              ned_file)

'''==============================================
== Gen ned file
=============================================='''

def gen_mul_net_ned_file():
    # open file
    with open(ned_file, 'w') as f:
        # Gen code init network
        f.write('''
package src;

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.inet.Router;
import inet.node.rtp.RtpHost;
import ned.DatarateChannel;


@license(LGPL);

network multicast_Network
{{
    types:
        channel ethernet extends ned.DatarateChannel
        {{
            parameters:
                delay = normal({}s, {}s);
                datarate = {}Mbps;
                ber = {};
        }}

    submodules:
'''.format(delay_normal_mean, delay_normal_var, datarate//(10**6), ber))
        # Gen code init host receiver
        y = 0
        for i in range(max_host):
            x = i % max_host_per_row
            if x == 0: y += row_padding
            f.write('''
        Host_{}: RtpHost {{
            parameters:
                destinationAddress = "225.0.0.1";
                @display(\"p={},{}\");
        }}
'''.format(i,col_padding + col_padding*x, y))
        
        # Gen code init router, config ipv4
        f.write('''
        // Định nghĩa router
        router: Router {{
            parameters:
                multicastForwarding = true;
                @display("p=240,{}");
        }}
        
        // Định nghĩa ipv4
        configurator: Ipv4NetworkConfigurator {{
            config = xml("<config>"
                +"<interface hosts='**' address='10.x.x.x' netmask='255.x.x.x'/>"
                +"<multicast-group hosts='**' address='225.0.0.1'/>"
                +"<multicast-route hosts='router' groups='225.0.0.1' children='ppp*'/>"
                +"</config>");
            @display("p=100,{};is=s");
        }}
'''.format(y+row_padding,y+row_padding ))
            
        
        # Gen code init connection transmitter with router
        f.write('''
    connections:
''')
        
        # Gen code init connection receiver with router
        for i in range(max_host):
            f.write('''
        Host_{}.pppg++ <--> ethernet <--> router.pppg++;
'''.format(i))
        
        # end
        f.write('\n}')
