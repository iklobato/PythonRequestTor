
# PythonRequestTor
Usage of random tor proxies with python requests

# Installation

```bash
$ apt-get install -y git net-tools vim python3 python3-pip tor
$ git clone https://github.com/henriqueblobato/PythonRequestTor.git
$ cd PythonRequestTor
$ apt update && apt upgrade
$ pip3 install requests stem bs4 socks pysocks
$ echo "ControlPort 9051" >> /etc/tor/torrc
$ echo HashedControlPassword $(tor --hash-password henrique | cut -d "." -f 2 | tail -n 1) >> /etc/tor/torrc
$ echo "CookieAuthentication 1" >> /etc/tor/torrc
$ service tor stop && service tor start
$ python3 run_me.py
```

# Demo

[![Demonstration](https://i.vimeocdn.com/filter/overlay?src0=https%3A%2F%2Fi.vimeocdn.com%2Fvideo%2F815264003_1280x720.webp&src1=https%3A%2F%2Ff.vimeocdn.com%2Fimages_v6%2Fshare%2Fplay_icon_overlay.png)](https://player.vimeo.com/video/360656360)

Tested on Ubuntu 18.04.3 LTS (Bionic Beaver)
