# USYD WAM Calculator
For some reason, USYD doesn't show you your overall WAM in Sydney Student or your transcript. 

This web app will read in a pdf (or csv export) of your transcript from Sydney Student and spit out your overall WAM (Weighted Average Mark).

## How to deploy (OSX/Linux)
If you want to parse a PDF transcript locally, you will need to install Java for this to work.

First, clone the repository by inputting the following into the command line:

```git clone git@github.com:invinceyble/iengage-webapp.git```

Then, `cd` into your local copy, and run the following to install the dependencies and launch the app:
```
make setup
make run
```

After you are done, clean up the files using:
```make clean```

## To Do / Possible Features
- Build front end properly
- Add in analytics (WAM by year, by session, by major, level) 
- Calculate SCIWAM
- Calculate your WAM required to reach a given goal
- Fix temp file requirement for pdf parsing
- Refactor parser

## Technical Details
This app was built using Flask, mostly because I wrote the initial calculations in Python, and wanted a way to build it into a web app. It's currently deployed using Heroku off the deploy branch.  