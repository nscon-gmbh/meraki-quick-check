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
(venv) $ python meraki_quick_check.py

INFO: For Meraki Dashboard API log files please check the "logs" folder.

Your API Key grants access to the following organizations:

╒═══════╤════════════════╤════════════════════╕
│   No. │ Org Name       │             Org ID │
╞═══════╪════════════════╪════════════════════╡
│     0 │ DevNet Sandbox │             549236 │
├───────┼────────────────┼────────────────────┤
│     1 │ sd-wan         │ 646829496481090802 │
├───────┼────────────────┼────────────────────┤
│     2 │ Test-org       │ 646829496481090803 │
├───────┼────────────────┼────────────────────┤
│     3 │ Adm!n123!      │            1206362 │
╘═══════╧════════════════╧════════════════════╛

Choose one organization no. from list: 0

Your organization "DevNet Sandbox" with ID 549236 includes the following networks:

╒═══════╤══════════════════════════════════╤══════════════════════╤════════════════════════════════════╤════════════════════╤════════════════════╕
│   No. │ Network Name                     │ Network ID           │ Devices                            │ Clients last 24h   │ Traffic last 24h   │
╞═══════╪══════════════════════════════════╪══════════════════════╪════════════════════════════════════╪════════════════════╪════════════════════╡
│     0 │ DevNet Sandbox ALWAYS ON         │ L_646829496481105433 │ 1 MX(s), 2 MS(s), 4 MR(s), 0 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│     1 │ Mike_test_vmx                    │ L_646829496481110685 │ 0 MX(s), 0 MS(s), 0 MR(s), 0 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│     2 │ PKC 3 Python Test                │ L_646829496481111123 │ 0 MX(s), 0 MS(s), 0 MR(s), 0 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│     3 │ Cisco Meraki Test LAB Noa        │ L_646829496481111455 │ 0 MX(s), 0 MS(s), 0 MR(s), 0 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│     4 │ yucansoft.co.uk                  │ L_646829496481111545 │ 0 MX(s), 0 MS(s), 0 MR(s), 0 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│     5 │ DNSMB5-exxxxltelecom-sudparis.eu │ L_646829496481111644 │ 1 MX(s), 0 MS(s), 1 MR(s), 0 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│     6 │ DNENT3-vxxxxxxadiscounttire.com  │ L_646829496481111677 │ 1 MX(s), 1 MS(s), 1 MR(s), 1 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│     7 │ DNSMB3-mxxxx6gmail.com           │ L_646829496481111687 │ 1 MX(s), 1 MS(s), 2 MR(s), 0 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│     8 │ DNSMB1-jxxxxxxxncisco.com        │ L_646829496481111689 │ 1 MX(s), 1 MS(s), 2 MR(s), 0 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│     9 │ DNENT1-kxxxxxugmail.com          │ L_646829496481111690 │ 0 MX(s), 0 MS(s), 0 MR(s), 0 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│    10 │ DNENT2                           │ L_646829496481111704 │ 0 MX(s), 0 MS(s), 0 MR(s), 0 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│    11 │ DNSMB2                           │ L_646829496481111705 │ 0 MX(s), 1 MS(s), 1 MR(s), 0 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│    12 │ vmx_1.1_mike                     │ N_646829496481187875 │ 1 MX(s), 0 MS(s), 0 MR(s), 0 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│    13 │ GLB_Network                      │ N_646829496481188321 │ 0 MX(s), 0 MS(s), 0 MR(s), 0 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│    14 │ vmx_1.2_mike                     │ N_646829496481188541 │ 1 MX(s), 0 MS(s), 0 MR(s), 0 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│    15 │ vmx_1.3_mike                     │ N_646829496481188542 │ 1 MX(s), 0 MS(s), 0 MR(s), 0 MV(s) │ 0 On / 0 Off       │ n/a                │
├───────┼──────────────────────────────────┼──────────────────────┼────────────────────────────────────┼────────────────────┼────────────────────┤
│    16 │ CLUS-22                          │ N_646829496481189507 │ 0 MX(s), 0 MS(s), 0 MR(s), 2 MV(s) │ 0 On / 0 Off       │ n/a                │
╘═══════╧══════════════════════════════════╧══════════════════════╧════════════════════════════════════╧════════════════════╧════════════════════╛
(venv) $ 
```

### DevNet Sandbox

This script was tested with the [Cisco DevNet Meraki Always On sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/a9487767-deef-4855-b3e3-880e7f39eadc?diagramType=Topology). Please double check that the API key provided in the instructions is a valid one and present in the profile of the sandbox user before using it.

## Known issues

There are currently no known issues. Please use [GitHub Issues](https://github.com/nscon-gmbh/meraki-quick-check/issues) to open a new issue by providing a helpful description about the issue.

## Getting help

If you have questions, concerns, bug reports, etc., please create an issue against this repository or get in contact with the author.

## Getting involved

Please get involved by giving feedback on features, fixing certain bugs, building important pieces, etc.

## Author(s)

This project was written and is maintained by the following individuals:

* Daniel Kuhl <kuhl@nscon.de>
