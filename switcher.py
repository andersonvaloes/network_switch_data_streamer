import pickle
import socket
import struct

class Switcher:

    obj_data = object()
    ip_host = str()
    port_host = int()
    clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def __init__(self, obj_data_sender, ip_host = "localhost", port_host = 8089):
        self.ip_host = ip_host
        self.port_host = port_host
        self.clientsocket.connect((self.ip_host, self.port_host))
        self.obj_data = obj_data_sender

    # def linker(self, obj_data_sender):
    #     self.obj_data = obj_data_sender

    def send_data(self, flow_number):
        function = self.obj_data.get_data_function_giver(flow_number)
        data_to_send = pickle.dumps(function())
        self.clientsocket.sendall(struct.pack("L", len(data_to_send)) + struct.pack("L", flow_number) + data_to_send)

    def send(self): # implement here the switch part
        self.send_data(0)