""" Modules """
import os
import tabulate
import meraki

MERAKI_DASHBOARD_API_KEY = os.environ.get("NSCON_MERAKI_API_KEY")

dashboard = meraki.DashboardAPI(MERAKI_DASHBOARD_API_KEY)

org = dashboard.organizations.getOrganizations()[0]
org_id = org.get('id')
org_name = org.get('name')

network_list = dashboard.organizations.getOrganizationNetworks(org_id)

# print(json.dumps(network_list,indent=4))

print(f'\nYour organization \"{org_name}\" with ID {org_id} includes the following networks:\n')

# Define table headers and values
headers=["No.", "Network Name", "Network ID"]
table = []

for network in network_list:
    network_id = network['id']
    network_name = network['name']
    #print(f"\n- Name: {network_name}, ID: {network_id}")
    row = [network_name, network_id]
    #print(row)
    table.append(row)

#print(table)
print(tabulate.tabulate(table, headers=headers, tablefmt="fancy_grid", showindex=True))

print("\nPlease enter a number to get more health details of a network or press \'e\' for exit: ")

"""
Next steps:
- add health overview to table
- implement function to get more health details of a network
- omit logs in output ans specify log folder
"""