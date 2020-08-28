#Summer-Jams-Hackathon-Submission
This is my hackathon submission for a MLH vacation-themed hackathon. Summer Jams provides a user with a relaxing getaway during the Covid-19 lockdown by simulating the experience of being on a holiday. It does this by bringing your pictures to life by audifying them.

#How it works?
On uploading a picture, a request is sent to the Google’s Vision API, which detects objects in the image such as birds. These labels are then used with a dataset containing sounds of the corresponding labels. Finally, an audio file is generated accompanying relaxing music and sounds of elements present in the picture.

#Technical Details
Flask micro-framework
HTML, CSS and JS
Google’s Vision API to find labels in the image
PyDub, a python music library to create the audio files.

#Trivia
This was my first hackathon experience and Summer Jams won the first place overall amongst approximately 65 project submissions and 280 participants.

#Demo
Find out more about Summer Jams and watch the project demo on [Devpost](https://devpost.com/software/summerjams).
