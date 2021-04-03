# ForwardTagRemoverBot - A Telegram Bot To Hide Forward Source
#Copyright (C) 2020 by Rasak <https://github.com/Artis7eeR>
#ForwardTagRemoverBot is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#ForwardTagRemoverBot is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os

class Config:
	
 TOKEN=os.environ.get("BOT_TOKEN",None)
 SOURCE="https://github.com/ImBhashitha/ForwardTagRemoverBot"
 START_TEXT="Hi [{}](tg://user?id={})\n*I am A Forward Tag remover Bot.*\n*Send */help *To Know What I Can Do \n ©NET.HACKER BOTs 🇱🇰*"
 HELP_TEXT="*Forward Me A File,Video,Audio,Photo or Anything And *\n*I will Send You the File Back*\n\n`*How to Set Caption?*`\n*Reply Caption to a File,Photo,Audio,Media*"
	
