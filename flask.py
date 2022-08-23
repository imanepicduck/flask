from flask import Flask, jsonify, request
app = Flask(__name__)
contacts = {
    "id" : "69",
    "name" : "Olaf Maifriend Sergei",
    "contact" : "365465", 
    'done' : 'false'
}

@app.route("/add-data", methods = ['POST'])
def add_data():
    if not request.json:
        return jsonify ({
            'status': 'error',
            'message' : 'Please provide the data so i can scam your friend >:)'
        }, 400)

contacts = {
    'id' : contacts[-1] ['id'] +1,
    'name' : request.json['name'],
    'contact' : request.json.get('contact', ""),
    'done' : False
}

contacts.append(contacts)
jsonify ({
    'status' : 'success',
    'message' : 'Data provided, so i can finally begin my scamming spree...'
})

if (__name__ == "__main__"):
    app.run(debug=True)
