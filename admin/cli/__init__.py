import saferoute
import web
import argparse
import socket
import os

__all__ = ['parser']

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()

saferoute.init_parser(subparser)
web.init_parser(subparser)

def main():
  args = parser.parse_args()
  args.func(args)

if __name__ == "__main__":
  main()
