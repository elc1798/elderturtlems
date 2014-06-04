#!/bin/bash

cd src

chmod +x connectivity.sh
./connectivity.sh

python startupVerNetsend.py
