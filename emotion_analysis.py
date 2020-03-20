import re
import pandas as pd
import emoji
import pymongo
import regex
import enchant
import string
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["TwitterData"]
mydb1 = myclient['TwitterData_process']

ExcitementClass = mydb.ExcitementClass
HappyClass = mydb.HappyClass
PleasantClass = mydb.PleasantClass
SurpriseClass = mydb.SurpriseClass
FearClass = mydb.FearClass
AngryClass = mydb.AngryClass



## parameters for hashtage analysis
filepath = "NRC-Hashtag-Emotion-Lexicon-v0.2.txt"
emolex_df = pd.read_csv(filepath, names=["word", "hashtag", "association"], skiprows=45, sep='\t')
list_of_hashtag = []
emotion_cal = {'anticipation': 0, 'anger': 0, 'disgust': 0, 'fear': 0, 'joy': 0, 'sadness': 0,'surprise': 0, 'trust': 0}

## parameters for emoji analysis
happy = ['U+1F601','U+1F602','U+1F606','U+1F639','U+1F64B','U+2764','U+1F619','U+1F617']
excitement = ['U+1F60B','U+1F60D','U+1F631','U+1F632','U+1F633','U+1F635','U+1F63B','U+1F640','U+1F62E','U+1F62F']
angry = ['U+1F620','U+1F621','U+1F624','U+1F63E','U+1F44A','U+1F44E','U+1F4A9']
surprise = ['U+1F605','U+1F612','U+1F613','U+1F61E','U+1F622','U+1F625','U+1F629','U+1F62A',
            'U+1F62B','U+1F62D','U+1F63C','U+1F645','U+1F64D','U+1F610','U+1F615','U+1F61F',
            'U+1F634']
fear = ['U+1F614','U+1F616','U+1F623','U+1F628','U+1F630','U+1F637','U+1F63F','U+1F647','U+1F64A',
        'U+1F608','U+1F611','U+1F626','U+1F627','U+1F636']
pleasant = ['U+1F603','U+1F604','U+1F609','U+1F60A','U+1F60C','U+1F60F','U+1F618','U+1F61A',
            'U+1F61C','U+1F61D','U+1F638','U+1F63A','U+1F63D','U+1F646','U+1F648','U+1F649','U+1F64C',
            'U+270C','U+263A','U+1F44C','U+1F44D','U+1F44F','U+1F600','U+1F607','U+1F60E',
            'U+1F61B','U+1F62C']

emotion_cal_emoji = {'happy': 0, 'excitement': 0, 'angry': 0, 'surprise': 0, 'fear': 0, 'pleasant': 0}
list_of_emoji = []


# this is the function used for extracting all emoji in the tweet
def split_count(text):
    emoji_list = []
    data = regex.findall(r'\X', text)
    for word in data:
        if any(char in emoji.UNICODE_EMOJI for char in word):
            emoji_list.append(word)

    return emoji_list

#this is the function used for pre-process the text of tweet
def pre_process(text):
    c1 = re.sub(r"(.)\1{2,}", r"\1", text)  ## replace three consecutive identical letters in a word with one letter eg.loooove
    c2 = re.sub(r"(.)\1+", r"\1" + r'\1', text) ## replace three consecutive identical letters in a word with two letters eg.foooooot

    res = re.findall(r'\w+', c1) ## split the sentence into lots of words
    for i in res:
        d = enchant.Dict("en_US") ## check whether each word in this sentence is existed in English dictionary
        if d.check(i) == False: ## if there is wrong word and change strategy by using two letters replace
            correct_sentence = c2
            return correct_sentence

##this is the fuctions for pre-process text
def strip_links(text):
    link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')
    return text

def strip_all_entities(text):
    entity_prefixes = ['@','#']
    for separator in string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                words.append(word)
    return ' '.join(words)

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won\’t", "will not", phrase)
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\’t", "can not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\’t", " not", phrase)
    phrase = re.sub(r"\’re", " are", phrase)
    phrase = re.sub(r"\’s", " is", phrase)
    phrase = re.sub(r"\’d", " would", phrase)
    phrase = re.sub(r"\’ll", " will", phrase)
    phrase = re.sub(r"\’t", " not", phrase)
    phrase = re.sub(r"\’ve", " have", phrase)
    phrase = re.sub(r"\’m", " am", phrase)

    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase

def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)




