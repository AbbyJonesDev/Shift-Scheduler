This script was created for a manager who needed a way to randomly assign employees to teams.  Each team would be responsible for running one machine during their shift.  

There are two primary jobs for each machine: feeders and sweepers.  Some employees can do either job, while others can only be feeders.  Each team needs to have at least one person who can be a sweeper.  

This script reads in the employee names for a given shift from a text file, uses Python's random module to shuffle them, and sorts them to ensure that each team has at least one person who can be either a feeder or a sweeper.  Then it assigns employees to teams and prints those teams to the screen.  It also offers the option of saving the teams to a text file.

The script also provides the option of creating schedules for multiple days at one time.
