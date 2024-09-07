# Capstone-Project-1-Initial
 Capstone Project 1 Initial Submission

API Selection and Schema Design:

For my API, I am using the nutritionix API, which gives access to nutrition information. My endpoint is the following 

https://trackapi.nutritionix.com/v2/natural/nutrients

This endpoint provides specific nutrtients for each food item searched. 

It is under the following form

<form method="post" action="{{ url_for('get_nutrition') }}">
        <label for="user_query">Enter food item:</label>
        <input type="text" id="user_query" name="user_query" required value="{{ request.form.get('user_query', '') }}">
        <button type="submit">Get Nutrition Info</button>
    </form>

On the Nutrition Information page, it is a get request to fetch a food item and get the number of calories, total fat and protein for each item. 

 <div>
        <h2>Nutrition Data</h2>
        <ul>
            {% for food in foods %}
                <li>{{ food.food_name }}: 
                    Calories: {{ food.nf_calories }}, 
                    Total Fat: {{ food.nf_total_fat }}g, 
                    Protein: {{ food.nf_protein }}g
                </li>
            {% endfor %}
        </ul>
    </div>


    This returns the get request. The name of the food, followed by the calories, then total fat and then protein. 


Documentation:

Food Welness Hub. http://127.0.0.1:5000/.

For my first Capstone i designed a website dedicated to a healthy lifestyle revolving around food. Furthermore, the site is organized into four pages. Food Groups, which highlights the food guide pyramid and each specific food group and information along with examples for each. Another page had diet types, which shows certain specific diets and a summary of each one and what you eat and why you would follow that lifestyle. I also have eating schedults, which furthers lifestyle which shows when and how to eat, rather than only showing what to eat. Last but not least, i have a page for nutrition information. Here you enter a food item and it gives you that foods calorie count, total fat and amount of protein. 


As far as features go, I provided five HTML pages. Four for each of the above categories and one for the homepage that brings you to each. Also, each page has a back to homepage button, so that the homepage truly works as a hub for what you are searching for. This way the site is organized and you can find where you want to go in one place. 

You start at the true food wellness hub on the homepage, which is the index.html. Here, You are greeted with Welcome to the Food Wellness Hub on the top of the page and Your guide to healthy eating habits and nutrition wellness as the subtitle. From here, there are four buttons. Food Groups, Diet Types, Eating Schedules and Nutrition Information. On this page, I really wanted to have a lot of emphasis on health, so i used a lot of shades of green to represent "greens", which symbolizes healthy foods along with the element of earth, which is often associated with wellbeing. I added a photo of various foods on the page so that the user knows that this is for food and wellness. 

The first buton is Food Groups. Here, you are brought to the Food Groups page. On this page, it is simply a list of each of the food groups from the food guide pyramid and a summary of each. Here, I chose colors that best represented each group along with a photo that showcased various foods from each group. I gave each food group's title a color to reflect them along with a banner to have a secondary color for each to accent them. For example, for Proteins, I had a beige-orange color to represent fish and nuts and poultry along with a dark red banner to represent meats which are synonymous with proteins. For the background, I chose a light granite grey to have a versatile tone since grey goes with almost everything. 

Next is the Diet Types Page. Here, I have everything centered instead of having only the titles and pictures. This way this page is distinguished. I decided not to add colors to these titles or paragraphs because there really are not any colors that are associated with certain diet types. Plus, I felt as if it would have been too cluttered and not as legible. Instead, I added a light blue to the background because it is a calming and welcoming color, which is important because diet types can be a difficult topic to persuade since many are turned off by feeling restricted to what they eat or having past experiences with diet types that have not been pleasant. With difficult subjects, it is important to make it as welcoming as possibie, which is why i chose a light blue. I also chose clipart images that were easy to look at for same reason. 

Next up, I have a page for Eating Schedules and Patterns. Here, I made the same decision to not add colors because there really being no colors associated with the subject. From personal experience, I found this topic to be easier to discuss since there are no restrictions to what you eat. Furthermore, I felt as if there was no need for fancy pictures or colors. Instead, I found a picture online of a clock aesthetic since this subject highlights time. I chose an aesthetic photo with a classic clock to make viewers feel nostalgic, since nostalgia can bring happiness. With that feeling, the user will feel that they will feel happier if they try one of these methods. 

