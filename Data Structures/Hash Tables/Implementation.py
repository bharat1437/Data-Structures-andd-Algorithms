# Hash tables are implemented in all coding languages. In python it is called dictionary.
# All the keys are converted into its hash equivalent like MD5 generator will generate hash of any string value.
# Hash value is then  mapped to memory address and both key & value are stored at that memory address.
# http://www.miraclesalad.com/webtools/md5.php

# All the hash table have time complexity of O(1) for all operations like insert, delete, search
# However there is drawback when multiple key values are converted to same memory address. This will cause multiple keys
# residing at same memory location and this will cause O(n) complexity. This is called memory collision in hash table.

import array as arr

class myHashTable:
    def __init__(self, length):
        self.length = length
        self.hashArray = [None] * length

    def getHash(self, key):
        sethash = 0
        for c in list(key):
            sethash = (sethash + ord(c) * list(key).index(c)) % self.length
        return sethash

    def set(self, key, value):
        address = self.getHash(key)
        if self.hashArray[address] is None:
            self.hashArray[address] = []
        self.hashArray[address].append([key, value])

    # get is also O(n) since we are iterating through list to find key
    def get(self, key):
        address = self.getHash(key)
        block = self.hashArray[address]
        if block is None:
            return None
        else:
            for item in block:
                if item[0] == key:
                    return item[1]

    # get keys will have to iterate through all items to find keys this is O(n) operation
    def getKeys(self):
        keys = []
        for item in self.hashArray:
            if item is not None:
                for items in item:
                    keys.append(items[0])
        return keys

    # O(n) operation
    def getValues(self):
        values = []
        for item in self.hashArray:
            if item is not None:
                for items in item:
                    values.append(items[1])
        return values


hash1 = myHashTable(2)
hash1.set("apple", 24)
hash1.set("mangoes", 32)
hash1.set("grapes", 52)
print(hash1.get("grapes"))
print(hash1.hashArray)
print(hash1.getKeys())
print(hash1.getValues())
