#!/usr/bin/env python3 


import time
import asyncio
from threading import Thread


async def do_some_work(x):
  print('  (Waiting' + str(x) + ')')
  await asyncio.sleep(x)


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

def do_actions(message):
  while True:
    print(message)
    time.sleep(1)


print('Test 1: Blocking asyncio call, test message A and B should print after 5 second asyncio call completes.')
loop = asyncio.get_event_loop()
print('  Starting asyncio call which should complete in 5 seconds.')
loop.run_until_complete(do_some_work(5))
print('  Test message A')
print('  Waiting one second then printing message B')
time.sleep(1)
print('  Test message B')

print('Test 2: Batch tasking')
tasks = [
    asyncio.ensure_future(do_some_work(2)), 
    asyncio.ensure_future(do_some_work(5))]
loop.run_until_complete(asyncio.gather(*tasks))

print('Test 3: Off-load to separate thread.')
#new_loop = asyncio.new_event_loop()
loop = asyncio.new_event_loop()
loop.call_soon_threadsafe(do_actions, 'loop message 1')
t1 = Thread(target=start_loop, args=(loop,))
loop = asyncio.new_event_loop()
loop.call_soon_threadsafe(do_actions, 'loop message 2')
t2 = Thread(target=start_loop, args=(loop,))
t1.start()
t2.start()

print('Test 4: Doing work with off-loaded loop')
#new_loop.call_soon_threadsafe(do_actions, 'loop message 1')
print('Test message C')
time.sleep(5)
print('test message D')
print('test message E')
time.sleep(1)
print('test mesage F')
#new_loop.call_soon_threadsafe(do_actions, 'loop message 2')
print('Test message G')
time.sleep(5)
print('test message H')
print('test message I')
time.sleep(1)
print('test mesage J')