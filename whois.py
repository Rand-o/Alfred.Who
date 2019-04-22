import sys
import socket
from workflow import Workflow
from netaddr import valid_ipv4

wf = Workflow()
query = sys.argv[1]
def main(_):
	try:
		if not valid_ipv4(query):
			result = socket.gethostbyname(query)
		else:
			result = socket.gethostbyaddr(query)[0]
		wf.add_item(
			title=str(result),
			subtitle="Copy to clipboard",
			arg=str(result),
			valid=True,
			)
		wf.send_feedback()
		return 0
	except Exception as e:
		wf.add_item(
			title="That doesn't look like a valid IP address (Make sure you are on VPN)",
			subtitle=str(e),
			valid=True,
			)
		wf.send_feedback()
		return 0

if __name__ == '__main__':
	wf.run(main)
	sys.exit(wf.run(main))