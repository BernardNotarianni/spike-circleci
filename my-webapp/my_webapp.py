from bottle import route, run, template
import my_domain

@route('/')
def index():
    message = my_domain.my_message()
    return '<html><h1>Otter world!!</h1><img src="https://www.otter-world.com/wp-content/uploads/Cute_European_Or_Eurasian_Otter_600.jpg"/><p>{}</p></html>'.format(message)

run(host='0.0.0.0', port=8000)

