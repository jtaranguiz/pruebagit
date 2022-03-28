import re
import json
def tweets():
    json_file = open('farmers_protest.json', "r")
    lista_tweets = []
    menor = 0
    print(json_file)
    data = json_file.readlines()
    datos = json.loads(json.dumps(data))
    for i in datos:
        retweet = re.search('retweetCount',i)
        final = retweet.span()[1]
        contador=0
        for j in i[final:]:
            if j == ',':
                break
            contador += 1
        retweets = int(i[final+2:final+contador])
        
        if retweets > menor and len(lista_tweets) >= 10:
            print("y por aqui que wea")
            for index in range(len(lista_tweets)):
                retweet = re.search('retweetCount',lista_tweets[index])
                final = retweet.span()[1]
                contador=0
                for j in lista_tweets[index][final:]:
                    if j == ',':
                        break
                    contador += 1
                valor_top = int(lista_tweets[index][final+2:final+contador])
                if retweets > valor_top:
                    lista_tweets.insert(index, i)
                    lista_tweets.pop()
                    retweet_ultimo = re.search('retweetCount',lista_tweets[9])
                    final_ultimo = retweet_ultimo.span()[1]
                    contador=0
                    for j in lista_tweets[9][final_ultimo:]:
                        if j == ',':
                            break
                        contador += 1
                    menor = int(lista_tweets[9][final_ultimo+2:final_ultimo+contador])
                    break
        if retweets <= menor and len(lista_tweets) < 10:
            print("pase por aca")
            menor = retweets
            lista_tweets.append(i)
            print(len(lista_tweets))
        if retweets > menor and len(lista_tweets) < 10:
            print("por aqui tambien")
            if len(lista_tweets) == 0:
                menor = retweets
            for index in range(len(lista_tweets)):
                retweet = re.search('retweetCount',lista_tweets[index])
                final = retweet.span()[1]
                contador=0
                for j in lista_tweets[index][final:]:
                    if j == ',':
                        break
                    contador += 1
                valor_top = int(lista_tweets[index][final+2:final+contador])
                if retweets > valor_top:
                    lista_tweets.insert(index, i)
                    break
                print(len(lista_tweets))
    for i in lista_tweets:
        print(i)
        print("-----------------------------------------------------------------------\n")   

    

    

    # for i in datos:
    #  for i in data:
    #      print(i)
    #  json_file.close()
tweets()
