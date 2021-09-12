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

	router.GET("/add", func(c *gin.Context) {

		// get post body content and save it into file.
		inputFileName := "tmp.orchx"
		log.Print("inputFileName: ", inputFileName)

		cmd := exec.Command("python3", "/orchestra-parser/orchestra_parser/src/orchx2json.py")//inputFileName)
		
		out, err := cmd.Output();
		message := string(out)
		if err != nil { 
			message = err.Error()
			log.Print("Error: ", err)
		}  

		log.Print("Out: ", message)
		c.JSON(200, gin.H{			
			"message": message,
		})

		log.Print("here: add")
	})

	router.POST("/add", func(c *gin.Context) {

		// get post body content and save it into file.
		inputFileName := "tmp.orchx"

		cmd := exec.Command("ls -la; cd /orchestra-parser;", "poetry", "run", "orchx2json", inputFileName)

		if err := cmd.Run(); err != nil { 
			log.Print("Error: ", err)
		}   

		log.Print("here: add")
	})

	

	log.Print("Listening for requests in :5000")
	router.Run(":5000")
}