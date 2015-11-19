# Tournament-proj

## What is this?
A [swiss-style]() tournament management system with functionality for

 - Storing players, their rankings, outcome of games
 - Determining optimum player matches for each round of the tournament based on the number of previous wins

The app also has support for
  
  - Matches that end up in ties
  - Odd number of players
  - Resorting to strenght of opposition players defeated to determine player matches if number of wins are identical 

## Instructions
This project requires python 2.7 and a [postgresql](http://www.postgresql.org/) databse.

Either install these locally or use the vagrant test environment

To set up the test environment 

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
1. Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) to \<some local folder\>
1. ```bash
cd <some local folder>
```
1. `vagrant up`
1. Download the files from this repo to <some local folder>/vagrant/tournament
1. `vagrant ssh` (you should now be logged into the vagrant virtual machine)
1. navigate to '/vagrant/tournament' this folder is shared from the host machine nd should have all the required files


To test the application

1. `psql -f tournament.sql` - This will create the tournament database and required tables.
1. Run `python tournament_test.py` to test the functions in 'tournament.py'
