import json

def openn(pyfile):
    with open(pyfile, 'r') as file:
        return json.load(file)

def print_(data):
    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU'}")
    print("-" * 80)
    
    
    for i in data["imdata"]:
        attributes = i['l1PhysIf']['attributes']
        DN = attributes['dn']
        description = attributes.get('descr', '')
        speed = attributes['speed']
        MTU = attributes['mtu']
        print(f"{DN:<50} {description:<20} {speed:<10} {MTU:<10}")


data = openn('sample-data.json')   
print_(data)
