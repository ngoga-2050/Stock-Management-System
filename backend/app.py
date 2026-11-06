from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/students', methods=['GET'])
def get_students():
    students = [
        {
            "id": 1,
            "name": "John",
            "course": "Information Technology"
        },
        {
            "id": 2,
            "name": "Mary",
            "course": "Networking"
        },
        {
            "id": 3,
            "name": "Peter",
            "course": "Software Development"
        },{
            
        }
    ]

    return jsonify(students)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "message": "Backend is running successfully!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)