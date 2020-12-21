package main

import (
	"fmt"
	"net/rpc"
)

func main() {
	//1.建立连接
	client, err :=rpc.Dial("tcp", "localhost:1234")
	if err != nil{
		panic("连接失败")
	}
	var reply string //有默认值
	//var reply *string = new(string)
	err = client.Call("HelloService.Hello","ixnay",&reply)
	//err = client.Call("HelloService.Hello","ixnay",reply)
	if err != nil{
		panic("调用失败")
	}
	fmt.Println(reply)
	//fmt.Println(*reply)
}

