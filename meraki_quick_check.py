""" Meraki Quick Check """

# Define Python modules
import os
import tabulate
import meraki

MERAKI_DASHBOARD_API_KEY = os.environ.get("NSCON_MERAKI_API_KEY")

dashboard = meraki.DashboardAPI(MERAKI_DASHBOARD_API_KEY, log_path="logs", print_console=False)

# Get organization details and assign variables
org = dashboard.organizations.getOrganizations()[0]
org_id = org.get('id')
org_name = org.get('name')

# Get list of networks for organization
network_list = dashboard.organizations.getOrganizationNetworks(org_id)
print(f'\nYour organization \"{org_name}\" with ID {org_id} includes the following networks:\n')

# Define table headers and values
headers=["No.", "Network Name", "Network ID", "Devices", "Clients last 24h", "Traffic last 24h"]
table = []

# Iterate through network_list and assign network variables
for network in network_list:
    network_id = network['id']
    network_name = network['name']

    # Get online and offline clients for a network
    clients_online = len(dashboard.networks.getNetworkClients(
        network_id, total_pages='all', statuses='Online'))
    clients_offline = len(dashboard.networks.getNetworkClients(
        network_id, total_pages='all', statuses='Offline'))
    clients = f"{clients_online} Online / {clients_offline} Offline"

    # Get devices of a network for each device model
    devices_list = dashboard.networks.getNetworkDevices(network_id)

    # Set device model variables to zero
    devices_mx = 0
    devices_ms = 0
    devices_mr = 0

    # Iterate through device list and count devices per model
    i = 0
    for device in devices_list:
        device = devices_list[i]

        if "MX" in device['model']:
            devices_mx += 1

        if "MS" in device['model']:
            devices_ms += 1

        if "MR" in device['model']:
            devices_mr += 1

        i+=1

    devices = f"{devices_mx} MX(s), {devices_ms} MS(s), {devices_mr} MR(s)"

    # Get network traffic for a network for the last 24h
    try:
        traffic_all = dashboard.networks.getNetworkTraffic(network_id, timespan=86400)
        i=0
        traffic_sum = 0
        for traffic in traffic_all:
            traffic = traffic_all[i]['recv'] + traffic_all[i]['sent']
            traffic_sum += traffic
            i+=1
        traffic_sum = f"{traffic_sum} bytes"

    # Set traffic sum to n/a in case traffic analysis is not activated on network
    except meraki.exceptions.APIError:
        traffic_sum = "n/a"

    # Add all data to table row and add row to table
    row = [network_name, network_id, devices, clients, traffic_sum]
    table.append(row)

# Print table using the received data
print(tabulate.tabulate(table, headers=headers, tablefmt="fancy_grid", showindex=True))
