from flask import Flask, Response
import requests

app = Flask(__name__)

def some_long_calculation(number):
  '''
  here will be some long calculation using this number
  let's simulate that using sleep for now :)
  '''
  import time
  time.sleep(5)

  return number

@app.route('/')
def check():
    output = []
    for i in range(10):
      output.append(some_long_calculation(str(i)))
    html = "<br/>".join(output)
    return Response(html, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
