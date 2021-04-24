package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
    "html/template"
    "fmt"
    "./database"
)


func main() {
    r := gin.Default()
	r.StaticFS("/bower_components", http.Dir("C:/Users/MKXDCCDB/Desktop/GinPra/template/bower_components"))
    r.StaticFS("/dist", http.Dir("C:/Users/MKXDCCDB/Desktop/GinPra/template/dist"))
    r.LoadHTMLFiles("template/starter.html")
    r.GET("/index", func (c *gin.Context) {
        c.HTML(http.StatusOK, "starter.html", gin.H{
            "title":"lll",
        })
    })
    r.Run(":8000") // listen and serve on 0.0.0.0:8080
}