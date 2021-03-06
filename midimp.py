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
parser.add_argument("--ip",
    help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=9000,
    help="The port the OSC server is listening on")
parser.add_argument('--device', type=int,
    help="The MIDI input device to send")
args = parser.parse_args()


# Choose PS4/PS5 IP Address
if args.ip is None:
    args.ip = input('Type in the IP address of your PS4/PS5 (skip next time with --ip): ')


# Choose MIDI input
input_port_options = mido.get_input_names()

if args.device is None:
    def print_ports(heading, port_names):
        print(heading)
        for i in range(len(port_names)):
            print("    {}:'{}'".format(i,port_names[i]))
        print()

    print_ports('Input Ports:', input_port_options)
    # print_ports('Output Ports:', mido.get_output_names())

    portname = input_port_options[int(input('Choose MIDI device (skip next time with (--device): '))]
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
            if( any([
                message.type == 'note_on',
                message.type == 'note_off',
                # message.type == 'control_change',
                # message.type == 'aftertouch',
                # message.type == 'pitchwheel',
                # message.type == 'start',
                # message.type == 'continue',
                # message.type == 'stop',
                # message.type == 'reset',
            ]) ):
                
                #change zero velocity note_on messages to note_off messages
                if(message.type == 'note_on' and message.velocity == 0):
                    message = mido.Message('note_off', channel=message.channel, note=message.note, time=message.time)

                # always use channel 0
                message = message.copy(channel = 0)

                midi_bytes = message.bytes()
                print('Received {} {}'.format(message, midi_bytes))
                builder = osc_message_builder.OscMessageBuilder(address="/notes")
                builder.add_arg((1, midi_bytes[0], midi_bytes[1], midi_bytes[2]), builder.ARG_TYPE_MIDI)
                bundle = builder.build()
                client.send_message("/notes", bundle)
            sys.stdout.flush()
except KeyboardInterrupt:
    pass
