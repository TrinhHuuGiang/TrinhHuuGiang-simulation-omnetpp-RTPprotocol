
package src;

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.inet.Router;
import inet.node.rtp.RtpHost;
import ned.DatarateChannel;


@license(LGPL);

network multicast_Network
{
    types:
        channel ethernet extends ned.DatarateChannel
        {
            parameters:
                delay = normal(0.00015s, 0.00005s);
                datarate = 1Mbps;
                ber = 0.0001;
        }

    submodules:

        Host_0: RtpHost {
            parameters:
                destinationAddress = "225.0.0.1";
                @display("p=80,60");
        }

        Host_1: RtpHost {
            parameters:
                destinationAddress = "225.0.0.1";
                @display("p=160,60");
        }

        // Định nghĩa router
        router: Router {
            parameters:
                multicastForwarding = true;
                @display("p=240,120");
        }
        
        // Định nghĩa ipv4
        configurator: Ipv4NetworkConfigurator {
            config = xml("<config>"
                +"<interface hosts='**' address='10.x.x.x' netmask='255.x.x.x'/>"
                +"<multicast-group hosts='**' address='225.0.0.1'/>"
                +"<multicast-route hosts='router' groups='225.0.0.1' children='ppp*'/>"
                +"</config>");
            @display("p=100,120;is=s");
        }

    connections:

        Host_0.pppg++ <--> ethernet <--> router.pppg++;

        Host_1.pppg++ <--> ethernet <--> router.pppg++;

}