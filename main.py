# <editor-fold desc="start">
import gspread
file_before = open('text before.txt', 'r+')
text = file_before.read()
file_before.close()
gs_name1 = 'під рукою робоча таблиця різне'
path_to_gspread_credentials_json = '/Users/ysenkiv/.config/gspread/credentials.json'
path_to_gspread_authorized_user = '/Users/ysenkiv/.config/gspread/authorized_user.json'
gc = gspread.oauth()
gs = gc.open(gs_name1)
hashtag_sheet = gs.worksheet('хештеги')
# </editor-fold>

# <editor-fold desc="get and built hashtags lists">
hashtags_keys_lst_of_lst = hashtag_sheet.get_values()

hashtags_keys_lst = []
for lst in hashtags_keys_lst_of_lst:
    for hashtag_key in lst:
        hashtags_keys_lst.append(hashtag_key)

hashtag_lst = []
for hashtag_key in hashtags_keys_lst:
    hashtag = '#' + hashtag_key.replace(' ', '')
    hashtag_lst.append(hashtag)
# </editor-fold>


def replace_last(string, old, new, occurrence):
    li = string.rsplit(old, occurrence)
    return new.join(li)


for i in range(2):
    for hashtag_key in hashtags_keys_lst:
        if hashtag_key in text:
            hashtag_key_index = hashtags_keys_lst.index(hashtag_key)
            text = replace_last(text, hashtag_key, hashtag_lst[hashtag_key_index], 1)
            hashtags_keys_lst[hashtag_key_index] = '#@)₴$0'

text = text.replace('##', '#')
text = text.replace('  ', ' ')
file_after = open('text after.txt', 'r+')
file_after.truncate(0)
file_after.write(text)
print('done')

# 1 push notification 2 push notification 3 push notification 4 targeting 5 targeting 6 targeting
