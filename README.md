# meraki-quick-check

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/nscon-gmbh/meraki-quick-check)

Quick Meraki Dashboard API Check
 
## Description

This script provides a quick and brief overview of the organization networks from the Meraki Dashboard API v1 you have access to using your Meraki API key. 

If you want to get a complete health check please take a look at the [Meraki Health Check](https://developer.cisco.com/codeexchange/github/repo/obrigg/meraki-health-check/) repository.

## Installation

Note: This installation was done on macOS Monterey 12.4 using Python 3.9.13.

1. Clone the repository and change into new directory:

```bash
git clone https://github.com/nscon-gmbh/meraki-quick-check.git
cd meraki-quick-check
```

2. Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install Python modules used in the script:

```bash
pip install -r requirements.txt
```

## Configuration

There is no need for any further configuration. It is optional to use your Meraki API key as environment variable called "YOUR_MERAKI_API_KEY" in the script. Otherwise you will get a prompt to paste your API key during execution of the script. All log files from the Meraki Dashboard API will be stored at the "logs" folder.

Make sure to have a valid Meraki API key. Please check the [Meraki Dashboard API documentation](https://developer.cisco.com/meraki/api-v1/) for any further information.


## Usage

Run the script:

```bash
python meraki_quick_check.py
```

Example output:

```bash
(venv) danielkuhl@localhost meraki-quick-check % python meraki_quick_check.py 

Enter your Meraki API key: <HERE IS YOUR API KEY>

Your organization "YOUR ORG NAME" with ID 123456 includes the following networks:

╒═══════╤═════════════════╤══════════════════════╤═══════════════════════════╤════════════════════════╤════════════════════╕
│   No. │ Network Name    │ Network ID           │ Devices                   │ Clients last 24h       │ Traffic last 24h   │
╞═══════╪═════════════════╪══════════════════════╪═══════════════════════════╪════════════════════════╪════════════════════╡
│     0 │ PROD_NET        │ L_123456789012345678 │ 2 MX(s), 6 MS(s), 8 MR(s) │ 45 Online / 9 Offline  │ 123456 bytes       │
├───────┼─────────────────┼──────────────────────┼───────────────────────────┼────────────────────────┼────────────────────┤
│     1 │ TEST_NET        │ L_098765432109876543 │ 1 MX(s), 1 MS(s), 1 MR(s) │ 0 Online / 0 Offline   │ n/a                │
╘═══════╧═════════════════╧══════════════════════╧═══════════════════════════╧════════════════════════╧════════════════════╛
```

## Known issues

There are currently no known issues. Please use [GitHub Issues](https://github.com/nscon-gmbh/meraki-quick-check/issues) to open a new issue by providing a helpful description about the issue.

## Getting help

If you have questions, concerns, bug reports, etc., please create an issue against this repository or get in contact with the author.

## Getting involved

Please get involved by giving feedback on features, fixing certain bugs, building important pieces, etc.

## Author(s)

This project was written and is maintained by the following individuals:

* Daniel Kuhl <kuhl@nscon.de>
