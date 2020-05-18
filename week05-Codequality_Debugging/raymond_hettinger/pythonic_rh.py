from nettools import NetworkElement

with NetworkElement('171.0.2.45') as ne:
	for route in ne.routing_table:
		print "%15s -> %s" % (route.name, route.ipaddr) 
