from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Placeholder for data fetching logic
    return jsonify({'message': 'Dữ liệu năng lượng sẽ được gửi ở đây.'})

if __name__ == '__main__':
    app.run(debug=True)