# USYD WAM Calculator

For some reason, USYD doesn't show you your overall WAM in Sydney Student or your transcript. 

This web app will read in a pdf (or csv export) of your transcript from Sydney Student and spit out your overall WAM (Weighted Average Mark).

## How to deploy (OSX/Linux)

First, clone the repository by inputting the following into Terminal:

`git clone git@github.com:invinceyble/iengage-webapp.git`

Then, `cd` into your local copy, and run the following to install the dependencies and launch the app:
```
make setup
make run
```

After you are done, clean up the files using:
`make clean`

## To Do / Possible Features
- Enable copy and paste of transcript into a textbox
- Build front end properly
- Add in analytics (WAM by year, by session, by major, level) 
- Calculate SCIWAM

## Technical Details

This WAM calc 