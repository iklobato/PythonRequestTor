
# PythonRequestTor
Usage of random tor proxies with python requests

# Installation

```bash
$ apt update
$ apt upgrade
$ apt install net-tools
$ ifconfig
$ apt-get install vim
$ apt-get install -y python3
$ apt-get install python3-pip
$ pip3 install requests stem bs4 socks pysocks
$ apt install tor
$ echo "ControlPort 9051" >> /etc/tor/torrc
$ echo HashedControlPassword $(tor --hash-password henrique | cut -d "." -f 2 | tail -n 1) >> /etc/tor/torrc
$ echo "CookieAuthentication 1" >> /etc/tor/torrc
$ service tor stop && service tor start
$ python3 run_me.py
```

Tested on Ubuntu 18.04.3 LTS (Bionic Beaver)
