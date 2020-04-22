class URLs():
	root = "http://www.neopets.com/"
	bd = root + "dome/"
	academy = root + "pirates/academy.phtml"
	sdb = root + "safetydeposit.phtml"

	general = {
		'root'		: root,
	}

	bd = {
		'main'		: bd,
		'fight'		: bd + "fight.phtml",
		'arena'		: bd + "arena.phtml",
		'stats'		: bd + "neopets.phtml",
	}

	academy = {
		'main'		: academy,
		'courses'	: academy + "?type=courses",
		'status'	: academy + "?type=status",
	}

	sdb = {
		'sdb'		: sdb,
		'odc'		: sdb + "?obj_name=One+Dubloon+Coin&category=0",
		'tdc'		: sdb + "?obj_name=Two+Dubloon+Coin&category=0",
		'fdc'		: sdb + "?obj_name=Five+Dubloon+Coin&category=0",
	}
