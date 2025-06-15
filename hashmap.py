class HashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def put(self, key, value):
        idx = hash(key) % self.capacity
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        idx = hash(key) % self.capacity
        bucket = self.buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        idx = hash(key) % self.capacity
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return True
        return False

if __name__ == "__main__":
    hm = HashMap()
    hm.put('x', 10)
    hm.put('y', 20)
    print(hm.get('x'))
    hm.remove('x')
    print(hm.get('x'))
