import soundcloud
import flickrapi

sclient = soundcloud.Client(client_id='f9fa7918930dcdebe0fb80b9bec4e1c9')

#Finds First SoundCloud Track based on Search Results of Inputted Query
def findTrack(input):
    track = sclient.get('/tracks',q=input)[0]
    return track


#Takes Track Object and creates a HTML for SoundCloud Widget of Track    
def getWidget(track):
    trackurl = track.permalink_url

    embed_info = sclient.get('/oembed', url=trackurl)
    return embed_info.html

#def findPic(input):

track = findTrack("Angels")
print getWidget(track) 
