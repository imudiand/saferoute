"""Command line interface to interface with jira"""
from mongoengine import connect
import admin.settings
import csv
import sys
import argparse

def cli(args):
    if args.app == 'public':
        from admin.web.app_http import run_debug
    elif args.app == 'saferoute':
        from admin.web.app_http import run_debug
    else:
        raise NotImplementedError("No app exists for %s" % args.app)
    run_debug('0.0.0.0' if args.expose else None, port=args.port)

def init_parser(parser):
    """Initialize parser specific to the stat commands"""
    p = parser.add_parser('web',
                          description='Web debug server')
    p.set_defaults(func=cli)

    p.add_argument('app', nargs='?',
                   default='public',choices=['public'],
                   help='Run both servers')

    p.add_argument('--expose',  '-e',
        dest='expose',default=False,action='store_true',
        help='Expose server over the network')

    p.add_argument('--port',  '-p',
        dest='port',default=3000, type=int,
        help='Port to run debug server')

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    subparsers = argparser.add_subparsers()
    init_parser(subparsers)

    cli_args = argparser.parse_args()
    cli_args.func(cli_args)


