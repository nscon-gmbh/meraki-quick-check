import requests, os
import json
import meraki

MERAKI_DASHBOARD_API_KEY = os.environ.get("NSCON_MERAKI_API_KEY")

dashboard = meraki.DashboardAPI(MERAKI_DASHBOARD_API_KEY)

org = dashboard.organizations.getOrganizations()[0]
org_id = org.get('id')
org_name = org.get('name')

network_list = dashboard.organizations.getOrganizationNetworks(org_id)

# print(json.dumps(network_list,indent=4))

print(f'\nYour organization \"{org_name}\" with ID {org_id} includes the following networks:')

i=0
for network in network_list:
    network_id = network['id']
    network_name = network['name']
    print(f"\n- Name: {network_name}, ID: {network_id}")

print("\nPlease enter a number to get more health details of a network or press 0 for exit: ")