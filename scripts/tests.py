import sys

import coverage
import pytest


def main():
    cov = coverage.Coverage()
    cov.start()
    pytest.main(sys.argv[1:])
    cov.stop()
    cov.save()
    cov.report()
