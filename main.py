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
print('text_lst\n', text_lst)
reversed_text_lst = text_lst[::-1]
print('reversed_text_lst\n', reversed_text_lst)
# </editor-fold>
# <editor-fold desc="get the index of hashtags in text">
hashtag_index_reversed_lst = []
for hashtag in hashtag_lst:
    for word in reversed_text_lst:
        if hashtag in word:
            if reversed_text_lst.index(word) not in hashtag_index_reversed_lst:
                hashtag_index_reversed_lst.append(reversed_text_lst.index(word))
backup_hashtag_index_reversed_lst = hashtag_index_reversed_lst
print('hashtag_index_reversed_lst\n', hashtag_index_reversed_lst)
# </editor-fold>

for word in reversed_text_lst:
    print('word', word)
    if reversed_text_lst.index(word) not in hashtag_index_reversed_lst:
        reversed_text_lst[reversed_text_lst.index(word)] = 'x'
    else:
        print(f'index {reversed_text_lst.index(word)} word {word}')
        # hashtag_index_in_hashtag_lst = hashtag_lst.index(reversed_text_lst[reversed_text_lst.index(word)])
        # reversed_text_lst[reversed_text_lst.index(word)] = hashtags_keys_lst[hashtag_index_in_hashtag_lst]

print(reversed_text_lst)

# <editor-fold desc="end">
file = open('Push notifcations.txt', 'r+')
file.write(text)
# </editor-fold>

# 1 #pushnotification 2 #pushnotification 3 #pushnotification 4 #targeting 5 #targeting 6 #targeting