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
      #print(next(i for i, x in enumerate(employees) if x.name == 'Emp1'))
      #delete_index_0 = next(i for i, x in enumerate(self.things) if x.id == remove_ids[0])
      #delete_index_1 = next(i for i, x in enumerate(self.things) if x.id == remove_ids[1])
      #delete_indexes = [ delete_index_0, delete_index_1 ]
      #print(f'Delete indexes: <{delete_indexes}>.')
      #for delete_index in delete_indexes:
      #  del(self.things, delete_index)

      #list_1 = filter(lambda x: x[3] <= 0.3 and x[2] < 5, list_1)
      self.things = list(filter(lambda x: x.id != remove_ids[0] and x.id != remove_ids[1], self.things))
      #self.things = new_things
    
      self.things.append(molecule)

    
        





    #atom = Atom()

    #molecule = Molecule()
    atom = Atom()
    #atoms = [
    #  Atom()
    #]
    #print(f'Going to create new molecule using atoms: <{atoms}>.')
    #molecule = Molecule(atoms)

    print(f'Appending new thing (<{ppretty(atom)}>) to game things (<{ppretty(self.things)}>).')
    #print(f'Appending new thing (<{ppretty(molecule)}>) to game things (<{ppretty(self.things)}>).')
    #self.things.append(molecule)
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
    #print(f'Assigning new thing instance id of <{ppretty(id)}>')
    print(f'Assigning new thing instance id of <{id}>.')
    self.id = id

    #print(f'Finished building thing instance: <{ppretty(self)}>')
    #print(self)
    #print(ppretty(self))



class Atom(Thing):
  def __init__(self, element=None):
    print('Instantiating new atom')
    super(Atom, self).__init__()

    #self.element = 'element_placeholder'
    if element is None:
      #element = getattr(PeriodicTable, 'hydrogen')
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
  #def __init__(self, composition=None):
    print(f'Instantiating new molecule with atoms: <{atoms}>.')
    super(Molecule, self).__init__()

    if atoms is None:

      #print('No atoms provided, using default...')
      #atoms = [Atom()]

      print('No atoms provided, randomizing...')
      atoms = []
      number_of_atoms = random.randint(1,3)
      #for i in itertools.repeat(None, number_of_atoms):
      for i in range(number_of_atoms):
        atoms.append(Atom())
      self.atoms = atoms
    else:
      self.atoms = atoms

    #if len(atoms > 1):
    #  marked_for_removal = []
    #  for atom in atoms:
    #    found_partner = False
    #    for other_atom in atoms:
    #      if atom.id == other_atom.id:
    #        continue
    #      if atom.can_bind_with(other_atom):
    #        atom.bind_with(other_atom)
    #    if not found_partner:
    #      marked_for_removal.append(atom.id)
          

    #previous_atom = None
    #if len(atoms > 1):
    #  for atom in atoms:
    #    #if previous_atom is not None:
    #    #  previous_atom
    #    for other_atom in atoms:
    #      if atom.id == other_atom.id:
    #        continue
    #      atom.bind_with(other_atom)

    #print(f'Instantiated new molecule: <{ppretty(self)}>.')
    print(f'Newly instantiated molecule hill notation: <{self.hill_notation}>.')

  #@property
  #def test_property(self):
  #  return 'blah'

  def can_react_with(self, other_thing):
    return False

  @property
  def hill_notation(self):
    #print(f'Attempting to get hill notation of molecule: <{ppretty(self)}>...')
    hill_notation = str('')
    
    #atom_notations = []

    
    #for atom in self.atoms.sort(key=lambda x: x.element.hill_notation):
    #for atom in self.atoms:
    #sorted_atoms = self.atoms.sort()
    #for atom in self.atoms.sort():
    for atom in sorted(self.atoms, key=lambda x: x.element.hill_notation):
    #for atom in sorted_atoms:
      atom_notation = atom.element.hill_notation

      #print('Checking if next character in notation is an')

      if len(hill_notation) > 0:
        print(f'Checking if current character (<{atom_notation}> matches last character (<{hill_notation}>).')
        if atom_notation == hill_notation[-1]:
          atom_notation = '2'

      #atom_notation = 'H'
      print(f'Adding atom notation (<{atom_notation}>) to molecule notation (<{hill_notation}>).')
        

      #atom_notations.append(atom_notation)
      #hill_notation.append(atom_notation)

      hill_notation += atom_notation
      #hill_notation += 'H'
    
    #hill_notation.append('H')
    #hill_notation += 'H'


    print(f'Returning hill notation: <{hill_notation}>.')
    #return hill_notation
    #return 'H'
    return hill_notation

    #for atom_notation in atom_notations:
    #  if atom_notation == 'C':
    #    hill_notation.append(atom_notation)

        
        





class PeriodicTable():
  hydrogen = Hydrogen




if __name__ == '__main__':
  print(f'(test) Game name: <{ppretty(Game.name)}>.')
  print(f'(test) Element hill notation: <{Element.hill_notation}>.')
  print(f'(test) Hydrogen hill notation: <{Hydrogen.hill_notation}>.')
  game = Game()
  game.loop()