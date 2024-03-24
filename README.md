# HackRUS2024

## Inspiration
The modern-day allure of endlessly scrolling through social media sites inspired us to make this app, which guides the user in an infinite quest for a captivating and compelling read. The members of our group all love reading and derive inspiration from a wide variety of subject areas, many of which are reflected in our app’s vast selection of books. Our project curates a unique and satisfying user experience that is bound to help all users pursue knowledge and leisure. We intend to further education with our project by encouraging more people to enjoy the pleasures of reading. 

## What it does
Our project generates book recommendations, given a list of liked books by the user. By analyzing the genres of the user’s chosen books, a machine learning model recommends books for the user to choose from. This process is continuous, much like Tinder is, so that the user will constantly be suggested new books to read. 

## How we built it
For the back end, we used a machine learning (ML) algorithm to generate recommendations based on the books a user chooses from a set of 12. We used scikit-learn to use TF-IDF Vectorizer and Nearest Neighbors which allowed us to generate recommendations based on the genre of a chosen book. We then used this to generate sets of 12 new books to output to the user so that the user can then choose to select more books. For the front end, we used HTML, CSS, and JavaScript to create our user interface. We then served our HTML file with Node.js and used a Flask server to integrate our front end and back end using HTTP requests.

## Challenges we ran into
We ran into two main challenges as we created our project. The first big challenge we encountered was learning how to simultaneously collaborate on the same project. None of us had used GitHub for a collaborative project before, so we initially tried to use Live Share on Visual Studio Code. However, we quickly realized that this was inefficient and decided to learn how to use a GitHub repository. The second challenge we faced was implementing a Flask server into our project, as it was something that none of us had ever used before. Our machine learning implementation was written in Python, so we needed to use Flask to connect it to the front end of our project. This proved to be a uniquely challenging task due to its novelty. In particular, we struggled with sending a POST request to our Flask server and processing its output. But in the end, we were able to overcome this challenge with teamwork, time, and a lot of debugging.

## Accomplishments that we're proud of
One accomplishment we are proud of is completing the machine learning algorithm in updating the recommended books. We are also proud of making a clean and convenient web application that works satisfactorily. 

## What we learned
We learned how to use GitHub collaboration when working on team projects. We also learned how to create a Flask project, which none of us knew how to do prior. Additionally, we learned how to develop a machine learning function and train it to recommend books for the user after a couple of runs. 

## What's next for Binder?
We plan to analyze more properties of each recommendation to better understand the user’s preferences in books, such as the genres they like and the authors they follow. We also plan on adding book covers to the recommendations by fetching the image URL from a search engine to make it more appealing and user-friendly. Furthermore, if possible, we can provide a larger dataset with a wider variety of books.
