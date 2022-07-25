def create_youtube_video(title, description):
	dictionary={"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}}
	return dictionary
def like(youtubevideo):
	if "likes" in youtubevideo:
		youtubevideo['likes']+=1
	return youtubevideo
def dislike(youtubevideo):
	if "dislikes" in youtubevideo:
		youtubevideo['dislikes']+=1
	return youtubevideo

def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"][username]= comment_text
	return youtubevideo

new_vid= create_youtube_video('meet y2 summer 2022', 'such a heartache already')
like(new_vid)
dislike(new_vid)
add_comment(new_vid)
print(new_vid)