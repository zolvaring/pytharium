#!/usr/bin/env python3


import time
import uuid
from ppretty import ppretty
import random
import itertools


class MolecularBond(object):
  pass


class CovalentBond(MolecularBond):
  pass


class Element(object):
  name = 'element'
  color = 'gray'
  symbol = '?'
  hill_notation = '?'
  electrons = 1

  @classmethod
  def can_make_covalent_bond_with(other_element):
    print('Checking if a covalent bond can be made between two elements.')
    if cls.electrons == other_element.electrons:
      print(f'<{cls.name}> forming covalent bond with <{other_element.name}>.')
      return True
    else:
      print(f'<{cls.name}> is unable to form covalent bond with <{other_element.name}> -- electron counts are not equal.')
      return False


class Carbon(Element):
  name = 'carbon'
  symbol = 'C'
  hill_notation = 'C'
  electrons = 6


class Hydrogen(Element):
  name = 'hydrogen'
  symbol = 'H'
  hill_notation = 'H'
  electrons = 1


class Game():

  elements_lookup = {
    'hydrogen'  : Hydrogen,
    'carbon'    : Carbon
  }

  name = 'test'

  def __init__(self):
    print('Instantiating new game')
    self.name = Game.name
    self.things = []
    

  def tick(self):
    print('Ticking game.')

    remove_ids = None
    molecule = None
    for thing in self.things:
      # Assume thing is an atom
      if random.randint(0, 1) == 1:
        
        other_thing = random.choice(self.things)
        if not thing.id == other_thing.id:
          if (thing.can_react_with(other_thing)):
            molecule = Molecule([thing, other_thing])
            remove_ids = [thing.id, other_thing.id]

    if molecule is not None:
      self.things = list(filter(lambda x: x.id != remove_ids[0] and x.id != remove_ids[1], self.things))
      self.things.append(molecule)

    atom = Atom()
    print(f'Appending new thing (<{ppretty(atom)}>) to game things (<{ppretty(self.things)}>).')
    self.things.append(atom)

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
    print(f'Assigning new thing instance id of <{id}>.')
    self.id = id



class Atom(Thing):
  def __init__(self, element=None):
    print('Instantiating new atom')
    super(Atom, self).__init__()

    if element is None:
      element = random.choice(list(Game.elements_lookup.values()))
    print(f'Assigning newly instantiated atom element <{ppretty(element)}> with name, color, symbol: <{element.name}>, <{element.color}>, <{element.symbol}>.')
    self.element = element
    
    
    print(f'Instatiated new atom: <{ppretty(self)}>.')

  def can_react_with(self, other_atom):
    return self.can_make_covalent_bond_with(other_atom)

  def can_make_covalent_bond_with(self, other_atom):
    print('Checking if a covalent bond can be made between two elements.')
    if not hasattr(other_atom, 'element'):
      print('Other atom does not appear to be an atom!')
      return False
    if self.element.electrons == other_atom.element.electrons:
      print(f'<{ppretty(self)}> forming covalent bond with <{ppretty(other_atom)}>.')
      return True
    else:
      print(f'<{ppretty(self)}> is unable to form covalent bond with <{ppretty(other_atom)}> -- electron counts are not equal.')
      return False



class Molecule(Thing):
  def __init__(self, atoms=None):
    print(f'Instantiating new molecule with atoms: <{atoms}>.')
    super(Molecule, self).__init__()

    if atoms is None:

      print('No atoms provided, randomizing...')
      atoms = []
      number_of_atoms = random.randint(1,3)
      for i in range(number_of_atoms):
        atoms.append(Atom())
      self.atoms = atoms
    else:
      self.atoms = atoms

    print(f'Newly instantiated molecule hill notation: <{self.hill_notation}>.')

  def can_react_with(self, other_thing):
    return False

  @property
  def hill_notation(self):
    hill_notation = str('')
    
    for atom in sorted(self.atoms, key=lambda x: x.element.hill_notation):
      atom_notation = atom.element.hill_notation

      if len(hill_notation) > 0:
        print(f'Checking if current character (<{atom_notation}> matches last character (<{hill_notation}>).')
        if atom_notation == hill_notation[-1]:
          atom_notation = '2'

      print(f'Adding atom notation (<{atom_notation}>) to molecule notation (<{hill_notation}>).')

      hill_notation += atom_notation


    print(f'Returning hill notation: <{hill_notation}>.')
    return hill_notation
        
        





class PeriodicTable():
  hydrogen = Hydrogen




if __name__ == '__main__':
  print(f'(test) Game name: <{ppretty(Game.name)}>.')
  print(f'(test) Element hill notation: <{Element.hill_notation}>.')
  print(f'(test) Hydrogen hill notation: <{Hydrogen.hill_notation}>.')
  game = Game()
  game.loop()