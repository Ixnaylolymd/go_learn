from concurrent import futures

import grpc

from grpc_hello.proto import hello_pb2, hello_pb2_grpc


class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message=f"你好,{request.name}")


if __name__ == '__main__':
    # 1.实例化server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 2.注册逻辑到server中
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    # 3.启动server
    # server.add_insecure_port('0.0.0.0:50051')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
