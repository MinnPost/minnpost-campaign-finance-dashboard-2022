# MinnPost Campaign Finance Dashboard 2022

The goal of this project is to give a quick overview of how much money Minnesota campaigns have raised and how much cash they have on hand 
for each reporting period. 

# Data Processing

Data is entered by hand into a Google Spreadsheet and downloaded as a csv. A python script (which uses only default libraries) converts it to
the JSON format the app needs. The JSON is hosted on S3.

To create the JSON, put a copy of the csv named `2022 Camfi Data - camfi.csv` in the `data-processing` directory then run `python make_json.py`.

# The dashboard

The dashboard is a svelte app. To run it, first install the dependencies...

```bash
cd svelte-app
npm install
```

...then start [Rollup](https://rollupjs.org):

```bash
npm run dev
```

Navigate to [localhost:5000](http://localhost:5000). You should see the app running. 

# Build

To create an optimised version of the app:

```bash
npm run build
```

You can run the newly built app with `npm run start`. This uses [sirv](https://github.com/lukeed/sirv), which is included in your package.json's `dependencies` so that the app will work when you deploy to platforms like [Heroku](https://heroku.com).