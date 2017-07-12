# blinker
A blinking LED tutorial for the Raspberry Pi!

![Use your blinker!](http://s2.quickmeme.com/img/d2/d24c1158ea222ce28b02507182b2ce132545baa745343ff028b70e966d8e772e.jpg "Use your blinker!")

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

Note that it's probably not required to upgrade all your packages, but it probably won't hurt, either. Also, while this _will_ work with Python 2, I prefer to use Python 3. Embrace the future!

6. Clone the git repo, which I assume you already found: `git clone https://github.com/johnnyRose/blinker.git`

7. Set up the hardware. This program uses pin 11 for power and pin 9 for ground. You should probably turn off your device so you don't accidentally fry anything.

`pin 11 (power) -> 220 Ohm resistor* -> standard red LED -> pin 9 (ground)`

8. All done! Run the program with `python3 blinker.py`. You can press Ctrl+C at any point to kill it.

---

*_We use Ohm's Law (Resistance = Voltage / Amperage) to calculate 220 Ohms. We know the output of GPIO pin 11 is 3.3 volts, but the LED only supports a maximum of 2 volts/20 milliamps. So, we plug it into `R = V / I` and we find that the required resistance is 3.3V/0.020A = 165 Ohms. I don't have a 165 Ohm resistor - the lowest I have is 220 Ohms - so I use that instead. The LED will still light up, but we don't need to worry about breaking it. Science!_

