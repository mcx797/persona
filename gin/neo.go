package main

import (
	"fmt"
    "neogo"
    //"strconv"
    "encoding/json"
)
/*
func tempH(w http.ResponseWriter, r *http.Request) {
    t, err := template.ParseFiles("./hello.tmpl")
    if err != nil {
        fmt.Println("trouble in 12")
    }
    err = t.Execute(w, "小王子")
    if (err != nil ) {
        fmt.Println("%v", err)
        return
    }
}
*/

type commitNode struct {
    //Id              int  `json:id`
    Sha             string  `json:"sha"   form:"sha"`
    Message         string  `json:"message"   form:"message"`
    Commit_date     string  `json:"commit_date"   form:"commit_date"`
    Committer_name  string  `json:"committer_name"    form:"committer_name"`
    Author_name     string  `json:"author_name"   form:"author_name"`
}

func main() {
    commitNodes := make([]commitNode, 0)
    var dbUri string = "bolt://localhost:7687"
	var userName string = "neo4j"
	var password string = "m19990124"
	driver, err := neogo.CreateDriver(dbUri, userName, password)
    if (err != nil) {
        fmt.Println(err)
    }
    var cypher string = "MATCH (n:commit) where n.root = 1 return n"
	data, err := neogo.NodeQuery(driver, cypher)
	if (err != nil) {
		fmt.Println(err)
	}
	//fmt.Println(data)
	for _, value := range data {
        node := commitNode{//strconv.FormatInt(value.Id, 10),
            value.Props["sha"].(string), 
            value.Props["message"].(string), 
            value.Props["commit_date"].(string), 
            value.Props["committer_name"].(string), 
            value.Props["author_name"].(string)}
        commitNodes = append(commitNodes, node)
    }
    buf, err := json.MarshalIndent(commitNodes, "", " ")
        if err != nil {
            fmt.Println("err = ", err)
            return
        }
        fmt.Println("buf = ", string(buf))
    neogo.CloseDriver(driver)
}