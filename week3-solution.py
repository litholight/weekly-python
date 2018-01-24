def line_to_dict(line):
    
    ip_address = line.split()[0]

    timestamp_start = line.index('[') + 1
    timestamp_end = line.index(']')
    timestamp = line[timestamp_start:timestamp_end]

    request_start = line.index('"') + 1
    request_end = line[request_start:].index('"')
    request = line[request_start:request_start+request_end]

    return {'ip address':ip_address, 'timestamp':timestamp, 'request':request} 
def logtodict(filename):
    return[line_to_dict(line) for line in open(filename)]

print(logtodict('mini-access-log.txt'))
