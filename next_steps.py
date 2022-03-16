#todo add "“What are game push notifications” is my first post in a series about game push notifications "
#todo add Be sure to check the next posts in the push notification series => other posts except the current one
#todo follow tag commetn share stuff
import re
import pprint
text2 = """
T1 Push notifications
P1 What are game push notifications?
Writing and targeting game push notifications is a part of my day-to-day routine or business-as-usual (BAU) stuff as we call it inside our team. While it looks like a pretty simple task at the first glance 👁, it is a really time-consuming daily challenge for me. 

P2 Why push notifications are important for games?
But why are game push notifications so important? Obviously, because they provide an additional way to notify the players about in-game sales or events. The most common way of information delivery to players is an in-game pop-up. 

P3 Avoid players unsubscribing from push notifications
Now, let’s talk about how to avoid player unsubscribing. This part may be relative to the email notifications too. Some of us are trying to play as many games as possible in order to be up to date with the market situation. Quite often we turn notifications off because of push notifications waterfall from these games."""

end_text2 = """\nFollow @gamedevbiz if you want to read the next part from push notification series
Tag a friend who may struggling as I was before found out these tricks
Share the post in your story or feed to show your colleagues this piece
Comment  your thoughts about where I was wrong or like a post if you found it useful\n\n"""

post_count_lst = ['first', 'second', 'third', 'fifth', 'sixth', 'seventh', 'tenth']
main_title = re.search(r'T\d.+', text2)
main_title = main_title.group()
titles_lst = re.findall(r'P\d.+', text2)
print(pprint.pformat(titles_lst))
print()

text2_lst = re.split(r'P\d\s.+', text2)
text2_lst = text2_lst[1:]
print(text2_lst)
print()

final_text2 = ''
for i in range(len(titles_lst)):
    start_text2 = f'\nThis is the {post_count_lst[i]} in {main_title} series\n'
    past_post_text2 = 'past post' + str(titles_lst[:i])
    next_post_text2 = 'next post' + str(titles_lst[i+1:])
    final_text2 += titles_lst[i] + start_text2 + past_post_text2 + '\n' + text2_lst[i] + '\n' + next_post_text2 + '\n' + end_text2

final_text2 = final_text2.replace('\n\n\n', '\n')
print(final_text2)
print('done')
