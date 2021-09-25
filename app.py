from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
    string = "devopsassessment"
    total_letters = 0
    for s in string:
        if s in all_letters:
            total_letters += 1
    print("Number of letters in the word devopsassessment is ", total_letters)

if __name == '__main__':
    app.run(debug=True, host='0.0.0.0')
