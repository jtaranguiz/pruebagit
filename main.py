import functions
import json
def main():
    json_file = open('farmers_protest.json', "r")
    print(json_file)
    data = json_file.readlines()
    datos = json.loads(json.dumps(data))
    functions.tweets(datos)
main()