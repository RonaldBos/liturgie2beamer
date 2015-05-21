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

lied : bundel nummer coupletten?;

bundel : psalm | gezang | liedboek | opwekking | nlb;

coupletten : ':' couplet+;

couplet : (nummer_of_nummers ',')* nummer_of_nummers;

nummer_of_nummers: nummer | nummers;

nummers : nummer '-' nummer;

psalm : 'Ps' Dot?  | 'Psalm';

gezang : 'Gz' Dot? | 'Gez' Dot? | 'Gezang' | 'GK';

liedboek : 'LB' Dot? | 'OLB' Dot? | 'Lied' | 'Liedboek';

opwekking : 'Opw' Dot? | 'Opwekking';

nlb : 'NLB' Dot?;

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

nummer : Digit+;

Digit : [0-9]+;
Character : [A-Za-z];
Punctuation : [-()];
Dot : '.';
WS : [ \t]+ -> skip;
fragment EOL : '\r'? '\n';
Separator : (EOL | ':' | '+' | ';');
