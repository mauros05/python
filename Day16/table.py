from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows([
        ["Pikachu", "Electric"],
        ["Charizard", "Fire"],
        ["Bulbasaur", "Grass"]
    ]
)

table.align = "l"

print(table)