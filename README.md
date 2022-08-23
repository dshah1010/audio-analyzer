# Audio Analyzer
A web application to upload .wav audio files and transcribe the text. 

# Demo
https://user-images.githubusercontent.com/104474913/185727846-f12252b6-59f4-44ec-a6cb-7f058f3fdbff.mov

# Inspiration 
During my first year in university, many of my classes were online, and going forward, I may have to get used to this. I recorded all these classes, but sometimes, understanding the professor was difficult, so with this application, I can understand the lectures with ease if I have the text format of the audio. 

# Technology 
This web application was built using a Flask backend to manage app routes and process GET/POST requests. I also used HTML and CSS to create a simple front-end. 

# Usage

If you would like to download my project, these are the steps:
        <ol>
        <li>
          Go to the directory you want in your command line and write:
          ```
          git clone https://github.com/dshah1010/audio-analyzer.git
          ```
       </li>
       <li>
          Write the following in the terminal:
          ```
          pip install flask
          ```
          and 
          ```
          pip install SpeechRecognition
          ```
       </li>
       <li>
          Run 
          ```
          app.py
          ```
       </li>
        <li>
          Should have the link to the web application in the terminal/command line, or you can copy it here: 
          ```
          [app.py](http://127.0.0.1:5000)
          ```
       </li>
       </ol>

# What's Next?
In the future, I plan to edit this by allowing users to choose other file formats such as .mp3 to upload as well, even though there are online converters to help with this situation. Upgrading the UI and adding a login could help with saving all these files and their captions within the account in case the audio is needed frequently. 
