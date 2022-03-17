import gspread
import re
import pyperclip


def replace_last(string, old, new, occurrence):
    li = string.rsplit(old, occurrence)
    return new.join(li)


hashtags_gs = gspread.oauth().open('hashtags')
hashtags_keys_lst = hashtags_gs.worksheet('hashtag keys').col_values(1)
important_hashtags_lst = hashtags_gs.worksheet('important hashtags').col_values(1)
text = open('text before.txt', 'r+').read()

hashtag_lst = []
for hashtag_key in hashtags_keys_lst:
    hashtag = '#' + re.sub('\s|-', '', hashtag_key)
    hashtag_lst.append(hashtag)

for i in range(2):
    for hashtag_key in hashtags_keys_lst:
        if hashtag_key in text:
            hashtag_key_index = hashtags_keys_lst.index(hashtag_key)
            text = replace_last(text, hashtag_key, hashtag_lst[hashtag_key_index], 1)
            hashtags_keys_lst[hashtag_key_index] = '#@)₴$0'

    text = text.replace('##', '#')
    text = text.replace('  ', ' ')
    text += '\n'

for important_hashtag in important_hashtags_lst:
    if important_hashtag not in text:
        text += '#' + important_hashtag + ' '

pyperclip.copy(text)
print('text_with_hashtags\n', text)

