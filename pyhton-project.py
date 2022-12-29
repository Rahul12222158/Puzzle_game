command = ""
started=False
stopped=False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car started.. ")
        else:
            started=True
            print("car already started")
    elif command == "stop":
        if stopped:
            print("car is already stopped")
        else:
            stopped=True
            print("car stopped...")
    elif command == "help":
        print("""
start-to start the car
stop-to stop the car
quit-to quit the car
""")
    elif command == "quit":
        break
    else:
        print("sorry i don't understand ")