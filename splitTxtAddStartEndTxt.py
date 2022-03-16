import gspread
import re
import pprint


# <editor-fold desc="start">
def replace_last(string, old, new, occurrence):
    li = string.rsplit(old, occurrence)
    return new.join(li)


post_count_lst = ['first', 'second', 'third', 'fifth', 'sixth', 'seventh', 'tenth']
end_text = """\nFollow @gamedevbiz if you want to read the next part from push notification series
Tag a friend who may struggling as I was before found out these tricks
Share the post in your story or feed to show your colleagues this piece
Comment  your thoughts about where I was wrong or like a post if you found it useful\n\n"""
hashtags_keys_lst_of_lst = gspread.oauth().open('під рукою робоча таблиця різне').worksheet('хештеги').get_values()
raw_text = open('text before.txt', 'r+').read()
text_lst = re.split(r'P\d_', raw_text)

hashtags_keys_lst = []
for lst in hashtags_keys_lst_of_lst:
    for hashtag_key in lst:
        hashtags_keys_lst.append(hashtag_key)

hashtag_lst = []
for hashtag_key in hashtags_keys_lst:
    hashtag = '#' + re.sub('\s|-', '', hashtag_key)
    hashtag_lst.append(hashtag)
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
print('+++++++++++++++++++++++++++++' * 3)
# </editor-fold>

# <editor-fold desc="add start and end text">
main_title = re.search(r'T\d.+', text_with_hashtags)
main_title = main_title.group()
titles_lst = re.findall(r'P\d.+', text_with_hashtags)
print(main_title)
print(pprint.pformat(titles_lst))
print()

posts_with_hashtags_lst = re.split(r'P\d\s.+', text_with_hashtags)
posts_with_hashtags_lst = posts_with_hashtags_lst[1:]
print(posts_with_hashtags_lst)
print()

final_text = ''
for i in range(len(titles_lst)):
    start_text = f"\nIt's {post_count_lst[i]} post in {main_title} series\n"
    past_posts_text = 'past post' + str(titles_lst[:i])
    next_posts_text = 'next post' + str(titles_lst[i+1:])
    final_text += titles_lst[i] + start_text + past_posts_text + '\n' + text_lst[i] + '\n' + next_posts_text + '\n' + end_text

final_text2 = final_text.replace('\n\n\n', '\n')
print(final_text)
# </editor-fold>

# <editor-fold desc="write into docs">
file_after = open('text after.txt', 'r+')
file_after.truncate(0)
file_after.write(final_text)
print('done')
# </editor-fold>






