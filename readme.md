# QR Code Generator

A simple Docker-based QR code generator for URLs.

## QR Code for GitHub Homepage

Scan this QR code to visit my GitHub homepage:

![QR Code for GitHub Homepage](qr_codes/github.com_20250402_025043.png)

## Features

- Generate QR codes for any URL
- Automatically saves QR codes with timestamped filenames
- Logs all operations
- Runs in a Docker container for easy deployment and isolation

## Prerequisites

- Docker
- Docker Compose

## Setup and Usage

### Building and Running with Docker Compose

1. Clone this repository:
   ```
   git clone <repository-url>
   cd qr-docker
   ```

2. Build and run the container:
   ```
   docker-compose up
   ```
   This will generate a QR code for the default URL (http://github.com/ladyarachne) and save it to the `qr_codes` directory.

3. To generate a QR code for a different URL, modify the `command` in `docker-compose.yml` or run:
   ```
   docker-compose run --rm qr-generator --url "https://your-custom-url.com"
   ```

### Running Without Docker

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the script:
   ```
   python main.py --url "https://your-custom-url.com"
   ```

## Command Line Arguments

- `--url`: The URL to encode in the QR code (default: http://github.com/ladyarachne)
- `--output`: Custom output path for the QR code image (optional)

## Project Structure

```
.
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Docker Compose configuration
├── main.py                 # Main Python script
├── requirements.txt        # Python dependencies
├── qr_codes/               # Directory for generated QR codes
└── logs/                   # Directory for logs
```

## License

[MIT License](LICENSE)
