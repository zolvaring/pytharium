#!/usr/bin/env python3


import time


class Game():

  name = 'test'

  def __init__(self):

    self.name = Game.name

  @staticmethod
  def tick():
    print('Ticking game.')

  @staticmethod
  def loop():
    while True:
      Game.tick()
      time.sleep(1)
    

if __name__ == '__main__':
  print(f'Game name: {Game.name}.')
  Game.loop()

