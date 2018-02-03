# XPaths of various elements with which Autoplayer interacts
# TODO: Modularize organization of XPaths

xpath = {
	'fishing'		: "/html/body/div[3]/div[3]/table/tbody/tr/td[2]/div[2]/center/form/input[2]",
	'login'			: ".//*[@id='header']/table/tbody/tr[1]/td[3]/a[1]",
	'logout'		: "html/body/div[3]/div[2]/table/tbody/tr[1]/td[3]/a[3]/b",
	'button'		: ".//*[@id='templateLoginPopup']/div/form/table/tbody/tr[3]/td/input",
	'username'		: ".//*[@id='templateLoginPopupUsername']",
	'password'		: "html/body/div[3]/div[2]/div/form/table/tbody/tr[2]/td[2]/input",
	'loggedin'		: "html/body/div[3]/div[2]/table/tbody/tr[1]/td[3]/a[1]",
	'loggedin2'		: ".//*[@id='header']/table/tbody/tr[1]/td[3]/a[1]",
	'dosh_s'		: "html/body/div[3]/div[2]/table/tbody/tr[1]/td[3]/a[2]",
	'dosh'			: ".//*[@id='npanchor']",
	'interest'		: ".//*[@id='content']/table/tbody/tr/td[2]/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td/div/form/input[2]",
	'withdraw'		: "html/body/div[3]/div[3]/table/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/input[1]",
	'deposit'		: "html/body/div[3]/div[3]/table/tbody/tr/td[2]/table[1]/tbody/tr/td[1]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/form/input[2]",
	'noitems'		: ".//*[@id='noItems']",
	'quickstock'	: ".//*[@id='invNav']/a[11]",
	'depositall'	: ".//*[@id='content']/table/tbody/tr/td[2]/form/table/tbody/tr[13]/td/input[1]",
	'gamble'		: "html/body/form/div[3]/div/input[1]",
	'winnings'		: "html/body/div[3]/div[3]/table/tbody/tr/td[2]/center[3]/center[2]/form/p/input[2]",
	'betamount'		: "html/body/div[3]/div[3]/table/tbody/tr/td[2]/p[4]/b",
	'mediocrity'	: "html/body/div[3]/div[3]/table/tbody/tr/td[2]/div[1]/embed",
	'excitement'	: "html/body/div[3]/div[3]/table/tbody/tr/td[2]/div[1]/embed",
	'scratchcard'	: ".//*[@id='content']/table/tbody/tr/td[2]/div[2]/center[2]/form/input",
	'anchor'		: ".//*[@id='btn-fire']/a/div",
	'altador'		: "html/body/div[3]/div[3]/table/tbody/tr/td[2]/div[2]/form/input[3]",
	'altador1'		: "html/body/div[3]/div[3]/table/tbody/tr/td[2]/p/map/area",
	'tombola'		: ".//*[@id='content']/table/tbody/tr/td[2]/div[2]/center[2]/form/input",
	'coltzan'		: "html/body/div[3]/div[3]/table/tbody/tr/td[2]/div[2]/div/form[1]/input[2]",
	'fruits'		: ".//*[@id='content']/table/tbody/tr/td[2]/div[2]/form/input[3]",
	'springs'		: ".//*[@id='content']/table/tbody/tr/td[2]/center[2]/form/input[2]",
	'store'			: ".//*[@id='content']/table/tbody/tr/td[2]/center[3]/form/input[2]",
	'jelly'			: "html/body/div[3]/div[3]/table/tbody/tr/td[2]/div[2]/center[2]/form/input[2]",
	'omelette'		: "html/body/div[3]/div[3]/table/tbody/tr/td[2]/center[2]/form/input[2]",
	'apple'			: ".//*[@id='bob_button']",
	'plushie'		: "html/body/div[3]/div[3]/table/tbody/tr/td[2]/div[2]/form/input[2]",
	'chest'			: "html/body/div[3]/div[3]/table/tbody/tr/td/div/div/div[2]/div/form/a/img",
	'shore'			: "html/body/div[3]/div[3]/table/tbody/tr/td[2]/center/div/a/div",
	'offers'		: "html/body/div[3]/div[3]/table/tbody/tr/td[2]",

	'buy'			: ".//*[@id='content']/table/tbody/tr/td[2]/center/table/tbody/tr[8]/td[1]/a/img",
	'sale'			: "html/body/div[3]/div[3]/table/tbody/tr/td[2]/center[3]/form/input[2]",
}

