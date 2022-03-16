# <editor-fold desc="start">
# <editor-fold desc="access files and sheets">
import gspread
import re
import pprint
file_before = open('text before.txt', 'r+')
text = file_before.read()
print('text', text)
file_before.close()
gs_name1 = 'під рукою робоча таблиця різне'
path_to_gspread_credentials_json = '/Users/ysenkiv/.config/gspread/credentials.json'
path_to_gspread_authorized_user = '/Users/ysenkiv/.config/gspread/authorized_user.json'
gc = gspread.oauth()
gs = gc.open(gs_name1)
hashtag_sheet = gs.worksheet('хештеги')
post_count_lst = ['first', 'second', 'third', 'fifth', 'sixth', 'seventh', 'tenth']
end_text = """\nFollow @gamedevbiz if you want to read the next part from push notification series
Tag a friend who may struggling as I was before found out these tricks
Share the post in your story or feed to show your colleagues this piece
Comment  your thoughts about where I was wrong or like a post if you found it useful\n\n"""
# </editor-fold>


# <editor-fold desc="get and built hashtags lists">
hashtags_keys_lst_of_lst = hashtag_sheet.get_values()

hashtags_keys_lst = []
for lst in hashtags_keys_lst_of_lst:
    for hashtag_key in lst:
        hashtags_keys_lst.append(hashtag_key)

hashtag_lst = []
for hashtag_key in hashtags_keys_lst:
    hashtag = '#' + re.sub('\s|-', '', hashtag_key)
    hashtag_lst.append(hashtag)

text_lst = re.split(r'P\d.+', text)

# </editor-fold>


def replace_last(string, old, new, occurrence):
    li = string.rsplit(old, occurrence)
    return new.join(li)


# </editor-fold>

# <editor-fold desc="add hashtags">
text_with_hashtags = ''
for post in text_lst:
    for i in range(2):
        for hashtag_key in hashtags_keys_lst:
            if hashtag_key in post:
                hashtag_key_index = hashtags_keys_lst.index(hashtag_key)
                post = replace_last(post, hashtag_key, hashtag_lst[hashtag_key_index], 1)
                hashtags_keys_lst[hashtag_key_index] = '#@)₴$0'

    post = post.replace('##', '#')
    post = post.replace('  ', ' ')
    text_with_hashtags += f'\n{post}'
print('text_with_hashtags\n', text_with_hashtags)
# </editor-fold>

# <editor-fold desc="add start and end text">
main_title = re.search(r'T\d.+', text)
main_title = main_title.group()
titles_lst = re.findall(r'P\d.+', text)
print(main_title)
print(pprint.pformat(titles_lst))
print()

text_with_hashtags_lst = re.split(r'P\d\s.+', text_with_hashtags)
text_with_hashtags_lst = text_with_hashtags_lst[1:]
print(text_with_hashtags_lst)
print()

final_text = ''
for i in range(len(titles_lst)):
    start_text2 = f'\nThis is the {post_count_lst[i]} in {main_title} series\n'
    past_posts_text = 'past post' + str(titles_lst[:i])
    next_posts_text = 'next post' + str(titles_lst[i+1:])
    final_text += titles_lst[i] + start_text2 + past_posts_text + '\n' + text_lst[i] + '\n' + next_posts_text + '\n' + end_text

final_text2 = final_text.replace('\n\n\n', '\n')
print(final_text)
# </editor-fold>

# <editor-fold desc="write into docs">
file_after = open('text after.txt', 'r+')
file_after.truncate(0)
file_after.write(final_text)
print('done')
# </editor-fold>

# 1 push notification 2 push notification 3 push notification 4 targeting 5 targeting 6 targeting