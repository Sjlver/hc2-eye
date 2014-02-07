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

#f_on = dmx.Frame([255]*512)
#f_off = dmx.Frame([0]*512)
# send(f_on)
# time.sleep(3.0)
# send(f_off)

global_frame = dmx.Frame([0] * 512)
def set_channel(channel, value):
    global_frame[channel] = value
    for i in range(3):
        send(global_frame)

# Channels
ch_color = 192
ch_gobo_rotate = 193
ch_gobo = 194
ch_dimmer = 195
ch_pan = 196
ch_tilt = 197
ch_effect = 198


