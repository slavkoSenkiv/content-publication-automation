# <editor-fold desc="start">
file = open('Push notifcations.txt', 'r+')
text = file.read()
file.truncate(0)
file.close()
# </editor-fold>

hashtags_keys_lst = ['push notification', 'targeting']
reversed_hashtags_keys_lst = ['notification push', 'targeting']
hashtag_lst = ['#pushnotification', '#targeting']
print(text)
txt_lst = text.split(' ')
print(txt_lst)
reversed_txt_lst = txt_lst[::-1]
print(reversed_txt_lst)
reversed_txt = ''
for word in reversed_txt_lst:
    reversed_txt += f'{word} '
print(reversed_txt)

for reversed_key in reversed_hashtags_keys_lst:
    print('iteration for reversed_key =', reversed_key)
    if reversed_key in reversed_txt:
        print(f'{reversed_key} in reversed_txt')
        reversed_key_index = reversed_hashtags_keys_lst.index(reversed_key)
        print('reversed_key_index =', reversed_key_index)
        print(f'reversing {reversed_key} => {hashtag_lst[reversed_key_index]}')
        new_reserved_txt = reversed_txt.replace(reversed_key, hashtag_lst[reversed_key_index])
        print(new_reserved_txt)
        reversed_key = 'x'
        print(f'{reversed_hashtags_keys_lst[reversed_key_index]} was X replaced from reversed_hashtags_keys_lst')
        print('\n')

print(reversed_txt)
# <editor-fold desc="end">
file = open('Push notifcations.txt', 'r+')
file.write(text)
# 1 push notification 2 push notification 3 push notification 4 targeting 5 targeting 6 targeting
# 1 #pushnotification 2 #pushnotification 3 #pushnotification 4 #targeting 5 #targeting 6 #targeting
# </editor-fold>

