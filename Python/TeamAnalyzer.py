import sqlite3  # This is the package for all sqlite3 access in Python
import sys      # This helps with command-line parameters

connection = sqlite3.connect('../pokemon.sqlite')

# All the "against" column suffixes:
all_types = ["bug", "dark", "dragon", "electric", "fairy", "fight",
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
    against = pokemonCursor.execute(
        "SELECT * FROM against WHERE type_source_id1=? AND type_source_id2=?", (type_ids[0][0], type_ids[1][0],)).fetchall()
    data = against[0][2:]
    for i in range(len(data)):
        if data[i] > 1:
            strong.append(all_types[i])
        elif data[i] < 1:
            weak.append(all_types[i])

    for id in type_ids:
        curr_type = pokemonCursor.execute(
            "SELECT name FROM type WHERE id=?", (id[0],)).fetchone()
        for ctype in curr_type:
            types.append(ctype)
    type_str = ""
    for val in types:
        type_str += val
        type_str += " "
    new = type_str.rstrip()
    print(name + " (" + new + ") is strong against " +
          str(strong) + " but weak against " + str(weak))

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
