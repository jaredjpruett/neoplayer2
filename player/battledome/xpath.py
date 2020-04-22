class XPaths():
	login = {
		'login_link'			: ".//*[@id='header']/table/tbody/tr[1]/td[3]/a[1]",
		'signup_link'			: ".//*[@id='header']/table/tbody/tr[1]/td[3]/a[3]",
		'username_field'		: ".//*[@id='templateLoginPopupUsername']",
		'password_field'		: ".//*[@id='templateLoginPopup']/div/form/table/tbody/tr[2]/td[2]/input",
		'login_button'			: ".//*[@id='templateLoginPopup']/div/form/table/tbody/tr[3]/td/input",
		'logout_link'			: ".//*[@id='logout_link']/b",
	}

	account = {
		'username'				: ".//*[@id='header']/table/tbody/tr[1]/td[3]/a[1]",
	}

	bd = {
		'main' : {
			'battle'			: ".//*[@id='bdHomeUpperBattle']",
		},
		'fight' : {
			'pet_name'			: ".//*[@id='bdFightPetInfo']/div[1]/div[4]",
			'continue1'			: ".//*[@id='bdFightStep1']/div[3]",
			'continue2'			: ".//*[@id='bdFightStep2']/div[4]",
			'opponent'			: ".//*[@id='npcTable']/tbody/tr[23]",
			'opponent_name'		: ".//*[@id='npcTable']/tbody/tr[23]/td[2]",
			'opponent_hard'		: ".//*[@id='npcTable']/tbody/tr[23]/td[4]/div[3]",
			'battle'			: ".//*[@id='bdFightStep3FightButton']",
		},
		'arena' : {
			'display'			: ".//*[@id='hudimg']",
			'fight1'			: ".//*[@id='start']",
			'slot1'				: ".//*[@id='p1e1m']/div",
			'slot2'				: ".//*[@id='p1e2m']/div",
			'slot3'				: ".//*[@id='p1am']/div",
			'item1'				: ".//*[@title='Ridiculously Heavy Battle Hammer']",
			'item2'				: ".//*[@title='Scarab Ring']",
			'ability1'			: ".//*[@id='p1ability']/div[3]/table/tbody/tr/td[4]/div/div",
			'ability2'			: ".//*[@id='p1ability']/div[3]/table/tbody/tr/td[3]/div/img",
			'fight2'			: ".//*[@id='fight']",
			'skip_replay'		: ".//*[@id='skipreplay']",
			'collect_rewards'	: ".//*[@id='playground']/div[2]/button[1]",
			'rewards'			: ".//*[@id='bd_rewardsloot']",
			'item_limit'		: ".//*[@id='bd_rewardsloot']/tbody/tr[2]/ul/li[3]",
			'play_again'		: ".//*[@id='bdplayagain']",
		}
	}

	academy = {
		'main' : {
			'courses'			: ".//*[@id='content']/table/tbody/tr/td[2]/center[1]/a[2]/b",
			'status'			: ".//*[@id='content']/table/tbody/tr/td[2]/center[1]/a[3]/b",
		},
		'courses' : {
			'course'			: ".//select[@name='course_type']",
			'pet'				: ".//select[@name='pet_name']",
			'start_course'		: ".//*[@id='content']/table/tbody/tr/td[2]/form/p[2]/input",
		},
		'status' : {
			'pet'				: ".//*[@id='content']/table/tbody/tr/td[2]/table/tbody/tr[3]/td/b",
			'level'				: ".//*[@id='content']/table/tbody/tr/td[2]/table/tbody/tr[4]/td[1]/font/b",
			'strength'			: ".//*[@id='content']/table/tbody/tr/td[2]/table/tbody/tr[4]/td[1]/b[1]",
			'defense'			: ".//*[@id='content']/table/tbody/tr/td[2]/table/tbody/tr[4]/td[1]/b[2]",
			'movement'			: ".//*[@id='content']/table/tbody/tr/td[2]/table/tbody/tr[4]/td[1]/b[3]",
			'hitpoints'			: ".//*[@id='content']/table/tbody/tr/td[2]/table/tbody/tr[4]/td[1]/b[4]",
			'pay'				: ".//*[@id='content']/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/table[2]/tbody/tr/td[1]/form/input[3]",
			'complete'			: ".//*[@id='content']/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/form/input[3]",
		}
	}

	sdb = {
		'remove_one'			: ".//*[@id='content']/table/tbody/tr/td[2]/form[1]/table[2]/tbody/tr[2]/td[6]/a",
	}
