from flask import Flask, request, jsonify
import json
app = Flask(__name__)

info = {
    "Machines": []
}

class Data_user:
    def __init__(self, ip, agent):
        self.ip = ip
        self.agent = agent

# Cбор информации о клиентском компьютере и системе
@app.route('/')
def stoleInfomation():
    ip_addr = request.remote_addr
    user_agent = request.user_agent.string
    info['Machines'].append(Data_user(ip_addr, user_agent).__dict__)
    write(info, 'infoMachines.json')
    return  ("это флеш-страница, чтобы зажечь белый свет")
    
@app.route('/machines')
def get_machine_info():
    try:
        with open('infoMachines.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "infoMachines.json not found"}), 404

# Запись информации о клиентах на локальный сетевой диск (доступен создателю скрипта)
def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
