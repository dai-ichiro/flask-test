from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/double', methods=['POST'])
def double_number():
    data = request.get_json()
    print(type(data))
    if 'number' not in data:
        return jsonify({'error': '数字が提供されていません'}), 400
    
    number = data['number']
    if not isinstance(number, (int, float)):
        return jsonify({'error': '有効な数字を入力してください'}), 400
    
    result = number * 2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)