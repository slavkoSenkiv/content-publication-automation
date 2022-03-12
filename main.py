# <editor-fold desc="start">
file = open('Push notifcations.txt', 'r+')
text = file.read()
file.truncate(0)
file.close()
# </editor-fold>

hashtags_keys_lst = ['push notification', 'targeting']
hashtag_lst = ['#pushnotification', '#targeting']
# <editor-fold desc="replays hashtag keys with hashtags">
for hashtag_key in hashtags_keys_lst:
    hashtag = f'#{hashtag_key.replace(" ", "")}'
    if hashtag_key in text:
        text = text.replace(hashtag_key, hashtag)
# </editor-fold>
# <editor-fold desc="convert text into reversed words list">
text = text.replace('\n', '\n ')
# <editor-fold desc="eliminate ##, '  ', '\n '">
while '##' in text:
    text = text.replace('##', '#')
while '  ' in text:
    text = text.replace('  ', ' ')
"""while '\n ' in text:
    text = text.replace('\n ', '\n')"""
# </editor-fold>
text_lst = text.split(' ')
print(text_lst)
reversed_text_lst = text_lst[::-1]
print(reversed_text_lst, '\n')
# </editor-fold>
# <editor-fold desc="get the index of hashtags in text">
hashtag_index_lst = []
for hashtag in hashtag_lst:
    for word in reversed_text_lst:
        print('h & w', hashtag, word)
        if hashtag in word:
            print('HERE hashtag in word')
            if reversed_text_lst.index(word) not in hashtag_index_lst:
                #todo how to eliminate one of 0 and 4 or one of 8 and 1 in hashtag_index_lst
                hashtag_index_lst.append(reversed_text_lst.index(word))
print(reversed_text_lst)
print(hashtag_index_lst)
# </editor-fold>

# <editor-fold desc="end">
file = open('Push notifcations.txt', 'r+')
file.write(text)
# </editor-fold>

