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
        buf.write(u" \u00bf\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\3\2\6\2<\n\2\r\2\16\2=\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3O\n\3\3\3\3\3\3")
        buf.write(u"\4\3\4\3\4\5\4V\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5^\n\5")
        buf.write(u"\3\6\3\6\6\6b\n\6\r\6\16\6c\3\7\3\7\3\7\7\7i\n\7\f\7")
        buf.write(u"\16\7l\13\7\3\7\5\7o\n\7\3\7\3\7\3\b\3\b\5\bu\n\b\3\t")
        buf.write(u"\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u0081\n")
        buf.write(u"\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write(u"\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3")
        buf.write(u"\26\3\26\5\26\u009a\n\26\5\26\u009c\n\26\3\26\3\26\3")
        buf.write(u"\27\6\27\u00a1\n\27\r\27\16\27\u00a2\3\27\3\27\3\30\3")
        buf.write(u"\30\5\30\u00a9\n\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write(u"\3\34\6\34\u00b3\n\34\r\34\16\34\u00b4\3\34\5\34\u00b8")
        buf.write(u"\n\34\3\35\6\35\u00bb\n\35\r\35\16\35\u00bc\3\35\2\2")
        buf.write(u"\36\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write(u"\62\64\668\2\6\3\2\n\13\3\2\16\17\3\2\24\26\3\2\31\31")
        buf.write(u"\u00c3\2;\3\2\2\2\4N\3\2\2\2\6R\3\2\2\2\b]\3\2\2\2\n")
        buf.write(u"_\3\2\2\2\fj\3\2\2\2\16t\3\2\2\2\20v\3\2\2\2\22z\3\2")
        buf.write(u"\2\2\24\u0080\3\2\2\2\26\u0082\3\2\2\2\30\u0084\3\2\2")
        buf.write(u"\2\32\u0086\3\2\2\2\34\u0088\3\2\2\2\36\u008a\3\2\2\2")
        buf.write(u" \u008c\3\2\2\2\"\u008e\3\2\2\2$\u0090\3\2\2\2&\u0092")
        buf.write(u"\3\2\2\2(\u0094\3\2\2\2*\u009b\3\2\2\2,\u00a0\3\2\2\2")
        buf.write(u".\u00a6\3\2\2\2\60\u00aa\3\2\2\2\62\u00ad\3\2\2\2\64")
        buf.write(u"\u00af\3\2\2\2\66\u00b2\3\2\2\28\u00ba\3\2\2\2:<\5\4")
        buf.write(u"\3\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>?\3\2\2")
        buf.write(u"\2?@\7\2\2\3@\3\3\2\2\2AO\5\6\4\2BO\5\36\20\2CO\5 \21")
        buf.write(u"\2DO\5\"\22\2EO\5$\23\2FO\5&\24\2GO\5(\25\2HO\5*\26\2")
        buf.write(u"IO\5.\30\2JO\5\60\31\2KO\5\62\32\2LO\5\64\33\2MO\13\2")
        buf.write(u"\2\2NA\3\2\2\2NB\3\2\2\2NC\3\2\2\2ND\3\2\2\2NE\3\2\2")
        buf.write(u"\2NF\3\2\2\2NG\3\2\2\2NH\3\2\2\2NI\3\2\2\2NJ\3\2\2\2")
        buf.write(u"NK\3\2\2\2NL\3\2\2\2NM\3\2\2\2NO\3\2\2\2OP\3\2\2\2PQ")
        buf.write(u"\7\31\2\2Q\5\3\2\2\2RS\5\b\5\2SU\5\66\34\2TV\5\n\6\2")
        buf.write(u"UT\3\2\2\2UV\3\2\2\2V\7\3\2\2\2W^\5\22\n\2X^\5\24\13")
        buf.write(u"\2Y^\5\26\f\2Z^\5\30\r\2[^\5\32\16\2\\^\5\34\17\2]W\3")
        buf.write(u"\2\2\2]X\3\2\2\2]Y\3\2\2\2]Z\3\2\2\2][\3\2\2\2]\\\3\2")
        buf.write(u"\2\2^\t\3\2\2\2_a\7\3\2\2`b\5\f\7\2a`\3\2\2\2bc\3\2\2")
        buf.write(u"\2ca\3\2\2\2cd\3\2\2\2d\13\3\2\2\2ef\5\16\b\2fg\7\4\2")
        buf.write(u"\2gi\3\2\2\2he\3\2\2\2il\3\2\2\2jh\3\2\2\2jk\3\2\2\2")
        buf.write(u"kn\3\2\2\2lj\3\2\2\2mo\7\5\2\2nm\3\2\2\2no\3\2\2\2op")
        buf.write(u"\3\2\2\2pq\5\16\b\2q\r\3\2\2\2ru\58\35\2su\5\20\t\2t")
        buf.write(u"r\3\2\2\2ts\3\2\2\2u\17\3\2\2\2vw\58\35\2wx\7\6\2\2x")
        buf.write(u"y\58\35\2y\21\3\2\2\2z{\7\32\2\2{\23\3\2\2\2|\u0081\7")
        buf.write(u"\33\2\2}\u0081\7\34\2\2~\177\7\34\2\2\177\u0081\7\33")
        buf.write(u"\2\2\u0080|\3\2\2\2\u0080}\3\2\2\2\u0080~\3\2\2\2\u0081")
        buf.write(u"\25\3\2\2\2\u0082\u0083\7\35\2\2\u0083\27\3\2\2\2\u0084")
        buf.write(u"\u0085\7\36\2\2\u0085\31\3\2\2\2\u0086\u0087\7\37\2\2")
        buf.write(u"\u0087\33\3\2\2\2\u0088\u0089\7 \2\2\u0089\35\3\2\2\2")
        buf.write(u"\u008a\u008b\7\7\2\2\u008b\37\3\2\2\2\u008c\u008d\7\b")
        buf.write(u"\2\2\u008d!\3\2\2\2\u008e\u008f\7\t\2\2\u008f#\3\2\2")
        buf.write(u"\2\u0090\u0091\t\2\2\2\u0091%\3\2\2\2\u0092\u0093\7\f")
        buf.write(u"\2\2\u0093\'\3\2\2\2\u0094\u0095\7\r\2\2\u0095\u0096")
        buf.write(u"\5,\27\2\u0096)\3\2\2\2\u0097\u0099\t\3\2\2\u0098\u009a")
        buf.write(u"\7\3\2\2\u0099\u0098\3\2\2\2\u0099\u009a\3\2\2\2\u009a")
        buf.write(u"\u009c\3\2\2\2\u009b\u0097\3\2\2\2\u009b\u009c\3\2\2")
        buf.write(u"\2\u009c\u009d\3\2\2\2\u009d\u009e\5,\27\2\u009e+\3\2")
        buf.write(u"\2\2\u009f\u00a1\t\4\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a2")
        buf.write(u"\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write(u"\u00a4\3\2\2\2\u00a4\u00a5\n\5\2\2\u00a5-\3\2\2\2\u00a6")
        buf.write(u"\u00a8\7\20\2\2\u00a7\u00a9\5,\27\2\u00a8\u00a7\3\2\2")
        buf.write(u"\2\u00a8\u00a9\3\2\2\2\u00a9/\3\2\2\2\u00aa\u00ab\7\21")
        buf.write(u"\2\2\u00ab\u00ac\5,\27\2\u00ac\61\3\2\2\2\u00ad\u00ae")
        buf.write(u"\7\22\2\2\u00ae\63\3\2\2\2\u00af\u00b0\7\23\2\2\u00b0")
        buf.write(u"\65\3\2\2\2\u00b1\u00b3\7\24\2\2\u00b2\u00b1\3\2\2\2")
        buf.write(u"\u00b3\u00b4\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5")
        buf.write(u"\3\2\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00b8\7\25\2\2\u00b7")
        buf.write(u"\u00b6\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\67\3\2\2\2\u00b9")
        buf.write(u"\u00bb\7\24\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00bc\3\2\2")
        buf.write(u"\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd9\3\2")
        buf.write(u"\2\2\22=NU]cjnt\u0080\u0099\u009b\u00a2\u00a8\u00b4\u00b7")
        buf.write(u"\u00bc")
        return buf.getvalue()


class LiturgieParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"':'", u"','", u"'en'", u"'-'", u"'Welkom'", 
                     u"'Stilte'", u"'Votum'", u"'Groet'", u"'Zegengroet'", 
                     u"'Amen'", u"'Gebed'", u"'Lezen'", u"'Schriftlezing'", 
                     u"'Preek'", u"'Geloofsbelijdenis'", u"'Collecte'", 
                     u"'Zegen'", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'.'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"Digit", u"Character", 
                      u"Punctuation", u"Dot", u"WS", u"Separator", u"Psalm", 
                      u"Gezang", u"GereformeerdKerkboek", u"Liedboek", u"Opwekking", 
                      u"NieuweLiedboek", u"PsalmenVoorNu" ]

    RULE_liturgie = 0
    RULE_regel = 1
    RULE_lied = 2
    RULE_bundel = 3
    RULE_coupletten = 4
    RULE_couplet = 5
    RULE_nummer_of_nummers = 6
    RULE_nummers = 7
    RULE_psalm = 8
    RULE_gezang = 9
    RULE_liedboek = 10
    RULE_opwekking = 11
    RULE_nlb = 12
    RULE_pvn = 13
    RULE_welkom = 14
    RULE_stilte = 15
    RULE_votum = 16
    RULE_groet = 17
    RULE_amen = 18
    RULE_gebed = 19
    RULE_lezen = 20
    RULE_de_rest = 21
    RULE_preek = 22
    RULE_belijdenis = 23
    RULE_collecte = 24
    RULE_zegen = 25
    RULE_liednummer = 26
    RULE_nummer = 27

    ruleNames =  [ u"liturgie", u"regel", u"lied", u"bundel", u"coupletten", 
                   u"couplet", u"nummer_of_nummers", u"nummers", u"psalm", 
                   u"gezang", u"liedboek", u"opwekking", u"nlb", u"pvn", 
                   u"welkom", u"stilte", u"votum", u"groet", u"amen", u"gebed", 
                   u"lezen", u"de_rest", u"preek", u"belijdenis", u"collecte", 
                   u"zegen", u"liednummer", u"nummer" ]

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
    Digit=18
    Character=19
    Punctuation=20
    Dot=21
    WS=22
    Separator=23
    Psalm=24
    Gezang=25
    GereformeerdKerkboek=26
    Liedboek=27
    Opwekking=28
    NieuweLiedboek=29
    PsalmenVoorNu=30

    def __init__(self, input):
        super(LiturgieParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class LiturgieContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.LiturgieContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LiturgieParser.EOF, 0)

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
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.regel()
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LiturgieParser.T__0) | (1 << LiturgieParser.T__1) | (1 << LiturgieParser.T__2) | (1 << LiturgieParser.T__3) | (1 << LiturgieParser.T__4) | (1 << LiturgieParser.T__5) | (1 << LiturgieParser.T__6) | (1 << LiturgieParser.T__7) | (1 << LiturgieParser.T__8) | (1 << LiturgieParser.T__9) | (1 << LiturgieParser.T__10) | (1 << LiturgieParser.T__11) | (1 << LiturgieParser.T__12) | (1 << LiturgieParser.T__13) | (1 << LiturgieParser.T__14) | (1 << LiturgieParser.T__15) | (1 << LiturgieParser.T__16) | (1 << LiturgieParser.Digit) | (1 << LiturgieParser.Character) | (1 << LiturgieParser.Punctuation) | (1 << LiturgieParser.Dot) | (1 << LiturgieParser.WS) | (1 << LiturgieParser.Separator) | (1 << LiturgieParser.Psalm) | (1 << LiturgieParser.Gezang) | (1 << LiturgieParser.GereformeerdKerkboek) | (1 << LiturgieParser.Liedboek) | (1 << LiturgieParser.Opwekking) | (1 << LiturgieParser.NieuweLiedboek) | (1 << LiturgieParser.PsalmenVoorNu))) != 0)):
                    break

            self.state = 61
            self.match(LiturgieParser.EOF)
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

        def Separator(self):
            return self.getToken(LiturgieParser.Separator, 0)

        def lied(self):
            return self.getTypedRuleContext(LiturgieParser.LiedContext,0)


        def welkom(self):
            return self.getTypedRuleContext(LiturgieParser.WelkomContext,0)


        def stilte(self):
            return self.getTypedRuleContext(LiturgieParser.StilteContext,0)


        def votum(self):
            return self.getTypedRuleContext(LiturgieParser.VotumContext,0)


        def groet(self):
            return self.getTypedRuleContext(LiturgieParser.GroetContext,0)


        def amen(self):
            return self.getTypedRuleContext(LiturgieParser.AmenContext,0)


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
            self.state = 76
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 63
                self.lied()

            elif la_ == 2:
                self.state = 64
                self.welkom()

            elif la_ == 3:
                self.state = 65
                self.stilte()

            elif la_ == 4:
                self.state = 66
                self.votum()

            elif la_ == 5:
                self.state = 67
                self.groet()

            elif la_ == 6:
                self.state = 68
                self.amen()

            elif la_ == 7:
                self.state = 69
                self.gebed()

            elif la_ == 8:
                self.state = 70
                self.lezen()

            elif la_ == 9:
                self.state = 71
                self.preek()

            elif la_ == 10:
                self.state = 72
                self.belijdenis()

            elif la_ == 11:
                self.state = 73
                self.collecte()

            elif la_ == 12:
                self.state = 74
                self.zegen()

            elif la_ == 13:
                self.state = 75
                self.matchWildcard()


            self.state = 78
            self.match(LiturgieParser.Separator)
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


        def liednummer(self):
            return self.getTypedRuleContext(LiturgieParser.LiednummerContext,0)


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
            self.state = 80
            self.bundel()
            self.state = 81
            self.liednummer()
            self.state = 83
            _la = self._input.LA(1)
            if _la==LiturgieParser.T__0:
                self.state = 82
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


        def pvn(self):
            return self.getTypedRuleContext(LiturgieParser.PvnContext,0)


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
            self.state = 91
            token = self._input.LA(1)
            if token in [LiturgieParser.Psalm]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.psalm()

            elif token in [LiturgieParser.Gezang, LiturgieParser.GereformeerdKerkboek]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.gezang()

            elif token in [LiturgieParser.Liedboek]:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.liedboek()

            elif token in [LiturgieParser.Opwekking]:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.opwekking()

            elif token in [LiturgieParser.NieuweLiedboek]:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.nlb()

            elif token in [LiturgieParser.PsalmenVoorNu]:
                self.enterOuterAlt(localctx, 6)
                self.state = 90
                self.pvn()

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
            self.state = 93
            self.match(LiturgieParser.T__0)
            self.state = 95 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 94
                self.couplet()
                self.state = 97 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==LiturgieParser.T__2 or _la==LiturgieParser.Digit):
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

        def nummer_of_nummers(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LiturgieParser.Nummer_of_nummersContext)
            else:
                return self.getTypedRuleContext(LiturgieParser.Nummer_of_nummersContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 99
                    self.nummer_of_nummers()
                    self.state = 100
                    self.match(LiturgieParser.T__1) 
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 108
            _la = self._input.LA(1)
            if _la==LiturgieParser.T__2:
                self.state = 107
                self.match(LiturgieParser.T__2)


            self.state = 110
            self.nummer_of_nummers()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Nummer_of_nummersContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.Nummer_of_nummersContext, self).__init__(parent, invokingState)
            self.parser = parser

        def nummer(self):
            return self.getTypedRuleContext(LiturgieParser.NummerContext,0)


        def nummers(self):
            return self.getTypedRuleContext(LiturgieParser.NummersContext,0)


        def getRuleIndex(self):
            return LiturgieParser.RULE_nummer_of_nummers

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterNummer_of_nummers(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitNummer_of_nummers(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitNummer_of_nummers(self)
            else:
                return visitor.visitChildren(self)




    def nummer_of_nummers(self):

        localctx = LiturgieParser.Nummer_of_nummersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_nummer_of_nummers)
        try:
            self.state = 114
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.nummer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.nummers()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NummersContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.NummersContext, self).__init__(parent, invokingState)
            self.parser = parser

        def nummer(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LiturgieParser.NummerContext)
            else:
                return self.getTypedRuleContext(LiturgieParser.NummerContext,i)


        def getRuleIndex(self):
            return LiturgieParser.RULE_nummers

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterNummers(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitNummers(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitNummers(self)
            else:
                return visitor.visitChildren(self)




    def nummers(self):

        localctx = LiturgieParser.NummersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_nummers)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.nummer()
            self.state = 117
            self.match(LiturgieParser.T__3)
            self.state = 118
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

        def Psalm(self):
            return self.getToken(LiturgieParser.Psalm, 0)

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
        self.enterRule(localctx, 16, self.RULE_psalm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(LiturgieParser.Psalm)
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

        def Gezang(self):
            return self.getToken(LiturgieParser.Gezang, 0)

        def GereformeerdKerkboek(self):
            return self.getToken(LiturgieParser.GereformeerdKerkboek, 0)

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
        self.enterRule(localctx, 18, self.RULE_gezang)
        try:
            self.state = 126
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.match(LiturgieParser.Gezang)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(LiturgieParser.GereformeerdKerkboek)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.match(LiturgieParser.GereformeerdKerkboek)
                self.state = 125
                self.match(LiturgieParser.Gezang)
                pass


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

        def Liedboek(self):
            return self.getToken(LiturgieParser.Liedboek, 0)

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
        self.enterRule(localctx, 20, self.RULE_liedboek)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(LiturgieParser.Liedboek)
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

        def Opwekking(self):
            return self.getToken(LiturgieParser.Opwekking, 0)

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
        self.enterRule(localctx, 22, self.RULE_opwekking)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(LiturgieParser.Opwekking)
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

        def NieuweLiedboek(self):
            return self.getToken(LiturgieParser.NieuweLiedboek, 0)

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
        self.enterRule(localctx, 24, self.RULE_nlb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(LiturgieParser.NieuweLiedboek)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PvnContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.PvnContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PsalmenVoorNu(self):
            return self.getToken(LiturgieParser.PsalmenVoorNu, 0)

        def getRuleIndex(self):
            return LiturgieParser.RULE_pvn

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterPvn(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitPvn(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitPvn(self)
            else:
                return visitor.visitChildren(self)




    def pvn(self):

        localctx = LiturgieParser.PvnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_pvn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(LiturgieParser.PsalmenVoorNu)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WelkomContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.WelkomContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LiturgieParser.RULE_welkom

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterWelkom(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitWelkom(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitWelkom(self)
            else:
                return visitor.visitChildren(self)




    def welkom(self):

        localctx = LiturgieParser.WelkomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_welkom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(LiturgieParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StilteContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.StilteContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LiturgieParser.RULE_stilte

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterStilte(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitStilte(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitStilte(self)
            else:
                return visitor.visitChildren(self)




    def stilte(self):

        localctx = LiturgieParser.StilteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stilte)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(LiturgieParser.T__5)
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
        self.enterRule(localctx, 32, self.RULE_votum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(LiturgieParser.T__6)
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
        self.enterRule(localctx, 34, self.RULE_groet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not(_la==LiturgieParser.T__7 or _la==LiturgieParser.T__8):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AmenContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.AmenContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LiturgieParser.RULE_amen

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterAmen(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitAmen(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitAmen(self)
            else:
                return visitor.visitChildren(self)




    def amen(self):

        localctx = LiturgieParser.AmenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_amen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(LiturgieParser.T__9)
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

        def de_rest(self):
            return self.getTypedRuleContext(LiturgieParser.De_restContext,0)


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
        self.enterRule(localctx, 38, self.RULE_gebed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(LiturgieParser.T__10)
            self.state = 147
            self.de_rest()
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

        def de_rest(self):
            return self.getTypedRuleContext(LiturgieParser.De_restContext,0)


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
        self.enterRule(localctx, 40, self.RULE_lezen)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if _la==LiturgieParser.T__11 or _la==LiturgieParser.T__12:
                self.state = 149
                _la = self._input.LA(1)
                if not(_la==LiturgieParser.T__11 or _la==LiturgieParser.T__12):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 151
                _la = self._input.LA(1)
                if _la==LiturgieParser.T__0:
                    self.state = 150
                    self.match(LiturgieParser.T__0)




            self.state = 155
            self.de_rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class De_restContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.De_restContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Separator(self):
            return self.getToken(LiturgieParser.Separator, 0)

        def Character(self, i=None):
            if i is None:
                return self.getTokens(LiturgieParser.Character)
            else:
                return self.getToken(LiturgieParser.Character, i)

        def Digit(self, i=None):
            if i is None:
                return self.getTokens(LiturgieParser.Digit)
            else:
                return self.getToken(LiturgieParser.Digit, i)

        def Punctuation(self, i=None):
            if i is None:
                return self.getTokens(LiturgieParser.Punctuation)
            else:
                return self.getToken(LiturgieParser.Punctuation, i)

        def getRuleIndex(self):
            return LiturgieParser.RULE_de_rest

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterDe_rest(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitDe_rest(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitDe_rest(self)
            else:
                return visitor.visitChildren(self)




    def de_rest(self):

        localctx = LiturgieParser.De_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_de_rest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 157
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LiturgieParser.Digit) | (1 << LiturgieParser.Character) | (1 << LiturgieParser.Punctuation))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 160 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 162
            _la = self._input.LA(1)
            if _la <= 0 or _la==LiturgieParser.Separator:
                self._errHandler.recoverInline(self)
            else:
                self.consume()
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

        def de_rest(self):
            return self.getTypedRuleContext(LiturgieParser.De_restContext,0)


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
        self.enterRule(localctx, 44, self.RULE_preek)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(LiturgieParser.T__13)
            self.state = 166
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LiturgieParser.Digit) | (1 << LiturgieParser.Character) | (1 << LiturgieParser.Punctuation))) != 0):
                self.state = 165
                self.de_rest()


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

        def de_rest(self):
            return self.getTypedRuleContext(LiturgieParser.De_restContext,0)


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
        self.enterRule(localctx, 46, self.RULE_belijdenis)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(LiturgieParser.T__14)
            self.state = 169
            self.de_rest()
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
        self.enterRule(localctx, 48, self.RULE_collecte)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(LiturgieParser.T__15)
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
        self.enterRule(localctx, 50, self.RULE_zegen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(LiturgieParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiednummerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LiturgieParser.LiednummerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Digit(self, i=None):
            if i is None:
                return self.getTokens(LiturgieParser.Digit)
            else:
                return self.getToken(LiturgieParser.Digit, i)

        def Character(self):
            return self.getToken(LiturgieParser.Character, 0)

        def getRuleIndex(self):
            return LiturgieParser.RULE_liednummer

        def enterRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.enterLiednummer(self)

        def exitRule(self, listener):
            if isinstance( listener, LiturgieListener ):
                listener.exitLiednummer(self)

        def accept(self, visitor):
            if isinstance( visitor, LiturgieVisitor ):
                return visitor.visitLiednummer(self)
            else:
                return visitor.visitChildren(self)




    def liednummer(self):

        localctx = LiturgieParser.LiednummerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_liednummer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 175
                self.match(LiturgieParser.Digit)
                self.state = 178 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==LiturgieParser.Digit):
                    break

            self.state = 181
            _la = self._input.LA(1)
            if _la==LiturgieParser.Character:
                self.state = 180
                self.match(LiturgieParser.Character)


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
        self.enterRule(localctx, 54, self.RULE_nummer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 183
                    self.match(LiturgieParser.Digit)

                else:
                    raise NoViableAltException(self)
                self.state = 186 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




