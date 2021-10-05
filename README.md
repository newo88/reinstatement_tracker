# REINSTATEMENT TRACKER SHEET.

Reinstatement tracker is a python based terminal application built for a civils company to save time 
on recording reinstatements and invoicing there clients. 

## Links to Site and Google Sheet.

* View the live project here. [Reinstatement_Tracker](https://tracker-application.herokuapp.com/)
* View the google sheet here. [Tracker_Spreadsheet](https://docs.google.com/spreadsheets/d/1BpOi3ajY4jSfYhaA6EqqBmWCc3Cy4oAlGxu9ruqyU4A/edit#gid=0)

## User Experience (UX)

### Project Goal's

The main goal of this project is to provide a terminal based application that saves a cizils company
both time and money while carrying out site based work measuring and calculating the amount of concrete needed 
to reinstate work after it is completed. The process before this was haven to measure write out the dimensions on site on a page and then transfer them to a spread sheet in the office. The way this application saves time and money is the whole thing is automated using python. The user enters all the details on site in the terminal which does the calculation for the concrete and automatically gets sent to a google sheet.   

### Site Owners Goals

* To build an application that is stream line and easy to use.
* To build an application that allows users to enter measurements and calculate the area squared.
* To build an application that can handle user errors effectively with out crashing the program.

### Site User Goals

* For the application to be easy use.
* To be able to enter data into the terminal and have it stored.
* To be able to easy access the data when needed.

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!