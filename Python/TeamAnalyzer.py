import sqlite3  # This is the package for all sqlite3 access in Python
import sys      # This helps with command-line parameters

connection = sqlite3.connect('../pokemon.sqlite')

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

for pokemon in sys.argv[1:]:
    strong = []
    weak = []
    print("Analyzing " + str(pokemon))
    pokemonCursor = connection.cursor()
    pokemon_name = pokemonCursor.execute(
        "SELECT name FROM pokemon WHERE id=?", (pokemon,)).fetchone()
    name = pokemon_name[0]
    type_ids = pokemonCursor.execute(
        "SELECT type_id FROM pokemon_type WHERE pokemon_id=?", (pokemon,)).fetchall()
    types = []
    for id in type_ids:
        # print(id[0])
        curr_type = pokemonCursor.execute(
            "SELECT name FROM type WHERE id=?", (id[0],)).fetchone()
        for type in curr_type:
            types.append(type)
            # print(type)
    # print(types)
    type_str = ""
    for val in types:
        type_str += val
        type_str += " "
    new = type_str.rstrip()
    print(name + " (" + new + ") is strong against")

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
