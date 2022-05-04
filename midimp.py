#!/usr/bin/env python

### mido imports
from __future__ import print_function
import sys
import mido
from tkinter.tix import INTEGER
from tokenize import Number
### osc imports
import argparse
from pythonosc import udp_client
from pythonosc import osc_message_builder


# Commandline Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
    help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=9000,
    help="The port the OSC server is listening on")
parser.add_argument('--device', type=int,
    help="The MIDI input device to send")
args = parser.parse_args()


# Choose MIDI input
input_port_options = mido.get_input_names()

if args.device is None:
    def print_ports(heading, port_names):
        print(heading)
        for i in range(len(port_names)):
            print("    {}:'{}'".format(i,port_names[i]))
        print()

    print_ports('Input Ports:', input_port_options)
    print_ports('Output Ports:', mido.get_output_names())

    portname = input_port_options[int(input('Choose input: '))]
else:
    portname = input_port_options[args.device]


# OSC client
client = udp_client.SimpleUDPClient(args.ip, args.port)


# Receive messages from MIDI and send them
ARG_TYPE_MIDI = "m"

try:
    with mido.open_input(portname) as port:
        print('Using {}'.format(port))
        print('Waiting for messages...')
        for message in port:
            print('Received {} {}'.format(message, message.bytes()))
            midi_bytes = message.bytes()
            builder = osc_message_builder.OscMessageBuilder(address="/notes")
            builder.add_arg((1, midi_bytes[0], midi_bytes[1], midi_bytes[2]), builder.ARG_TYPE_MIDI)
            bundle = builder.build()
            client.send_message("/notes", bundle)
            sys.stdout.flush()
except KeyboardInterrupt:
    pass
