package main

import (
	"fmt"
	"net"
	"net/rpc"
	"net/rpc/jsonrpc"
	"time"
)



type HelloService struct {
}

func (s *HelloService) Hello(request string, reply *string) error {
	//返回值是通过修改reply的值
	*reply = "hello, " + request
	return nil
}

func main() {
	//1.实例化一个server
	listener, _ := net.Listen("tcp", ":1234")

	//2.注册处理逻辑
	_ = rpc.RegisterName("HelloService", &HelloService{})
	//3.启动服务
	for {
		conn, _ := listener.Accept() //当一个新的连接进来的时候
		go rpc.ServeCodec(jsonrpc.NewServerCodec(conn))
		fmt.Println(time.Now())
	}
}