Last but not least as far as pages go, I have Nutrition Information. Here is where the API comes in. I have Nutrition Information as the header, and underneath I have Enter Food Item, along with a search bar and a Get Nutrition Info button. Here, I used the Nutritionix API and https://trackapi.nutritionix.com/v2/natural/nutrients as an endpoint. This endpoint is a get request for nutrtion information for specific food items. For example, if you type in apple in the search bar and click Get Nutrtion Information, it is a get request that returns Nutrition Data as a title, and underneath the paragraph apple: Calories: 94.64, Total Fat: 0.31g, Protein: 0.47g. You can do this for almost any food item. As far as the background goes, I found an image that has a bottle, cup and carton with Nutrtion Facts labels on each of them. Front and center is a magifying glass on one of them so that there is further emphasis on how this is a Nutrition Facts page. 

As far as technology goes, this site is run on python. There is one file called app.py, which provides the routes for each HTML page. This was done on a macbook pro, so i activated the virtual environment to make the page. I also installed Flask to make it easier to navigate terminal and to make the website easier to run and put together. I used HTML for each page and I decorated each using CSS. 

From flask import Flask imports the Flask class render_template renders the HTML files, request handles HTTP requests. Import os is imported to interact with the operating system. import requests is imported to make HTTP requests to the API. app = Flask(__name__) this is to make the flask class and for the site to run on flask. nutritionix_app_id = os.environ.get('NUTRITIONIX_APP_ID') and nutritionix_api_key = os.environ.get('NUTRITIONIX_API_KEY') both authenticate the API for use accross the site. if not (nutritionix_app_id and nutritionix_api_key): raise ValueError("Please set the NUTRITIONIX_APP_ID and NUTRITIONIX_API_KEY environment variables.") This checks if there is something not in the API key and if there isnt, an error is returned. app.config['DEBUG'] = True installs debug mode in flask and automatic reloads and better error messages. def get_nutrition_data(query): defines a function to make a POST request to the Nutritionix API.     url = "https://trackapi.nutritionix.com/v2/natural/nutrients"  sets the endpoint URL for the Nutritionix API. headers = { 'x-app-id': nutritionix_app_id, 'x-app-key': nutritionix_api_key, 'x-remote-user-id': '0', 'Content-Type': 'application/json' this creates a dictionary for the headers with the API ID and keys and adds a required header to identify the user. It also sets the content to JSON for the API. body = {'query': query} prepares the request body with the user's food query. response = requests.post(url, json=body, headers=headers)  makes a POST request to the API with the given URL, headers, and body. if response.status_code == 200:  this checks if the response status code is 200 (OK), indicating the request was successful. return response.json()  // this returns the response data in JSON format if the request is successful. else: return None this returns none if the request is not successful. @app.route('/')  defines a route for the root URL ('/'). return render_template('index.html') handles the request routes such as food-groups, diet-types and the rest of the html pages and renders their templates. For the get-nutrtion page, there were a few more steps. if request.method == 'GET': checks if the request method is GET. return render_template('nutrition_info.html') renders the 'nutrition_info.html' template if it is a GET request. elif request.method == 'POST': checks if the request is a POST request. user_query = request.form['user_query'] retreives the user's input (food item) from the form data. response = get_nutrition_data(user_query) calls the function to get nutrition data using the user's input. if response and 'foods' in response: checks if the response contains data and has the 'foods' key. foods = response['foods'] extracts the 'foods' data from the API response. return render_template('nutrition_info.html', foods=foods) renders the 'nutrition_info.html' template with the foods data. else:return "An error occurred", 400  returns an error message with a 400 status code if the API fails. if __name__ == '__main__': checks if the script is run directly (not imported as a module). app.run() runs the Flask application with the default settings.











      




Overall, my goal was to make my site welcoming and easy to navigate and read. I wanted to make the website make others feel good with the use of specific colors and images to make them feel more welcome. Also, organized so that each page emphasizes a certain topic. Talking about a healthy lifestyle can be daunting, and using the right structure, colors and images can make the topic more pleasant. 


