import discord
from dotenv import load_dotenv
import os
import requests
from course import Course, CourseNotFound

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
load_dotenv()

if (TOKEN := os.getenv("TOKEN")) is None:
    print("TOKEN is not defined")
    exit(1)

BASE_URL = "https://csuf-courses-backend.vercel.app/api/course/"


def embed_builder(response: dict):
    """
    Constructs an embed from a JSON response from the backend
    """

    try:
        course = Course(response)
        embed = discord.Embed(title=course.title, description=course.description)
        embed.add_field(name="Prerequisites", value=course.prerequisites)
        embed.add_field(name="Corequisites", value=course.corequisites)
        embed.color = discord.Color.green()
        return embed
    except CourseNotFound as e:
        embed = discord.Embed(title="Error", description=str(e))
        embed.color = discord.Color.red()
        return embed


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    # ensure not self trigger
    if message.author == client.user:
        return

    if message.content.startswith("$course"):
        # check if contains course
        if len(message.content.split()) < 2:
            await message.channel.send("Please specify a course")
            return

        # extract course
        course = " ".join(message.content.split()[1:]).strip()

        # send request to backend
        response = requests.get(BASE_URL + course)

        # construct embed
        await message.channel.send(embed=embed_builder(response.json()))


client.run(TOKEN)
