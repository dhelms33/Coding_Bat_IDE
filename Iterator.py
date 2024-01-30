class Iterator:
    def __init__(self,name):
        self.name = name
    def front_times(str,n):
        front = str[0:3]
        if len(str) < 3:
            front = str[0:]
        start = ""
        for i in range(n):
            start += front
        return start
    
    obj = Iterator("Hello!")
    obj.front_times("Hello", 3)