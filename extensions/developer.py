# -*- coding: utf-8 -*-

# Developer functions
# Provides functions only useable for developers

'''Developer Cog'''

import discord
from discord.ext import commands
import os
# import psutil
import aiohttp
import random

class Developer(commands.Cog):
    def  __init__(self, bot):
        self.bot = bot
        self.request = bot.request
        self.instances = bot.instances

    async def _instance_check(self, instance, info):
        '''Checks the quality of an instance.'''

        # Makes sure proper values exist
        if 'error' in info:
            return False
        if not ('engines' in info and 'initial' in info['timing']):
            return False
        if not ('google' in info['engines'] and 'enabled' in info['engines']['google']):
            return False

        # Makes sure google is enabled
        if not info['engines']['google']['enabled']:
            return False

        # Makes sure is not Tor
        if info['network_type'] != 'normal':
            return False

        # Only picks instances that are fast enough
        timing = int(info['timing']['initial'])
        if timing > 0.20:
            return False

        # Check for Google captcha
        test_search = f'{instance}/search?q=test&format=json&lang=en-US'
        try:
            async with self.request.get(test_search) as resp:
                response = await resp.json()
            response['results'][0]['content']
        except (aiohttp.ClientError, KeyError, IndexError):
            return False

        # Reached if passes all checks
        return True

    @commands.command()
    async def rejson(self, ctx):
        '''Refreshes the list of instances for searx.'''

        msg = await ctx.send('<a:updating:403035325242540032> Refreshing instance list...\n\n'
            '(Due to extensive quality checks, this may take a bit.)')
        plausible = []

        # Get, parse, and quality check all instances
        async with self.request.get('https://searx.space/data/instances.json') as r:
            # Parsing
            searx_json = await r.json()
            instances = searx_json['instances']

            # Quality Check
            for i in instances:
                info = instances.get(i)
                is_good = await self._instance_check(i, info)
                if is_good:
                    plausible.append(i)

        # Save new list
        self.instances = plausible
        with open('searxes.txt', 'w') as f:
            f.write('\n'.join(plausible))

        await msg.edit(content='Instances refreshed!')

    @commands.command(aliases=['exit', 'reboot'])
    async def restart(self, ctx):
        await ctx.send(':zzz: **Restarting.**')
        exit()

#     @commands.command()
#     async def stats(self, ctx):
#         mem = psutil.virtual_memory()
#         currproc = psutil.Process(os.getpid())
#         total_ram = self.humanbytes(mem[0])
#         available_ram = self.humanbytes(mem[1])
#         usage = self.humanbytes(currproc.memory_info().rss)
#         text = f"""
# ```
# Total RAM: {total_ram}
# Available RAM: {available_ram}
# RAM used by bot: {usage}
# Number of bot commands: {len(ctx.bot.commands)}
# Number of extensions present: {len(ctx.bot.cogs)}
# Number of users: {len(ctx.bot.users)}
# ```
# """
#         await ctx.send(text)

    @commands.command(hidden=True)
    async def error(self, ctx):
        3 / 0

    async def cog_check(self, ctx):
        return commands.is_owner()

def setup(bot):
    bot.add_cog(Developer(bot))