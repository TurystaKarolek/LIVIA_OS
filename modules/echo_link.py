from modules.base_module import BaseModule

class EchoLink(BaseModule):
    def __init__(self):
         super().__init__("Echo-Link")

    def initialize(self):
        print("[Echo-Link] Module initialized.")

    def shutdown(self):
        print("[Echo-Link] Module shutdown.")

    def on_system_start(self, data):
        print("[Echo-Link] System startup event received.")
