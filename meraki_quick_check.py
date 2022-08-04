""" Modules """
import os
import tabulate
import meraki

MERAKI_DASHBOARD_API_KEY = os.environ.get("NSCON_MERAKI_API_KEY")

dashboard = meraki.DashboardAPI(MERAKI_DASHBOARD_API_KEY, log_path="logs", print_console=False)

org = dashboard.organizations.getOrganizations()[0]
org_id = org.get('id')
org_name = org.get('name')

network_list = dashboard.organizations.getOrganizationNetworks(org_id)

# print(json.dumps(network_list,indent=4))

print(f'\nYour organization \"{org_name}\" with ID {org_id} includes the following networks:\n')

# Define table headers and values
headers=["No.", "Network Name", "Network ID", "Devices", "Clients last 24h", "Traffic last 24h", "Events last 24h"]
table = []

for network in network_list:
    network_id = network['id']
    network_name = network['name']
    clients_online = len(dashboard.networks.getNetworkClients(network_id, total_pages='all', statuses='Online'))
    clients_offline = len(dashboard.networks.getNetworkClients(network_id, total_pages='all', statuses='Offline'))
    clients = f"{clients_online} Online / {clients_offline} Offline"

    # Get network traffic for network_id for last 24h
    # try:
    #     traffic = dashboard.networks.getNetworkTraffic(network_id, timespan=86400)
    # except meraki.exceptions.APIError:
    #     traffic = "n/a"

    # Get devices for network_id for each model
    devices_all = dashboard.networks.getNetworkDevices(network_id)
    mx=0
    ms=0
    mr=0
    i=0
    for device in devices_all:
        device = devices_all[i]
        if "MX" in device['model']:
            mx+=1
        if "MS" in device['model']:
            ms+=1
        if "MR" in device['model']:
            mr+=1
        i+=1
    
    devices = f"{mx} MX(s), {ms} MS(s), {mr} MR(s)"

    # Add data to table row and add row to table
    row = [network_name, network_id, devices, clients]
    table.append(row)

#print(table)
print(tabulate.tabulate(table, headers=headers, tablefmt="fancy_grid", showindex=True))

