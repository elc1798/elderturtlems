The Elder Turtle Messaging Service - A tiny messaging service written in Python

Use run.sh to run the normal messaging service.
'cd' into the elderturtlems directory.
To give run.sh executable permissions, type:

chmod +x run.sh

To run normally, use ./run.sh
It is recommended that the user make an alias for elderturtlems in their .bash_aliases file.

If you do not have a .bash_aliases file, cd into your home directory. In terminal:

cd ~
touch .bash_aliases
nano .bash_aliases

In nano, type in:

alias elderTurtle='sh [PATH TO run.sh]'

Use Ctrl+X, y, [ENTER] to save and exit.

For servers with dynamic IP addresses, startupVer.sh is intended to email you your server IP upon login.
Go into the src and open turtleconfigs.txt with a text editor, type in your email password, use carriage return 
to make a new line, then your username.
It should look like:

password
username@service.com

Save the file.

Then open 'Startup Applications' and add an entry for startupVer.sh. The command should be:

sh <PATH>/startupVer.sh

It should now email you on startup.
