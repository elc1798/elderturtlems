#!/bin/bash

cd src

echo "Do you wish to include your IP Address in the message?"
read -p "y or n: " CONTINUEYN
if [ "$CONTINUEYN" = "y" ] || [ "$CONTINUEYN" = "yes" ] || [ "$CONTINUEYN" = "Y" ] ; then
	chmod +x connectivity.sh
	./connectivity.sh
elif [ "$CONTINUEYN" = "n" ] || [ "$CONTINUEYN" = "no" ] || [ "$CONTINUEYN" = "N" ] ; then 
	echo "IP Will not be sent with the message."
	sleep 3
else
	echo "Invalid response."
	echo "Run script again, and enter y or n and hit [ENTER]"
	sleep 3
fi

python main.py
python netsend.py
