import json
from http.server import BaseHTTPRequestHandler

from MetaServer.aws_client import get_imds_token, get_instance_metadata


class InstanceMetadataHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handles GET requests on /metadata."""
        if self.path == "/metadata":
            token = get_imds_token()
            if not token:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"Failed to retrieve IMDS token")
                return

            metadata = get_instance_metadata(token)
            if metadata:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(metadata, indent=2).encode())
            else:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"Failed to retrieve instance metadata")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
