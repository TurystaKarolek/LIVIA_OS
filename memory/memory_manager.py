class MemoryManager:
    def __init__(self):
        self.memory = []

    def store(self, entry):
        self.memory.append(entry)

    def recall(self):
        return self.memory
