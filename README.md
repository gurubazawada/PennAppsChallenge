# PennApps Backend Technical Challenge

# Structure of Application Portal
The way I structured the application portal was that the home page will initially have just a start application buttton. 
After clicking the start application button it will either let you login or signup if you need to signup.
After you signup it will direct you back to the login page where you can input your new credentials to login. 
After login, it will take you to the application and you can fill out your application.
After submitting your application it will take you to the home page which now lets you edit your application, look at your application status and logout.

# Part 1: Authentification
I used the inbuilt views from django.contrib.auth to implement the login and logout features.
For the signup feature, I created a createUser view which uses a form I made to create a applicant.
This form extends from the user creation form but with field "is_penn_student".

(Note) The signup worked well about 5 minutes ago and I can't figure out what I changed. If you want to use my portal, please use admin to create users. Everything else I implemented works

Bonus: I used login_required from django.contrib.auth.decorators to make some routes protected.
I made the logout route protected because you shouldn't be able to logout unless you are logged in.
I made the application route protected because you cant create an application unless you are logged in because each application is tied to a user.

# Part 2: User Application
I built upon the existing application model and added fields for all the inputs from the from.
The logic for creatinga Application object is in views.py
I found this out later, but I realized that to implement the Bonus part of part 2 it would have been helpful to save my emails differently rather just text. 
But, I did not have enough time to fix this.

Bonus: I implemented half of the bonus where you can only add emails of valid partners. 
Everytime a post request is sent to the application view, if one of the emails is not tied to a user it doesn't take you back to the home page but keeps you on the application page until you provide a valid email.

# Part 3: Bonuses
I implemented the feature that allows users to edit their applications. 
Everytime there is a get request sent to applications, it returns back the application and in the template it renders all the previously filled out sections.
I also implemented some conditional rendering on the home page. I wanted it to say edit application if there was already a application submitted. 
I also added some simple unit tests in the tests.py folder.


