# Tournament-proj

## What is this?
A swiss style tournament management system with functions to 
- store playeyers, their rankings
- outcome of games
- automatic matching of players of similar calibre based on their performance

## Instructions
This project requires python 2.7 and a [postgresql](http://www.postgresql.org/)
Either install these locally or use the vagrant test environment

To set up the test environment 

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
1. Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) to <some local folder>
1. `$ cd <some local folder>`
1. `$ vagrant up`
1. download the files from this folder to <some local folder>/vagrant/tournament
1. `$ vagrant up` (you should now be logged into the vagrant virtual machine)
1. navigate to '/vagrant/tournament' this folder is shared from the host machine nd should have all the required files


To test the application 
1. Create a database called 'tournament' in psql
1. Import 'tournament.sql' to create the required tables 
1. Run 'tournament_test.py' and  'tournament_test_extended.py' to test the functions in 'tournament.py'
