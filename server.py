#!/usr/bin/env python3


import tornado.ioloop
import tornado.web
import asyncio
from threading import Thread
from ppretty import ppretty

from main import Game, Thing, Element, Atom, Hydrogen, Carbon, Oxygen


class MainHandler(tornado.web.RequestHandler):
  def get(self):

    
    
    '''
    display_loop = asyncio.new_event_loop()
    display_loop.call_soon_threadsafe(simple_display_loop, )
    display_loop_thread = Thread(target=start_asyncio_loop, args=(display_loop,))
    display_loop_thread.start()
    '''

    #self.write('Hello world')



    #game.start_loop()
    #self.write("Hello, world")
    #self.write(ppretty(game, seq_length=1000))
    for thing in game.things:
      #self.write('test')
      self.write(f'{ppretty(thing)}<br/>')
      #self.write(f'{ppretty(thing.element)}<br/>')
    

def simple_display_loop():
  #self.write('Hello world')
  #app.write('Hello world')
  #MainHandler.write('Hello world')
  print('test')


def make_app():

  return tornado.web.Application([
    (r"/", MainHandler),
  ])


def start_asyncio_loop(loop):
  asyncio.set_event_loop(loop)
  loop.run_forever()

if __name__ == "__main__":
  app = make_app()
  app.listen(8888)

  print(f'(test) Game name: <{ppretty(Game)}>.')
  print(f'(test) Game name: <{ppretty(Game.name)}>.')
  print(f'(test) Element hill notation: <{Element.hill_notation}>.')
  print(f'(test) Hydrogen hill notation: <{Hydrogen.hill_notation}>.')
  game = Game()

  game_loop = asyncio.new_event_loop()
  #game_loop.call_soon_threadsafe(game.start_loop, )
  game_loop.call_soon_threadsafe(game.loop, )
  game_loop_thread = Thread(target=start_asyncio_loop, args=(game_loop,))
  game_loop_thread.start()

  tornado.ioloop.IOLoop.current().start()