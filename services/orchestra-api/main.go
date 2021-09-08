package main

import (
	"log"

	"github.com/gin-gonic/gin"
	"os/exec"
)

func main() {
	router := gin.Default()

	router.GET("/check", func(c *gin.Context) {
		
		c.JSON(200, gin.H{
			"message": "server is working",
		})
	})

	router.GET("/show", func(c *gin.Context) {
		log.Print("here: show")
	})

	router.POST("/add", func(c *gin.Context) {

		// get post body content and save it into file.
		inputFileName := "tmp.orchx"	

		c := exec.Command("cd /orchestra-parser;", "poetry", "run", "orchx2json", inputFileName)

		if err := c.Run(); err != nil { 
			log.Print("Error: ", err)
		}   

		log.Print("here: add")
	})

	

	log.Print("Listening for requests in :5000")
	router.Run(":5000")
}