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
if [[ -a ${colorama} ]]
then
    echo "colorama exists"
else
    pip install colorama
fi


#check if passlib is installed if not then install it.
if [[ -a ${passlib} ]]
then
    echo "passlib exists"
else
    pip install passlib
fi

rm -f $0
