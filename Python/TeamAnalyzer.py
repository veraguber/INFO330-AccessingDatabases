import sqlite3  # This is the package for all sqlite3 access in Python
import sys      # This helps with command-line parameters

connection = sqlite3.connect("pokemon.sqlite")

# All the "against" column suffixes:
types = ["bug", "dark", "dragon", "electric", "fairy", "fight",
         "fire", "flying", "ghost", "grass", "ground", "ice", "normal",
         "poison", "psychic", "rock", "steel", "water"]

# Take six parameters on the command-line
if len(sys.argv) < 6:
    print("You must give me six Pokemon to analyze!")
    sys.exit()

team = []
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue

    # Analyze the pokemon whose pokedex_number is in "arg"

for pokemon in sys.argv:
    print("Analyzing" + str(pokemon))
    type_ids = connection.execute(
        "SELECT type_id FROM pokemon_type WHERE pokemon_id=", pokemon)
    for id in type_ids:
        current_type = connection.execute(
            "SELECT name FROM type WHERE id=", id)
    print("Bulbasaur (" + str(current_type) +
          ") is strong against [] but weak against []")

    # You will need to write the SQL, extract the results, and compare
    # Remember to look at those "against_NNN" column values; greater than 1
    # means the Pokemon is strong against that type, and less than 1 means
    # the Pokemon is weak against that type

answer = input("Would you like to save this team? (Y)es or (N)o: ")
if answer.upper() == "Y" or answer.upper() == "YES":
    teamName = input("Enter the team name: ")

    # Write the pokemon team to the "teams" table
    print("Saving " + teamName + " ...")
else:
    print("Bye for now!")
