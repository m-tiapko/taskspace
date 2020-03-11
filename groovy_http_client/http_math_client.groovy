#!/usr/bin/env groovy
import groovy.json.JsonSlurper


public class HttpResponse {
    String body;
    String message;
    Integer statusCode;
    boolean failure = false;

    public HttpResponse(HttpURLConnection connection) {
        this.statusCode = connection.responseCode;
        this.message = connection.responseMessage;

        if (statusCode == 200 || statusCode == 201) {
            this.body = connection.content.text;//this would fail the pipeline if there was a 400
        } else {
            this.failure = true;
            this.body = connection.getErrorStream().text;
        }

        connection = null; //set connection to null for good measure, since we are done with it
    }   
}

def do_POST(args) {
    String PORT = "8080"
    String ADDR = "127.0.0.1"

    def dataOperation = [
        "operation": "${args[1]}",
        "arg1": "${args[0]}",
        "arg2": "${args[2]}"
    ]
    String json = groovy.json.JsonOutput.toJson(dataOperation)

    URL url = new URL ("http://${ADDR.toString()}:${PORT.toString()}")
    HttpURLConnection connection = url.openConnection()

    connection.setRequestMethod("POST")
    connection.setRequestProperty("Content-Type", "application/json")
    connection.doOutput = true

    def writer = new OutputStreamWriter(connection.outputStream)
    writer.write(json)
    writer.flush()
    writer.close()

    connection.connect()

    HttpResponse response = new HttpResponse(connection)
    if (response.isFailure()){
        "Something went wrong with status code $response.statusCode"
    }
    else{
        def dict = new JsonSlurper().parseText(response.body) as Map
        dict["value"]
    }
}

def args_handler() {
    if ( this.args.size() != 3)
    {
        println "You have to put 3 params"
        println "For instance: 5 + 9"
        return 1
    }
    else if ( !['/','*','-','+'].contains(this.args.getAt(1)) )
    {
        println "Your second parameter has to be '*', '/', '-', '+'"
        return 1
    }
    try{
        def num1 = args[0].toDouble()
        def num2 = args[2].toDouble()
    }catch(NumberFormatException){
        println "Your params has to be numbers"
        return 1
    }

    switch(this.args[1]) 
    {
        case '+': this.args[1] = "add"; break
        case '-': this.args[1] = "sub"; break
        case '/': this.args[1] = "div"; break
        case '*': this.args[1] = "mult"; break
        default: this.args[1] = ""; break
    }
    args
}

def main() {
    def line = args.join(" ") + " ="
    params = args_handler()
    if (params == 1){
        return 1
    }
    def result = do_POST(params)
    if ("wrong".contains(result)){
        println("$result")
    }else{
        println("$line $result")
    }
}

main()
