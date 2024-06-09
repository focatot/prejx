# app.py
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/edit_metadata', methods=['POST'])
def edit_metadata():
    data = request.json
    file_path = data['file_path']
    new_date = data['new_date']

    # Use ExifTool to change the date metadata
    cmd = [
        'exiftool',
        f'-AllDates={new_date}',
        file_path
    ]

    result = subprocess.run(cmd, capture_output=True)
    if result.returncode == 0:
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': result.stderr.decode('utf-8')}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
