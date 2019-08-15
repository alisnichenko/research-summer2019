import json
import os
import emoji
import regex
import csv
import time

# function to get unique values
def unique(items): 
        unique_list = []
        for item in items:
                if item not in unique_list:
                        unique_list.append(item)
        
        return unique_list

# make a single list from list of lists
def flat(list_items):
        flat_list = []
        for sublist in list_items:
                for item in sublist:
                        flat_list.append(item)
        
        return flat_list

# extracting all emojis
# using emojis and regex modules
def find_emojis(text):
        emoji_list = []
        flag_list = regex.findall(u'[\U0001F1E6-\U0001F1FF]', text) 
        data = regex.findall(r'\X', text)
        for word in data:
                if any(char in emoji.UNICODE_EMOJI for char in word):
                        emoji_list.append(word)

        return emoji_list + flag_list, len(emoji_list), len(flag_list)

# writing a list to a given file
def write_list_to_csv_user(file_to_write, hashtag, screen_name, stance, name, description, tweet_date, tweet_id, tweet_fulltext):
        if len(tweet_fulltext) > 0:
                # with open(file_to_write, 'a+', encoding="utf8") as file:
                #         file.write(hashtag + ',' + screen_name + ',' + name_emoji + ',' + description_emoji + ',' + stance + ',')
                #         for item in items:
                #                 file.write(item)
                #         file.write('\n')
                with open(file_to_write, 'a+', newline='', encoding='utf-8') as csvfile:
                        tweetswriter = csv.writer(csvfile, delimiter='\t')
                        row = [hashtag, screen_name, stance, name, description, tweet_date, tweet_id, tweet_fulltext]
                        tweetswriter.writerow(row)
                        # print(row)

# stance lookup
def find_stance_csv(username, hashtag):
        csv_path = 'directory/is/unknown/and/unnecessary'
        with open(csv_path + '/' + hashtag + '.csv', 'r', encoding="utf8", errors='ignore') as file:
                r = csv.reader(file, delimiter=',')
                for row in r:
                        if row[0] == username: return row[1]
        return '-1'

# saving a dictionary?..
def save_dict_to_json(filename, dict_emoji):
       json_emojis = json.dumps(dict_emoji, ensure_ascii=False)
       with open(filename, "w", encoding='utf8') as f:
                f.write(json_emojis)

# extracting constant repeating values from the first line of .json
# def extract_basic_val(user_file):
        

# ==============================================================

rootdir = 'directory/is/unknown/and/unnecessary'
dict_emoji = {
        '#whitelivesmatter_Pro':'',
        '#whitelivesmatter_Anti':'',
        'AntiWhite_Pro':'',
        'AntiWhite_Anti':'',
        'WhiteGenocide_Pro':'',
        'WhiteGenocide_Anti':'',
        'whitepower_Pro':'',
        'whitepower_Anti':'',
        'whitesupremacist_Pro':'',
        'whitesupremacist_Anti':'',
        'whitesupremacy_Pro':'',
        'whitesupremacy_Anti':''
}
screen_name = ''
tweet_id = ''
tweet_date = ''
name = ''
description = ''
screen_name = ''
stance = '-1'
hashtag = ''
counter = 0
# walking through directories and subdirectories
for subdir, dirs, files in os.walk(rootdir):
        for file in files:
                if '.json' in file:
                        list_emojis = []
                        with open(os.path.join(subdir, file), 'r', encoding='utf8', errors='ignore') as user_file:
                                for line in user_file:
                                        parsed_user_json = json.loads(line)
                                        tweet_id = parsed_user_json["id"]
                                        tweet_date = parsed_user_json["created_at"]
                                        name = parsed_user_json["user"]["name"].replace('\n', ' ').replace('\t', ' ')
                                        description = parsed_user_json["user"]["description"].replace('\n', ' ').replace('\t', ' ')
                                        screen_name = '@' + parsed_user_json["user"]["screen_name"].replace('\n', ' ').replace('\t', ' ')
                                        break
                                hashtag = regex.findall(r'hashtags_user.*\\(.*)', subdir)[0]
                                stance = find_stance_csv(screen_name, hashtag)
                                all_tweets = ''
                                for line in user_file:
                                        parsed_user_json = json.loads(line)
                                        all_tweets = all_tweets + parsed_user_json["full_text"].replace('\n', ' ').replace('\t', ' ')
                                        # list_emojis.append(find_emojis(name_emoji))
                                        # list_emojis.append(find_emojis(description_emoji))
                                write_list_to_csv_user('name_emojis_v2.tsv', hashtag, screen_name, stance, name, description, tweet_date, tweet_id, all_tweets)
                                print(file, hashtag, ' row created.')
