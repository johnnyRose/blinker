# blinker
A blinking LED tutorial for the Raspberry Pi!

## Getting Started

If you've never set up a Raspberry Pi, or it's been a while, hopefully these instructions can help you get moving quickly.

1. Download the latest version of Raspbian [here](https://www.raspberrypi.org/downloads/raspbian/). At the time of writing, the latest version is Raspbian Jessie 2017-07-05. You can download either the desktop version or "Raspbian Lite" (only console, but less than one-fifth the size of the desktop version).

2. Follow the official [Raspbian Installation Guide](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) to install the image to your SD card.

3. After flashing your SD card, mount the disk and add an empty file named `ssh` (no extension) to the root of the "boot" partition. This enables SSH access.

4. SSH (port 22) into raspberrypi.local, using `pi` as the default username and `raspberry` as the default password. If you're running some sort of Unix, it's as simple as `ssh pi@raspberrypi.local`. Otherwise, you can download and run [PuTTY](http://www.putty.org). Note that you'll need to connect your Pi to the Internet if it isn't already. For devices other than the Zero, this is a piece of cake: connect it to your router via a network cable. For the Raspberry Pi Zero, this is a bit more involved, so I'll defer you to one of the many tutorials available online. 

5. Update packages and install dependencies:

```
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install python3
    sudo apt-get install python-rpi.gpio python3-rpi.gpio
    sudo apt-get install git
```

6. Clone the git repo, which I assume you already found: `git clone https://github.com/johnnyRose/blinker.git`

7. Set up the hardware. This program uses pin 11 for power and pin 9 for ground. You should probably turn off your device so you don't accidentally fry anything.

`pin 11 (power) -> 220 ohm resistor -> standard red LED -> pin 9 (ground)`

8. All done! Run the program with `python3 blinker.py`. You can press Ctrl+C at any point to kill it.


