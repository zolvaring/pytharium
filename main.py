#!/usr/bin/env python3


import time
import uuid
from ppretty import ppretty


class Game():
  name = 'test'

  def __init__(self):
    print('Instantiating new game')
    self.name = Game.name
    self.things = []

  #@staticmethod
  def tick(self):
    print('Ticking game.')
    #thing = Thing()
    atom = Atom()
    #print(f'Appending new thing (<{thing}>) to game things (<{self.things}>).')
    print(f'Appending new thing (<{ppretty(atom)}>) to game things (<{ppretty(self.things)}>).')
    self.things.append(atom)


  #@staticmethod
  def loop(self):
    while True:
      tick_time = time.time()
      print(f'Tick time: <{ppretty(tick_time)}>')
      self.tick()
      time.sleep(1)
    
  
class Thing(object):
  def __init__(self):
    print('Instantiating new thing')
    super(Thing, self).__init__()

    id = str(uuid.uuid4())
    print(f'Assigning new thing instance id of <{ppretty(id)}>')
    self.id = id

    print(f'Finished building thing instance: <{ppretty(self)}>')


class Atom(Thing):
  def __init__(self):
    print('Instantiating new atom')
    super(Atom, self).__init__()

    self.element = 'element_placeholder'


if __name__ == '__main__':
  print(f'Game name: <{ppretty(Game.name)}>.')
  game = Game()
  game.loop()