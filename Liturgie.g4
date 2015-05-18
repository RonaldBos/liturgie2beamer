/**
 * Liturgie parser
 */
grammar Liturgie;

liturgie: regel+;

regel : (lied |
		 votum |
		 groet |
		 gebed |
		 lezen |
		 preek |
		 belijdenis |
		 collecte |
		 zegen
		 ) EOL;

lied : bundel nummer coupletten?;

bundel : psalm | gezang | liedboek | opwekking | nlb;

coupletten : ':' couplet+;

couplet : (nummer ',')* nummer; 

psalm : 'Ps' Dot?  | 'Psalm';

gezang : 'Gz' Dot? | 'Gezang';

liedboek : 'LB' Dot? | 'OLB' Dot? | 'Lied';

opwekking : 'Opw' Dot? | 'Opwekking';

nlb : 'NLB' Dot?;

votum : 'Votum';

groet : 'Groet';

gebed : 'Gebed' ~EOL*;

lezen : ('I' | 'II') ~EOL*;

preek : 'Preek';

belijdenis : 'Geloofsbelijdenis' ~EOL*;

collecte : 'Collecte';

zegen : 'Zegen';

nummer : Digit+;

Digit : [0-9]+;
Character : [A-Za-z];
Dot : '.';
WS : [ \t]+ -> skip;
EOL : '\r'? '\n';
