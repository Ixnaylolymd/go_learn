# 1.json_rpc_client
# import json
# import socket
# 
# request = {
#     "id": "0",
#     "params": ["ymdlol"],
#     "method": "HelloService.Hello"
# }
# 
# client = socket.create_connection(("localhost", 1234))
# client.sendall(json.dumps(request).encode())
# 
# # 获取服务器返回的数据
# rsp = client.recv(1024).decode()
# print(json.loads(rsp))

# 2.http_rpc_client
import requests

rsp = requests.post("http://localhost:1234/jsonrpc", json={"id": "0",
                                                           "params": ["ymdlol"],
                                                           "method": "HelloService.Hello"})
print(rsp.text)
