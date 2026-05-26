from kernel.events import EventBus
from kernel.context import RuntimeContext
from kernel.logger import Logger
from config.config_loader import ConfigLoader
from modules.module_registry import AVAILABLE_MODULES

class Kernel:
    def __init__(self):
        self.modules = {}
        self.events = EventBus()
        self.context = RuntimeContext()
        self.logger = Logger()
        
        self.config_loader = ConfigLoader()
        self.config = self.config_loader.load()

    def load_all_modules(self):
        
        for module_class in AVAILABLE_MODULES:
            module = module_class()
            self.register_module(module)
    
    def register_module(self, module):
        self.modules[module.name] = module

        if hasattr(module, "initialize"):
            module.initialize()

        self.logger.info(f"Module loaded: {module.name}")

    def unload_module(self, module_name):
        if module_name in self.modules:
            module = self.modules[module_name]

            if hasattr(module, "shutdown"):
                module.shutdown()

            del self.modules[module_name]

            self.logger.info(f"Module unloaded: {module_name}")

        else:
            self.logger.warning("Module not found.")
            
    def list_modules(self):
        return list(self.modules.keys())

    def system_status(self):
        return {
            "loaded_modules": len(self.modules),
            "status": "operational"
        }
