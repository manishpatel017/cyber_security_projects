#!/usr/bin/python3
import nmap

def port_scan(start,end,ip):
	scanner = nmap.PortScanner()
	print("\n\n\n----------------------")
	print("-------Scanning-------")
	print("----------------------\n\n\n")
	
	for i in range(start,end+1):

		res = scanner.scan(target,str(i))
		
		res = res['scan'][target]['tcp'][i]['state']
		if (res == 'open'):
		    print(f' -port {i} is {res}.')

if __name__ == "__main__":
    target = input("IP: ")
    start = 1
    top_100 = 100
    top_1000 = 1000
    all = 65545

    print("-----Choose 1 scan-----")
    print("1.Scan 100 ports\n2.Scan 1000 ports\n3.Scan all ports")
    no = int(input("Enter: "))
    if (no == 1):
	    port_scan(start,top_100,target)
    elif (no == 2):
	    port_scan(start,top_1000,target)
    elif (no == 3):
	    port_scan(start,all,target)
    else: 
	    print("unknown option")








