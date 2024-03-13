class HashTable3:
    ## initiate the hash table
    def __init__(self, m = 10):
        self.MAX = m ## set the maximum capacity of 10
        self.arr = [None for i in range(self.MAX)] ## creates an array with MAX amount of size possible

    ## search function of the hash. return hash
    def get_hash(self, key):
        hash = 0 ## creates a variable to store the hash
        for char in key:
            hash += ord(char) ## creates a loop. for every loop, order of the alphabet will be accumulated.
        return hash % self.MAX ## return the accumulated hash and then mod it with MAX/10 default.
    
    ## retrieve item. confirming if the value is present in the hashtable.
    def __getitem__(self, key):
        h = self.get_hash(key) ## creates var h that is the hash value of key. 
        if self.arr[h] is None: ## if the hash index is empty, abort mission.
            return

        prob_range = self.get_prob_range(h) ## searched for the range of possible hash location.

        ## searched for all of the possible location.
        for prob_index in prob_range:
            element = self.arr[prob_index] ## creates an element var that stores the value of array with the index of prob_index
            if element is None: ## if there's no valu in the array. abort ops.
                return
            if element[0] == key: ## if there's a hash match "element[0]". return the value "element[1]"
                return element[1]

    ## input data into hash table
    def __setitem__(self, key, val):
        h = self.get_hash(key) ## !repeated ## creates a var that stores the hash of the input.
        if self.arr[h] is None: ## if the index of the hash is empty, input key and val into the array. as a dictionary.
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h) ## find a new place to store the item into hash.
            self.arr[new_h] = (key, val)  ## input the item into hash. 
        print(self.arr)                     ## print the array. just checking if it works flawlessly prolly.

    ## looks for a suitable space for your hash to settel by.
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)] ## basically do "create a list in the range of index to the end of the array" + "a list from 0 to the current position of the array"

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index

        raise Exception("Hashmap full")

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return 
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
        print(self.arr)



t = HashTable3(m = 7)
t["merah"] = 100000
t["biru"] = 50000
t["hijau"] = 20000
t["ungu"] = 10000
t["peach"] = 5000
t["abu"] = 2000
t["olive"] = 1000