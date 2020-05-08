import sys
import socket
from pprint import pprint

# from LRUCache import LRUCache
from bloom_filter import BloomFilter
from node_ring import NodeRing
from sample_data import USERS
from server_config import NODES
from pickle_hash import serialize_GET, serialize_PUT
from lru_cache import lru_cache


BUFFER_SIZE = 1024
UDP_IP = "127.0.0.1"
UDP_PORT = 5005


class UDPClient():
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)
        # self.client_ring = self.initializeRing()

    def setRing(self, client_ring):
        return client_ring

    def send(self, request):
        print('Connecting to server at {}:{}'.format(self.host, self.port))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(request, (self.host, self.port))
            response, ip = s.recvfrom(BUFFER_SIZE)
            return response
        except socket.error:
            print("Error! {}".format(socket.error))
            exit()


bloomfilter = BloomFilter(100, 0.2)


def put(key, value, client_ring):
    bloomfilter.add(key)
    return client_ring.get_node(key).send(value)


def delete(key, value, client_ring):
    if bloomfilter.is_member(key):
        return client_ring.get_node(key).send(value)
    else:
        return None


@lru_cache(5)
def get(key, value, client_ring):
    if bloomfilter.is_member(key):
        return client_ring.get_node(key).send(value)
    else:
        return None


def process(udp_clients):
    udp_client = udp_clients
    hash_codes = set()
    client_ring = NodeRing(udp_client)

    # PUT all users.
    for u in USERS:
        data_bytes, key = serialize_PUT(u)
        response = put(key, data_bytes, client_ring)
        hash_codes.add(response)
    print(hash_codes)

    print(
        f"Number of Users={len(USERS)}\nNumber of Users Cached={len(hash_codes)}")

    # for hc in hash_codes:
    #     data_bytes, key = serialize_GET(hc)
    #     fix_me_server_id = 0
    #     response = udp_clients[fix_me_server_id].send(data_bytes)
    #     print(response)


if __name__ == "__main__":
    clients = [
        UDPClient(server['host'], server['port'])
        for server in NODES
    ]

    process(clients)
