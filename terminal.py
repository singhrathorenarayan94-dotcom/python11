from datetime import datetime

try:
    while True:
        cmd = input("MyTerminal> ")

        if cmd == "hello":
            print("Hello User!")

        elif cmd == "time":
            print(datetime.now())

        elif cmd == "exit":
            print("Exiting...")
            break

        else:
            print("Unknown command")

except KeyboardInterrupt:
    print("\nKeyboard Interrupt detected. Exiting safely...")

print("end")
