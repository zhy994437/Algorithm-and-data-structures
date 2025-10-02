class HashTable:
    def __init__(self):
        self.size = 26
        self.table = ["never used"] * self.size

    def hash(self, key):
        return ord(key[-1]) - ord('a')

    def insert(self, key):
        hashvalue = self.hash(key)
        index = hashvalue
        while True:
            if self.table[index] == "never used" or self.table[index] == "tombstone":
                self.table[index] = key
                return
            elif self.table[index] == key:
                return  
            index = (index + 1) % self.size
            if index == hashvalue:
                break

    def delete(self, key):
        hashvalue = self.hash(key)
        index = hashvalue
        while True:
            if self.table[index] == key:
                self.table[index] = "tombstone"
                return
            index = (index + 1) % self.size
            if index == hashvalue:
                break

    def getkey(self):
        return [key for key in self.table if key != "never used" and key != "tombstone"]


def main():
    hashtable = HashTable()
    moves = input().split()
    for move in moves:
        action, key = move[0], move[1:]
        if action == 'A':
            hashtable.insert(key)
        elif action == 'D':
            hashtable.delete(key)

    keys = hashtable.getkey()
    print(' '.join(keys))


if __name__ == "__main__":
    main()