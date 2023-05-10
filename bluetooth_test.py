from bluetooth import *
 
#######################################################
# Scan
#######################################################
 
target_name = "iot_test"   # target device name
target_address = None
port = 1         # RFCOMM port
 
nearby_devices = discover_devices()
 
# scanning for target device
for bdaddr in nearby_devices:
    print(lookup_name( bdaddr ))
    if target_name == lookup_name( bdaddr ):
        target_address = bdaddr
        break
 
if target_address is not None:
    print('device found. target address %s' % target_address)
else:
    print('could not find target bluetooth device nearby')
 
#######################################################
# Connect
#######################################################
 
# establishing a bluetooth connection
try:
    sock=BluetoothSocket( RFCOMM )
    sock.connect((target_address, port))
 
    while True:         
        try:
            recv_data = sock.recv(1024) #sock.recv(bufsize) ->maximum of buffer size

            #receive Data: bytes type so we need to Encode/Decode when using with string
            '''example
            example of Encoding : my_bytes = b"Hello world"
            example of Decoding : my_str = my_bytes.decode('utf-8')
                                  my_str = str(bytes, 'utf-8')
            '''
            


            print('bytes receive : ' ,recv_data)
            print('encode receive : ' ,recv_data.decode('utf-8'))
            #sock.send(recv_data) #rasberry -> smartphone
        except KeyboardInterrupt:
            print("disconnected")
            sock.close()
            print("all done")
except btcommon.BluetoothError as err:
    print('An error occurred : %s ' % err)
    pass