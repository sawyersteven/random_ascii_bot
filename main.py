import praw
import replies
import pdb
import time

'''
comment_properties = [
    'controversiality',
    'saved',
    'num_comments',
    'likes',
    'banned_at_utc',
    'ups',
    'parent_id',
    'user_reports',
    'banned_by',
    'body_html',
    'body',
    'collapsed_reason',
    'author',
    'author_flair_background_color',
    'approved_at_utc',
    'quarantine',
    'permalink',
    'link_title',
    'approved_by',
    'link_id',
    'author_flair_css_class',
    'removal_reason',
    'mod_reason_by',
    '_replies',
    'stickied',
    'downs',
    'link_author',
    'author_flair_text',
    'mod_reason_title',
    'author_flair_template_id',
    'mod_note',
    'subreddit_type',
    'link_permalink',
    'subreddit_name_prefixed',
    'num_reports',
    'author_flair_text_color',
    'name',
    'collapsed',
    '_fetched',
    'mod_reports',
    'link_url',
    'created',
    'subreddit',
    'score_hidden',
    'can_gild',
    'can_mod_post',
    'created_utc',
    'author_flair_type',
    'subreddit_id',
    'score',
    'edited',
    '_info_params',
    'is_submitter',
    '_mod',
    'report_reasons',
    'rte_mode',
    'author_flair_richtext',
    '_submission',
    '_reddit',
    'gilded',
    'distinguished',
    'over_18',
    'archived',
    'no_follow',
    'id',
    'send_replies'
]
'''

reddit = praw.Reddit(client_id='v2rSm1WhCQgXkQ',
                     client_secret='Y3JVltd0UGF3XX7FfXboJn1U2VY',
                     password='iAh9LN$!54EY',
                     user_agent='random_ascii_bot',
                     username='random_ascii')


def start():
    start_time = time.time()

    for comment in reddit.subreddit('popular').stream.comments():
        try:
            if comment.created_utc < start_time:
                continue

            reply = None

            if ' ftw' in comment.body.lower():
                reply = replies.ftw(comment.body)
            elif len(comment.body) > 6 and all(i == ' ' for i in comment.body[1::2]):
                reply = replies.spaced_out(comment.body)

            if reply is not None:
                comment.reply(reply)
                print('REPLIED TO: ')
                print(comment.link_url)
                print('\n')
                start_time += 3600
        except Exception as e:  # noqa
            print(e)
            start_time += 600
            start_time = time.time()
			
if __name__ == '__main__':
	start()
