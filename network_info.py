import json
import pingparsing

def get_ping_stats(destination = "localhost"):
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination_host = destination
    transmitter.count = 3
    result = transmitter.ping()
    a = json.dumps(ping_parser.parse(result).as_dict(), indent=4)
    result = json.loads(a)
    return result


'''
result atributes
{
    "destination": "::1",
    "packet_transmit": 3,
    "packet_receive": 3,
    "packet_loss_count": 0,
    "packet_loss_rate": 0.0,
    "rtt_min": 0.0,
    "rtt_avg": 0.0,
    "rtt_max": 0.0,
    "rtt_mdev": null,
    "packet_duplicate_count": null,
    "packet_duplicate_rate": null
}

install pingparsing 
python -m pip install pingparsing
'''