if __name__ == '__main__':
    # mydb1['ExcitementLabel'].drop()
    # mydb1['HappyLabel'].drop()
    # mydb1['PleasantLabel'].drop()
    # mydb1['SurpriseLabel'].drop()
    # mydb1['FearLabel'].drop()
    # mydb1['AngryLabel'].drop()

    # results = ExcitementClass.find()  ## change different class
    # results = HappyClass.find()
    # results = PleasantClass.find()
    # results = SurpriseClass.find()
    results = FearClass.find()
    # results = AngryClass.find()
    list_of_text = []
    for tweet in results:
        if 'retweeted_status' in tweet:
            if 'extended_tweet' in tweet['retweeted_status']:
                full_text = tweet['retweeted_status']['extended_tweet']['full_text'] # get the full_text of tweet
                list_of_text.append(full_text)
                new_list = set(list_of_text) # compare full_text in order to remove duplicate
for text in new_list:
    global text1
    text1 = text
    hashtag = re.findall(r"#(\w+)", text1)
    list_of_hashtag.append(hashtag)      ## all hashtags in list_of_hashtag
    for n1 in list_of_hashtag:           ## n1 contains all hashtags in one tweet
        for h in n1:                     ## h represents each hashtag in one tweet
            # print(emolex_df[emolex_df.hashtag == h].hashtag.values)  ## hashtag name
            # print(emolex_df[emolex_df.hashtag == h].word.values)     ## hashtag corresponds to emotion name
            # print(emolex_df[emolex_df.hashtag == h].association.values) ## association value of this hashtag
            for i in range(len(emolex_df[emolex_df.hashtag == h].word.values)):
                emotion_cal[emolex_df[emolex_df.hashtag == h].word.values[i]] += emolex_df[emolex_df.hashtag == h].association.values[i] ## each class add association value of hashtag
            # print(emotion_cal) ## show the result everytime calculate a hashtag and check the addition
    max_emotion1 = max(emotion_cal, key=lambda k: emotion_cal[k])   ## take the class with max value as the emotion of this tweet
    # print(max_emotion1)
    # print("-------------------------A tweet hashtag analysis end--------------------------")
    emotion_cal = {'anticipation': 0, 'anger': 0, 'disgust': 0, 'fear': 0, 'joy': 0, 'sadness': 0, 'surprise': 0,'trust': 0} ## clean the calculation record for the next tweet

    counter = split_count(text)
    emoji_all = ' '.join(emoji for emoji in counter)
    list_of_emoji.append(emoji_all) ## all emoji in list_of_emoji
    for e1 in list_of_emoji:        ## e1 contains all emoji in one tweet
        for e2 in e1:               ## e2 represents each emoji in one tweet
            e_unicode = 'U+{:X}'.format(ord(e2))  ## convert emoji into unicode
            if e_unicode in happy:
                emotion_cal_emoji['happy'] += 1
            elif e_unicode in excitement:
                emotion_cal_emoji['excitement'] += 1
            elif e_unicode in angry:
                emotion_cal_emoji['angry'] += 1
            elif e_unicode in surprise:
                emotion_cal_emoji['surprise'] += 1
            elif e_unicode in fear:
                emotion_cal_emoji['fear'] += 1
            else:
                emotion_cal_emoji['pleasant'] += 1
    # print(emotion_cal_emoji) ## show the calculation result of tweet
    max_emotion2 = max(emotion_cal_emoji, key=lambda k: emotion_cal_emoji[k]) ## find the emotion with max value
    # print(max_emotion2)
    # print("---------------tweet emoji analysis end--------------------")
    emotion_cal_emoji = {'happy': 0, 'excitement': 0, 'angry': 0, 'surprise': 0, 'fear': 0, 'pleasant': 0} ## clean the calculation record for the next tweet
    ## if there is no emoji in tweet, just follow the hashtag analysis result
    if max_emotion1 == 'joy':
        emotion_cal_emoji['happy'] += 1
    elif max_emotion1 == 'trust':
        emotion_cal_emoji['pleasant'] += 1
    elif max_emotion1 == 'anticipation':
        emotion_cal_emoji['excitement'] += 1
    elif max_emotion1 == 'anger':
        emotion_cal_emoji['angry'] += 1
    elif max_emotion1 == 'fear' or max_emotion1 == 'disgust':
        emotion_cal_emoji['fear'] += 1
    elif max_emotion1 == 'surprise' or max_emotion1 == 'sadness':
        emotion_cal_emoji['surprise'] += 1

    list_of_emoji.clear() #clean the emoji of the last tweet

    happy_related_class = ['happy','pleasant','excitement']
    excitement_related_class = ['happy', 'pleasant', 'excitement']
    pleasant_related_class = ['happy', 'pleasant', 'excitement']
    surprise_related_class = ['surprise', 'fear','angry']
    fear_related_class = ['surprise', 'fear']
    angry_related_class = ['surprise', 'angry']


    if max_emotion1 == 'joy': ## comparison between the label of hashtag process and that of emoji process
        if max_emotion2 in happy_related_class:
            print('this tweet label is happy')
            # print('-----------------get tweet label-------------------')
            no_url_text = re.sub(r"https\S+", "", text1)
            no_contarction_text = decontracted(no_url_text)
            no_emoji_text = remove_emojis(no_contarction_text)
            final_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",no_emoji_text).split())
            final_text = pre_process(final_text)
            # print(text1)
            print(final_text)
            mydb1['HappyLabel'].insert_one({"original_text":text1,"label":"happy","process_text":final_text})
        # else:
            # print('delete this tweet')
            # print('-------------this tweet is removed------------------')
    elif max_emotion1 == 'trust':
        if max_emotion2 in pleasant_related_class:
            print('this tweet lable is pleasant')
            # print('-----------------get tweet label-------------------')
            no_url_text = re.sub(r"https\S+", "", text1)
            no_contarction_text = decontracted(no_url_text)
            no_emoji_text = remove_emojis(no_contarction_text)
            final_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",no_emoji_text).split())
            final_text = pre_process(final_text)
            # print(text1)
            print(final_text)
            mydb1['PleasantLabel'].insert_one({"original_text": text1, "label": "pleasant", "process_text": final_text})
        # else:
            # print('delete this tweet')
            # print('-------------this tweet is removed------------------')
    elif max_emotion1 == 'anticipation':
        if max_emotion2 in excitement_related_class:
            print('this tweet lable is excitement')
            # print('-----------------get tweet label-------------------')
            no_url_text = re.sub(r"https\S+", "", text1)
            no_contarction_text = decontracted(no_url_text)
            no_emoji_text = remove_emojis(no_contarction_text)
            final_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",no_emoji_text).split())
            final_text = pre_process(final_text)
            # print(text1)
            print(final_text)
            mydb1['ExcitementLabel'].insert_one({"original_text": text1, "label": "excitement", "process_text": final_text})
        # else:
            # print('delete this tweet')
            # print('-------------this tweet is removed------------------')
    elif max_emotion1 == 'anger':
        if max_emotion2 in angry_related_class:
            print('this tweet lable is angry')
            # print('-----------------get tweet label-------------------')
            no_url_text = re.sub(r"https\S+", "", text1)
            no_contarction_text = decontracted(no_url_text)
            no_emoji_text = remove_emojis(no_contarction_text)
            final_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",no_emoji_text).split())
            final_text = pre_process(final_text)
            # print(text1)
            print(final_text)
            mydb1['AngryLabel'].insert_one({"original_text": text1, "label": "angry", "process_text": final_text})
        # else:
            # print('delete this tweet')
            # print('-------------this tweet is removed------------------')
    elif max_emotion1 == 'fear'or max_emotion1 == 'disgust':
        if max_emotion2 in fear_related_class:
            print('this tweet lable is fear')
            # print('-----------------get tweet label-------------------')
            no_url_text = re.sub(r"https\S+", "", text1)
            no_contarction_text = decontracted(no_url_text)
            no_emoji_text = remove_emojis(no_contarction_text)
            final_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",no_emoji_text).split())
            final_text = pre_process(final_text)
            # print(text1)
            print(final_text)
            mydb1['FearLabel'].insert_one({"original_text":text1,"label":"fear","process_text":final_text})
        # else:
            # print('delete this tweet')
            # print('-------------this tweet is removed------------------')
    elif max_emotion1 == 'surprise'or max_emotion1 == 'sadness':
        if max_emotion2 in surprise_related_class:
            print('this tweet lable is surprise')
            # print('-----------------get tweet label-------------------')
            no_url_text = re.sub(r"https\S+", "", text1)
            no_contarction_text = decontracted(no_url_text)
            no_emoji_text = remove_emojis(no_contarction_text)
            final_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",no_emoji_text).split())
            final_text = pre_process(final_text)
            # print(text1)
            print(final_text)
            mydb1['SurpriseLabel'].insert_one({"original_text": text1, "label": "surprise", "process_text": final_text})
        # else:
            # print('delete this tweet')
            # print('-------------this tweet is removed------------------')



