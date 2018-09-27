import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client()
client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
    print("bot on")

@client.event
async def on_message(message):
    if message.content == "hello":
        await client.send_message(message.channel, "jai guru dev " + (message.author.name) + " :pray:")
    if message.content == "Hello":
        await client.send_message(message.channel, "jai guru dev " + (message.author.name) + " :pray:")
    if message.content == "bye":
        await client.send_message(message.channel, "bye " + "@" + (message.author.name) + " :hand_splayed:" + " :hand_splayed:" )
    if message.content == "Bye":
        await client.send_message(message.channel, "bye " + "@" + (message.author.name) + " :hand_splayed:" + " :hand_splayed:" )
    if message.content == "about mvm":
        await client.send_message(message.channel, "Consciousness is the prime mover of life. Maharishi Vidya Mandir Schools are offering complete theoretical and practical knowledge of consciousness, which will open the gate of all possibilities in the life of the students. Through the technology of Maharishi Vedic Science, the schools offer mastery in the field of consciousness, enabling the student to accomplish anything and live a complete life.")
    if message.content == "Sci list":
        await client.send_message(message.channel, "♥Order is present everywhere" +
" ♥Life is found in layers" +
" ♥Outer depends on inner" +
" ♥Seek the highest first" +
" ♥Rest and activity are the steps of progress" +
" ♥Enjoy greater efficiency and accomplish more" +
" ♥Every action has a reaction" +
" ♥Purification leads to progress" +
" ♥The field of all possibilities is the source of all solutions" +
" ♥Thought leads to action, action leads to achievement" +
" And achievement leads to fulfillment"+
" ♥Knowledge is gained from inside and outside" +
" ♥Knowledge is structured in consciousness" +
" ♥Harmony exists in diversity" +
" ♥Whole is contained in every part" +
" ♥The whole is greater than the sum of the parts")
    if message.content == "What is TM":
        await client.send_message(message.channel, "a technique for detaching oneself from anxiety and promoting harmony and self-realization by meditation, repetition of a mantra, and other yogic practices, promulgated by an international organization founded by the Indian guru Maharishi Mahesh Yogi ( c. 1911–2008)")
    if message.content == "TM in detail":
        await client.send_message(message.channel, "Transcendental Meditation (TM) refers to a specific form of silent mantra meditation called the Transcendental Meditation technique,[1] and less commonly to the organizations that constitute the Transcendental Meditation movement.[1][2] Maharishi Mahesh Yogi introduced the TM technique and TM movement in India in the mid-1950s." + 

"The Maharishi taught thousands of people during a series of world tours from 1958 to 1965, expressing his teachings in spiritual and religious terms.[3][4] TM became more popular in the 1960s and 1970s, as the Maharishi shifted to a more technical presentation, and his meditation technique was practiced by celebrities. At this time, he began training TM teachers and created specialized organizations to present TM to specific segments of the population such as business people and students. By the early 2000s, TM had been taught to millions of people, and the worldwide TM organization had grown to include educational programs, health products, and related services. " + 

"The TM technique involves the use of a sound called a mantra, and is practiced for 15–20 minutes twice per day. It is taught by certified teachers through a standard course of instruction, which costs a fee that varies by country. According to the Transcendental Meditation movement, it is a non-religious method for relaxation, stress reduction, and self-development. The technique has been seen as both religious and non-religious; sociologists, scholars, and a New Jersey judge and court are among those who have expressed views.[4][5][6] The United States Court of Appeals upheld the federal ruling that TM was essentially religious in nature and therefore could not be taught in public schools.")



    
client.run("NDk0ODEwMzI2NDEyNTU4MzM2.Do48YQ.Ibd0804_vNERfOp61JxmlDU6Swo")


