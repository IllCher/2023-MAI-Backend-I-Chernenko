from cache import LRUCache          

cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
print(cache.get('Jesse')) # вернёт 'James'
cache.rem('Walter')
print(cache.get('Walter')) # вернёт ''