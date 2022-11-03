from distutils.core import setup

setup(
    name = "playlistsTime",
    version = "0.1",
    description="Creat sub-playlist of a specific given time and plays its",
    long_description="""
    Parameter : 
        -Set of music : repository or spotify playlist ,...
        -Time of the sub_playlist
        -Time of the break
    Do : 
        Play the sub-playlists of the specific given time with 
        a specific given time break between each of those
        """,
    author = "Blopausore/Smaug/Gush",
    url = "https://github.com/Blopausore/PlaylistPython",
    install_requires = [
        'mutagen.mp3',
        'spotipy',
        'vlc',
        'time',
        'abc'
    ]
     
)