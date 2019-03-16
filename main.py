#!/usr/bin/env python3


#import threading
#import 
#from multiprocessing import Pool
import time
#import threading


#class Meta():

#  def __init__(self):
#    self.start_time

#  @property
#  time = time.time()


class Game():

  name = 'test'

  def __init__(self):

    self.name = Game.name
    #self.start_time = time.time()

  @staticmethod
  def tick():
    print('Ticking game.')

  @staticmethod
  def loop():
    while True:
      Game.tick()
      time.sleep(1)
    

#def main_loop():
#  threading.Timer(1, Game.tick).start()

if __name__ == '__main__':
  print(f'Game name: {Game.name}.')
  #main_loop()
  Game.loop()



  #print('Instantiating new Game...')
  #game = Game()
  #print(f'Instantiated new game <{game}> with name, start_time: <{game.name}>, <{game.start_time}>.')
  #Game.tick()
  #threading.Timer(1.0, Game.tick).start()
  #pool = Pool(processes=1)
  #print('Starting main loop...')
  #while True:
    #time_interval = 1
    #print(f'Setting tick delay with start_time, delay, current_time: <{game.start_time}>, <{time_interval}>, <{time.time()}>.')
    #time.sleep(game.start_time + time_interval - time.time())
  #  time.sleep(1 - time.monotonic() % 1))
  #  Game.tick()
  #threading.Timer(1, Game.tick).start()

