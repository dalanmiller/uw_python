







class Storage(list):
    
    def __init__(self,storage):
        self.db = []
        self.db.append(storage)
        

    def __add__(self,x):
        self.db.append(tuple(x))
        return self

    def 


