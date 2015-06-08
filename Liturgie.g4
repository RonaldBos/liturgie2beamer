/**
 * Liturgie parser
 */
grammar Liturgie;

liturgie: regel+;

regel : (lied |
		 welkom |
		 stilte |
		 votum |
		 groet |
		 amen |
		 gebed |
		 lezen |
		 preek |
		 belijdenis |
		 collecte |
		 zegen
		 )? Separator;

lied : bundel liednummer coupletten?;

bundel : psalm | gezang | liedboek | opwekking | nlb | pvn;

coupletten : ':' couplet+;

couplet : (nummer_of_nummers ',')* 'en'? nummer_of_nummers;

nummer_of_nummers: nummer | nummers;

nummers : nummer '-' nummer;

psalm : Psalm;

gezang : Gezang | GereformeerdKerkboek | GereformeerdKerkboek Gezang;

liedboek : Liedboek;

opwekking : Opwekking;

nlb : NieuweLiedboek;

pvn : PsalmenVoorNu;

welkom : 'Welkom';

stilte : 'Stilte';

votum : 'Votum';

groet : 'Groet' | 'Zegengroet';

amen : 'Amen';

gebed : 'Gebed' de_rest;

lezen : (('Lezen' | 'Schriftlezing') ':'?)? de_rest;

de_rest : (Character | Digit | Punctuation)+ ~Separator;

preek : 'Preek' de_rest?;

belijdenis : 'Geloofsbelijdenis' de_rest;

collecte : 'Collecte';

zegen : 'Zegen';

liednummer : Digit+ Character?;

nummer : Digit+;

Digit : [0-9]+;
Character : [A-Za-z];
Punctuation : [-()];
Dot : '.';
WS : [ \t]+ -> skip;
fragment EOL : '\r'? '\n';
Separator : (EOL | ':' | '+' | ';' | '=');

Psalm : 'ps' '.'? | 'psalm';
Gezang : 'g' 'e'? 'z' '.'? | 'gezang';
GereformeerdKerkboek : 'gk' '.'?;
Liedboek : 'o'? 'lb' '.'? | 'liedboek' | 'lied';
Opwekking : 'opw' '.'? | 'opwekking';
NieuweLiedboek : 'nlb' '.'?;
PsalmenVoorNu : 'pvn' '.'?;
