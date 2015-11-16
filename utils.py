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

#With inputted search query, return image url of top result from flickr
def getPic(search):
    photoset = flickr.photos.search(text=search, per_page='1')
    #Photoset is Dictionary, with sub-dict 'photos' representing all results, containing key 'photo' whose value is photos according to search query in 'photo',
    #key 'photo' contain list of sub-dicts that represent search-result photos
    #print photoset['photos']['photo']
    p = photoset['photos']['photo'][0]
    #print p
    farmid = str(p['farm'])
    servid = str(p['server'])
    id = str(p['id'])
    sec = str(p['secret'])
    imgurl = "https://farm" + farmid + ".staticflickr.com/" + servid + "/" + id + "_" + sec + ".jpg"
    return imgurl


#Returns the Title of the picture
def picTitle(search):
    photoset = flickr.photos.search(text = search, per_page='1')
    p = photoset['photos']['photo'][0] 
    title = p['title']
    return title


#Returns the Username of the person who uploaded the picture
def picUser(search):
    photoset = flickr.photos.search(text = search, per_page='1')
    p = photoset['photos']['photo'][0]
    print p
    ownerid= str(p['owner'])
    #print ownerid
    j = flickr.people.getInfo(ownerid) '<==error is here'
    '^ random variable cause I thought that it was the cause of an error'
    #print "anything"
    print user[username]


#flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
#sets   = flickr.photosets.getList(user_id='73509078@N00')
#title  = sets['photosets']['photoset'][0]['title']['_content']

#print('First set title: %s' % title)

getPic("Greg")
picTitle("Greg")
#picUser("Greg")

#track = findTrack("Angels")
# print getWidget(track) 
