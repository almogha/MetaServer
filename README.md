# MetaServer

MetaServer is a Python-based server designed to retrieve instance metadata from the Amazon EC2 Instance Metadata Service (IMDS) using IMDSv2.

## Features

- Retrieves and displays metadata from the AWS EC2 Instance Metadata Service (IMDS).
- Utilizes IMDSv2 token-based requests for enhanced security.
- Serves metadata in a structured JSON format over HTTP.

## Requirements

- **Python**: Version 3.7 or higher

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/almogha/MetaServer.git
cd MetaServer
```

### Running on host (EC2)

Ensure all dependencies are installed, then run the application directly.

1. **Install Python 3.9** and the necessary libraries if not already available:

    ```bash
    # Install required packages
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. **Run the Application**:

    ```bash
    python main.py
    ```

    The application will be accessible at `http://localhost:8080/metadata` (default).

## Endpoints

- `GET /metadata`: Returns JSON-formatted metadata for the running instance.

Example response:
```json
{
  "instance-id": "i-1234567890abcdef0",
  "instance-type": "t2.micro",
  ...
}
```

## Configuration

- **Environment Variables**:
  - `PORT`: Specifies the port number on which the server listens. Defaults to `8080`.