xpath_d = {
	'fishing'		: ".//*[@id='content']/table/tbody/tr/td[2]/div[2]/center[1]/form/input[2]",
	'dosh'			: ".//*[@id='npanchor']",
	'withdraw'		: ".//*[@id='content']/table/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/input[1]",
	'deposit'		: ".//*[@id='content']/table/tbody/tr/td[2]/table[1]/tbody/tr/td[1]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/form/input[2]",
	'altador'		: ".//*[@id='content']/table/tbody/tr/td[2]/div[2]/form/input[3]",
	'altador1'		: ".//*[@id='content']/table/tbody/tr/td[2]/p/map/area",
	'jelly'			: ".//*[@id='content']/table/tbody/tr/td[2]/div[2]/center[2]/form/input[2]",
	'chest'			: ".//*[@id='content']/table/tbody/tr/td/div/div/div[2]/div/form/a/img",
	'plushie'		: ".//*[@id='content']/table/tbody/tr/td[2]/div[2]/form/input[2]",
	'shore'			: ".//*[@id='shore_np']",
}


battledome = {
	'battle1' : ".//*[@id='bdHomeUpperBattle']",
	'continue1' : ".//*[@id='bdFightStep1']/div[3]",
	'continue2' : ".//*[@id='bdFightStep2']/div[4]",
	'chiaclown' : ".//*[@id='npcTable']/tbody/tr[23]/td[4]/div[1]",
	'battle2' : ".//*[@id='bdFightStep3FightButton']",
	'fight1' : ".//*[@id='start']",
	'slot1' : ".//*[@id='p1e1m']/div",
	'item1' : "html/body/div[3]/div[3]/table/tbody/tr/td/div[4]/div[2]/div[3]/ul/li[1]/img",
	'slot2' : ".//*[@id='p1e2m']/div",
	'item2' : "html/body/div[3]/div[3]/table/tbody/tr/td/div[4]/div[2]/div[3]/ul/li[2]/img",
	'ability' : ".//*[@id='p1am']/div",
	'flare' : ".//*[@id='p1ability']/div[3]/table/tbody/tr/td[4]/div/div",
	'fight2' : ".//*[@id='fight']",
	'skip' : ".//*[@id='skipreplay']",
	'collect' : ".//*[@id='playground']/div[2]/button[1]",
	'again' : ".//*[@id='bdplayagain']",
	'exit' : ".//*[@id='bdexit']",
}

battledome_s = {
	'battle'		: "html/body/div[3]/div[3]/table/tbody/tr/td/div[4]/div[1]/div[1]/a/div",
	'continue1'		: "html/body/div[3]/div[3]/table/tbody/tr/td/div[7]/div[5]/div[2]/div[3]",
	'continue2'		: "html/body/div[3]/div[3]/table/tbody/tr/td/div[7]/div[5]/div[3]/div[4]",
	'select'		: "html/body/div[3]/div[3]/table/tbody/tr/td/div[7]/div[5]/div[4]/div[1]/div[3]/div[2]/table/tbody/tr[22]/td[4]/div[1]",
	'fight'			: "html/body/div[3]/div[3]/table/tbody/tr/td/div[7]/div[5]/div[4]/div[1]/div[3]/div[4]",
	'start'			: "html/body/div[3]/div[3]/table/tbody/tr/td/div[4]/div[1]/div[1]/button",
	'item1'			: "html/body/div[3]/div[3]/table/tbody/tr/td/div[4]/a[1]/div",	
	'item2'			: "html/body/div[3]/div[3]/table/tbody/tr/td/div[4]/a[2]/div",
	'ability'		: "html/body/div[3]/div[3]/table/tbody/tr/td/div[4]/a[3]/div",
	'slot1'			: "html/body/div[3]/div[3]/table/tbody/tr/td/div[4]/div[2]/div[3]/ul[3]/li/img",
	'slot2'			: "html/body/div[3]/div[3]/table/tbody/tr/td/div[4]/div[2]/div[3]/ul[2]/li[1]/img",
	'flare'			: "html/body/div[3]/div[3]/table/tbody/tr/td/div[4]/div[6]/div[3]/table/tbody/tr/td[4]/div/div",
	'attack'		: "html/body/div[3]/div[3]/table/tbody/tr/td/div[4]/form/button[3]",
	'collect'		: "html/body/div[3]/div[3]/table/tbody/tr/td/div[4]/div[1]/div[2]/button[1]",
	'again'			: "html/body/div[3]/div[3]/table/tbody/tr/td/div[4]/div[8]/div[3]/div[2]/div/table[2]/tbody/tr/td[1]/a",
}

