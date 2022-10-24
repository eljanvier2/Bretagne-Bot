import tweepy
from random import randrange
import time
from datetime import datetime, timedelta
from rfc3339 import rfc3339
from dotenv import load_dotenv
import os
load_dotenv()
phrases = ["Salut! Pas mal ton tweet! Mais si je peux me permettre il serait encore mieux s'il parlait un peu plus de notre belle Bretagne! Mais pas de soucis tu pourras en parler dans ton prochain tweet j'espere...",
           "Hmmmm, pas mal, mais ça manque un peu de Bretagne!",
           "Avec un peu de Bretagne en plus ton tweet serait parfait. Pas grave, ça sera pour la prochaine fois!",
           "C'est vrai que de temps en temps, on a le droit de parler d'autre chose que de notre belle Bretagne. Mais pas trop longtemps (:",
           "Cool ton tweet! Le prochain devrait parler de Bretagne je pense. En tout cas moi ça me ferait beaucoup plaisir!",
           "Tu sais où on mange les meilleures galettes bretonnes? En Bretagne! Parles-en dans ton prochain tweet ahah",
           "Tu sais à quoi ton tweet me fait penser? À notre belle Bretagne! Tu devrais tweeter dessus ahah",
           "C'est vrai que le cidre breton est le meilleur du monde! Oups! Je me suis trompé de tweet... Néanmoins tu devrai goûter!",
           "Encore un tweet où tu aurai pu parler de Bretagne... C'est pas grave, je croise les doigts pour que tu en parles dans ton prochain tweet!",
           "Ton tweet me donne envie de kouign-amann! Non je rigole! J'ai toujours envie de kouign-amann... BRETAGNE!",
           "Super tweet! Je touche du bois pour que le prochain parle de Bretagne!",
           "Vive la Bretagne! Ah mince je me suis trompé de tweet... Vive la Bretagne quand même!",
           "*Pense à notre belle Bretagne*",
           "*Bretagne thinking intensifies*",
           "GET BRETAGNED! Hahaha",
           "Je suis ton daily reminder de ne surtout pas oublier de parler de la Bretagne aujourd'hui! Bonne journée!",
           "#BRETAGNE #FIER #KOUIGNAMANN #CIDRE #VENT #PLUIE #PLAISIR",
           "J'entend le loup le renard et la be... OH! Excuse-moi je ne t'avais pas vu... J'étais trop concentré à penser à la Bretagne",
           "Pense a aller a ton cours de Biniou aujourd'hui!",
           "J'ai bien envie d'aller au Mont Saint Michel ! Un patrimoine Breton incomparable.",
           "La Bretagne, ça vous gagne!",
           "Laisse toi gagner par la Bretagne...",
           "Bons Baisers de Bretagne !",
           "BRETAGNE !",
           "Oui, mais avant tout le Kouign Aman.",
           "Je suis d'accord avec ça, mais je pense que tu as oublié de parler du Finistère.",
           "Bel article, mais je préfère les galettes de sarrasin",
           "jE vOiS cE tWeEt eN PoRtanT UniQuemEnt Mon PeTiT Ciré JaUne et Toi ? 🍆💦💦",
           "*Like ce tweet les pieds dans les algues*",
           "*Like ce tweet depuis mon phare breton*",
           "As-tu pensé à faire ton soin aux algues aujourd'hui?",
           "Tu imagines que des gens ne sont jamais allés en Bretagne??? Moi non.",
           "Tu sens ca ? C'est notre beau mistral breton qui vient sur ton tweet!",
           "Tu avais toutes tes chances d'evoquer la Bretagne dans ton tweet.. tu m'en vois decu!",
           "Les gens disent qu'il pleut en Bretagne, moi je pense qu'en Bretagne il ne pleut que sur les cons!",
           "Like si toi aussi tu voudrais un emoji Bretagne!",
           "Like si tu penses aussi que la Bretagne est la plus belle des regions !",
           "Like si tu veux que je reponde a tes tweets, je ne parlerai que de Bretagne promis!",
           "BRETAAAAAAAAAAAAGNE",
           "AAAAAAAAAAAAAAAAAA *en breton*",
           "Ho karan ! (Ca veut dire je vous aime en Breton)",
           "Breizh Forever !"]

paths = ["./gifs/1.gif", "./gifs/2.gif", "./gifs/3.gif",
    "./gifs/4.gif", "./gifs/5.gif", "./gifs/6.gif","./gifs/7.gif", "./gifs/8.gif", "./gifs/8.gif", "./gifs/10.gif", "./gifs/11.gif",
    "./gifs/12.gif", "./gifs/13.gif", "./gifs/14.gif", "./gifs/15.gif", "./gifs/16.gif"]

auth = tweepy.OAuthHandler(os.getenv("consumer_key"),os.getenv("consumer_secret"))

auth.set_access_token(os.getenv("access_token"),
                      os.getenv("access_secret"))
api = tweepy.API(auth)

client = tweepy.Client(
    os.getenv("bearer_token"))

query = "-bretagne -kouign-aman -Finistère (from:bon_vieux_gui OR from:_Elvince OR from:Frederic_Molas OR from:terracid OR from:Mediavenir OR from:JoycaOff OR from:MrAntoineDaniel OR from:EmmanuelMacron OR from:Inoxtag OR from:JLMelenchon OR from:karmaaOfficiel OR from:DephaseuR OR from:LaPvlga OR from:LouisPoucineau OR from:MarxFanAccount OR from:Youridefou OR from:xSqueeZie OR from:le_egar OR from:Arkunir OR from:honeeymoooon OR from:J_Bardella OR from:PatrickAdemo OR from:le_gorafi OR from:_dieuoff)"
poster = tweepy.Client(consumer_key=os.getenv("consumer_key"),
                       consumer_secret=os.getenv("consumer_secret"),
                       access_token=os.getenv("access_token"),
                       access_token_secret=os.getenv("access_secret"))
timestamp = time.time()
d = datetime.fromtimestamp(timestamp)
timeStart = d - timedelta(minutes=10)
timeStart = rfc3339(timeStart)

while True:
    if (timeStart != ""):
        tweets = client.search_recent_tweets(query=query, tweet_fields=[
                                             'context_annotations', 'created_at'], max_results=10, start_time=timeStart)
    else:
        tweets = client.search_recent_tweets(query=query, tweet_fields=[
                                             'context_annotations', 'created_at'], max_results=10)
    if tweets.data is not None:
        file = open(paths[randrange(0, 14)], 'rb')
        r1 = api.media_upload(filename="gif" + str(randrange(0,1999)), file=file)
        media_ids = [r1.media_id_string]
        for tweet in tweets.data:
            print(tweet.text)
            try:
                response = poster.create_tweet(text=phrases[randrange(0, 42)], in_reply_to_tweet_id=tweet.id, media_ids=media_ids)
            except Exception as e:
                print(e)
    timestamp = time.time()
    d = datetime.fromtimestamp(timestamp)
    timeStart = rfc3339(d)
    time.sleep(300)
    print("5 min left")
    time.sleep(240)
    print("1 min left")
    time.sleep(60)
