from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_PortStatus(event):
	if event.ofp.desc.state == 1:
		log.info("PORT DOWN ")
	else:
		log.info("PORT UP")

def launch():
	core.openflow.addListenerByName("PortStatus", _handle_PortStatus)
	log.info("Port Monitor Running ")

