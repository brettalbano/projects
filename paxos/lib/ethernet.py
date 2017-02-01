'''
Provides the Ethernet Class
'''

import node
import port

class Ethernet():
  '''
  This class will handle the exchange of commands between nodes and will
  connect two and only two nodes together for each Ethernet object.
  '''

  def __init__(self, port1, port2):
    self.port1 = port1
    self.port2 = port2
