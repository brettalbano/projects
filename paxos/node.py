'''
Provides the Node class
'''

import port
import ethernet

class Node():
  '''
  This class will be the paxos members. It will listen to elections and
  proposals of other nodes and send out information through the port
  and ethernet classes.
  '''

