def make_album (artist_name,album,count=''):
  if count:
    music = {'Artist':artist_name.title(),'Album_name':album.title(),'No.of Tracks':count}
  else:
     music = {'Artist':artist_name,'Album_name':album}

  return music
song1 = make_album('justin','baby',5)
print(song1)

song2 = make_album('shawn','senorita')
song3 = make_album('sushant','sarangi',2)
print(song2)
print(song3)
