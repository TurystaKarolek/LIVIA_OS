from kernel.events import EventBus
from kernel.context import RuntimeContext

class Kernel:
    def __init__(self):
        self.modules = {}
        self.events = EventBus()
        self.context = RuntimeContext()

    def register_module(self, module):
        self.modules[module.name] = module

        if hasattr(module, "initialize"):
            module.initialize()

        print(f"[+] Module loaded: {module.name}")

    def unload_module(self, module_name):
        if module_name in self.modules:
            module = self.modules[module_name]

            if hasattr(module, "shutdown"):
                module.shutdown()

            del self.modules[module_name]

            print(f"[-] Module unloaded: {module_name}")

        else:
            print("[!] Module not found.")

    def list_modules(self):
        return list(self.modules.keys())

    def system_status(self):
        return {
            "loaded_modules": len(self.modules),
            "status": "operational"
        }
