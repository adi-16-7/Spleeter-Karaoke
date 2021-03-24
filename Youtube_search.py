import pafy
from youtubesearchpython import VideosSearch


videosSearch = VideosSearch('ikul rae mulla', limit =10)
results = videosSearch.result()
print(results)

downloadFolder = "/home/aditya/Desktop/spleeter"
url = results.get(result[0])
