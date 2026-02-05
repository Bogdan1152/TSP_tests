import pytest
import sys

if __name__ == "__main__":
    args = [
        "--cov=tsp",
        "--cov-report=term-missing"]
    
    exit_code = pytest.main(args)
    sys.exit(exit_code)
