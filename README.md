# MIDImp
headless script to send MIDI over OSC to your PS4/PS5

## Install

```sh
python3 -m venv .venv
python3 -m pip3 install -r requirements.txt
```

The script is written in Python 3 and requires installing a few open source packages. To make installation more clean for your personal computer, a virtual environment is used. This means you can install these dependencies without making a mess of your own machine, and when the day comes that you decide to delete the MIDImp folder, everything will go along with it.


## Run

```sh
python3 midimp.py
```
You will be prompted to provide the IP address of your PS4/PS5 and which MIDI device you want to use.


## Run Without Menu

```sh
python3 midimp.py --ip=192.168.1.100 --midi-input=1
```

You may want the option to bypass the menus so you can do things like run MIDImp at startup. Providing arguments on the commandline will do this.


## Make it stop!

kill the script by pressing Ctrl+C


## Thanks

The original midi2osc is a much more attractive piece of software. Thanks to Alex Evans and others at Media Molecule who keep the original app slightly maintained so that the feature keeps working.
