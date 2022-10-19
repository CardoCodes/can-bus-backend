import csv

class PacketManager:

    def readPackets(packets_csv_file):
        fieldNames = ['Timestamp', 'Type', 'ID', 'Data']
        with open(packets_csv_file, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldNames, delimiter=';')
            for row in reader:
                print(row)

PacketManager.readPackets('utils/packets.csv')