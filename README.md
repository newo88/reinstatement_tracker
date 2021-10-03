# REINSTATEMENT TRACKER SHEET.

Reinstatement tracker is a python based terminal application built for a civils company to save time 
on recording reinstatements and invoicing there clients. 

## Links to Site and Google Sheet.

* View the live project here. [Reinstatement_Tracker](https://tracker-application.herokuapp.com/)
* View the google sheet here. [Tracker_Spreadsheet](https://docs.google.com/spreadsheets/d/1BpOi3ajY4jSfYhaA6EqqBmWCc3Cy4oAlGxu9ruqyU4A/edit#gid=0)

## User Experience (UX)

### Site Owners Goals

* 
* 
* 

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