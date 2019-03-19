#!/usr/bin/env python3


import time
import uuid
from ppretty import ppretty
import random
import itertools
#import asyncio

# Dumb hack to fix potential asyncio bug
# (https://github.com/jupyter/notebook/issues/3397)
#import nest_asyncio
#nest_asyncio.apply()


class Thing(object):
  def __init__(self):
    print('Instantiating new thing')
    super(Thing, self).__init__()

    id = str(uuid.uuid4())
    print(f'Assigning new thing instance id of <{id}>.')
    self.id = id

    name = 'thing'
    self.name = name


class Atom(Thing):

  name = 'atom'
  color = 'gray'
  symbol = '?'
  hill_notation = '?'
  #electrons = 1
  electrons = [1]

  #def __init__(self, element=None):
  def __init__(self):
    print('Instantiating new atom')
    super(Atom, self).__init__()

    #if element is None:
    #  element = random.choice(list(Game.elements_lookup.values()))
    #print(f'Assigning newly instantiated atom element <{ppretty(element)}> with name, color, symbol: <{element.name}>, <{element.color}>, <{element.symbol}>.')
    #self.element = element
    
    
    print(f'Instatiated new atom: <{ppretty(self)}>.')


  @property
  def valence_electrons(self):
    '''
    Return the number of electrons in the first index (the outer orbit)
    '''
    return self.electrons[0]

  @property
  def missing_valence_electrons(self):
    return int(8 - self.electrons[0])

  def can_react_with(self, other_atom):
    #return self.can_make_covalent_bond_with(other_atom)
    return self.can_make_diatomic_bond_with(other_atom)

  def can_make_covalent_bond_with(self, other_atom):

    # old logic
    '''
    print('Checking if a covalent bond can be made between two elements.')
    if not hasattr(other_atom, 'electrons'):
      print('Other atom does not appear to be an atom!')
      return False
    if self.valence_electrons == other_atom.valence_electrons:
      print(f'<{ppretty(self)}> forming covalent bond with <{ppretty(other_atom)}>.')
      return True
    else:
      print(f'<{ppretty(self)}> is unable to form covalent bond with <{ppretty(other_atom)}> -- electron counts are not equal.')
      return False
    print('Checking if a covalent bond can be made between two elements.')
    if not hasattr(other_atom, 'electrons'):
      print('Other atom does not appear to be an atom!')
      return False
    if self.valence_electrons == other_atom.valence_electrons:
      print(f'<{ppretty(self)}> forming covalent bond with <{ppretty(other_atom)}>.')
      return True
    else:
      print(f'<{ppretty(self)}> is unable to form covalent bond with <{ppretty(other_atom)}> -- electron counts are not equal.')
      return False
    '''

    return False

  def can_make_diatomic_bond_with(self, other_atom):

    if hasattr(other_atom, 'electrons'):

      if (self.name == other_atom.name and 
          self.missing_valence_electrons == other_atom.missing_valence_electrons):
        print(f'{ppretty(self)} forming diatomic bond with another {ppretty(other_atom)}.')
        return True
      else:
        return False

    else:
      return False



#class MolecularBond(object):
#  pass


#class CovalentBond(MolecularBond):
#  pass


#class ElementMetaClass():
#  @property
#  def valence_electrons(self):
#    return self.electrons[0]


class Element(Atom):

  name = 'element'
  color = 'gray'
  symbol = '?'
  hill_notation = '?'
  #electrons = 1
  electrons = [1]


  def __init__(self):
    super(Element, self).__init__()
    print(f'Created new element: <{ppretty(self)}>.')
  

  # Remnant of when this was a component class of atom
  '''
  #@property
  #@classmethod
  #def valence_electrons(cls):
  #  return cls.electrons[0]
  '''

  # Moved to super
  """
  @property
  def valence_electrons(self):
    '''
    Return the number of electrons in the first index (the outer orbit)
    '''
    return self.electrons[0]

  @property
  def missing_valence_electrons(self):
    return int(8 - self.electrons[0])
  """
  
  # Uses super (atom)
  '''
  @classmethod
  def can_make_covalent_bond_with(cls, other_element):
    print('Checking if a covalent bond can be made between two elements.')
    #if cls.electrons == other_element.electrons:
    #if cls.electrons[0] == other_element.electrons[0]
    if cls.valence_electrons == other_element.valence_electrons:
      print(f'<{cls.name}> forming covalent bond with <{other_element.name}>.')
      return Truez
    else:
      print(f'<{cls.name}> is unable to form covalent bond with <{other_element.name}> -- electron counts are not equal.')
      return False
  '''


class Carbon(Element):
  name = 'carbon'
  symbol = 'C'
  hill_notation = 'C'
  electrons = [2,4]

  def __init__(self):
    super(Carbon, self).__init__()
    print(f'Created new element: <{ppretty(self)}>.')


class Hydrogen(Element):
  name = 'hydrogen'
  symbol = 'H'
  hill_notation = 'H'
  atomic_weight = 1.007
  electrons = [1]

  def __init__(self):
    super(Hydrogen, self).__init__()
    print(f'Created new element: <{ppretty(self)}>.')

class Oxygen(Element):
  name = 'oxygen'
  symbol = 'O'
  hill_notation = 'O'
  electrons = [2,6]
  atomic_weight = 15.999

  def __init__(self):
    super(Oxygen, self).__init__()
    print(f'Created new element: <{ppretty(self)}>.')


class Game():

  elements_lookup = {
    'hydrogen'  : Hydrogen,
    'carbon'    : Carbon,
    'oxygen'    : Oxygen
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

    #atom = Atom()
    #atom = Hydrogen()
    atom = random.choice(list(Game.elements_lookup.values()))()
    print(f'Appending new thing (<{ppretty(atom)}>) to game things (<{ppretty(self.things)}>).')
    self.things.append(atom)

  def loop(self):
    while True:
      tick_time = time.time()
      print(f'Tick time: <{ppretty(tick_time)}>')
      self.tick()
      time.sleep(1)
      #await asyncio.sleep(1)

  #def start_loop(self):
  #  asyncio.run(self.loop())
    
  







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
    
    #for atom in sorted(self.atoms, key=lambda x: x.element.hill_notation):
    for atom in sorted(self.atoms, key=lambda x: x.hill_notation):
      #atom_notation = atom.element.hill_notation
      atom_notation = atom.hill_notation

      if len(hill_notation) > 0:
        print(f'Checking if current character (<{atom_notation}> matches last character (<{hill_notation}>).')
        if atom_notation == hill_notation[-1]:
          atom_notation = '2'

      print(f'Adding atom notation (<{atom_notation}>) to molecule notation (<{hill_notation}>).')

      hill_notation += atom_notation


    print(f'Returning hill notation: <{hill_notation}>.')
    return hill_notation
        
        





#class PeriodicTable():
#  hydrogen = Hydrogen




if __name__ == '__main__':
  print(f'(test) Game name: <{ppretty(Game.name)}>.')
  print(f'(test) Element hill notation: <{Element.hill_notation}>.')
  print(f'(test) Hydrogen hill notation: <{Hydrogen.hill_notation}>.')
  game = Game()
  game.loop()