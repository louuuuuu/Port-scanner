

#imports
#--------------------------------
import socket
#--------------------------------


print("!!!!!!!!!!!!!!!!!!!!")
print("!!!!!!!!!!!!!!!!!!!!")
print("Port scanner")
print("!!!!!!!!!!!!!!!!!!!!")
print("!!!!!!!!!!!!!!!!!!!!")






#lists aviable commands
def commandhelp():
    print("COMMANDS")
    print("port - port scanner : ARGS [HOST] [PORT] - [PORT]")
    print("")




#port command
#scans TCP ports and looks for open ports. 
def port(target, port1, port2):
    finished = []

    #Validate port range
    if int(port1) > int(port2):
        print("invalid port range")


    # Validate port boundaries
    if int(port1) <= int(port2):
        if int(port2) >= int(65536):
            print("Select ports between 0 and 65535")
        if int(port2) <= int(65536):
            try:
                print("PORT SCANNER")
                print(f"host {target}    :    port {port1}-{port2}")

                for port in range(int(port1), int(port2) + 1):

                    #starts connecting

                    print(f"{port}")
                    #↓ ensures the socket is closes automatically when not needed
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:# AF_INET = IPv4 SOCK_STREAM = TCP
                        sock.settimeout(0.1) #scanning speed
                        result = sock.connect_ex((target, port))
                        portlist = "0"

                        #gets header

                        try: #gets banner
                            sock.sendall(f"HEAD / HTTP/1.1\r\nHost: {target}\r\n\r\n".encode())
                            banner = sock.recv(4096).decode(errors="ignore").strip()
                        except socket.timeout:
                            banner = "TIMED OUT"        
                        except Exception:
                            banner = "Unavailable"


                        #gets service
                        
                        try: 
                            service_name = socket.getservbyport(port, "tcp")
                        except OSError:
                            service_name = "Unknown"


                        try: 
                            if result == 0: # 0 = port open
                                portlist = port
                                print(f"found - {port} - service {service_name} banner - {banner}")

                                finished.append(f"OPEN PORTS:{portlist} | Service:{service_name} | STATUS:{banner}\n\n")


                        except socket.gaierror:
                            print("\nHostname could not be resolved.")
                        except socket.error:
                            print("\nCouldn't connect to server.")



            except Exception as error:
                print(error)
                


            print("finished scanning")
            print("\n\n")
            print("\n".join(finished))

        



#starts inputs

print("What method would you like to go with? | help\n")
while True:
    try:
        while True:
            x = input("")


            if x =="help":
                commandhelp()

            elif x.startswith("port"):
                try:
                    x.strip()
                    command, ip, pp, pp2 = x.split()
                    port(ip,pp,pp2)
                except ValueError as e:
                    print(e)
                    continue
            else:
                print("not a command")

    except TypeError as e:
        print(e)
        continue




"""
Disclaimer:
This tool is intended for educational purposes only. Only scan systems
you own or have explicit permission to test.
"""