import logging
import sys

from MetaServer.server import run_server

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO, stream=sys.stdout, format="%(asctime)s - %(message)s"
)

if __name__ == "__main__":
    run_server()
