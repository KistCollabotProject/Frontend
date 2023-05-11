from bluetooth import *

#########################
## Scan
##########################

target_name = "Galaxy S8+" #target device name
target_address = "94:8B:C1:01:E2:71"
port = 1 #RFCOMM port

nearby_devices = discover_devices()

for bdaddr in nearby_devices:
    print(lookup_name(bdaddr))
    if target_name == lookup_name(bdaddr):
        target_address = bdaddr
        print("Update target address : ", target_address)
        break

if target_address is not None:
    print("Device found.")
else:
    print("Could not find target bluetooth device nearby")

####################
## Connect
####################

try:
    print("Try to connect Bluetooth socket")
    sock = BluetoothSocket(RFCOMM)
    print("RFCOMM : " ,RFCOMM)
    sock.connect((target_address,port))
    print("Success to connect target_address : ",target_address,"port : ", port)

    sock.bind(("",port))
    sock.listen(1)

    client_socket, address = sock.accept()

    while True:
        try:
            recv_data = client_socket.recv(1024)
            msg = recv_data.decode()[:-2]
            print("Received : %s" % msg)
        
        except KeyboardInterrupt:
            print("disconnected")
            sock.close()
            print("all done")

except btcommon.BluetoothError as err :
    print("An error occured : %s" %err)
    sock.close()
    pass
