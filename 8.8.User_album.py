def make_album (artist_name,album_title,count=''):
  album = {
    'artist': artist_name.title(),
    'title': album_title.title(),
  }
  if count:
    album['tracks'] = count
  return album

while True:
      print("\nEnter the artist's name and album title (or 'quit' to stop):")

      artist = input('artist name: ')
      if artist.lower() == 'quit':
         break
      title = input('Album title: ')
      if title.lower() == 'quit':
         break
      
      count = input('Number of tracks (optional,press Enter to skip):')
      if count.lower() == 'quit':
         break
      if count:
         album = make_album(artist,title,int(count))
      else:
         album = make_album(artist, title)


      print("\nAlbum details: ")
      print(album)   
