import discord
from googleapiclient.discovery import build
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='$', intents=intents)

youtube_key=os.getenv('env_youtube_key')
youtube = build('youtube', 'v3', developerKey=youtube_key)

def search_videos(query):
    request = youtube.search().list(
        part='snippet',
        q=query,
        type='video',
        maxResults=5
    )
    response = request.execute()
    return response['items']

def get_videos(search):
    videos = search_videos(search)
    for video in videos:
        title = video['snippet']['title']
        video_id = video['id']['videoId']
        url = f'https://www.youtube.com/watch?v={video_id}'
        # print(title, url)
        vid=title + url
        return vid

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    voice_channel = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_channel is None:
        await channel.connect()
        await ctx.send(f"Joined {channel}")
    else:
        await ctx.send("I'm already in a voice channel.")

# Leave voice channel
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

# Play a song
@bot.command()
async def play(ctx, url):
    voice_channel = get(ctx.guild.voice_channels, name='Your Voice Channel')
    voice_client = get(bot.voice_clients, guild=ctx.guild)

    if not voice_client.is_playing():
        voice_client.play(discord.FFmpegPCMAudio(url))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
        voice_client.source.volume = 0.5
        await ctx.send('Now playing: {}'.format(url))
    else:
        await ctx.send('Bot is already playing a song.')

# Pause playback
@bot.command()
async def pause(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client.is_playing():
        voice_client.pause()
        await ctx.send('Playback paused.')
    else:
        await ctx.send('Bot is not playing anything.')

# Resume playback
@bot.command()
async def resume(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client.is_paused():
        voice_client.resume()
        await ctx.send('Playback resumed.')
    else:
        await ctx.send('Playback is not paused.')

# Skip the current song
@bot.command()
async def skip(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client.is_playing():
        voice_client.stop()
        await ctx.send('Skipped the current song.')
    else:
        await ctx.send('Bot is not playing anything.')