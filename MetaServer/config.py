import os

IMDS_BASE_URL = os.environ.get("IMDS_BASE_URL", "http://169.254.169.254/latest")
TOKEN_TTL_SECONDS = os.environ.get("TOKEN_TTL_SECONDS", "21600")
PORT = int(os.environ.get("PORT", 8080))
