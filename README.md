# Tournament-proj

## What is this?
A swiss style tournament management system with functions to

 - Store players, their rankings, outcome of games
 - Automatic matching of players of similar calibre based on their performance

The app can also
  
  - Supports matches that end up in ties
  - Mutiple tournaments
  - Odd number of players

## Instructions
This project requires python 2.7 and a [postgresql](http://www.postgresql.org/) databse.

Either install these locally or use the vagrant test environment

To set up the test environment 

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
1. Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) to \<some local folder\>
1. `$ cd <some local folder>`
1. `$ vagrant up`
1. Download the files from this repo to <some local folder>/vagrant/tournament
1. `$ vagrant ssh` (you should now be logged into the vagrant virtual machine)
1. navigate to '/vagrant/tournament' this folder is shared from the host machine nd should have all the required files


To test the application

1. Create a database called 'tournament' in psql
1. Import 'tournament.sql' to create the required tables 
1. Run 'tournament_test.py' and  'tournament_test_extended.py' to test the functions in 'tournament.py'
