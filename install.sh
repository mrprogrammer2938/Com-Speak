#!/usr/bin/env bash
# This Code Write by Mr.nope
# Com-Speak
if [[ "$(id -u)" -ne 0 ]];
then
    echo "Please, Run This Programm as Root!"
    exit 1
fi
function main() {
    printf '\033]2;Com-Speak\a'
    clear
    echo "Installing..."
    chmod +x speak.py
    sleep 2
    apt install python
    apt install python3
    apt install python3-pip
    pip3 install --upgrade pip
    echo "
Finish...!
Usage:
      python3 speak.py
    "
    exit 1
}
main