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
        buf.write(u"%\u00c6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\3\2\6\28\n\2\r\2")
        buf.write(u"\16\29\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\5\3H\n\3\3\3\3\3\3\4\3\4\3\4\5\4O\n\4\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\5\5V\n\5\3\6\3\6\6\6Z\n\6\r\6\16\6[\3\7\3\7")
        buf.write(u"\3\7\7\7a\n\7\f\7\16\7d\13\7\3\7\3\7\3\b\3\b\5\bj\n\b")
        buf.write(u"\3\t\3\t\3\t\3\t\3\n\3\n\5\nr\n\n\3\n\5\nu\n\n\3\13\3")
        buf.write(u"\13\5\13y\n\13\3\13\3\13\5\13}\n\13\3\13\3\13\5\13\u0081")
        buf.write(u"\n\13\3\f\3\f\5\f\u0085\n\f\3\f\3\f\5\f\u0089\n\f\3\f")
        buf.write(u"\3\f\5\f\u008d\n\f\3\r\3\r\5\r\u0091\n\r\3\r\5\r\u0094")
        buf.write(u"\n\r\3\16\3\16\5\16\u0098\n\16\3\17\3\17\3\20\3\20\3")
        buf.write(u"\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25\3\25")
        buf.write(u"\5\25\u00a9\n\25\5\25\u00ab\n\25\3\25\3\25\3\26\6\26")
        buf.write(u"\u00b0\n\26\r\26\16\26\u00b1\3\26\3\26\3\27\3\27\5\27")
        buf.write(u"\u00b8\n\27\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\6")
        buf.write(u"\33\u00c2\n\33\r\33\16\33\u00c3\3\33\2\2\34\2\4\6\b\n")
        buf.write(u"\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\2\6\3")
        buf.write(u"\2\26\27\3\2\32\33\3\2 \"\3\2%%\u00d4\2\67\3\2\2\2\4")
        buf.write(u"G\3\2\2\2\6K\3\2\2\2\bU\3\2\2\2\nW\3\2\2\2\fb\3\2\2\2")
        buf.write(u"\16i\3\2\2\2\20k\3\2\2\2\22t\3\2\2\2\24\u0080\3\2\2\2")
        buf.write(u"\26\u008c\3\2\2\2\30\u0093\3\2\2\2\32\u0095\3\2\2\2\34")
        buf.write(u"\u0099\3\2\2\2\36\u009b\3\2\2\2 \u009d\3\2\2\2\"\u009f")
        buf.write(u"\3\2\2\2$\u00a1\3\2\2\2&\u00a3\3\2\2\2(\u00aa\3\2\2\2")
        buf.write(u"*\u00af\3\2\2\2,\u00b5\3\2\2\2.\u00b9\3\2\2\2\60\u00bc")
        buf.write(u"\3\2\2\2\62\u00be\3\2\2\2\64\u00c1\3\2\2\2\668\5\4\3")
        buf.write(u"\2\67\66\3\2\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:\3\3")
        buf.write(u"\2\2\2;H\5\6\4\2<H\5\34\17\2=H\5\36\20\2>H\5 \21\2?H")
        buf.write(u"\5\"\22\2@H\5$\23\2AH\5&\24\2BH\5(\25\2CH\5,\27\2DH\5")
        buf.write(u".\30\2EH\5\60\31\2FH\5\62\32\2G;\3\2\2\2G<\3\2\2\2G=")
        buf.write(u"\3\2\2\2G>\3\2\2\2G?\3\2\2\2G@\3\2\2\2GA\3\2\2\2GB\3")
        buf.write(u"\2\2\2GC\3\2\2\2GD\3\2\2\2GE\3\2\2\2GF\3\2\2\2GH\3\2")
        buf.write(u"\2\2HI\3\2\2\2IJ\7%\2\2J\5\3\2\2\2KL\5\b\5\2LN\5\64\33")
        buf.write(u"\2MO\5\n\6\2NM\3\2\2\2NO\3\2\2\2O\7\3\2\2\2PV\5\22\n")
        buf.write(u"\2QV\5\24\13\2RV\5\26\f\2SV\5\30\r\2TV\5\32\16\2UP\3")
        buf.write(u"\2\2\2UQ\3\2\2\2UR\3\2\2\2US\3\2\2\2UT\3\2\2\2V\t\3\2")
        buf.write(u"\2\2WY\7\3\2\2XZ\5\f\7\2YX\3\2\2\2Z[\3\2\2\2[Y\3\2\2")
        buf.write(u"\2[\\\3\2\2\2\\\13\3\2\2\2]^\5\16\b\2^_\7\4\2\2_a\3\2")
        buf.write(u"\2\2`]\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2ce\3\2\2")
        buf.write(u"\2db\3\2\2\2ef\5\16\b\2f\r\3\2\2\2gj\5\64\33\2hj\5\20")
        buf.write(u"\t\2ig\3\2\2\2ih\3\2\2\2j\17\3\2\2\2kl\5\64\33\2lm\7")
        buf.write(u"\5\2\2mn\5\64\33\2n\21\3\2\2\2oq\7\6\2\2pr\7#\2\2qp\3")
        buf.write(u"\2\2\2qr\3\2\2\2ru\3\2\2\2su\7\7\2\2to\3\2\2\2ts\3\2")
        buf.write(u"\2\2u\23\3\2\2\2vx\7\b\2\2wy\7#\2\2xw\3\2\2\2xy\3\2\2")
        buf.write(u"\2y\u0081\3\2\2\2z|\7\t\2\2{}\7#\2\2|{\3\2\2\2|}\3\2")
        buf.write(u"\2\2}\u0081\3\2\2\2~\u0081\7\n\2\2\177\u0081\7\13\2\2")
        buf.write(u"\u0080v\3\2\2\2\u0080z\3\2\2\2\u0080~\3\2\2\2\u0080\177")
        buf.write(u"\3\2\2\2\u0081\25\3\2\2\2\u0082\u0084\7\f\2\2\u0083\u0085")
        buf.write(u"\7#\2\2\u0084\u0083\3\2\2\2\u0084\u0085\3\2\2\2\u0085")
        buf.write(u"\u008d\3\2\2\2\u0086\u0088\7\r\2\2\u0087\u0089\7#\2\2")
        buf.write(u"\u0088\u0087\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008d")
        buf.write(u"\3\2\2\2\u008a\u008d\7\16\2\2\u008b\u008d\7\17\2\2\u008c")
        buf.write(u"\u0082\3\2\2\2\u008c\u0086\3\2\2\2\u008c\u008a\3\2\2")
        buf.write(u"\2\u008c\u008b\3\2\2\2\u008d\27\3\2\2\2\u008e\u0090\7")
        buf.write(u"\20\2\2\u008f\u0091\7#\2\2\u0090\u008f\3\2\2\2\u0090")
        buf.write(u"\u0091\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0094\7\21\2")
        buf.write(u"\2\u0093\u008e\3\2\2\2\u0093\u0092\3\2\2\2\u0094\31\3")
        buf.write(u"\2\2\2\u0095\u0097\7\22\2\2\u0096\u0098\7#\2\2\u0097")
        buf.write(u"\u0096\3\2\2\2\u0097\u0098\3\2\2\2\u0098\33\3\2\2\2\u0099")
        buf.write(u"\u009a\7\23\2\2\u009a\35\3\2\2\2\u009b\u009c\7\24\2\2")
        buf.write(u"\u009c\37\3\2\2\2\u009d\u009e\7\25\2\2\u009e!\3\2\2\2")
        buf.write(u"\u009f\u00a0\t\2\2\2\u00a0#\3\2\2\2\u00a1\u00a2\7\30")
        buf.write(u"\2\2\u00a2%\3\2\2\2\u00a3\u00a4\7\31\2\2\u00a4\u00a5")
        buf.write(u"\5*\26\2\u00a5\'\3\2\2\2\u00a6\u00a8\t\3\2\2\u00a7\u00a9")
        buf.write(u"\7\3\2\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9")
        buf.write(u"\u00ab\3\2\2\2\u00aa\u00a6\3\2\2\2\u00aa\u00ab\3\2\2")
        buf.write(u"\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\5*\26\2\u00ad)\3\2")
        buf.write(u"\2\2\u00ae\u00b0\t\4\2\2\u00af\u00ae\3\2\2\2\u00b0\u00b1")
        buf.write(u"\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write(u"\u00b3\3\2\2\2\u00b3\u00b4\n\5\2\2\u00b4+\3\2\2\2\u00b5")
        buf.write(u"\u00b7\7\34\2\2\u00b6\u00b8\5*\26\2\u00b7\u00b6\3\2\2")
        buf.write(u"\2\u00b7\u00b8\3\2\2\2\u00b8-\3\2\2\2\u00b9\u00ba\7\35")
        buf.write(u"\2\2\u00ba\u00bb\5*\26\2\u00bb/\3\2\2\2\u00bc\u00bd\7")
        buf.write(u"\36\2\2\u00bd\61\3\2\2\2\u00be\u00bf\7\37\2\2\u00bf\63")
        buf.write(u"\3\2\2\2\u00c0\u00c2\7 \2\2\u00c1\u00c0\3\2\2\2\u00c2")
        buf.write(u"\u00c3\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2")
        buf.write(u"\2\u00c4\65\3\2\2\2\319GNU[biqtx|\u0080\u0084\u0088\u008c")
        buf.write(u"\u0090\u0093\u0097\u00a8\u00aa\u00b1\u00b7\u00c3")
        return buf.getvalue()


class LiturgieParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"':'", u"','", u"'-'", u"'Ps'", u"'Psalm'", 
                     u"'Gz'", u"'Gez'", u"'Gezang'", u"'GK'", u"'LB'", u"'OLB'", 
                     u"'Lied'", u"'Liedboek'", u"'Opw'", u"'Opwekking'", 
                     u"'NLB'", u"'Welkom'", u"'Stilte'", u"'Votum'", u"'Groet'", 
                     u"'Zegengroet'", u"'Amen'", u"'Gebed'", u"'Lezen'", 
                     u"'Schriftlezing'", u"'Preek'", u"'Geloofsbelijdenis'", 
                     u"'Collecte'", u"'Zegen'", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'.'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"Digit", u"Character", 
                      u"Punctuation", u"Dot", u"WS", u"Separator" ]

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
    RULE_welkom = 13
    RULE_stilte = 14
    RULE_votum = 15
    RULE_groet = 16
    RULE_amen = 17
    RULE_gebed = 18
    RULE_lezen = 19
    RULE_de_rest = 20
    RULE_preek = 21
    RULE_belijdenis = 22
    RULE_collecte = 23
    RULE_zegen = 24
    RULE_nummer = 25

    ruleNames =  [ u"liturgie", u"regel", u"lied", u"bundel", u"coupletten", 
                   u"couplet", u"nummer_of_nummers", u"nummers", u"psalm", 
                   u"gezang", u"liedboek", u"opwekking", u"nlb", u"welkom", 
                   u"stilte", u"votum", u"groet", u"amen", u"gebed", u"lezen", 
                   u"de_rest", u"preek", u"belijdenis", u"collecte", u"zegen", 
                   u"nummer" ]

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
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    Digit=30
    Character=31
    Punctuation=32
    Dot=33
    WS=34
    Separator=35

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
            self.state = 53 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 52
                self.regel()
                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LiturgieParser.T__3) | (1 << LiturgieParser.T__4) | (1 << LiturgieParser.T__5) | (1 << LiturgieParser.T__6) | (1 << LiturgieParser.T__7) | (1 << LiturgieParser.T__8) | (1 << LiturgieParser.T__9) | (1 << LiturgieParser.T__10) | (1 << LiturgieParser.T__11) | (1 << LiturgieParser.T__12) | (1 << LiturgieParser.T__13) | (1 << LiturgieParser.T__14) | (1 << LiturgieParser.T__15) | (1 << LiturgieParser.T__16) | (1 << LiturgieParser.T__17) | (1 << LiturgieParser.T__18) | (1 << LiturgieParser.T__19) | (1 << LiturgieParser.T__20) | (1 << LiturgieParser.T__21) | (1 << LiturgieParser.T__22) | (1 << LiturgieParser.T__23) | (1 << LiturgieParser.T__24) | (1 << LiturgieParser.T__25) | (1 << LiturgieParser.T__26) | (1 << LiturgieParser.T__27) | (1 << LiturgieParser.T__28) | (1 << LiturgieParser.Digit) | (1 << LiturgieParser.Character) | (1 << LiturgieParser.Punctuation) | (1 << LiturgieParser.Separator))) != 0)):
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
            self.state = 69
            token = self._input.LA(1)
            if token in [LiturgieParser.T__3, LiturgieParser.T__4, LiturgieParser.T__5, LiturgieParser.T__6, LiturgieParser.T__7, LiturgieParser.T__8, LiturgieParser.T__9, LiturgieParser.T__10, LiturgieParser.T__11, LiturgieParser.T__12, LiturgieParser.T__13, LiturgieParser.T__14, LiturgieParser.T__15]:
                self.state = 57
                self.lied()
                pass
            elif token in [LiturgieParser.T__16]:
                self.state = 58
                self.welkom()
                pass
            elif token in [LiturgieParser.T__17]:
                self.state = 59
                self.stilte()
                pass
            elif token in [LiturgieParser.T__18]:
                self.state = 60
                self.votum()
                pass
            elif token in [LiturgieParser.T__19, LiturgieParser.T__20]:
                self.state = 61
                self.groet()
                pass
            elif token in [LiturgieParser.T__21]:
                self.state = 62
                self.amen()
                pass
            elif token in [LiturgieParser.T__22]:
                self.state = 63
                self.gebed()
                pass
            elif token in [LiturgieParser.T__23, LiturgieParser.T__24, LiturgieParser.Digit, LiturgieParser.Character, LiturgieParser.Punctuation]:
                self.state = 64
                self.lezen()
                pass
            elif token in [LiturgieParser.T__25]:
                self.state = 65
                self.preek()
                pass
            elif token in [LiturgieParser.T__26]:
                self.state = 66
                self.belijdenis()
                pass
            elif token in [LiturgieParser.T__27]:
                self.state = 67
                self.collecte()
                pass
            elif token in [LiturgieParser.T__28]:
                self.state = 68
                self.zegen()
                pass
            elif token in [LiturgieParser.Separator]:
                pass
            else:
                raise NoViableAltException(self)
            self.state = 71
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
            self.state = 73
            self.bundel()
            self.state = 74
            self.nummer()
            self.state = 76
            _la = self._input.LA(1)
            if _la==LiturgieParser.T__0:
                self.state = 75
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
            self.state = 83
            token = self._input.LA(1)
            if token in [LiturgieParser.T__3, LiturgieParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.psalm()

            elif token in [LiturgieParser.T__5, LiturgieParser.T__6, LiturgieParser.T__7, LiturgieParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.gezang()

            elif token in [LiturgieParser.T__9, LiturgieParser.T__10, LiturgieParser.T__11, LiturgieParser.T__12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.liedboek()

            elif token in [LiturgieParser.T__13, LiturgieParser.T__14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self.opwekking()

            elif token in [LiturgieParser.T__15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 82
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
            self.state = 85
            self.match(LiturgieParser.T__0)
            self.state = 87 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 86
                self.couplet()
                self.state = 89 
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 91
                    self.nummer_of_nummers()
                    self.state = 92
                    self.match(LiturgieParser.T__1) 
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 99
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
            self.state = 103
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.nummer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
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
            self.state = 105
            self.nummer()
            self.state = 106
            self.match(LiturgieParser.T__2)
            self.state = 107
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
        self.enterRule(localctx, 16, self.RULE_psalm)
        self._la = 0 # Token type
        try:
            self.state = 114
            token = self._input.LA(1)
            if token in [LiturgieParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(LiturgieParser.T__3)
                self.state = 111
                _la = self._input.LA(1)
                if _la==LiturgieParser.Dot:
                    self.state = 110
                    self.match(LiturgieParser.Dot)



            elif token in [LiturgieParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(LiturgieParser.T__4)

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
        self.enterRule(localctx, 18, self.RULE_gezang)
        self._la = 0 # Token type
        try:
            self.state = 126
            token = self._input.LA(1)
            if token in [LiturgieParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(LiturgieParser.T__5)
                self.state = 118
                _la = self._input.LA(1)
                if _la==LiturgieParser.Dot:
                    self.state = 117
                    self.match(LiturgieParser.Dot)



            elif token in [LiturgieParser.T__6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.match(LiturgieParser.T__6)
                self.state = 122
                _la = self._input.LA(1)
                if _la==LiturgieParser.Dot:
                    self.state = 121
                    self.match(LiturgieParser.Dot)



            elif token in [LiturgieParser.T__7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.match(LiturgieParser.T__7)

            elif token in [LiturgieParser.T__8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
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
        self.enterRule(localctx, 20, self.RULE_liedboek)
        self._la = 0 # Token type
        try:
            self.state = 138
            token = self._input.LA(1)
            if token in [LiturgieParser.T__9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(LiturgieParser.T__9)
                self.state = 130
                _la = self._input.LA(1)
                if _la==LiturgieParser.Dot:
                    self.state = 129
                    self.match(LiturgieParser.Dot)



            elif token in [LiturgieParser.T__10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(LiturgieParser.T__10)
                self.state = 134
                _la = self._input.LA(1)
                if _la==LiturgieParser.Dot:
                    self.state = 133
                    self.match(LiturgieParser.Dot)



            elif token in [LiturgieParser.T__11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.match(LiturgieParser.T__11)

            elif token in [LiturgieParser.T__12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 137
                self.match(LiturgieParser.T__12)

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
        self.enterRule(localctx, 22, self.RULE_opwekking)
        self._la = 0 # Token type
        try:
            self.state = 145
            token = self._input.LA(1)
            if token in [LiturgieParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(LiturgieParser.T__13)
                self.state = 142
                _la = self._input.LA(1)
                if _la==LiturgieParser.Dot:
                    self.state = 141
                    self.match(LiturgieParser.Dot)



            elif token in [LiturgieParser.T__14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(LiturgieParser.T__14)

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
        self.enterRule(localctx, 24, self.RULE_nlb)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(LiturgieParser.T__15)
            self.state = 149
            _la = self._input.LA(1)
            if _la==LiturgieParser.Dot:
                self.state = 148
                self.match(LiturgieParser.Dot)


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
        self.enterRule(localctx, 26, self.RULE_welkom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(LiturgieParser.T__16)
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
        self.enterRule(localctx, 28, self.RULE_stilte)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(LiturgieParser.T__17)
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
        self.enterRule(localctx, 30, self.RULE_votum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(LiturgieParser.T__18)
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
        self.enterRule(localctx, 32, self.RULE_groet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            _la = self._input.LA(1)
            if not(_la==LiturgieParser.T__19 or _la==LiturgieParser.T__20):
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
        self.enterRule(localctx, 34, self.RULE_amen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(LiturgieParser.T__21)
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
        self.enterRule(localctx, 36, self.RULE_gebed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(LiturgieParser.T__22)
            self.state = 162
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
        self.enterRule(localctx, 38, self.RULE_lezen)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            _la = self._input.LA(1)
            if _la==LiturgieParser.T__23 or _la==LiturgieParser.T__24:
                self.state = 164
                _la = self._input.LA(1)
                if not(_la==LiturgieParser.T__23 or _la==LiturgieParser.T__24):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 166
                _la = self._input.LA(1)
                if _la==LiturgieParser.T__0:
                    self.state = 165
                    self.match(LiturgieParser.T__0)




            self.state = 170
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
        self.enterRule(localctx, 40, self.RULE_de_rest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 172
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LiturgieParser.Digit) | (1 << LiturgieParser.Character) | (1 << LiturgieParser.Punctuation))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 175 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 177
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
        self.enterRule(localctx, 42, self.RULE_preek)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(LiturgieParser.T__25)
            self.state = 181
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LiturgieParser.Digit) | (1 << LiturgieParser.Character) | (1 << LiturgieParser.Punctuation))) != 0):
                self.state = 180
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
        self.enterRule(localctx, 44, self.RULE_belijdenis)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(LiturgieParser.T__26)
            self.state = 184
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
        self.enterRule(localctx, 46, self.RULE_collecte)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(LiturgieParser.T__27)
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
        self.enterRule(localctx, 48, self.RULE_zegen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(LiturgieParser.T__28)
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
        self.enterRule(localctx, 50, self.RULE_nummer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 190
                    self.match(LiturgieParser.Digit)

                else:
                    raise NoViableAltException(self)
                self.state = 193 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




