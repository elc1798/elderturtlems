#!/bin/bash

IP=$(curl -s checkip.dyndns.org | grep -Eo '[0-9\.]+')
echo "Sent from (IPv4 ADDR): " > MESSAGE.txt
echo $IP > MESSAGE.txt
