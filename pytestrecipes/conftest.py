from _pytest.config import argparsing


def pytest_addoption(parser: argparsing.Parser):

    parser.addoption(
        '--rand-seed', '--randseed',
        type=float,
        help='the seed to use for tests in the seededrandom package.  If not '
             'provided, the system time will be used as the seed.  To retrieve '
             'the seed used in the previous test run, retrieve the "rand_seed" '
             'key from pytest cache: pytest --cache-show rand_seed.'
    )
    parser.addoption(
        '--reuse-rand-seed',
        action='store_true',
        help='reuse the most recently used seed for tests in the seedable fuzz '
             'package.  Test collection will fail if this and --rand-seed are '
             'both specified, or if this is specified but there is no cached '
             'previous seed value.'
    )
