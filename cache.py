class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.cache = {}

    def get(self, key: str) -> str:
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        else:
            return ""

    def set(self, key: str, value: str) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            first_key = next(iter(self.cache))
            self.cache.pop(first_key)

    def rem(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]