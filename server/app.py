from flask import Flask, jsonify

app = Flask(__name__)
#This sets up the core Flask app, __name__ is always "__main__" when running this file directly, it tells Flask where its being run from

#sample car lease data
leases = [
    {
        "make": "Toyota",
        "model": "Camry",
        "year": 2024,
        "monthly_cost": 299,
        "down_payment": 2500,
        "lease_length_months": 36
    },
    {
        "make": "Honda",
        "model": "Civic",
        "year": 2023,
        "monthly_cost": 279,
        "down_payment": 1999,
        "lease_length_months": 24
    }
]

#This code sets up a route for when someone visits /api/leases, flask will respond with a list of lease offers
@app.route("/api/leases") #REST API endpoint that responds to GET http://localhost:5000/api/leases
def get_leases():
#turns the python data into JSON response
    return jsonify(leases)

#This part ensures that app.run() only runs when you launch app.py and not when imported as a module by another script
if __name__ == "__main__":
    app.run(debug=True)