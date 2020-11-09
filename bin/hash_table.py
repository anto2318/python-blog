class hash:
    def __init__(self):
        self.__d = {}

    def insert(self, key, value):
        self.__d[key] = value

    def delete(self, key):
        print("key", key)
        if key in self.__d.keys():
            del self.__d[key]
            print("Deleted")
        else:
            print("not found")

    def search(self, key):
        print("key", key)
        if key in self.__d.keys():
            print("Value: ", self.__d[key])
        else:
            print("not found")

    def __str__(self):
        for i, j in self.__d.items():
            print(i, j, sep=' : ')
        return ''

hash = hash()

hash.insert('Name', 'Shivam')
hash.insert('Branch', 'CS')
hash.insert('Semester', 6)
hash.insert('Year', 3)

hash.search('Name')
hash.search('Roll_no.')

print("\nAccesing all data: -")
print(hash)

hash.delete('Year')

print("\nAgain accesing all data: -")
print(hash)