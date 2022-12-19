from os import path
import random
from PIL import Image, ImageDraw, ImageFont

def get_circle_avatar(avatar, size):
	avatar = avatar.resize((size, size))
	avatar = avatar.convert('RGBA')
	mask = Image.new('L', (size,size), 0)
	draw = ImageDraw.Draw(mask)
	draw.ellipse((0, 0, size, size), fill=255)
	ret_img = avatar.copy()
	ret_img.putalpha(mask)
	return ret_img

def generate_gif(frame_dir: str, avatar: Image.Image) -> Image.Image:
	avatar_size = (110,110)
	avatar_pos = (71,27)
	imgs = []
	flametime_list=[10,60,120]
	avatar= get_circle_avatar(avatar, 110)
	fontdir = path.join(frame_dir,'pinfang.ttf')
	flametime = flametime_list[random.randint(0,2)]
	for i in range(5):
		woodenfish = Image.open(path.join(frame_dir, f'woodenfish_{i+1}.jpg'))
		woodenfish = woodenfish.convert('RGBA')
		woodenfish.paste(woodenfish)
		woodenfish.paste(avatar,avatar_pos,avatar)
		draw = ImageDraw.Draw(woodenfish)
		ttf = ImageFont.truetype(fontdir,18+(i*3))
		if flametime == 10:
			draw.text((30,80-(i*20)),"+100",font=ttf,fill=(0+(i*63),0,0))
		elif flametime == 60:
			draw.text((30,80-(i*20)),"+10",font=ttf,fill=(0+(i*63),0,0))
		else:
			draw.text((30,80-(i*20)),"+1",font=ttf,fill=(0+(i*63),0,0))
		imgs.append(woodenfish)
	out_path = path.join(frame_dir, 'output.gif')
	imgs[0].save(fp=out_path, save_all=True, append_images=imgs,
                 duration=flametime, loop=0, quality=80, transparency=255)
	return out_path