import codecs
import sys
from antlr4 import *
from generated.LiturgieLexer import LiturgieLexer
from generated.LiturgieParser import LiturgieParser
from generated.LiturgieListener import LiturgieListener
from generated.LiturgieVisitor import LiturgieVisitor
from win32security import CtxtHandleType
from opensong import OpenSongLibrary

#
# Mapping of parser book labels to OpenSong book labels 
#
PARSER_BOOK_TO_OPENSONG_BOOK = {
    "psalm" : "Ps.",
    "gezang" : "GK",
    "liedboek" : "Lb.",
    "opwekking" : "Opw.",
    "nlb" : "NLB",
    "pvn" : "PvN"
}

class LiturgieSong(object):
    "Liturgie Song Element"
    def __init__(self, bundel, nummer, coupletten):
        self.bundel = bundel
        self.nummer = nummer
        self.coupletten = coupletten
        
    def printText(self, database):
        "Print full text of this element"
        databaseBook = PARSER_BOOK_TO_OPENSONG_BOOK[self.bundel]
        song = database.getSongFromBook(databaseBook, self.nummer)
        
        if song is None:
            print "***%s %s niet in bibliotheek gevonden***" % (databaseBook, self.nummer)
            print
            return
        
        # do we have verses?
        if self.coupletten:
            # yes: print only selected coupletten
            for coupletNummer in self.coupletten:
                print "%s %s: %d" % (self.bundel.capitalize(), self.nummer, coupletNummer)
                print
                regels = song.getVerse(coupletNummer)
                print "\n".join(regels)
                print
        else:
            # no: print song in OpenSong order
            for coupletNummer, regels in song.getVerses():
                print "%s %s: %s" % (self.bundel.capitalize(), self.nummer, coupletNummer)
                print
                print "\n".join(regels)
                print
        
    def __repr__(self):
        return "%s %s %s" % (self.bundel, self.nummer, self.coupletten)
    
class MyLiturgieVisitor(LiturgieVisitor):
    """
    Visitor for liturgie parse tree
    Returns list of liturgie elements.
    """
    def visitLiturgie(self, ctx):
        result = []
        for regel in ctx.regel():
            regelResult = self.visit(regel)
            if regelResult:
                result.append(regelResult)
        return result
        
    def visitRegel(self, ctx):
        result = None
        if ctx.lied():
            result = self.visit(ctx.lied())
        return result
    
    def visitLied(self, ctx):
        bundel = self.visit(ctx.bundel())
        nummer = ctx.liednummer().getText()
        couplettenList = None
        if ctx.coupletten():
            couplettenList = self.visit(ctx.coupletten())
        return LiturgieSong(bundel, nummer, couplettenList)
    
    def visitPsalm(self, ctx):
        return "psalm"
    
    def visitGezang(self, ctx):
        return "gezang"
    
    def visitLiedboek(self, ctx):
        return "liedboek"
    
    def visitOpwekking(self, ctx):
        return "opwekking"
    
    def visitNlb(self, ctx):
        return "nlb"
    
    def visitPvn(self, ctx):
        return "pvn"
    
    def visitCoupletten(self, ctx):
        result = []
        for couplet in ctx.couplet():
            result.extend(self.visit(couplet))
        return result
        
    def visitCouplet(self, ctx):
        result = []
        for nummer_of_nummers in ctx.nummer_of_nummers():
            result.extend(self.visit(nummer_of_nummers))
        return result
    
    def visitNummer_of_nummers(self, ctx):
        obj = ctx.getChild(0)
        if isinstance(obj, LiturgieParser.NummerContext):
            return [int(obj.getText())]
        else:
            rangeStart = int(obj.getChild(0).getText())
            rangeEnd = int(obj.getChild(2).getText())
            return range(rangeStart, rangeEnd + 1)

def convertStream(input, database):
    "Parse input character stream and print out song texts"
    lexer = LiturgieLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LiturgieParser(stream)
    tree = parser.liturgie()
        
    # get list of objects from liturgie
    visitor = MyLiturgieVisitor();
    liturgieObjectList = visitor.visitLiturgie(tree)
        
    # print texts
    for element in liturgieObjectList:
        element.printText(database)
        
def main(argv):
    "Program entry point"
    paths = argv[1:]
    if len(paths) == 0:
        return
    
    # read in song database
    print "reading song database..."
    database = OpenSongLibrary("..\\songs\\")

    for inputPath in paths:
        print "####" * 20
        print "handling %s" % inputPath
        print "####" * 20
        
        # parse input
        input = FileStream(inputPath)
        convertStream(input, database)

if __name__ == "__main__":
 	main(sys.argv)
 	