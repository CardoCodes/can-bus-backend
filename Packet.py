from dataclasses import dataclass

@dataclass
class Packet:
    timestamp: str
    packet_type: int
    packet_ud: str
    data: str