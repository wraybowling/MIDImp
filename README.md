# MIDImp
headless script to send MIDI over OSC to your PS4/PS5

![MIDImp promotional image](https://repository-images.githubusercontent.com/482833910/1803727c-044f-4e8a-bbbc-6d7e55e19884)

## Install

The script is written in Python 3 and requires installing a few open source packages. To make installation more clean for your personal computer, a virtual environment is used. This means you can install these dependencies without making a mess of your own machine, and when the day comes that you decide to delete the MIDImp folder, everything will go along with it.

### Activate Virtual Environment

You can either activate the virtual environment manually using the scripts below or open the project in VS Code which will detect it automatically.

For Powershell (Windows)
```powershell
.venv\Scripts\Activate.ps1
```

For Shell (MacOS & Linux)
```sh
source .venv/bin/activate
```

### Fetch Dependencies

```sh
python3 -m venv .venv
python3 -m pip3 install -r requirements.txt
```


## Run

```sh
python3 midimp.py
```
You will be prompted to provide the IP address of your PS4/PS5 and which MIDI device you want to use.


## Run Without Menu

```sh
python3 midimp.py --ip=192.168.1.100 --device=1
```

You may want the option to bypass the menus so you can do things like run MIDImp at startup. Providing arguments on the commandline will do this.


## Make it stop!

kill the script by pressing Ctrl+C


## Thanks

The original midi2osc is a much more attractive piece of software. Thanks to Alex Evans and others at Media Molecule who keep the original app slightly maintained so that the feature keeps working.
