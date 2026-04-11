from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    issue = request.json.get('issue')

    if "no internet" in issue.lower():
        priority = "High"
    elif "slow" in issue.lower():
        priority = "Medium"
    else:
        priority = "Low"

    return jsonify({"priority": priority})

if __name__ == '__main__':
    app.run(port=5000)
