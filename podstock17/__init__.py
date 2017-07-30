#!/usr/bin/python3

from renderlib_podstock17 import *
from easing import *

scheduleUrl = 'https://frab.podstock.de/de/podstock2017/public/schedule.xml'

def introFrames(p):
	# 4 sec. show nothing (animation in video) 
	frames = 100
	for i in range(0, frames):
		yield (
			('layer1', 'style',    'opacity', "%.4f" % 0),  # nix 
		)

	# 6 Frames Text Fadein
	frames = 6
	for i in range(0, frames):
		yield (
			('layer1', 'style',    'opacity', "%.4f" % easeLinear(i, 0, 1, frames)),
		)

	# 7.8 sec show text
	frames = 195
	for i in range(0, frames):
		yield (
			('layer1', 'style',    'opacity', "%.4f" %1),
		)

def debug():
	render(
		'intro.svg',
		'../intro.ts',
		 introFrames,
		{
			'$id': 65,
			'$title': 'Podcasts im 23. Jahrhundert'.upper(),
			'$subtitle': 'Warpantrieb und Zeitreisen',
			'$personnames': 'Commander Future'
		}
	)

def tasks(queue, args, idlist, skiplist):
    # iterate over all events extracted from the schedule xml-export
    for event in events(scheduleUrl):
        # generate a task description and put it into the queue
        queue.put(Rendertask(
            infile = 'intro.svg',
            outfile = str(event['id'])+".ts",
            sequence = introFrames,
            parameters = {
                '$id': event['id'],
                '$title': event['title'],
                '$subtitle': event['subtitle'],
                '$personnames': event['personnames']
                }
            ))
