# Overview

Uma Racer is a Django web app that lets users choose racers and run a simulated horse-girl race. The simulation includes straight sections, corners, an uphill section, and abilities that can affect a racer's score.

Open up the website on lesliejury.github.io/uma_racer


I wrote this software to practice building a web application with Django. It helped me learn how a web page can receive information from a user, send that information to Python code, and display the result in an HTML template.

[Software Demo Video](https://youtu.be/hNIxZyXrYqg)

# Web Pages

## Race Setup

The first page is the race setup page. The user chooses at least two racers and selects a race distance. The racer choices and their stats are created from data in the Python code.

When the user submits the form, Django sends the selected racers and distance to the race view.

## Race Results

The results page is created after the user submits the setup form. It displays the racers in their finishing order, each racer's score, ability events, and the sections of the track used in the simulation.

The results change based on the racers and distance selected by the user.

# Development Environment

I used Visual Studio Code to write and organize the project. I used the Windows PowerShell terminal to install packages and start the Django development server.

The application is written in Python using the Django web framework. It uses Django templates for the HTML pages, CSS for the page styling, and Python's built-in `random` library for small changes in race scores.

# Useful Websites

* [Django Documentation](https://docs.djangoproject.com/en/5.2/)
* [Django Tutorial](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)
* [Python Documentation](https://docs.python.org/3/)
* [MDN HTML Forms](https://developer.mozilla.org/en-US/docs/Learn/Forms)

# Future Work

* Add a database page that saves previous race results.
* Add more racers, abilities, weather options, and track conditions.
* Add a simple visual race replay showing racer positions.
* Add more helpful error messages for invalid form selections.
