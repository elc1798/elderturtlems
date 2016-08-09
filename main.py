import os
import argparse

import config
import netsend

def get_user_input():
    """
    Opens the default text editor to edit the message file. If no text editor is
    set via environment variables, then it will default to nano.

    After editting, it will prompt the user to confirm the message.

    Returns:
        True if the message is confirmed, False otherwise
    """
    # If the default text editor isn't set, default to nano
    editor = "nano"
    if config.EDITOR != "":
        # Get the program editor
        editor = config.EDITOR
    else:
        # Get the default text editor of the user
        editor = os.getenv("EDITOR")
    os.system("%s %s" % (editor, config.MESSAGE_FILE))
    print "Confirm message:"
    print "=" * 80
    os.system("cat %s" % (config.MESSAGE_FILE,))
    print "=" * 80
    confirm = ""
    while confirm not in [ "Y", "N" ]:
        confirm = str(raw_input("Send this message? (Y/N): ")).upper()
    if confirm == "Y":
        return True
    else:
        assert(confirm == "N")
        return False

def get_subject():
    return str(raw_input("Subject: "))

def get_message():
    get_user_input()
    f = open(config.MESSAGE_FILE)
    message = f.read()
    f.close()
    return message

def get_recipient():
    print "Enter the recipient. If you do not include the '@service.domain', then it will default to 'gmail.com'"
    recipient = str(raw_input("Recipient: "))
    if len(recipient.split("@")) == 1:
        recipient += "@gmail.com"
    return recipient

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Prompt user to log in"
    )
    parser.add_argument(
        "-u",
        "--username",
        action="append",
        help="Login Username"
    )
    parser.add_argument(
        "-p",
        "--password",
        action="append",
        help="Login Password"
    )
    args = parser.parse_args()

    sender = None
    if args.username and args.password:
        sender = netsend.Sender(str(args.username), str(args.password))
    else:
        sender = netsend.Sender()

    if args.interactive:
        sender.interactive_login(str(args.username) if args.username else "")

    sender.send_message(get_subject(), get_message(), get_recipient())

if __name__ == "__main__":
    main()
