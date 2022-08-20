# Deep Shah
# August 8th, 2022
# This project analyzes the upload audio file (in .wav format) and displays it in text. It uses Python and Flask for the main analyzing part of the code, and HTML and CSS for the clarity and styling. 

from flask import Flask, render_template, request, redirect # Flask creates the web application, render_template generates an output from a template file (in our case, index.html), requests allows us to change the HTTP web requests, and redirect just redirects the user to another URL
import speech_recognition as sr # This is the module that helps with the analyzing of the audio files

app = Flask(__name__) # Basic app
@app.route("/", methods = ["GET", "POST"]) # This route points towards the home page
                                           # GET is receiving data 
                                           # POST is sending data

def index(): # Function points towards to what should be returned on the home page

    transcript = ""

    if request.method == "POST":
        print("FORM DATA RECEIVED") # When transcribe button is hit, this message is displayed in the terminal, meaning the POST method has been done

        if "file" not in request.files: # If transcribe button is hit and there is no file uploaded, the page will just refresh
            return redirect(request.url)

        file = request.files["file"] 
        if file.filename == "": # Same scenario as no file uploaded but in this case, the file uploaded is blank
            return redirect(request.url)

        if file: # Checks if the file exists 

            recognizer = sr.Recognizer() # Initalizes the instance of the speech recognition class
            audioFile = sr.AudioFile(file) 

            with audioFile as source: # Loop to read the audio file
                data = recognizer.record(source) # Parses the audio file and stores into data

            transcript = recognizer.recognize_google(data, key=None) # The key can be an API of your choice if you have one, but we are using the recognizer_google, so we do not need one
            print(transcript) 

    return render_template('index.html', transcript = transcript) # Renders page again with transcript

if __name__ == "__main__": # Basic flask syntax
    app.run(debug=True, threaded=True) # Debug=True means that flask instance will refresh to its latest updates when saved
                                       # Threaded=True means that multiple requests can be fulfilled without computer overloading