# The server side from TimeTrack
The App Engine server side component written in Python.

## How to Build
### Setup App Engine project
The first thing you need to run TimeTrack is to create a new App Engine project in your [Google Developer Console](https://console.developers.google.com).
On to right upper corner you see a DropDown menu. Click it and choose "Create project...".
Than you can enter a name you like. Below the input you find a project-id. Save it, because you will need it in the following step.
After entered a cool name click on "Create".

### Config `app.yaml`
Now you need to configure the `app.yaml` file.
On the top of this file you find a `application: [PROJECTID]`. Well, thats explains all.
Replace the upper-case letters with your App Engine project id.

You can also use the `setup.sh` script in the root path to make this happen.

### Upload to App Engine
If you haven't already done it, download and install the [Google App Engine SDK for Python](https://cloud.google.com/appengine/downloads).
When it is installed you can upload these app via the `GoogleAppEngineLauncher` (which I have never used :)) or via a terminal.
Navigate in the terminal to these project (project/) and type
```
appcfg.py update server/
```

That's all. Now the TimeTrack server runs on your App Engine!

## A new User
To create a new user go to
```
YOUR_APP_ENGINE_PROJECT_ID.appspot.com/admin
```
in your browser and create a new user.
You get a new `token` to communicate with the Android App and these Server.

## JSON Documentation
The current JSON documentation can be find under `json_documentation/`.
The documentation to saving a new TimeTrack is described in `save_post`.
To get all your TimeTrack's read the `get_post` documentation.

## TODO:
* Better naming for objects/* classes
* nicer default handler (explanation? Redirecting to GitHub page?)
* GET for /rest/* things same like default handler
