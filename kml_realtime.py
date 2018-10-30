import time
import os

path = os.path.realpath('./kml/')

#path = r'D:\Bibliotecas\Descargas'
xy=['-75.59176655058938,2.703800409020358,0', '-75.59169521975352,2.703776063649411,0', '-75.59166500477164,2.703777223065771,0',
'-75.59160684628473,2.703765955903321,0', '-75.59157143717012,2.703753846931174,0', '-75.59153096796345,2.703728566361539,0', 
'-75.59149069788215,2.703703409633991,0', '-75.59145062453779,2.703678376257565,0', '-75.59141539583568,2.703665916215658,0',
'-75.59137487090698,2.703639601345602,0', '-75.59133948413586,2.703626507654711,0', '-75.59130147194769,2.703626536520836,0',
'-75.59126564015453,2.703612347732574,0', '-75.59122654556229,2.703610165385743,0', '-75.59118747551408,2.703607984677606,0',
'-75.59116125615095,2.703619965231084,0', '-75.59114781617753,2.703646210565597,0', '-75.59111858900614,2.703671708805524,0', 
'-75.59109708910881,2.703697782253817,0', '-75.5910705278377,2.703709976599547,0', '-75.59104390433176,2.703722199300316,0',
'-75.59101721731037,2.703734450197799,0', '-75.5909825617284,2.703746279706009,0', '-75.59096054909367,2.70377273845488,0', 
'-75.59093842066093,2.703799337232745,0', '-75.59091617534007,2.703826074236527,0', '-75.59088906431791,2.703838574687219,0', 
'-75.5908698679679,2.70385156718685,0', '-75.59083464717685,2.703863665236833,0', '-75.59081198828658,2.703890740471775,0', 
'-75.59078920950446,2.70391795941243,0', '-75.59076170332307,2.703930681468866,0', '-75.59073354298791,2.703942048740339,0', 
'-75.59070055041332,2.703964687051626,0', '-75.59067596557101,2.703989031972783,0', '-75.59065127088331,2.704013486182498,0', 
'-75.59062176299344,2.7040224974855,0', '-75.59058830641985,2.704045462091204,0', '-75.59058045916662,2.704073457494021,0', 
'-75.59054676056684,2.704096634081269,0', '-75.59052153374945,2.70412156974535,0', '-75.5904875694993,2.70414494443406,0', 
'-75.59046661274233,2.704186092829393,0', '-75.59043651349397,2.704195364773922,0', '-75.59041081037501,2.704220746806011,0',
'-75.59038058299876,2.704230070391625,0', '-75.59035467588601,2.70425560789441,0', '-75.5903243185407,2.704264984101895,0',
'-75.59029804944035,2.704290231142436,0', '-75.59027191874876,2.704284819106115,0', '-75.59023713495415,2.704277614726534,0',
'-75.59018563494831,2.704236498314722,0', '-75.59014779406948,2.704183394512593,0', '-75.59013204168825,2.704120403743158,0',
'-75.59012489079443,2.704059706313283,0', '-75.59011769490847,2.703999344021466,0', '-75.59011869335495,2.703940595407032,0',
'-75.59010942936472,2.703875258996467,0', '-75.59007464991122,2.703803365105151,0', '-75.5900447437178,2.703809755587347,0',
'-75.59003191621409,2.703852030270628,0', '-75.59000601076367,2.703874955137024,0', '-75.58998426693289,2.703915024374453,0',
'-75.5899587861371,2.703940351974857,0', '-75.58994226994001,2.703969838700623,0', '-75.58992565545736,2.703999499502243,0',
'-75.5898910381986,2.704022225800297,0', '-75.58986422525409,2.704045285851056,0', '-75.58983383948014,2.704052885665871,0',
'-75.58980684112157,2.704076067330719,0', '-75.58977973164581,2.70409934356598,0', '-75.58974916467815,2.704107005537809,0',
'-75.58971009293991,2.704112668137952,0', '-75.58966778837367,2.704102647103053,0', '-75.58963824749,2.704036446160779,0', 
'-75.58964075620918,2.703972837058779,0', '-75.58965021306614,2.703907289028936,0', '-75.58967182772327,2.703862661118175,0',
'-75.58967267593529,2.703796360230511,0', '-75.58969394329586,2.703752740446001,0', '-75.58966184857511,2.703679300202321,0',
'-75.58962098629631,2.703668511545082,0', '-75.58958024845425,2.703657756809207,0', '-75.58955871488836,2.703700467088067,0',
'-75.58953334495534,2.703726239422886,0', '-75.58950425198103,2.703734795848432,0', '-75.58947512080017,2.703743364748757,0',
'-75.5894506304884,2.703736793842574,0', '-75.58941332085418,2.703743171429661,0', '-75.589384125671,2.703751746190487,0',
'-75.58935971623927,2.703745167892743,0', '-75.589314251945,2.703749356460283,0', '-75.58928817509457,2.703775335029801,0',
'-75.58925382580046,2.703799229208299,0', '-75.5892243884193,2.703807882260322,0', '-75.58918378843906,2.703796788925374,0',
'-75.58914622836035,2.703803214126186,0', '-75.58911673398913,2.703811866240858,0', '-75.58909001730926,2.70383813538747,0',
'-75.58906038877107,2.703846838116081,0', '-75.5890307209702,2.703855553469224,0', '-75.58900367644273,2.70388203943148,0',
'-75.5889712645741,2.703873017569137,0', '-75.58894402955471,2.70389958464695,0', '-75.5889166532662,2.703926290440015,0',
'-75.58888667309988,2.703935121868952,0', '-75.58885665246265,2.703943965911857,0', '-75.58882659091027,2.703952820838857,0',
'-75.58880459355817,2.703963987253841,0', '-75.58877669820929,2.703991012223529,0', '-75.58874845082413,2.704016838869706,0', 
'-75.58871152011,2.704037698514143,0', '-75.58868254058356,2.704060581401452,0', '-75.58865664052252,2.70411432081186,0',
'-75.58865336791246,2.70415918700912,0', '-75.5886516977011,2.704220335115922,0', '-75.58865000725592,2.704282219595173,0',
'-75.58866338935263,2.704575942359672,0', '-75.58866171272292,2.704642208585445,0', '-75.58866893245082,2.704714018426931,0', 
'-75.58867465670475,2.704770403015485,0', '-75.58866697598916,2.704861817921105,0', '-75.5886766689965,2.704958822793724,0', 
'-75.58866691211908,2.705033643054896,0', '-75.58864814773693,2.705107436209061,0', '-75.58862913025936,2.705182223517317,0',
'-75.58860797408728,2.705237387755861,0', '-75.58857760905862,2.705290948477489,0', '-75.58854518325443,2.705324054060204,0',
'-75.5885306496623,2.705361695851769,0', '-75.5884909552077,2.705418637327269,0', '-75.58845838496613,2.705457305184495,0', 
'-75.58843288007212,2.705474195028757,0', '-75.58839258081359,2.705535429535212,0', '-75.58835934256987,2.705574891408654,0',
'-75.58831666395477,2.705612009172228,0',   '-75.58864829644429,2.704344853242219,0', '-75.58865660398222,2.70442701175031,0',
'-75.5886549095905,2.704491422959089,0', '-75.5882814027932,2.705626725443198,0', '-75.58823829682849,2.705664165545747,0',
'-75.58823050092387,2.705686947897727,0', '-75.58818834973337,2.705750476790936,0', '-75.58814448700034,2.705788710331719,0',
'-75.58810849783524,2.705803850878471,0', '-75.58807350748971,2.705845151878834,0', '-75.58801863985468,2.705854950114976,0',
'-75.58797301167883,2.70586750228421,0', '-75.58793584093553,2.705856544623849,0', '-75.58789943551774,2.705871837797584,0',
'-75.58785366692609,2.705884414838642,0', '-75.58780735534917,2.70587068454752,0', '-75.58775197196225,2.705854903345068,0',
'-75.58771517957985,2.705846703378747,0', '-75.58768762790784,2.705840563736118,0', '-75.58764178963187,2.705830347555135,0',
'-75.5876143354198,2.705824228971164,0', '-75.58756865891434,2.705814049493597,0', '-75.58752308217501,2.705803892860874,0',
'-75.58747760673978,2.705793757250833,0', '-75.58745072054136,2.705762753877606,0', '-75.58739647365698,2.705750696563784,0', '-75.58736038820969,2.705742676125162,0', '-75.58731601703188,2.705707994781229,0', '-75.58728015181134,2.705700045090525,0', '-75.58724434938492,2.705692110484364,0', '-75.58719968367417,2.705682210488285,0', '-75.58715511532472,2.705672332365692,0', '-75.58712842071081,2.705666415607564,0', '-75.58708169635798,2.705705524159672,0', '-75.58703982329425,2.705821676876919,0', '-75.58700751445331,2.705916739555971,0', '-75.58698379622888,2.706015504354215,0', '-75.58696902010117,2.70611600531943,0', '-75.58696211018385,2.706242564947497,0', '-75.58693781737736,2.706339713511192,0', '-75.58692252141196,2.706441541877607,0', '-75.58689749588449,2.706541955202631,0', '-75.58687205533533,2.706644033948169,0', '-75.58685580005039,2.706751094798319,0', '-75.58684274041465,2.706803674534855,0', '-75.58681265724917,2.706967498148555,0', '-75.58678749572751,2.707047575698481,0', '-75.58673242889631,2.707118168779794,0', '-75.58669868475522,2.707166823160593,0', '-75.58665256209919,2.707242257800302,0', '-75.58661038333823,2.707260456635584,0', '-75.58655500145676,2.707312681243207,0', '-75.58650167047867,2.707336005960031,0', '-75.58646783654899,2.707368608147237,0', '-75.58642355810453,2.707400546851944,0', '-75.58636876768537,2.70743181143858,0', '-75.58630912857504,2.707506911146626,0', '-75.5862762131916,2.707424307517929,0', '-75.5862207470679,2.707457438159349,0', '-75.58615433180583,2.70749246825803,0', '-75.58611854515819,2.707530594069164,0', '-75.58607218084337,2.707567978373846,0', '-75.58600477361881,2.707603621067693,0', '-75.58593699653638,2.707639437035317,0', '-75.5859060160909,2.707635001188291,0', '-75.5858486574041,2.707669263378401,0', '-75.58580731132811,2.707663323108223,0', '-75.58577027983267,2.707700719376998,0', '-75.58571853479903,2.707693254843608,0', '-75.58567682805447,2.707689367354979,0', '-75.58561809681399,2.707726938471608,0', '-75.58555902326812,2.707764727623254,0', '-75.58551029354616,2.70780271737644,0', '-75.5854568465749,2.707802825634417,0', '-75.58538673340178,2.707838545684485,0', '-75.58532881055731,2.707865429362263,0', '-75.58527824060924,2.707850442010045,0', '-75.58521773411981,2.707832507265038,0', '-75.58515954690712,2.707859354285318,0', '-75.5851092532385,2.707844388263967,0', '-75.58505258556777,2.707916377627337,0', '-75.58500222832151,2.707901276108883,0', '-75.58497356351805,2.70793747610605,0', '-75.58489553964279,2.708004331182684,0', '-75.58486524452471,2.707995137673656,0', '-75.5847964816043,2.70806565362633,0', '-75.58472636826208,2.70809029510927,0', '-75.58467627143521,2.708121266503795,0', '-75.5846170338212,2.708192434443983,0', '-75.5845653319228,2.70822763735141,0', '-75.58452453944464,2.708262510285904,0', '-75.58443301603184,2.708233820260146,0', '-75.5843716039406,2.708262237107766,0', '-75.58431081923573,2.708243105536638,0', '-75.5842502335253,2.708224035710401,0', '-75.58419989641037,2.708208193905912,0', '-75.58415831580736,2.708242844047397,0', '-75.58410804707972,2.708226956641733,0', '-75.58406965993396,2.708167203511828,0', '-75.58403973597719,2.708157784517936,0', '-75.5839899703836,2.708142121759186,0', '-75.58392820844341,2.70817012182316,0', '-75.58385568525881,2.708196860135521,0', '-75.58373903102805,2.708262126220383,0', '-75.58362819166499,2.708378606595994,0', '-75.5835731365471,2.708415306072325,0', '-75.58350716175559,2.708450647542011,0', '-75.58344344831521,2.70844134533392,0', '-75.58341162934451,2.70843669965793,0', '-75.58334806538687,2.708427420204293,0', '-75.58329209250728,2.708464364900145,0', '-75.58323909512953,2.708456599086798,0', '-75.58318590280051,2.708449551893271,0', '-75.58314123145991,2.708449660516232,0', '-75.58308539112652,2.708449796240512,0', '-75.58302955018684,2.708449931538504,0', '-75.58298487582874,2.708450040051869,0', '-75.582917863231,2.708450203918619,0', '-75.58287318724035,2.708450312847308,0', '-75.58280750212074,2.708447190487378,0', '-75.58274689627034,2.70849189905645,0', '-75.58268588907144,2.708536905668924,0', '-75.58264188861871,2.708534702312936,0', '-75.58258034146441,2.708579991327472,0', '-75.58251152442382,2.708674289942262,0', '-75.58244322216822,2.708707153426373,0', '-75.58238667377046,2.708738612478302,0', '-75.58233126588314,2.708767017889914,0', '-75.58227565123697,2.708795528096985,0', '-75.58220394472636,2.70886594887992,0', '-75.58214375020161,2.708846343221322,0', '-75.58208749802233,2.708875149420644,0', '-75.58203103377251,2.708904064067069,0', '-75.58195763380674,2.708975508457216,0', '-75.58185628548723,2.709087366201994,0', '-75.58179968842872,2.709114680873921,0', '-75.58171191098018,2.709220157026643,0', '-75.58165692981844,2.709242918195988,0', '-75.58161133020786,2.70927052584807,0', '-75.58152919567829,2.709330848876677,0', '-75.58145597606499,2.709396507778794,0', '-75.58139170203171,2.709467644543696,0', '-75.58128783953529,2.709576237037077,0', '-75.58118183386921,2.709687736130802,0', '-75.58110776480264,2.709751692461323,0', '-75.58104093190045,2.709800418588808,0', '-75.58094845202741,2.709881563990273,0', '-75.58086254218215,2.709973129429679,0', '-75.58081867771924,2.709992901974445,0', '-75.58073726253804,2.710098713191227,0', '-75.58067391197923,2.710162217454471,0', '-75.58056700179263,2.710267536665107,0', '-75.58049554794771,2.710345495237269,0', '-75.58039485862203,2.710461083050188,0', '-75.5802966562743,2.710570829360866,0', '-75.58022115520915,2.710629989709438,0', '-75.58015210068224,2.71070072914993,0', '-75.58005090290328,2.710813612354413,0', '-75.57994901540205,2.71092676667283,0', '-75.57985360558368,2.71105130077491,0', '-75.57974981417662,2.711166068831073,0', '-75.57965853738776,2.71130591550997,0', '-75.57955189732611,2.711424091697964,0', '-75.57942351201976,2.71161268509295,0', '-75.57935483213942,2.711702329829548,0', '-75.57921644536957,2.711882403961336,0', '-75.57911102587124,2.712019467334846,0', '-75.57900920868909,2.712123950618125,0', '-75.57891272613335,2.712217993550719,0', '-75.57882052897588,2.712328838588901,0', '-75.5787228915344,2.712448771044634,0', '-75.5786133109594,2.712589266352523,0', '-75.57850207326378,2.712731888033487,0', '-75.57842697535594,2.712828172777743,0']



	# Wait for 5 seconds
for p in xy:
	lon = p.split(',')[0]
	lat = p.split(',')[1]
	print(p.split(',')[0],p.split(',')[1])
	time.sleep(2)
	with open(path + '\\' +'location.kml','w',encoding='utf-8') as f:
		f.write("""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" 
xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Placemark>
	<name>location</name>
	<description>Location real time.</description>
	<Point>
		<coordinates>{},{},0</coordinates>
	</Point>
</Placemark>
</kml>""".format(lon,lat))
	print('ok')
print('final')