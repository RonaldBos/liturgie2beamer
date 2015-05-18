# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .LiturgieListener import LiturgieListener
    from .LiturgieVisitor import LiturgieVisitor
else:
    from LiturgieListener import LiturgieListener
    from LiturgieVisitor import LiturgieVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\34\u00a1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\3\2\6\2,\n\2\r\2\16\2")
        buf.write(u"-\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\39\n\3\3\3\3")
        buf.write(u"\3\3\4\3\4\3\4\5\4@\n\4\3\5\3\5\3\5\3\5\3\5\5\5G\n\5")
        buf.write(u"\3\6\3\6\6\6K\n\6\r\6\16\6L\3\7\3\7\3\7\7\7R\n\7\f\7")
        buf.write(u"\16\7U\13\7\3\7\3\7\3\b\3\b\5\b[\n\b\3\b\5\b^\n\b\3\t")
        buf.write(u"\3\t\5\tb\n\t\3\t\5\te\n\t\3\n\3\n\5\ni\n\n\3\n\3\n\5")
        buf.write(u"\nm\n\n\3\n\5\np\n\n\3\13\3\13\5\13t\n\13\3\13\5\13w")
        buf.write(u"\n\13\3\f\3\f\5\f{\n\f\3\r\3\r\3\16\3\16\3\17\3\17\7")
        buf.write(u"\17\u0083\n\17\f\17\16\17\u0086\13\17\3\20\3\20\7\20")
        buf.write(u"\u008a\n\20\f\20\16\20\u008d\13\20\3\21\3\21\3\22\3\22")
        buf.write(u"\7\22\u0093\n\22\f\22\16\22\u0096\13\22\3\23\3\23\3\24")
        buf.write(u"\3\24\3\25\6\25\u009d\n\25\r\25\16\25\u009e\3\25\2\2")
        buf.write(u"\26\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(\2\4")
        buf.write(u"\3\2\34\34\3\2\22\23\u00ab\2+\3\2\2\2\48\3\2\2\2\6<\3")
        buf.write(u"\2\2\2\bF\3\2\2\2\nH\3\2\2\2\fS\3\2\2\2\16]\3\2\2\2\20")
        buf.write(u"d\3\2\2\2\22o\3\2\2\2\24v\3\2\2\2\26x\3\2\2\2\30|\3\2")
        buf.write(u"\2\2\32~\3\2\2\2\34\u0080\3\2\2\2\36\u0087\3\2\2\2 \u008e")
        buf.write(u"\3\2\2\2\"\u0090\3\2\2\2$\u0097\3\2\2\2&\u0099\3\2\2")
        buf.write(u"\2(\u009c\3\2\2\2*,\5\4\3\2+*\3\2\2\2,-\3\2\2\2-+\3\2")
        buf.write(u"\2\2-.\3\2\2\2.\3\3\2\2\2/9\5\6\4\2\609\5\30\r\2\619")
        buf.write(u"\5\32\16\2\629\5\34\17\2\639\5\36\20\2\649\5 \21\2\65")
        buf.write(u"9\5\"\22\2\669\5$\23\2\679\5&\24\28/\3\2\2\28\60\3\2")
        buf.write(u"\2\28\61\3\2\2\28\62\3\2\2\28\63\3\2\2\28\64\3\2\2\2")
        buf.write(u"8\65\3\2\2\28\66\3\2\2\28\67\3\2\2\29:\3\2\2\2:;\7\34")
        buf.write(u"\2\2;\5\3\2\2\2<=\5\b\5\2=?\5(\25\2>@\5\n\6\2?>\3\2\2")
        buf.write(u"\2?@\3\2\2\2@\7\3\2\2\2AG\5\16\b\2BG\5\20\t\2CG\5\22")
        buf.write(u"\n\2DG\5\24\13\2EG\5\26\f\2FA\3\2\2\2FB\3\2\2\2FC\3\2")
        buf.write(u"\2\2FD\3\2\2\2FE\3\2\2\2G\t\3\2\2\2HJ\7\3\2\2IK\5\f\7")
        buf.write(u"\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\13\3\2\2")
        buf.write(u"\2NO\5(\25\2OP\7\4\2\2PR\3\2\2\2QN\3\2\2\2RU\3\2\2\2")
        buf.write(u"SQ\3\2\2\2ST\3\2\2\2TV\3\2\2\2US\3\2\2\2VW\5(\25\2W\r")
        buf.write(u"\3\2\2\2XZ\7\5\2\2Y[\7\32\2\2ZY\3\2\2\2Z[\3\2\2\2[^\3")
        buf.write(u"\2\2\2\\^\7\6\2\2]X\3\2\2\2]\\\3\2\2\2^\17\3\2\2\2_a")
        buf.write(u"\7\7\2\2`b\7\32\2\2a`\3\2\2\2ab\3\2\2\2be\3\2\2\2ce\7")
        buf.write(u"\b\2\2d_\3\2\2\2dc\3\2\2\2e\21\3\2\2\2fh\7\t\2\2gi\7")
        buf.write(u"\32\2\2hg\3\2\2\2hi\3\2\2\2ip\3\2\2\2jl\7\n\2\2km\7\32")
        buf.write(u"\2\2lk\3\2\2\2lm\3\2\2\2mp\3\2\2\2np\7\13\2\2of\3\2\2")
        buf.write(u"\2oj\3\2\2\2on\3\2\2\2p\23\3\2\2\2qs\7\f\2\2rt\7\32\2")
        buf.write(u"\2sr\3\2\2\2st\3\2\2\2tw\3\2\2\2uw\7\r\2\2vq\3\2\2\2")
        buf.write(u"vu\3\2\2\2w\25\3\2\2\2xz\7\16\2\2y{\7\32\2\2zy\3\2\2")
        buf.write(u"\2z{\3\2\2\2{\27\3\2\2\2|}\7\17\2\2}\31\3\2\2\2~\177")
        buf.write(u"\7\20\2\2\177\33\3\2\2\2\u0080\u0084\7\21\2\2\u0081\u0083")
        buf.write(u"\n\2\2\2\u0082\u0081\3\2\2\2\u0083\u0086\3\2\2\2\u0084")
        buf.write(u"\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085\35\3\2\2\2\u0086")
        buf.write(u"\u0084\3\2\2\2\u0087\u008b\t\3\2\2\u0088\u008a\n\2\2")
        buf.write(u"\2\u0089\u0088\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089")
        buf.write(u"\3\2\2\2\u008b\u008c\3\2\2\2\u008c\37\3\2\2\2\u008d\u008b")
        buf.write(u"\3\2\2\2\u008e\u008f\7\24\2\2\u008f!\3\2\2\2\u0090\u0094")
        buf.write(u"\7\25\2\2\u0091\u0093\n\2\2\2\u0092\u0091\3\2\2\2\u0093")
        buf.write(u"\u0096\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2")
        buf.write(u"\2\u0095#\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u0098\7\26")
        buf.write(u"\2\2\u0098%\3\2\2\2\u0099\u009a\7\27\2\2\u009a\'\3\2")
        buf.write(u"\2\2\u009b\u009d\7\30\2\2\u009c\u009b\3\2\2\2\u009d\u009e")
        buf.write(u"\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f")
        buf.write(u")\3\2\2\2\26-8?FLSZ]adhlosvz\u0084\u008b\u0094\u009e")
        return buf.getvalue()


class LiturgieParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"':'", u"','", u"'Ps'", u"'Psalm'", 
                     u"'Gz'", u"'Gezang'", u"'LB'", u"'OLB'", u"'Lied'", 
                     u"'Opw'", u"'Opwekking'", u"'NLB'", u"'Votum'", u"'Groet'", 
                     u"'Gebed'", u"'I'", u"'II'", u"'Preek'", u"'Geloofsbelijdenis'", 
                     u"'Collecte'", u"'Zegen'", u"<INVALID>", u"<INVALID>", 
                     u"'.'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"Digit", u"Character", 
                      u"Dot", u"WS", u"EOL" ]

    RULE_liturgie = 0
    RULE_regel = 1
    RULE_lied = 2
    RULE_bundel = 3
    RULE_coupletten = 4
    RULE_couplet = 5
    RULE_psalm = 6
    RULE_gezang = 7
    RULE_liedboek = 8
    RULE_opwekking = 9
    RULE_nlb = 10
    RULE_votum = 11
    RULE_groet = 12
    RULE_gebed = 13
    RULE_lezen = 14
    RULE_preek = 15
    RULE_belijdenis = 16
    RULE_collecte = 17
    RULE_zegen = 18
    RULE_nummer = 19

    ruleNames =  [ u"liturgie", u"regel", u"lied", u"bundel", u"coupletten", 
                   u"couplet", u"psalm", u"gezang", u"liedboek", u"opwekking", 
                   u"nlb", u"votum", u"groet", u"gebed", u"lezen", u"preek", 
                   u"belijdenis", u"collecte", u"zegen", u"nummer" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    Digit=22
    Character=23
    Dot=24
    WS=25
    EOL=26

    def __init__(self, input):
        super(LiturgieParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class LiturgieContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.LiturgieContext, self).__init__(parent, invokingState)
            self.parser = parser

        def regel(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LiturgieParser.RegelContext)
            else:
                return self.getTypedRuleContext(LiturgieParser.RegelContext,i)


        def getRuleIndex(self):
            return LiturgieParser.RULE_liturgie

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterLiturgie(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitLiturgie(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitLiturgie(self)
            else:
                return visitor.visitChildren(self)




    def liturgie(self):

        localctx = LiturgieParser.LiturgieContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_liturgie)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.regel()
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LiturgieParser.T__2) | (1 << LiturgieParser.T__3) | (1 << LiturgieParser.T__4) | (1 << LiturgieParser.T__5) | (1 << LiturgieParser.T__6) | (1 << LiturgieParser.T__7) | (1 << LiturgieParser.T__8) | (1 << LiturgieParser.T__9) | (1 << LiturgieParser.T__10) | (1 << LiturgieParser.T__11) | (1 << LiturgieParser.T__12) | (1 << LiturgieParser.T__13) | (1 << LiturgieParser.T__14) | (1 << LiturgieParser.T__15) | (1 << LiturgieParser.T__16) | (1 << LiturgieParser.T__17) | (1 << LiturgieParser.T__18) | (1 << LiturgieParser.T__19) | (1 << LiturgieParser.T__20))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegelContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.RegelContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOL(self):
            return self.getToken(LiturgieParser.EOL, 0)

        def lied(self):
            return self.getTypedRuleContext(LiturgieParser.LiedContext,0)


        def votum(self):
            return self.getTypedRuleContext(LiturgieParser.VotumContext,0)


        def groet(self):
            return self.getTypedRuleContext(LiturgieParser.GroetContext,0)


        def gebed(self):
            return self.getTypedRuleContext(LiturgieParser.GebedContext,0)


        def lezen(self):
            return self.getTypedRuleContext(LiturgieParser.LezenContext,0)


        def preek(self):
            return self.getTypedRuleContext(LiturgieParser.PreekContext,0)


        def belijdenis(self):
            return self.getTypedRuleContext(LiturgieParser.BelijdenisContext,0)


        def collecte(self):
            return self.getTypedRuleContext(LiturgieParser.CollecteContext,0)


        def zegen(self):
            return self.getTypedRuleContext(LiturgieParser.ZegenContext,0)


        def getRuleIndex(self):
            return LiturgieParser.RULE_regel

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterRegel(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitRegel(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitRegel(self)
            else:
                return visitor.visitChildren(self)




    def regel(self):

        localctx = LiturgieParser.RegelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_regel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            token = self._input.LA(1)
            if token in [LiturgieParser.T__2, LiturgieParser.T__3, LiturgieParser.T__4, LiturgieParser.T__5, LiturgieParser.T__6, LiturgieParser.T__7, LiturgieParser.T__8, LiturgieParser.T__9, LiturgieParser.T__10, LiturgieParser.T__11]:
                self.state = 45
                self.lied()

            elif token in [LiturgieParser.T__12]:
                self.state = 46
                self.votum()

            elif token in [LiturgieParser.T__13]:
                self.state = 47
                self.groet()

            elif token in [LiturgieParser.T__14]:
                self.state = 48
                self.gebed()

            elif token in [LiturgieParser.T__15, LiturgieParser.T__16]:
                self.state = 49
                self.lezen()

            elif token in [LiturgieParser.T__17]:
                self.state = 50
                self.preek()

            elif token in [LiturgieParser.T__18]:
                self.state = 51
                self.belijdenis()

            elif token in [LiturgieParser.T__19]:
                self.state = 52
                self.collecte()

            elif token in [LiturgieParser.T__20]:
                self.state = 53
                self.zegen()

            else:
                raise NoViableAltException(self)

            self.state = 56
            self.match(LiturgieParser.EOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiedContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.LiedContext, self).__init__(parent, invokingState)
            self.parser = parser

        def bundel(self):
            return self.getTypedRuleContext(LiturgieParser.BundelContext,0)


        def nummer(self):
            return self.getTypedRuleContext(LiturgieParser.NummerContext,0)


        def coupletten(self):
            return self.getTypedRuleContext(LiturgieParser.CouplettenContext,0)


        def getRuleIndex(self):
            return LiturgieParser.RULE_lied

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterLied(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitLied(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitLied(self)
            else:
                return visitor.visitChildren(self)




    def lied(self):

        localctx = LiturgieParser.LiedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_lied)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.bundel()
            self.state = 59
            self.nummer()
            self.state = 61
            _la = self._input.LA(1)
            if _la==LiturgieParser.T__0:
                self.state = 60
                self.coupletten()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BundelContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.BundelContext, self).__init__(parent, invokingState)
            self.parser = parser

        def psalm(self):
            return self.getTypedRuleContext(LiturgieParser.PsalmContext,0)


        def gezang(self):
            return self.getTypedRuleContext(LiturgieParser.GezangContext,0)


        def liedboek(self):
            return self.getTypedRuleContext(LiturgieParser.LiedboekContext,0)


        def opwekking(self):
            return self.getTypedRuleContext(LiturgieParser.OpwekkingContext,0)


        def nlb(self):
            return self.getTypedRuleContext(LiturgieParser.NlbContext,0)


        def getRuleIndex(self):
            return LiturgieParser.RULE_bundel

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterBundel(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitBundel(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitBundel(self)
            else:
                return visitor.visitChildren(self)




    def bundel(self):

        localctx = LiturgieParser.BundelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bundel)
        try:
            self.state = 68
            token = self._input.LA(1)
            if token in [LiturgieParser.T__2, LiturgieParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.psalm()

            elif token in [LiturgieParser.T__4, LiturgieParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.gezang()

            elif token in [LiturgieParser.T__6, LiturgieParser.T__7, LiturgieParser.T__8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.liedboek()

            elif token in [LiturgieParser.T__9, LiturgieParser.T__10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.opwekking()

            elif token in [LiturgieParser.T__11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 67
                self.nlb()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CouplettenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.CouplettenContext, self).__init__(parent, invokingState)
            self.parser = parser

        def couplet(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LiturgieParser.CoupletContext)
            else:
                return self.getTypedRuleContext(LiturgieParser.CoupletContext,i)


        def getRuleIndex(self):
            return LiturgieParser.RULE_coupletten

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterCoupletten(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitCoupletten(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitCoupletten(self)
            else:
                return visitor.visitChildren(self)




    def coupletten(self):

        localctx = LiturgieParser.CouplettenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_coupletten)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(LiturgieParser.T__0)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.couplet()
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==LiturgieParser.Digit):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CoupletContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.CoupletContext, self).__init__(parent, invokingState)
            self.parser = parser

        def nummer(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LiturgieParser.NummerContext)
            else:
                return self.getTypedRuleContext(LiturgieParser.NummerContext,i)


        def getRuleIndex(self):
            return LiturgieParser.RULE_couplet

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterCouplet(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitCouplet(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitCouplet(self)
            else:
                return visitor.visitChildren(self)




    def couplet(self):

        localctx = LiturgieParser.CoupletContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_couplet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 76
                    self.nummer()
                    self.state = 77
                    self.match(LiturgieParser.T__1) 
                self.state = 83
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 84
            self.nummer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PsalmContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.PsalmContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Dot(self):
            return self.getToken(LiturgieParser.Dot, 0)

        def getRuleIndex(self):
            return LiturgieParser.RULE_psalm

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterPsalm(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitPsalm(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitPsalm(self)
            else:
                return visitor.visitChildren(self)




    def psalm(self):

        localctx = LiturgieParser.PsalmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_psalm)
        self._la = 0 # Token type
        try:
            self.state = 91
            token = self._input.LA(1)
            if token in [LiturgieParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(LiturgieParser.T__2)
                self.state = 88
                _la = self._input.LA(1)
                if _la==LiturgieParser.Dot:
                    self.state = 87
                    self.match(LiturgieParser.Dot)



            elif token in [LiturgieParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(LiturgieParser.T__3)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GezangContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.GezangContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Dot(self):
            return self.getToken(LiturgieParser.Dot, 0)

        def getRuleIndex(self):
            return LiturgieParser.RULE_gezang

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterGezang(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitGezang(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitGezang(self)
            else:
                return visitor.visitChildren(self)




    def gezang(self):

        localctx = LiturgieParser.GezangContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_gezang)
        self._la = 0 # Token type
        try:
            self.state = 98
            token = self._input.LA(1)
            if token in [LiturgieParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(LiturgieParser.T__4)
                self.state = 95
                _la = self._input.LA(1)
                if _la==LiturgieParser.Dot:
                    self.state = 94
                    self.match(LiturgieParser.Dot)



            elif token in [LiturgieParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.match(LiturgieParser.T__5)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiedboekContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.LiedboekContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Dot(self):
            return self.getToken(LiturgieParser.Dot, 0)

        def getRuleIndex(self):
            return LiturgieParser.RULE_liedboek

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterLiedboek(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitLiedboek(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitLiedboek(self)
            else:
                return visitor.visitChildren(self)




    def liedboek(self):

        localctx = LiturgieParser.LiedboekContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_liedboek)
        self._la = 0 # Token type
        try:
            self.state = 109
            token = self._input.LA(1)
            if token in [LiturgieParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(LiturgieParser.T__6)
                self.state = 102
                _la = self._input.LA(1)
                if _la==LiturgieParser.Dot:
                    self.state = 101
                    self.match(LiturgieParser.Dot)



            elif token in [LiturgieParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(LiturgieParser.T__7)
                self.state = 106
                _la = self._input.LA(1)
                if _la==LiturgieParser.Dot:
                    self.state = 105
                    self.match(LiturgieParser.Dot)



            elif token in [LiturgieParser.T__8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 108
                self.match(LiturgieParser.T__8)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpwekkingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.OpwekkingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Dot(self):
            return self.getToken(LiturgieParser.Dot, 0)

        def getRuleIndex(self):
            return LiturgieParser.RULE_opwekking

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterOpwekking(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitOpwekking(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitOpwekking(self)
            else:
                return visitor.visitChildren(self)




    def opwekking(self):

        localctx = LiturgieParser.OpwekkingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_opwekking)
        self._la = 0 # Token type
        try:
            self.state = 116
            token = self._input.LA(1)
            if token in [LiturgieParser.T__9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(LiturgieParser.T__9)
                self.state = 113
                _la = self._input.LA(1)
                if _la==LiturgieParser.Dot:
                    self.state = 112
                    self.match(LiturgieParser.Dot)



            elif token in [LiturgieParser.T__10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(LiturgieParser.T__10)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NlbContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.NlbContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Dot(self):
            return self.getToken(LiturgieParser.Dot, 0)

        def getRuleIndex(self):
            return LiturgieParser.RULE_nlb

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterNlb(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitNlb(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitNlb(self)
            else:
                return visitor.visitChildren(self)




    def nlb(self):

        localctx = LiturgieParser.NlbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_nlb)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(LiturgieParser.T__11)
            self.state = 120
            _la = self._input.LA(1)
            if _la==LiturgieParser.Dot:
                self.state = 119
                self.match(LiturgieParser.Dot)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VotumContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.VotumContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LiturgieParser.RULE_votum

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterVotum(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitVotum(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitVotum(self)
            else:
                return visitor.visitChildren(self)




    def votum(self):

        localctx = LiturgieParser.VotumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_votum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(LiturgieParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroetContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.GroetContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LiturgieParser.RULE_groet

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterGroet(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitGroet(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitGroet(self)
            else:
                return visitor.visitChildren(self)




    def groet(self):

        localctx = LiturgieParser.GroetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_groet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(LiturgieParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GebedContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.GebedContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOL(self, i=None):
            if i is None:
                return self.getTokens(LiturgieParser.EOL)
            else:
                return self.getToken(LiturgieParser.EOL, i)

        def getRuleIndex(self):
            return LiturgieParser.RULE_gebed

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterGebed(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitGebed(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitGebed(self)
            else:
                return visitor.visitChildren(self)




    def gebed(self):

        localctx = LiturgieParser.GebedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_gebed)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(LiturgieParser.T__14)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LiturgieParser.T__0) | (1 << LiturgieParser.T__1) | (1 << LiturgieParser.T__2) | (1 << LiturgieParser.T__3) | (1 << LiturgieParser.T__4) | (1 << LiturgieParser.T__5) | (1 << LiturgieParser.T__6) | (1 << LiturgieParser.T__7) | (1 << LiturgieParser.T__8) | (1 << LiturgieParser.T__9) | (1 << LiturgieParser.T__10) | (1 << LiturgieParser.T__11) | (1 << LiturgieParser.T__12) | (1 << LiturgieParser.T__13) | (1 << LiturgieParser.T__14) | (1 << LiturgieParser.T__15) | (1 << LiturgieParser.T__16) | (1 << LiturgieParser.T__17) | (1 << LiturgieParser.T__18) | (1 << LiturgieParser.T__19) | (1 << LiturgieParser.T__20) | (1 << LiturgieParser.Digit) | (1 << LiturgieParser.Character) | (1 << LiturgieParser.Dot) | (1 << LiturgieParser.WS))) != 0):
                self.state = 127
                _la = self._input.LA(1)
                if _la <= 0 or _la==LiturgieParser.EOL:
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LezenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.LezenContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOL(self, i=None):
            if i is None:
                return self.getTokens(LiturgieParser.EOL)
            else:
                return self.getToken(LiturgieParser.EOL, i)

        def getRuleIndex(self):
            return LiturgieParser.RULE_lezen

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterLezen(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitLezen(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitLezen(self)
            else:
                return visitor.visitChildren(self)




    def lezen(self):

        localctx = LiturgieParser.LezenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_lezen)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if not(_la==LiturgieParser.T__15 or _la==LiturgieParser.T__16):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LiturgieParser.T__0) | (1 << LiturgieParser.T__1) | (1 << LiturgieParser.T__2) | (1 << LiturgieParser.T__3) | (1 << LiturgieParser.T__4) | (1 << LiturgieParser.T__5) | (1 << LiturgieParser.T__6) | (1 << LiturgieParser.T__7) | (1 << LiturgieParser.T__8) | (1 << LiturgieParser.T__9) | (1 << LiturgieParser.T__10) | (1 << LiturgieParser.T__11) | (1 << LiturgieParser.T__12) | (1 << LiturgieParser.T__13) | (1 << LiturgieParser.T__14) | (1 << LiturgieParser.T__15) | (1 << LiturgieParser.T__16) | (1 << LiturgieParser.T__17) | (1 << LiturgieParser.T__18) | (1 << LiturgieParser.T__19) | (1 << LiturgieParser.T__20) | (1 << LiturgieParser.Digit) | (1 << LiturgieParser.Character) | (1 << LiturgieParser.Dot) | (1 << LiturgieParser.WS))) != 0):
                self.state = 134
                _la = self._input.LA(1)
                if _la <= 0 or _la==LiturgieParser.EOL:
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PreekContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.PreekContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LiturgieParser.RULE_preek

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterPreek(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitPreek(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitPreek(self)
            else:
                return visitor.visitChildren(self)




    def preek(self):

        localctx = LiturgieParser.PreekContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_preek)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(LiturgieParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BelijdenisContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.BelijdenisContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOL(self, i=None):
            if i is None:
                return self.getTokens(LiturgieParser.EOL)
            else:
                return self.getToken(LiturgieParser.EOL, i)

        def getRuleIndex(self):
            return LiturgieParser.RULE_belijdenis

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterBelijdenis(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitBelijdenis(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitBelijdenis(self)
            else:
                return visitor.visitChildren(self)




    def belijdenis(self):

        localctx = LiturgieParser.BelijdenisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_belijdenis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(LiturgieParser.T__18)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LiturgieParser.T__0) | (1 << LiturgieParser.T__1) | (1 << LiturgieParser.T__2) | (1 << LiturgieParser.T__3) | (1 << LiturgieParser.T__4) | (1 << LiturgieParser.T__5) | (1 << LiturgieParser.T__6) | (1 << LiturgieParser.T__7) | (1 << LiturgieParser.T__8) | (1 << LiturgieParser.T__9) | (1 << LiturgieParser.T__10) | (1 << LiturgieParser.T__11) | (1 << LiturgieParser.T__12) | (1 << LiturgieParser.T__13) | (1 << LiturgieParser.T__14) | (1 << LiturgieParser.T__15) | (1 << LiturgieParser.T__16) | (1 << LiturgieParser.T__17) | (1 << LiturgieParser.T__18) | (1 << LiturgieParser.T__19) | (1 << LiturgieParser.T__20) | (1 << LiturgieParser.Digit) | (1 << LiturgieParser.Character) | (1 << LiturgieParser.Dot) | (1 << LiturgieParser.WS))) != 0):
                self.state = 143
                _la = self._input.LA(1)
                if _la <= 0 or _la==LiturgieParser.EOL:
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CollecteContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.CollecteContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LiturgieParser.RULE_collecte

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterCollecte(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitCollecte(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitCollecte(self)
            else:
                return visitor.visitChildren(self)




    def collecte(self):

        localctx = LiturgieParser.CollecteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_collecte)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(LiturgieParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ZegenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.ZegenContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LiturgieParser.RULE_zegen

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterZegen(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitZegen(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitZegen(self)
            else:
                return visitor.visitChildren(self)




    def zegen(self):

        localctx = LiturgieParser.ZegenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_zegen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(LiturgieParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NummerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.NummerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Digit(self, i=None):
            if i is None:
                return self.getTokens(LiturgieParser.Digit)
            else:
                return self.getToken(LiturgieParser.Digit, i)

        def getRuleIndex(self):
            return LiturgieParser.RULE_nummer

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterNummer(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitNummer(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitNummer(self)
            else:
                return visitor.visitChildren(self)




    def nummer(self):

        localctx = LiturgieParser.NummerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_nummer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 153
                    self.match(LiturgieParser.Digit)

                else:
                    raise NoViableAltException(self)
                self.state = 156 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




