from kernel.kernel import Kernel
from modules.echo_link import EchoLink


def main():
    kernel = Kernel()

    echo_link = EchoLink()
    kernel.register_module(echo_link)
    
    kernel.events.subscribe(
    "system_start",
    echo_link.on_system_start
)

    kernel.events.emit("system_start")

    while True:
        print()
        print("=== LIVIA OS ===")
        print("1. List modules")
        print("2. System status")
        print("3. Unload Echo-Link")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":
            print()
            print("Loaded modules:")
            print(kernel.list_modules())

        elif choice == "2":
            print()
            print(kernel.system_status())

        elif choice == "3":
            kernel.unload_module("Echo-Link")

        elif choice == "4":
            print()
            print("Shutting down LIVIA OS...")
            break

        else:
            print()
            print("Unknown command.")


if __name__ == "__main__":
    main()
