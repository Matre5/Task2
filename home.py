from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)


@app.route('/api')
def get_info():

    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    if track != 'backend':
        return jsonify({'Error': 'invalid track'}), 400

    # getting the current date and time
    current_day = datetime.datetime.now().strftime('%A')

    # Getting the UTC time
    utc_time = datetime.datetime.now().strftime("%Y-%m-%dT %H:%M:%SZ")


    git_file = "https://github.com/Matre5/Task2/blob/master/home.py"

    git_repo = "https://github.com/Matre5/Task2.git"


    status_code = 200

    result = {
        'slack_name': slack_name,
        'track': track,
        'current_day': current_day,
        'utc_time': utc_time,
        'github_file_url': git_file,
        'github_repo_url': git_repo,
        'status_code': status_code
    }

    # response = jsonify(result)

    # response.headers['Content-type'] = 'application/json'

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

