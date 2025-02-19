import json

# Load the JSON data from the file
with open("sample-data.json", "r") as file:
    data = json.load(file)

# Extract relevant information
interfaces = data["imdata"]

# Print header
print("Interface Status")
print("=" * 80)
print("{:<20} {:<10} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Print each interface's details
for interface in interfaces:
    attributes = interface["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else "N/A"
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print("{:<20} {:<10} {:<10} {:<10}".format(dn, descr, speed, mtu))
