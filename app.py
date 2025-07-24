from flask import Flask, jsonify

app = Flask(__name__)

# variables housing dictionaries of travel routes from USA
# to destination countries
USA = [{'destination': "USA",
        'list': ["USA"]}]

CAN = [{'destination': "CAN",
        'list': ["USA", "CAN"]}]

MEX = [{'destination': "MEX",
        'list': ["USA", "MEX"]}]

BLZ = [{'destination': "BLZ",
        'list': ["USA", "MEX", "BLZ"]}]

SLV = [{'destination': "SLV",
        'list': ["USA", "MEX", "GTM", "SLV"]}]

GTM = [{'destination': "GTM",
        'list': ["USA", "MEX", "GTM"]}]

HND = [{'destination': "HND",
        'list': ["USA", "MEX", "GTM", "HND"]}]

NIC = [{'destination': "NIC",
        'list': ["USA", "MEX", "GTM", "HND", "NIC"]}]

CRI = [{'destination': "CRI",
        'list': ["USA", "MEX", "GTM", "HND", "NIC", "CRI"]}]

PAN = [{'destination': "PAN",
        'list': ["USA", "MEX", "GTM", "HND", "NIC", "CRI", "PAN"]}]

# instantiating index page
@app.route('/')
def index():
    return "To return a list of countries for which you will need customs forms, please add the destination country code at the end of this URL."

# instantiating /<country_code> pages
@app.route("/USA",methods=['GET'])
def toUSA():
    return jsonify({'USA':USA})


@app.route("/CAN",methods=['GET'])
def toCAN():
    return jsonify({'CAN':CAN})


@app.route("/MEX",methods=['GET'])
def toMEX():
    return jsonify({'MEX':MEX})


@app.route("/BLZ",methods=['GET'])
def toBLZ():
    return jsonify({'BLZ':BLZ})


@app.route("/SLV",methods=['GET'])
def toSLV():
    return jsonify({'SLV':SLV})


@app.route("/GTM",methods=['GET'])
def toGTM():
    return jsonify({'GTM':GTM})


@app.route("/HND",methods=['GET'])
def toHND():
    return jsonify({'HND':HND})


@app.route("/NIC",methods=['GET'])
def toNIC():
    return jsonify({'NIC':NIC})


@app.route("/CRI",methods=['GET'])
def toCRI():
    return jsonify({'CRI':CRI})


@app.route("/PAN",methods=['GET'])
def toPAN():
    return jsonify({'PAN':PAN})


if __name__ == "__main__":
    app.run(debug=True)