battledome_stats = {
	'pet_name'		: ".//*[@id='bdStatusFrame']/div[6]/div[3]/div[6]/div[1]",
	'hitpoints'		: ".//*[@id='bdStatusFrame']/div[6]/div[3]/div[2]/div[2]",
	'attack'		: ".//*[@id='bdStatusFrame']/div[6]/div[3]/div[2]/div[4]",
	'defense'		: ".//*[@id='bdStatusFrame']/div[6]/div[3]/div[2]/div[7]",
	'agility'		: ".//*[@id='bdStatusFrame']/div[6]/div[3]/div[2]/div[10]",
	'intelligence'	: ".//*[@id='bdStatusFrame']/div[6]/div[3]/div[2]/div[13]",
	'level'			: ".//*[@id='bdStatusFrame']/div[6]/div[3]/div[5]",
}


foodclub = {
	'maxed'			: "html/body/div[1]/div/div[1]",
	'tenth'			: "html/body/div[3]/div[3]/table/tbody/tr/td[2]/center[3]/center[1]/table/tbody/tr[12]/td[1]/b",
	'round'			: "html/body/center[2]/table/tbody/tr[3]/td[1]/b",
	'error'			: "html/body/form/div[3]/div/input",
}

foodclub_d = {
	'maxed'			: ".//*[@id='content']/table/tbody/tr/td[2]/div[2]/center[1]/form/input[2]",
	'tenth'			: ".//*[@id='content']/table/tbody/tr/td[2]/center[3]/center[1]/table/tbody/tr[12]/td[1]/b",
}


pirates = {
	'lvl'			: ".//*[@id='content']/table/tbody/tr/td[2]/table/tbody/tr[4]/td[1]/font/b",
	'str'			: ".//*[@id='content']/table/tbody/tr/td[2]/table/tbody/tr[4]/td[1]/b[1]",
	'def'			: ".//*[@id='content']/table/tbody/tr/td[2]/table/tbody/tr[4]/td[1]/b[2]",
	'mov'			: ".//*[@id='content']/table/tbody/tr/td[2]/table/tbody/tr[4]/td[1]/b[3]",
	'hps'			: ".//*[@id='content']/table/tbody/tr/td[2]/table/tbody/tr[4]/td[1]/b[4]",

	'complete'		: ".//*[@id='content']/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/form/input[3]",
	'return'		: "html/body/center/form/input",
}



# html/body/div[4]/div[3]/table/tbody/tr/td[2]/div[1]/div						# event
# .//*[@id='content']/table/tbody/tr/td[2]/div[1]/div							# event_d

# html/body/div[4]/div[3]/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td		# bdome challenger
# .//*[@id='content']/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td			# bdome challenger d
# html/body/div[4]/div[3]/table/tbody/tr/td[2]/div[2]/table[2]					# accompanied event
# .//*[@id='content']/table/tbody/tr/td[2]/div[2]/table[2]						# accompanied event d
