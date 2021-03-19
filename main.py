import socket
import click



def checkPorts(ip, port, timeout):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    conf = sock.connect_ex((ip, port))

    if conf == 0:
        print(f"Port {port} is open!")
    else:
        print(f"Port {port} is closed!")

    sock.settimeout(None)
    sock.close()



def rangePorts(ip, timeout, startPort, endPort):
        for p in range(startPort, endPort):
            print("Start scanning...", p)
            if checkPorts(ip, p, timeout):
                print(f"Port {p} is open")


@click.command()
@click.option('--ip', default=None, show_default=True, help="Checking IPv4 address")
@click.option('--port', default=None, type=int, help="Checking port")
@click.option('--timeout', default=None, type=float, help="Time which program has to show us result")
@click.option('--startport' , type=int, help="Port from we start scanning")
@click.option('--endport', type=int, help="Port on which we end the scan")
def clickMain(ip, port, timeout, startport, endport):

    if not port and startport and endport:
        rangePorts(ip, timeout, startport, endport)
        print("You cant scan port range if you scan one port already")

    if ip and port and timeout:
        checkPorts(ip, port, timeout)
        if not ip and not port and not timeout:
            raise click.UsageError("must provide ip address, port and timeout")


if __name__ == "__main__":
    clickMain()
