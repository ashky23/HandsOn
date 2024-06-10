from cache import LRUCache
def main():
    lru_cache = LRUCache(cacheCapacity=5)
    while True:
        print("input your option\n1 for set(key, val), 2 for get(key)")
        input_val = int(input())
        if input_val == 1:
            print(">>Enter Key")
            key = input()
            print(">>Enter Value")
            val = input()
            lru_cache.set(key, val)
        elif input_val == 2:
            print(">>Enter Key")
            key = input()
            value = lru_cache.get(key)
            if value == None:
                print("Key doesn't exist")
            else:
                print("Here's the value of your key")
                print(value)
            
main()