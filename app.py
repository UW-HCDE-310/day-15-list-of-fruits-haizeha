from flask import Flask, render_template
import requests
import keys

app = Flask(__name__)
@ app.route("/")
def index():
	fruits =[
		{"name":"apples", "quantity":3},
		{"name":"oranges", "quantity":2},
		{"name":"strawberries", "quantity":6}
	]

	filtered_fruits = [
		fruit for fruit in fruits
		if fruit["name"].startswith("o") and fruit["quantity"] < 3
	]

	print(keys.MY_SECRET_API_KEY_1)
	print(keys.MY_SECRET_API_KEY_2)

	response = requests.get("https://api.sunrise-sunset.org/json?lat=47.6062&lng=-122.3321&formatted=0")
	if response.status_code == 200:
		data = response.json()
		sunrise = data["results"]["sunrise"]
		sunset = data["results"]["sunset"]
	else:
		sunrise = "N/A"
		sunset = "N/A"

	return render_template("index.html", fruits = filtered_fruits, sunrise=sunrise, sunset=sunset)

if __name__ == '__main__':
	app.run(debug=True)
