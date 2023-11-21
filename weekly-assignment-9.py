import subprocess

# Create a 3-minute clip starting at 00:33:17:
ffmpeg_cmd = [
	'ffmpeg',
	'-i', 'The_Rocky_Horror_Picture_Show (1975).mp4',
	'-ss', '00:33:17',
	'-codec', 'copy',
	'-t', '180',
	'rocky_birthday.mp4'
	]

subprocess.run(ffmpeg_cmd, check=True)

# Take that clip and change the aspect ratio to 4:3:
ffmpeg_cmd = [
	'ffmpeg',
	'-i', 'rocky_birthday.mp4',
	'-aspect', '4:3',
	'square_rocky.mp4'
	]

subprocess.run(ffmpeg_cmd, check=True)
