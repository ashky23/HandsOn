package main

import (
	"fmt"
	"os"

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

	// create a queue named - jobs
	queue, err := channel.QueueDeclare(
		"jobs", 	// name
		false,     	// durable
		false,     	// auto delete
		false,     	// exclusive
		false,     	// no wait
		nil,       	// args
	)
	if err != nil {
		panic(err)
	}
	
	// get command line arg
	custom_mssg := os.Args[1:]
	mssg := fmt.Sprintf("I am testing RabbitMQ with the custom mssg: %v ", custom_mssg)
	//publish a message over that queue
	err = channel.Publish(
		"",        	// exchange
		"jobs", 	// key
		false,     	// mandatory
		false,     	// immediate
		amqp.Publishing{
			ContentType: "text/plain",
			Body:        []byte(mssg),
		},
	)
	if err != nil {
		panic(err)
	}

	fmt.Println("Queue status: ", queue)
	fmt.Println("Successfully publised to RabbitMQ!")
}