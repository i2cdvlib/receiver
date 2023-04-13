# Receiver App

from flask import Flask, request

app = Flask(__name__)

# Define an endpoint to receive data from the Sender App
@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.form['data']
    # Process the received data as needed
    print("Received data:", data)
    return "Data received"

if __name__ == '__main__':
    app.run(port=5001)  # Run the app on a different port than the Sender App
