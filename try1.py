from flask import Flask, request, render_template
from flask_cors import CORS
import json
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

info = {
    "Machines": []
}

class Data_user:
    def __init__(self, ip, agent):
        self.ip = ip
        self.agent = agent

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Collect information about the client's computer and system
@app.route('/')
def stoleInformation():
    try:
        ip_addr = request.remote_addr
        user_agent = request.user_agent.string
        data_user = Data_user(ip_addr, user_agent).__dict__
        info['Machines'].append(data_user)
        write(info, 'infoMachines.json')

        app.logger.info(f"Data received from {ip_addr}: {data_user}")
        return render_template("game.html")
    except Exception as e:
        app.logger.error(f"Error: {e}")
        return "An error occurred", 500

# Write information about clients to a local disk (accessible to the script creator)
def write(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=False)
