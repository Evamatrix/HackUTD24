from flask import Flask, jsonify, request, render_template
import csv

app = Flask(__name__)

# Load data from CSV file
def load_data():
    data = []
    with open('toyota_fuel_economy.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# API route to get vehicle data
@app.route('/api/vehicles', methods=['GET'])
def get_vehicles():
    year = request.args.get('year')
    model = request.args.get('model')
    fuel_type = request.args.get('fuel_type')

    data = load_data()

    # Filter data based on query parameters
    if year:
        data = [v for v in data if v['Year'] == year]
    if model:
        data = [v for v in data if model.lower() in v['Model'].lower()]
    if fuel_type:
        data = [v for v in data if v['Fuel Type'] == fuel_type]

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
