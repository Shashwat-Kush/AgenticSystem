class VectorMemory:
    def __init__(self, db_uri=None):
        # you’ll wire a real vector DB here later
        self.store_data = []

    def store(self, key, value):
        self.store_data.append((key, value))

    def get_all(self):
        return self.store_data

    def retrieve(self, query):
        # simple keyword‐match stub
        return [v for k, v in self.store_data if query in k or query in v]