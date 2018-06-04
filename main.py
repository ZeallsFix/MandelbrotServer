from flask import Flask, render_template
from flask import request
import json
from Calculation import Mandelbrot
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'passwort123'
socket_io = SocketIO(app)


@app.route('/')
def response():
    data = request.get_json(force=True)  # request.post might also work
    Mandelbrot(data['RealFrom'], data['RealTo'], data['ImaginaryFrom'], data['ImaginaryTo'], data['Intervall'],
               data['MaxIteration'])
    mandel = Mandelbrot(max_iterations=10, increase_per_increment=0.1, min_x_coordinate=1, max_x_coordinate=-1,
                        min_y_coordinate=1, max_y_coordinate=-1)
    #Mandelbrot.start_calc
    #return Mandelbrot.return_as_json(Mandelbrot.start_calc())
    # mandel = Mandelbrot(10,1, 2,1,3,1)
    # print(mandel.start_calc)
    return render_template('front_end.html')

@app.route('/lasse')
def test():
    return 'hallo world'

@socket_io.on('data_sent')
def prepare_calculation():
    emit('my response', {'data': 'got it!'})
    
if __name__ == '__main__':
    socket_io.run(app, port=8080)
    
    #send = mandel.start_calc()
    #print(send)
