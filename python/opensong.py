"Open song library parser"
import io
import os
import sys
import xml.etree.ElementTree as ET

def parse_opensong_lyrics(text):
    "OpenSong lyrics parser. Returns dict(verse label -> list(lyrics lines))"
    result = {}
    currentVerseNumber = "V1"
    currentVerseLines = []
    for line in iter(text.splitlines()):
        line = line.strip()
        if not line:
            continue
        # strip out comments and empty lines
        if line.startswith(";") or line.startswith("."):
            continue
        # verse code
        if line.startswith("["):
            # start of a new verse
            # first, if we already had a verse, add it to result
            if currentVerseLines:
                result[currentVerseNumber] = currentVerseLines
            # clear state
            currentVerseNumber = line[1:-1]
            currentVerseLines = []
            # sanity check
            if currentVerseNumber.find("[") != -1 or currentVerseNumber.find("]") != -1:
                raise ValueError("%s: invalid verse number %s" % (text, currentVerseNumber))
        else:
            # continuation of verse
            currentVerseLines.append(line)
    # add last verse (if any) to result
    if currentVerseLines:
        result[currentVerseNumber] = currentVerseLines
    return result

class OpenSong(object):
    "Class for holding OpenSong data for one song."
    KNOWN_SONGBOOKS = ("Ps.", "GK", "Lb.", "NLB", "Opw.", "E&amp;R", "PvN", "NGB")
    
    def __init__(self, path):
        self.title = None
        self.songbook = None
        self.number = None
        self.presentation = []
        self.verses = {}
        self.path = path
        try:
            tree = ET.parse(path)
            song = tree.getroot()
            title = song.find("title").text
            self.title = title
            songBook = title.split(" ")[0]
            if not songBook in self.KNOWN_SONGBOOKS:
                songBook = None
            self.songbook = songBook
            hymnNumberNode = song.find("hymn_number")
            if hymnNumberNode is not None:
                hymnNumber = hymnNumberNode.text
            else:
                hymnNumber = None
            self.number = hymnNumber
            presentation = []
            presentationNode = song.find("presentation")
            if presentationNode is not None:
                presentationText = presentationNode.text
                if presentationText:
                    presentation = presentationText.strip().split(" ")
            self.presentation = presentation
            lyrics = song.find("lyrics").text
            self.verses = parse_opensong_lyrics(lyrics)
        except ET.ParseError:
            raise ValueError("%s: failed to parse" % path)
    
    def getVerse(self, number):
        verseKey = "V%d" % number
        if not verseKey in self.verses.keys():
            sys.stderr.write("Verse %s not found in %s %s\n" % (number, self.songbook, self.number))
            return ["***%s %s vers %s bestaat niet***" % (self.songbook, self.number, number)]
        return self.verses[verseKey]
    
    def verseKeyToCouplet(self, key):
        if key.startswith("V"):
            return key[1:]
        return key
    
    def getVerses(self):
        for verseKey in self.verses:
            yield self.verseKeyToCouplet(verseKey), self.verses[verseKey]
    
    def __str__(self):
        return "%s %s, presentation %s, verses %s" % (self.songbook, self.number, self.presentation, self.verses)
        

class OpenSongLibrary(object):
    "OpenSong library"
    def __init__(self, rootPath):
        self.books = {}
        self.songs = {}
        
        for path, subdirs, files in os.walk(rootPath):
            for name in files:
                songPath = os.path.join(path, name)
                #print songPath
                try:
                    openSong = OpenSong(songPath)
                except ValueError:
                    continue
                
                # Put song in book, if it has a book
                if openSong.songbook:
                    book = openSong.songbook
                    if self.books.has_key(book):
                        bookContents = self.books[book]
                    else:
                        bookContents = {}
                        self.books[book] = bookContents
                    bookContents[openSong.number] = openSong
                    
                # Put song in global song list
                title = openSong.title
                if self.songs.has_key(title):
                    #raise ValueError("%s: duplicate song title with %s" % (songPath, self.songs[title].path))
                    sys.stderr.write("Warning: %s: duplicate song title with %s, discarding\n" % (songPath, self.songs[title].path))
                self.songs[title] = openSong
                
    def getSongFromBook(self, book, number):
        bookDict = self.books[book]
        return bookDict[number]

if __name__ == "__main__":
    library = OpenSongLibrary('..\\songs\\')
    print "library: %d songs in %d categories" % (len(library.songs), len(library.books.keys()))
    