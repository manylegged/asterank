#
# Scoring function for asteroid objects
#
#from bigfloat import *   # TODO use this
import math
import estimate

DEFAULT_RADIUS = 5  # km
DEFAULT_MASS = 1.47e15  # kg

def closeness_weight(obj):
  emoid = 1 if isinstance(obj['GM'], basestring) else obj['moid']
  s = (10-(emoid*emoid)) * 3
  s = s * ((1/obj['ad']) * 100)    # penalize aphelion distance
  # TODO probably get more technical about the orbit
  return s

def price(obj):
  """
  Returns a tuple of $ by two metrics:
    0. Asteroid value per kg in raw materials.
    1. Asteroid $ saved per kg versus sending it up from Earth.
  """
  G = 6.67300e-20   # km^3 / kgs^2

  # mass in kg
  exactmass = False
  if isinstance(obj['GM'], basestring):
    mass = DEFAULT_MASS
  else:
    exactmass = True
    mass = obj['GM'] / G

  """
  # radius in m
  if isinstance(obj['diameter'], basestring):
    if exactmass:
      # If we know the mass, don't make assumptions about radius
      print 'Disqualified', obj['full_name']
      return -1

    # 5km radius by default
    radius = DEFAULT_RADIUS
  else:
    if not exactmass:
      # If we know the radius, don't make assumptions about mass
      # a lot of things meet this test
      #print 'Disqualified', obj['full_name']
      radius = DEFAULT_RADIUS
    else:
      radius = obj['diameter'] / 2

  # vol in km^3
  # TODO switch to ellipsoid vol
  vol = 4/3 * math.pi * math.pow(radius, 3) # model as sphere

  # density in kg/km^3
  #density = mass / vol
  """

  stype = obj['spec_B']
  return [estimate.valuePerKg(stype) * mass,
          estimate.savedPerKg(stype) * mass,
         ]