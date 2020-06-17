# Vysioneer Takehome Challenge

### Setup
1. Clone this repository
2. Create a virtual environment
3. Run `pip install requirements.txt`
4. `cd` into `app` and run `python app.py`
5. In a separate terminal, `cd` into `app` and run `pytest tests`
6. You can use curl or an application like Postman to test different URL endpoints.

### Notes and Design Choices
After doing some research, I came across a Python library called Connexion that was extremely useful for this challenge. It parses the OAS YAML file and connects Python functions to the endpoints in the YAML file based on operationId. Also, Connexion validates request parameters for you. However, because I used a third party library (Connexion), there were some features of the library that I could not override. In a lot of the cases where you wanted me to return a `405` error, I had to return a `400` error instead because that's what Connexion defaults to when a parameter is invalid. 

The YAML file you guys provided (`openapi.yaml`) was missing some lines that took me a while to find, I added them so you guys can fix it for future take home challenges, specifically lines 147 and 348. I also added some comments into the YAML file explaining why I cannot return certain error codes due to limitations of Connexion.

Finally, even though you told me that I didn't have to implement business logic, I included an in-memory database and some basic business logic for better program flow and for testing purposes.

I learned a lot from doing this takehome challenge. I have a lot of experience in building REST APIs, but never directly from an OAS specification. Learning how Connexion worked was extremely rewarding! Thank you for taking the time to review my takehome challenge!