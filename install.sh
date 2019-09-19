#!/bin/bash
apt update && apt -y upgrade && apt-get install -y git net-tools python3 python3-pip tor
pip3 install requests stem bs4 pysocks
git clone https://github.com/henriqueblobato/PythonRequestTor.git
cd PythonRequestTor
echo "ControlPort 9051" >> /etc/tor/torrc
echo HashedControlPassword $(tor --hash-password henrique | cut -d "." -f 2 | tail -n 1) >> /etc/tor/torrc
echo "CookieAuthentication 1" >> /etc/tor/torrc
service tor stop && service tor start
#python3 run_me.py
