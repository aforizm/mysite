import pafy

def GetLink(link):
	url = link
	video = pafy.new(url)
	streams = video.streams
	best = video.getbest()
	return best.url

if __name__ == '__main__':
	print(GetLink('https://www.youtube.com/watch?v=_Va9uu_aWj8'))
