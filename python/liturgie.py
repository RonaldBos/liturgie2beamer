import sys
from antlr4 import *
from generated.LiturgieLexer import LiturgieLexer
from generated.LiturgieParser import LiturgieParser
from generated.LiturgieListener import LiturgieListener
from generated.LiturgieVisitor import LiturgieVisitor
from win32security import CtxtHandleType


""" TODO change visitor so that it returns a list of 
    song objects """
class MyLiturgieVisitor(LiturgieVisitor):
    "Visitor for liturgie parse tree"
    def visitLiturgie(self, ctx):
        for regel in ctx.regel():
            self.visit(regel)
        
    def visitRegel(self, ctx):
        if ctx.lied():
            self.visit(ctx.lied())
    
    def visitLied(self, ctx):
        bundelType = self.visit(ctx.bundel())
        print 'Soort: ' + bundelType
        print 'Nummer: ' + ctx.nummer().getText()
        if ctx.coupletten():
            couplettenList = self.visit(ctx.coupletten())
            print 'Coupletten: ' + str(couplettenList)
        print '---'
    
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
    
    def visitCoupletten(self, ctx):
        result = []
        for couplet in ctx.couplet():
            result.extend(self.visit(couplet))
        return result
        
    def visitCouplet(self, ctx):
        result = []
        for nummer in ctx.nummer():
            result.append(nummer.getText())
        return result
        

def main(argv):
    "program entry point"
    # parse input
    input = FileStream(argv[1])
    lexer = LiturgieLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LiturgieParser(stream)
    tree = parser.liturgie()
    
    # visit nodes
    visitor = MyLiturgieVisitor();
    visitor.visitLiturgie(tree)


if __name__ == "__main__":
 	main(sys.argv)
 	