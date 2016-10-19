import requests # HTTP request system
import random # random number generator
import time # printing access times and waiting
import re # regular expression searcher
import json # json interpreter
import pprint # printing nicely
#from fake_useragent import UserAgent # fake useragent
from sys import argv # take in input file
import sys # to exit program [ sys.exit() ]
import datetime # to convert unix to readable date

def printer( instagramData ): # prints info for all items on one page load
    count = 0
    while( count < 11 ): # every reload loads 12 elements
        
        target.write( instagramData['entry_data']['ProfilePage'][0]['user']['media']['nodes'][count]['code'] ) # printing the code of the photo
        target.write( "\t" )
    
        target.write( str( instagramData['entry_data']['ProfilePage'][0]['user']['media']['nodes'][count]['likes']['count'] ) ) # printing the # of likes
        target.write( "\t" )

        target.write( str( instagramData['entry_data']['ProfilePage'][0]['user']['media']['nodes'][count]['date'] ) )
        target.write( "\t" )

        target.write( str( instagramData['entry_data']['ProfilePage'][0]['user']['media']['page_info']['end_cursor'] ) ) # this is where the start cursor and start cursor buttons are
        target.write( "\n" )
        
    
        count = count + 1

    return

def response_call( extension ):
    #    headers = {'user-agent': ua.random}
    username = "realdonaldtrump"
    baseURL = "http://instagram.com/"
    #response = requests.get( baseURL + username + extension, headers = headers )
    response = requests.get( baseURL + username + extension )
    #print( baseURL + username + extension )

    return response

def time_elapsed( start_time, end_time ):

    time_diff = ( end_time - start_time )

    return time_diff

def array_builder ( instagramData ):
    count = 0
    while (count < 11)

        array1[ instagramData['entry_data']['ProfilePage'][0]['user']['media']['nodes'][count]['date'] ] += instagramData['entry_data']['ProfilePage'][0]['user']['media']['nodes'][count]['likes']['count']
    return array1

















script, filename = argv
target = open(filename, 'w')

#ua = UserAgent() # WHY DOES THIS WORK
pp = pprint.PrettyPrinter( indent=2 )




extension = "" # for next page, not necessary at first
response = response_call( extension ) # getting basic data


match = re.search( '<script type="text/javascript">window\._sharedData = (.+);</script>',
                   str(response.content, 'utf-8') )
if match:
	instagramData = json.loads( match.group(1) )
else:
	instagramData = None







target.write( "Number of posts: " )
target.write( "\t" )
post_count = instagramData['entry_data']['ProfilePage'][0]['user']['media']['count']  #Calling number of posts
target.write( str ( post_count ) ) # writing number of posts
target.write( "\n" )

target.write( "\n" )
target.write( "\n" )
target.write( "\n" )





target.write( 'Code' ) #header
target.write( "\t" )
target.write( "\t" )
target.write( 'Likes' )
target.write( "\t" )
target.write( 'Date' )
target.write( "\t" )
target.write( "\t" )
target.write( 'end_cursor' )
target.write( "\n" )
target.write( "\n" )



#printer( instagramData ) # call for writing to output.txt (first page load)

array1 = [None] * 1500000000

count = 0
while ( count < ( post_count / 12 ) ): # iterating requests

    extension = ( "/?max_id=" + str( instagramData['entry_data']['ProfilePage'][0]['user']['media']['page_info']['end_cursor'] ) ) #calling the end_cursor int to append to the url calls

    response = response_call( extension ) # loading page

    ########

    match = re.search( '<script type="text/javascript">window\._sharedData = (.+);</script>',
                      str(response.content, 'utf-8') ) # searching for json

    if match:
        instagramData = json.loads( match.group(1) )
    else:
        instagramData = None


    ########
    #printer( instagramData ) # printing the data

    array1 = array_builder( instagramData ) # building the array

    target.write( "\n" )

    time.sleep( random.randint(1,2) / 5.0 )



    count = count + 1














