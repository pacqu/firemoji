import soundcloud
import flickrapi

sclient = soundcloud.Client(client_id='f9fa7918930dcdebe0fb80b9bec4e1c9')

#finds song pased on input, creates widget
def findSong(input):
    #find song
    track = sclient.get('/tracks',q=input)[0]
    trackurl = sclient.get(track.stream_url, allow_redirects=False)

    #test 
    print stream_url.location

    #make widget
    embed_info = client.get('/oembed', url=trackurl)
    print embed_info['html']

def findPic(input):
    
