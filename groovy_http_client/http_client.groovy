#!/usr/bin/env groovy
import groovy.transform.Field


@Field String PORT = "9000"
@Field String ADDR = "172.18.214.46" 

def get_request(first_parameter,second_parameter,operation) {
    sign = ""
    switch(operation) {
        case '+': operation = "add"; break
        case '-': operation = "sub"; break
        case '/': operation = "div"; break
        case '*': operation = "mult"; break
        default: operation = ""; break
    }
    def get = new URL("http://$ADDR:$PORT/api/$operation/$first_parameter/$second_parameter").openConnection()
    if (get.getResponseCode().equals(200)){
        "$first_parameter $operation $second_parameter = $get.content.text"
    }
    else 
    {
        "Something is going wrong"
    }
}

def post_request(first_parameter,second_parameter,operation){
    def num_of_operation = "4"
    switch(operation) {
        case '+':  num_of_operation = "1"; break
        case '-':  num_of_operation = "0"; break
        case '/':  num_of_operation = "3"; break
        case '*':  num_of_operation = "2"; break
        default: operation = "4"; break
    }

    def header = "a=$first_parameter&b=$second_parameter&op=$num_of_operation"
    def post = new URL("http://$ADDR:$PORT").openConnection()
    post.with {
        doOutput = true
        requestMethod = 'POST'
        outputStream.withWriter { writer ->
        writer << header
    }
    answer = post.getInputStream().getText()
    "$first_parameter $operation $second_parameter = $answer"
    }
}

def params = []
for (param in this.args){
    params << param
}
if ( params.size() != 4){
    println "You have to put 4 params"
    println "For instance: get 5 + 9"
    return 1
}
else if ( !["get","post"].contains(params.getAt(0))){
    println "Your first parameter has to be 'get' or 'post' "
    return 1
}
else if ( !['/','*','-','+'].contains(params.getAt(2)) )
{
    println "Your third parameter has to be '*', '/', '-', '+'"
    return 1
}

method = params[0]

method == "get" ? println(get_request(params[1],params[3],params[2]))
: println(post_request(params[1],params[3],params[2]))

return 0