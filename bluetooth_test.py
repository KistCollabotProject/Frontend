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



    while True:
        try:
            recv_data = sock.recv(1024)


            #receive Data: bytes type so we need to Encode/Decode when using with string
            '''example
            example of Encoding : my_bytes = b"Hello world"
            example of Decoding : my_str = my_bytes.decode('utf-8')
                                  my_str = str(bytes, 'utf-8')
            '''
            print('bytes receive : ' ,recv_data)
            print('encode receive : ' ,recv_data.decode('utf-8'))


            #msg = recv_data.decode()[:-2]
            #print("Received : %s" % msg)
        
        except KeyboardInterrupt:
            print("disconnected")
            sock.close()
            print("all done")

except btcommon.BluetoothError as err :
    print("An error occured : %s" %err)
    sock.close()
    pass
