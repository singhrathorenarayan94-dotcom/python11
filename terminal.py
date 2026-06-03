while True:
    cmd = input("MyTerminal> ")

    if cmd == "hello":
        print("Hello User!")

    elif cmd == "time":
        from datetime import datetime
        print(datetime.now())

    elif cmd == "exit":
        break

    else:
        print("Unknown command")
