import Pyro4
@Pyro4.expose
class Salut():
    def salut(self, name):
         return "hello " +name
    def add(self, x,y):
        return x+y
deamon = Pyro4.Daemon()
uri = deamon.register(Salut)
ns =Pyro4.locateNS()
ns.register("uri", uri)
print("Ready. ", uri)
deamon.requestLoop()