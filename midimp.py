#!/usr/bin/env python

### mido imports
from __future__ import print_function
import sys
import mido
from tkinter.tix import INTEGER
from tokenize import Number
### osc imports
import argparse
# import random
# import time
from pythonosc import udp_client
from pythonosc import osc_message_builder

"""
List available ports.
This is a simple version of mido-ports.
"""
def print_ports(heading, port_names):
    print(heading)
    for i in range(len(port_names)):
        print("    {}:'{}'".format(i,port_names[i]))
    print()

input_port_options = mido.get_input_names()

print_ports('Input Ports:', input_port_options)
print_ports('Output Ports:', mido.get_output_names())

val = int(input('Choose input: '))
portname = input_port_options[val]
print(portname)


"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""

ARG_TYPE_MIDI = "m";

# if __name__ == "__main__":
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="192.168.1.145",
    help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=9000,
    help="The port the OSC server is listening on")
args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)

#   for x in range(10):
#     client.send_message("/notes", random.random())
#     time.sleep(1)


"""
Receive messages from the input port and print them out.
"""
# if len(sys.argv) > 1:
#     portname = sys.argv[1]
# else:
#     portname = None  # Use default port

try:
    with mido.open_input(portname) as port:
        print('Using {}'.format(port))
        print('Waiting for messages...')
        for message in port:
            print('Received {} {}'.format(message, message.bytes()))
            # client.send_message("/notes", message)
            midi_bytes = message.bytes()
            builder = osc_message_builder.OscMessageBuilder(address="/notes")
            builder.add_arg((1, midi_bytes[0], midi_bytes[1], midi_bytes[2]), builder.ARG_TYPE_MIDI)
            bundle = builder.build()
            client.send_message("/notes", bundle)
            sys.stdout.flush()
except KeyboardInterrupt:
    pass
