package main

import (
	"log"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	router.GET("/check", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "server is working",
		})
	})

	log.Print("Listening for requests in :5000")
	router.Run(":5000")
}