package main

import (
	"context"
	"fmt"

	"google.golang.org/grpc"

	"learn_rpc/grpc_test/proto"
)

func main() {
	conn, err := grpc.Dial("127.0.0.1:8080",grpc.WithInsecure())
	if err != nil{
		panic(err)
	}
	defer conn.Close()

	c := proto.NewGreeterClient(conn)
	r, err := c.SayHello(context.Background(),&proto.HelloRequest{Name:"ixnaylolllll"})
	if err != nil{
		panic(err)
	}
	fmt.Println(r.Message)
}