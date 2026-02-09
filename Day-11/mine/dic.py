
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

def get_server_status(server_name):
    #return server_config.get(server_name, {}).get('status', 'Server not found')
    if server_name in server_config:
        return server_config[server_name]['status']
    else:
        return 'Server NOT FOUND'
    #return server_config[server_name]['status'] if server_name in server_config else 'Server not found'     

print(get_server_status('server1'))  # Output: active
print(get_server_status('server2'))  # Output: inactive
print(type(server_config))  # Output: <class 'dict'>