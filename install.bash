#!/bin/bash

#installation script for encryption-machine

#dont run script as root
if (( $EUID == 0)); then
    echo "Please do not run as root"
    exit
fi

#clone repo
git clone https://github.com/Falk-Witte/encryption-machine


#check if colorama is installed if not then install it.
colorama=~/.local/lib/python3.10/site-packages/colorama/
colorama2=/usr/lib/python3.10/site-packages/colorama/

if [[ -d $colorama ]] || [[ -d $colorama2 ]]
then
    echo "colorama exists"
else
    pip install colorama
fi

#self destruct after running
rm -f $0
