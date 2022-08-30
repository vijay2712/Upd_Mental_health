from flask import Flask,render_template,request,jsonify
from chatbot_em import get_response
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# run_with_ngrok(app)

@app.route('/',methods=['GET'])
def home():
    return render_template('base.html')

@app.route('/predict',methods=['POST'])
def predict():
  text=request.get_json().get("message")
  response=get_response(text)
  # response=text
  message = {"answer":response}
  return jsonify(message)

if __name__ == "__main__":
  app.run(debug=True,threaded=True)