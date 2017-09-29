# -*- coding: utf-8 -*- python3
# Created At 2017.9.30
# For ARP.py
# By R3turn0927
# Github @return0927 | Facebook @R3turn.01 | KakakoTalk @bc1916

from scapy.all import *
from subprocess import getoutput
import threading as 멀티코어

타임아웃 = 2
conf.verb = 0

class 랜네트워크_디스커버리():
    def __init__(클래스):
        클래스.타임아웃 = 5
        클래스.테이블 = {}
        클래스.쓰레드 = []

    def 핑(클래스, 아이피):
        패킷 = IP(dst=아이피, ttl=64)/ICMP()
        응답 = sr1(패킷, timeout=클래스.타임아웃, verbose=0)

        클래스.테이블[아이피] = 응답

    def 핑2(클래스, 아이피):
        결과 = getoutput("ping -c 1 -s 1 %s"%아이피)
        try:
            클래스.테이블[아이피] = 결과.split("\n")[-2][23:24]
            #클래스.테이블[아이피] = 결과.split("\n")[-2][:33] = "1 packets trasmitted, 1 received"
        except Exception as ex:
            클래스.테이블[아이피] = str(ex)


    def 생성(클래스, 아이피대역, B클래스):
        return ".".join(아이피대역.split(".")[:3])+"."+str(B클래스)


    def 트리거(클래스):
        아이피대역 = input("아이피대역을 입력해주세요. /24만 가능\n [192.168.0.0]: ")

        if 아이피대역 == "":
            아이피대역 = "192.168.0.0"

        for B클래스 in range(1, 256):
            클래스.쓰레드.append(멀티코어.Thread(target=클래스.핑2, args=( 클래스.생성(아이피대역, B클래스) ,)))

        for 쓰레드 in 클래스.쓰레드:
            쓰레드.start()

        반복 = True

        while 반복:
            임시 = False

            for 쓰레드 in 클래스.쓰레드:
                if 쓰레드.isAlive():
                    임시 = True
                    break

            if 임시:
                반복 = True
            else:
                반복 = False

        print("\n".join( [ "%30s %s" % ( 키, str(클래스.테이블[키]) ) for 키 in sorted( list(filter( lambda x: 클래스.테이블[x] == '1', 클래스.테이블.keys() )) ) ] ))

핑 = 랜네트워크_디스커버리()
핑.트리거()
