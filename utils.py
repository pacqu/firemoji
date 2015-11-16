import soundcloud
import flickrapi
import json

sclient = soundcloud.Client(client_id='f9fa7918930dcdebe0fb80b9bec4e1c9')

#Finds First SoundCloud Track based on Search Results of Inputted Query
def findTrack(input):
    track = sclient.get('/tracks',q=input)[0]
    return track


#Takes Track Object and creates a HTML for SoundCloud Widget of Track    
def getWidget(track):
    #Should be something here to take into account if track is null object
    trackurl = track.permalink_url

    embed_info = sclient.get('/oembed', url=trackurl)
    return embed_info.html


#*********************Flickrapi******************************

api_key = u'8ab8c53a1cbb1ce32cf6329f35f38c29'
api_secret = u'89c00afdacfc0a80'
    
flickr = flickrapi.FlickrAPI(api_key, api_secret,format='parsed-json')


def getPhotoset(search):
    return flickr.photos.search(text=search, per_page='4')
    #Photoset is Dictionary, with sub-dict 'photos' representing all results, containing key 'photo' whose value is photos according to search query in 'photo',
    #key 'photo' contain list of sub-dicts that represent search-result photos
    #print photoset['photos']['photo']


#With inputted photoset, returns array of top 4 image urls from flickr
def getUrl(photoset,i):
    #for x in range(0, 4):
    p = photoset['photos']['photo'][i]
        #print p
    farmid = str(p['farm'])
    servid = str(p['server'])
    id = str(p['id'])
    sec = str(p['secret'])
    imgurl = "https://farm" + farmid + ".staticflickr.com/" + servid + "/" + id + "_" + sec + ".jpg"
        #imgset.append(imgurl)
    return imgurl

#With inputted photoset, returns array of top 4 image titles from flickr
def getTitle(photoset,i):
    titleset =[] 
    #for x in range(0,4):
    p = photoset['photos']['photo'][i] 
    title = p['title']
    #    titleset.append[title]
    return title


#Returns the Username of the person who uploaded the picture
def getUser(photoset,i):
    #print p
    p = photoset['photos']['photo'][i]
    ownerid= p['owner']
    #print ownerid
    user = flickr.people.getInfo(user_id='52673967@N00') 
    #print "anything"
    return user['person']['username']['_content']


def getPics(photoset):
    imgset = []
    for x in range(0,4):
        dict = {
            'url' :  getUrl(photoset,x),
            'title' : getTitle(photoset,x),
            'user' :  getUser(photoset,x)
            }
        imgset.append(dict)
    return imgset
    
p = getPhotoset("Greg")
#print p
print getPics(p)
