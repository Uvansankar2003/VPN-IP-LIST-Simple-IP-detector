# from VPN_Checker import Ip


all_ip_path   = "full_ip_list.txt"
nord_ip_path  = "NordVPN.txt"
forti_ip_path = "fortiVPN.txt"
ghost_ip_path = "cyberghostVPN.txt"
block_ip_path = "blocklist_ip.txt"

all_ip_LIST   = []
nord_ip_LIST  = []
forti_ip_LIST = []
ghost_ip_LIST = []
block_ip_LIST = []

#program 

with open(all_ip_path,"r") as data:
    list_value = data.readlines()
    length =len(list_value)
    print(length)
    for x in list_value:
        x = x.replace("\n","")
        all_ip_LIST.append(x)
        
with open(nord_ip_path,"r") as data:
    list_value = data.readlines()
    length =len(list_value)
    print(length)
    for x in list_value:
        x = x.replace("\n","")
        nord_ip_LIST.append(x)
        
with open(forti_ip_path,"r") as data:
    list_value = data.readlines()
    length =len(list_value)
    print(length)
    for x in list_value:
        x = x.replace("\n","")
        forti_ip_LIST.append(x)
        
with open(ghost_ip_path,"r") as data:
    list_value = data.readlines()
    length =len(list_value)
    print(length)
    for x in list_value:
        x = x.replace("\n","")
        ghost_ip_LIST.append(x)
        
with open(block_ip_path,"r") as data:
    list_value = data.readlines()
    length =len(list_value)
    print(length)
    for x in list_value:
        x = x.replace("\n","")
        block_ip_LIST.append(x)
        
#program to find IP in list 
            
x = str(input("Enter IP Address :"))       
if x in all_ip_LIST or x in nord_ip_LIST or x in forti_ip_LIST or x in ghost_ip_LIST or x in block_ip_LIST:

    if x in nord_ip_LIST:
        print("Nord VPN IP DETECTED")
    elif x in forti_ip_LIST:
        print("Forti VPN IP DETECTED")
    elif x in ghost_ip_LIST:
        print("Cyber Ghost VPN IP DETECTED")
    elif x in block_ip_LIST:
        print("BLOCK LISTED IP DETECTED")
    elif x in all_ip_LIST:
        print("VPN/Proxy IP DETECTED")
else:
    print("NOT DETECTED")
