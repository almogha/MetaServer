import logging
import urllib.request

from MetaServer.config import IMDS_BASE_URL, TOKEN_TTL_SECONDS

IMDS_TOKEN_URL = f"{IMDS_BASE_URL}/api/token"
IMDS_METADATA_URL = f"{IMDS_BASE_URL}/meta-data"
TOKEN_HEADER = {"X-aws-ec2-metadata-token-ttl-seconds": TOKEN_TTL_SECONDS}


def get_imds_token():
    """Fetches a token for IMDSv2 requests."""
    try:
        request = urllib.request.Request(
            IMDS_TOKEN_URL, headers=TOKEN_HEADER, method="PUT"
        )
        with urllib.request.urlopen(request) as response:
            logging.info(f"IMDS token fetched")
            return response.read().decode()
    except Exception as e:
        logging.error(f"Error fetching IMDS token: {e}")
        return None


def get_instance_metadata(token, path=""):
    """Recursively retrieves the instance metadata using the IMDSv2 token."""
    headers = {"X-aws-ec2-metadata-token": token}
    url = f"{IMDS_METADATA_URL}/{path}".rstrip("/")
    try:
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request) as response:
            data_list = response.read().decode().splitlines()
            metadata = {}
            for item in data_list:
                item_path = f"{path}/{item}".lstrip("/")
                if item.endswith("/"):
                    metadata[item[:-1]] = get_instance_metadata(token, item_path)
                else:
                    request_item = urllib.request.Request(
                        f"{IMDS_METADATA_URL}/{item_path}", headers=headers
                    )
                    with urllib.request.urlopen(request_item) as item_response:
                        metadata[item] = item_response.read().decode()
            return metadata
    except Exception as e:
        logging.error(f"Error fetching instance metadata at path {path}: {e}")
        return None
