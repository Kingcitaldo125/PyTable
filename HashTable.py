class HashTable():
	def __init__(self, size):
		self.size = size
		self.n_elems = 0
		self.keys = set()
		self.container = [[] for i in range(self.size)]
		self.load_factor = 0

	def hash_function(self, key, size):
		chrs = 2
		key=str(key)
		for i in key:
			chrs += ord(i)
		return chrs % size

	def get_item(self, key):
		if key not in self.keys:
			return None

		hres = self.hash_function(key, self.size)
		for itm in self.container[hres]:
			if itm[0] == key:
				return itm[1]

		return None

	def _resize(self):
		new_size = self.size*2
		container = [[] for i in range(new_size)]
		
		for itm in self.container:
			for i in itm:
				key = i[0]
				val = i[1]
				hsh = self.hash_function(key, new_size)
				container[hsh].append([key, val])

		self.container = container
		self.size = new_size

	def insert(self, key, val):
		if key in self.keys:
			print("Key already exists in structure.")
			return

		print("inserting", key, val)
		self.keys.add(key)
		hsh = self.hash_function(key, self.size)
		self.container[hsh].append([key, val])
		self.n_elems += 1

		self.load_factor = self.n_elems / self.size
		if self.load_factor >= 0.8:
			print("Load factor hit. Resizing...")
			self._resize()

htable = HashTable(6)

htable.insert('Paul', 27)
htable.insert('Jim', 45)
htable.insert('Dave', 38)
htable.insert('Harry', 40)

print("htable.keys", htable.keys)
print("htable.container", htable.container)

htable.insert('Fred', 18)

print("htable.keys", htable.keys)
print("htable.container", htable.container)

#'''
get=lambda x: htable.get_item(x)

print(get('Paul'))
print(get('Jim'))
print(get('Dave'))
print(get('Harry'))
print(get('Fred'))
print(get(123))
#'''
