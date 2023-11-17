from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)

nutritionix_app_id = os.environ.get('NUTRITIONIX_APP_ID')
nutritionix_api_key = os.environ.get('NUTRITIONIX_API_KEY')

if not (nutritionix_app_id and nutritionix_api_key):
    raise ValueError("Please set the NUTRITIONIX_APP_ID and NUTRITIONIX_API_KEY environment variables.")

app.config['DEBUG'] = True 

def get_nutrition_data(query):
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        'x-app-id': nutritionix_app_id,
        'x-app-key': nutritionix_api_key,
        'x-remote-user-id': '0',
        'Content-Type': 'application/json'
    }
    body = {'query': query}
    response = requests.post(url, json=body, headers=headers)
    if response.status_code == 200:
        return response.json() 
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/food-groups')
def food_groups():

    return render_template('food_groups.html')

@app.route('/diet-types')
def diet_types():
    return render_template('diet_types.html')

@app.route('/eating-schedules')
def eating_schedules():
    return render_template('eating_schedules.html')

@app.route('/nutrition-info')
def nutrition_info():
    return render_template('nutrition_info.html')

@app.route('/get-nutrition', methods=['GET', 'POST'])
def get_nutrition():
    if request.method == 'GET':
        return render_template('nutrition_info.html')
    elif request.method == 'POST':
        user_query = request.form['user_query']
        response = get_nutrition_data(user_query)
        if response and 'foods' in response:
            foods = response['foods']
            return render_template('nutrition_info.html', foods=foods)
        else:
            return "An error occurred", 400

if __name__ == '__main__':
    app.run()


