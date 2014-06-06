def signFilter(poi):
	if poi['id'] == 'Sign':
		return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])

worlds["Lomonation"] = "~/minecraft/survival/lomo"

renders["survivalday"] = {
	"world": "Lomonation",
	"title": "Overworld",
	"rendermode": smooth_lighting,
	"dimension": "overworld",
	"markers": [dict(name="Signs", filterFunction=signFilter)],
}

renders["survivalnether"] = {
	"world": "Lomonation",
	"title": "Nether",
	"rendermode": nether_smooth_lighting,
	"dimension": "nether",
}

renders["survivalend"] = {
	"world": "Lomonation",
	"title": "The End",
	"rendermode": smooth_lighting,
	"dimension": "end",
}

outputdir = "/var/www/minecraft/maps/lomonation"
texturepath = "~/minecraft/Isabella_II_1.7f.zip"

from observer import JSObserver
observer = JSObserver(outputdir, 10)
