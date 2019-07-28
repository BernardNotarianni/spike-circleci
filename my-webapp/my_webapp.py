from bottle import route, run, template
import my_domain

@route('/')
def index():
    message = my_domain.my_message()
    return '<html><h1>Welcome to branch for issue 10</h1><img src="https://placekitten.com/200/300"/><p>{}</p></html>'.format(message)

run(host='0.0.0.0', port=8000)

