package main

import (
	"fmt"

	"github.com/streadway/amqp"
)

func main(){
	fmt.Println("RabbitMQ - producer started!")

	// create a connection
	connection, err := amqp.Dial("amqp://guest:guest@localhost:5672/")
	if err!=nil{
		panic(err)
	}
	defer connection.Close()

	// create a channel using that connection
	channel, err := connection.Channel()
	if err != nil {
		panic(err)
	}
	defer channel.Close()
	
	// declaring consumer with its properties over channel opened
	msgs, err := channel.Consume(
		"jobs", 	// queue
		"",         // consumer
		true,       // auto ack
		false,      // exclusive
		false,      // no local
		false,      // no wait
		nil,        //args
	)
	if err != nil {
		panic(err)
	}

	// print consumed messages from queue
	forever := make(chan bool)
	go func() {
		for msg := range msgs {
			fmt.Printf("Received Message: %s\n", msg.Body)
		}
	}()

	fmt.Println("Waiting for messages...")
	<-forever
}