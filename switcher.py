import pickle
import socket
import struct
from obj_data_to_send import Obj_data_giver
from network_info import get_ping_stats

class Switcher:
    counter = 0
    obj_data = object()
    functs = None
    flow_number = 0
    n_functs = 0
    ip_host = str()
    port_host = int()
    clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def __init__(self, obj_data_sender, ip_host = "localhost", port_host = 8089):
        self.ip_host = ip_host
        self.port_host = port_host
        self.clientsocket.connect((self.ip_host, self.port_host))
        self.obj_data = obj_data_sender
        self.linker(obj_data_sender)

    def linker(self, obj_data_sender):
        self.functs = obj_data_sender.get_data_function_giver()
        self.n_functs = len(self.functs)
        self.flow_number = self.n_functs - 1

    def send_data(self, flow_number):
        # function = self.obj_data.get_data_function_giver(flow_number)
        data_to_send = pickle.dumps(self.functs[flow_number]())
        self.clientsocket.sendall(struct.pack("L", len(data_to_send)) + struct.pack("L", flow_number) + data_to_send)

    def send(self): # implement here the switch part

        # Attribute to variable flow_number the number that is related to the list of functions
        a = get_ping_stats()
        if(a["rtt_avg"] > 3 and self.flow_number > 0):
            self.flow_number -= 1
        elif(a["rtt_avg"] < 1.5 and self.flow_number < self.n_functs - 1):
            self.flow_number += 1

        # if(self.counter > 125):
        #     flow_number = 0
        # elif(self.counter > 100):
        #     flow_number = 1
        # else:
        #     flow_number = 2
        self.send_data(self.flow_number)


obj = Obj_data_giver()
swt = Switcher(obj)
while True:
    swt.send()


