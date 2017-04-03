# Project: Tournament Results

tournament.sql creates the database, tables, and view
tournament.py contains a number of functions to add to and access the database
tournament_test.py contains a number of test functions

In order to run the project, you must have Python 2 and PostgreSQL installed;
Connect to PostgreSQL: $psql
Create a database called "tournament": $CREATE DATABASE tournament
Create tables and views: $\i tournament.sql
Virtualbox will be needed to run vagrant for this project;
Launch vagrant and go to the cloned repository where you win run, vagrant up, vagrant ssh;
Next navigate to the tournament directory with, cd /vagrant/tournament;
Run tests with: $python tournament_test.py
