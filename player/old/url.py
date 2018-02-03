# URLs of various site activities
# TODO: Modularize URL organization

root				= "http://www.neopets.com/"
battledome			= root + "dome/"
foodclub			= root + "pirates/foodclub.phtml"
academy				= root + "pirates/academy.phtml"

url = {
	'main'			: root,

	'bank'			: root + "bank.phtml",
	'interest'		: root + "bank.phtml",

	'inventory'		: root + "inventory.phtml",
	'quickstock'	: root + "quickstock.phtml",

	'foodclub'		: root + "pirates/foodclub.phtml?type=bet",
	'foodclubbets'	: root + "~myfoodclubbets",
	'bets'			: root + "pirates/foodclub.phtml?type=current_bets",
	'winnings'		: root + "pirates/foodclub.phtml?type=collect",

	'mediocrity'	: root + "prehistoric/mediocrity.phtml",
	'excitement'	: root + "faerieland/wheel.phtml",

	'jelly'			: root + "jelly/jelly.phtml",
	'omelette'		: root + "prehistoric/omelette.phtml",

	'scratchcard'	: root + "winter/kiosk.phtml",
	'anchor'		: root + "pirates/anchormanagement.phtml",
	'altador'		: root + "altador/council.phtml?prhv=63338403060c35110b2e7e73f103af77",
	'altador1'		: root + "altador/council.phtml",
	'tombola'		: root + "island/tombola.phtml",
	'coltzan'		: root + "desert/shrine.phtml",
	'fruits'		: root + "desert/fruit/index.phtml",
	'shore'			: root + "pirates/forgottenshore.phtml",
	'springs'		: root + "faerieland/springs.phtml",
	'fishing'		: root + "water/fishing.phtml",
	'offers'		: root + "shop_of_offers.phtml?slorg_payout=yes",
	'freebies'		: root + "freebies/index.phtml",
	'apple'			: root + "halloween/applebobbing.phtml?",
	'apple2'		: root + "halloween/applebobbing.phtml?bobbing=1",
	'plushie'		: root + "faerieland/tdmbgpop.phtml",
	'chest'			: root + "petpetpark/daily.phtml",
}

battledome_url = {
	'main'			: battledome,
	'fight'			: battledome + "fight.phtml",
	'arena'			: battledome + "arena.phtml",
	'stats'			: battledome + "neopets.phtml",
}

url_foodclub = {
	'hugo'			: root + "~myfoodclubbets",

	'place'			: foodclub + "?type=bet",
	'current'		: foodclub + "?type=current_bets",
	'collect'		: foodclub + "?type=collect",
}

url_academy = {
	'main'			: academy,
	'status'		: academy + "?type=status",
	'courses'		: academy + "?type=courses",
}
