def make_album(artist_name, album_title, number_of_tracks=''):
    album = {'artist': artist_name, 'title': album_title}
    if number_of_tracks:
        album['tracks'] = number_of_tracks 
    return album

# album1 = make_album('billie eilish', 'when we all fall asleep')
# album2 = make_album('lana del rey', 'norman fucking rock')
# album3 = make_album('solange', 'when i get home')
# album4 = make_album('big thief', 'u.f.o.f.', 10)

# print(album1)
# print(album2)
# print(album3)
# print(album4)

while True:
    artist = input("Input Artist: ('q' for exit)")
    if artist == 'q':
        break
    title = input("Input Title: ('q' for exit)")
    if title == 'q':
        break

    print(make_album(artist, title))


