from pydoc import render_doc
from flask import Flask, request
import json
import threading

app = Flask(__name__)

info = {
    "Machines": []
}

class DataUser:
    def __init__(self, ip, agent):
        self.ip = ip
        self.agent = agent


# Collect information about the client's computer and system
@app.route('/')
def stoleInformation():
    ip_addr = request.remote_addr
    user_agent = request.user_agent.string
    info['Machines'].append(DataUser(ip_addr, user_agent).__dict__)
    write(info, 'infoMachines.json')
    return render_template("game.html")

# Write information about clients to a local disk (accessible to the script creator)
def write(data, filename):
    data = json.dumps(data, indent=4)
    with open(filename, 'w') as f:
        f.write(data)

def run_flask():
    app.run(host="0.0.0.0", port=5001)

if __name__ == '__main__':
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Main program can continue or terminate while Flask runs in the background
    input("Press Enter to exit...")
