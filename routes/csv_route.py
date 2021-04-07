from flask import Blueprint, jsonify, request
from config import CSV_FILE_PATH
from init_controllers import create_all_from_csv
import os


csv = Blueprint("csv", __name__)


@csv.route('/csv/load_from_file', methods=['POST'])
def load_from_file():
    csv_data = request.json
    filename = csv_data['filename']
    path = os.path.join(CSV_FILE_PATH, filename)

    create_all_from_csv(path)

    return jsonify({'response': 'success'})
