from flask import Flask, Response
import requests
import time

app = Flask(__name__)

def some_long_calculation(number):
  '''
  here will be some long calculation using this number
  let's simulate that using sleep for now :)
  '''
  time.sleep(1)

  return number

@app.route('/')
def check():
    def generate():
        for i in range(10):
            print("jsjs")
            yield "<br/>"   # notice that we are yielding something as soon as possible
            yield str(some_long_calculation(i))
    return Response(generate(), mimetype='text/html')


def check2():
    output = []
    for i in range(10):
      output.append(some_long_calculation(str(i)))
    html = "<br/>".join(output)
    return Response(html, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
