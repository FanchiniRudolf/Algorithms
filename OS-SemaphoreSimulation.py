class process(object):
   name = ""



   def __init__(self, name):
       self.name = name

   def request(self):
       print()

class semaphor(object):
    counter = 1
    list = []
    critSect = 0

    def __init__(self, crit):
        self.critSect = crit

    def wait(self):
        while (self.counter <=0):
            #busy waiting
            print("hola")
        self.counter -= 1

    def singal(self):
        self.counter += 1

    def insert(self, process):
        self.list.insert(0, process)

    def pop(self):
        if(self.list):
            self.list.pop()


