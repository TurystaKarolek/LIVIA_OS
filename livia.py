from kernel.kernel import Kernel
from modules.echo_link import EchoLink
from config.system_config import SYSTEM_CONFIG

def main():
    kernel = Kernel()

    echo_link = EchoLink()
    kernel.register_module(echo_link)
    
    kernel.events.subscribe(
    "system_start",
    echo_link.on_system_start
    )

    kernel.events.emit("system_start")

    kernel.context.set("system_mode", "development")

    while True:
        print()
        print("=== LIVIA OS ===")
        print("1. List modules")
        print("2. System status")
        print("3. Show runtime context")
        print("4. Unload Echo-Link")
        print("5. Exit")

        choice = input("> ")

        if choice == "1":
            print()
            print("Loaded modules:")
            print(kernel.list_modules())

        elif choice == "2":
            print()
            print(kernel.system_status())

        elif choice == "3":
            print()
            print(kernel.context.dump())

        elif choice == "4":
            kernel.unload_module("Echo-Link")

        elif choice == "5":
            print()
            print("Shutting down LIVIA OS...")
            break

        else:
            print()
            print("Unknown command.")


if __name__ == "__main__":
    main()
