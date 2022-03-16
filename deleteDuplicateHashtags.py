import gspread


def del_duplicates(sheet_name_str):
    lst = hashtags_gs.worksheet(sheet_name_str).col_values(1)
    lst = list(dict.fromkeys(lst))
    for i in range(len(lst)):
        lst[i] = [lst[i]]
    hashtags_gs.worksheet(sheet_name_str).clear()
    hashtags_gs.worksheet(sheet_name_str).update(f'A1:A{len(lst)}', lst)


hashtags_gs = gspread.oauth().open('hashtags')
hashtags_keys_lst = hashtags_gs.worksheet('hashtag keys').col_values(1)
important_hashtags_lst = hashtags_gs.worksheet('important hashtags').col_values(1)

del_duplicates('hashtag keys')
del_duplicates('important hashtags')


