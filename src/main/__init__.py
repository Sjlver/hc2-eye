import socket
import time

from artnet import packet, dmx

# Initialize a socket that we use to talk with artnet
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#sock.bind(('', packet.ARTNET_PORT))


# Sends a packet
def send(frame):
    p = packet.DmxPacket(frame)
    sock.sendto(p.encode(), ('<broadcast>', packet.ARTNET_PORT))

f_on = dmx.Frame([255]*512)
f_off = dmx.Frame([0]*512)

send(f_on)
time.sleep(3.0)
send(f_off)
