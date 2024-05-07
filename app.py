from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

# Define a route to handle prediction requests
@app.route('/predict', methods=['POST'])
def predict():
    # Parse incoming JSON data
    data = request.json
    
    # Extract features from JSON data and convert to numpy array
    features = np.array([data['battery_power'], data['blue'], data['clock_speed'], data['dual_sim'], data['fc'],
                         data['four_g'], data['int_memory'], data['m_dep'], data['mobile_wt'], data['n_cores'],
                         data['pc'], data['px_height'], data['px_width'], data['ram'], data['sc_h'], data['sc_w'],
                         data['talk_time'], data['three_g'], data['touch_screen'], data['wifi']])
    
    # Make prediction
    prediction = pipeline.predict([features])[0]
    
    # Ensure prediction is a serializable Python data type
    prediction = int(prediction)  # Convert to regular Python integer
    
    # Return prediction as JSON response
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
