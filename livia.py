from kernel.kernel import Kernel
from modules.echo_link import EchoLink
from config.system_config import SYSTEM_CONFIG
from providers.mock_provider import MockProvider

def main():
    kernel = Kernel()

    kernel.load_all_modules()
    
    kernel.events.subscribe(
    "system_start",
    echo_link.on_system_start
    )

    kernel.events.emit("system_start")

    kernel.context.set("system_mode", "development")

    kernel.context.set("config", kernel.config)

    provider = MockProvider()

    while True:
        print()
        print("=== LIVIA OS ===")
        print("1. List modules")
        print("2. System status")
        print("3. Show runtime context")
        print("4. Show config")
        print("5. Unload Echo-Link")
        print("6. Test AI provider")
        print("7. Store memory")
        print("8. Show memory")
        print("9. Exit")

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
            print()
            print(kernel.context.get("config"))

        elif choice == "5":
            kernel.unload_module("Echo-Link")

        elif choice == "6":
            prompt = input("Prompt: ")
            response = provider.generate(prompt)

            print()
            print(response)

        elif choice == "7":
            entry = input("Memory entry: ")

            kernel.memory.store(entry)

            print()
            print("Memory stored.")

        elif choice == "8":
            print()
            print(kernel.memory.recall())
            

        elif choice == "9":
            print()
            print("Shutting down LIVIA OS...")
            break

        else:
            print()
            print("Unknown command.")


if __name__ == "__main__":
    main()
