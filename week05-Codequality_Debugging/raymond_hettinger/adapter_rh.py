''' Pythonic means "coding beautifully in harmony with
    the language to get the maximum benefits from Python"
    Learn to recognize non-pythonic APIs and to recognize
    good code.  Don't get distracted by PEP 8.  Focus
    first an Pythonic versus NonPython (P vs NP).
    When needed, write an adapter class to convert from
    the former to the latter.
    * Avoid unnecessart packageing in favor of 
      simpler imports
    * Create custom exceptions
    * Use properties instaed of getter methods
    * Create a context manager for recurring
      set-up and teardown logic
    * Use magic methods:
          __len__ instead of getSize()
          __getitem__ instead of getRouteByIndex()
          make the table iterable
    * Add good __repr__ for better dubuggability
'''

# Adapter ###########################################

import jnetool.tools.elements.NetworkElement
import jnetool.tools.Routing

class NetworkElementError(Exception):
    pass

class NetworkElement(object):

    def __init__(self, ipaddr):
        self.ipaddr = ipaddr
        self.oldne = jnetool.tools.elements.NetworkElement(ipaddr)

    @property
    def routing_table(self):
        try:
            return RoutingTable(self.oldne.getRoutingTable())
        except jnetool.tools.elements.MissingVar:
            raise NetworkElementError('No routing table found')

    def __enter__(self):
        return self

    def __exit__(self, exctype, excinst, exctb):
        if exctype == NetworkElementError:
            logging.exception('No routing table found')
            self.oldne.cleanup('rollback')
        else:
            self.oldne.cleanup('commit')
        self.oldne.disconnect()

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.ipaddr)


class RoutingTable(object):

    def __init__(self, oldrt):
        self.oldrt = oldrt

    def __len__(self):
        return self.oldrt.getSize()

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        return Route(self.oldrt.getRouteByIndex(index))


class Route(object):

    def __init__(self, old_route):
        self.old_route = old_route

    @property
    def name(self):
        return self.old_route.getName()

    @property
    def ipaddr(self):
        return self.old_route.getIPAddr()