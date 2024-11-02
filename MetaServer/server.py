import logging
from http.server import HTTPServer

from MetaServer.config import PORT
from MetaServer.metadata_handler import InstanceMetadataHandler


def run_server():
    """Initialize and run the HTTP server."""
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, InstanceMetadataHandler)
    logging.info(f"Starting server on port {PORT}")

    httpd.serve_forever()
