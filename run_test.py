import pytest
import sys


if __name__ == "__main__":

    args = ["-v"]

    exit_code = pytest.main(args)

    sys.exit(exit_code)


