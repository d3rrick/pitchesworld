
## HOW TO USE PITCH APP

+ First clone The Project from github.
+ Then setup the project by creating a virtual environment and installing all the packages by running ``` pip3 install -r requirements.txt ``` 
+ Then on the terminal start the server by running ``` python manage.py runserver ```
+ On any browser type ``` https://localhost:5000```


### Behaviour

## Authentication

+ Once the url is entered the user is welcomed to the app and redirected to the registration and login form. 
- If the user is anonymouse, He/she can only view the categories and can't vote or comment.
- If the user on the the other hand is Authnticated but logged out, can login again to interact with the app by entering email and password details into a form.
- The user last option is to register using a unique username and a password after which the user is redirected to login to the app.
- Once the user is authenticated, can logout at will.

## Pitches.

+ The user Can add pitches and they get displayed from the most resent one.
+ The user can upvote,downvote and comment on a pitch.
+ The pitch information is displayed alongside other pitches, a pitch contains information such as pitch body, pithch author, downvotes,upvotes and total vote count.
+ The user can click the author of the pitch to view all their information such as their bio, profile picture and all their pitches.

## Categories

+ The pitches are categorized as punchline, product, intrview and promotion pitches.
+ The user can view all these categories whether authenticated or not.
