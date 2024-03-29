from main import Psql
import json

psql = Psql('1234',
            dbname='lb2',
            user='postgres',
            host='localhost')


print("database initialised")
table_list = psql.execute_fetch(
    "SELECT table_name FROM information_schema.tables WHERE (table_schema = 'public') ORDER BY table_name;")
data = {}
for table in table_list:
    table_data = psql.get_table_contents(table[0])
    data.update({table[0]: table_data})

print(data)
for key in data:
    l_d_ = [{data[key][0][i]: data[key][1][j][i] for i in range(3)} for j in range(len(data[key][1]))]
    with open(f"{key}.json", "w") as f:
        json.dump(l_d_, f)
