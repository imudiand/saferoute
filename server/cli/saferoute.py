from server import settings

def suite():
    return


def cli_test(args):
    saferoute_suite = suite()
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(saferoute_suite)


__all__ = ['init_parser']

def cli(args):
    if args.action == 'test':
        cli_test(args)
    else:
        raise NotImplementedError('Action not implemented')

def init_parser(parser):
  p = parser.add_parser('saferoute', description='CLI for saferoute server')
  p.add_argument('action', nargs='?',
                 default='public',choices=['test'],
                 help='Run both servers')

  p.set_defaults(func=cli)
