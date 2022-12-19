import re
import base64
from io import BytesIO
from os import path

from PIL import Image

from hoshino import R, Service, aiorequests
from hoshino.typing import HoshinoBot, CQEvent 
from .data_source import generate_gif

#from .._res import Res as R

sv = Service('woodenfish', bundle='电子功德', help_='''
@bot攒功德 | 开始攒功德
'''.strip())
#res_dir = path.expanduser(hoshino.config.RES_DIR)
#data_dir = path.join(res_dir, 'woodenfish')
data_dir = R.img("woodenfish/").path

@sv.on_fullmatch('攒功德', only_to_me=True)
async def creep(bot, ev: CQEvent):

	uid = ev.user_id
	
	url = f'http://q1.qlogo.cn/g?b=qq&nk={uid}&s=160'
	resp = await aiorequests.get(url)
	resp_cont = await resp.content
	avatar = Image.open(BytesIO(resp_cont))
	output = generate_gif(data_dir, avatar)
	#img = Image.open(output)
	#buf = BytesIO()
	#img.save(buf, format='GIF')
	#base64_str = f'base64://{base64.b64encode(buf.getvalue()).decode()}'
	print(output)
	await bot.send(ev,f'{R.img("woodenfish/","output.gif").cqcode}')
	
	
	#await bot.send(ev, f'[CQ:image,file={base64_str}]')