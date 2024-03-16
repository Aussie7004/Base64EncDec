import base64

try:

    while True:
        options = input("Would you like to decode or encode? ").lower()

        if (options == "encode"):
            message = input("Enter your message: ")
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            print(base64_message)

        if (options == "decode"):
            base64_message = input("Enter your base64 ascii code: ")
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('ascii')
            print (message)

        print("\nPress CTRL + C if you would like to quit. Starting over.\n\n")

except KeyboardInterrupt:
    print("\n\nYou pressed CTRL + C. Quitting")
    quit()