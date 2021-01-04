from rpc_test import hello_pb2
import json

request = hello_pb2.HelloRequest()
request.name = "ixnaylol"
res_str = request.SerializeToString()
print(res_str)
print(len(res_str))

# 如何通过字符串反向生成对象
request2 = hello_pb2.HelloRequest()
request2.ParseFromString(res_str)
print(request2.name)
print(len(request2.name))

# 对比json
res_json = {
    "name": "ixnaylol"
}
print(json.dumps(res_json))
print(len(json.dumps(res_json)))
