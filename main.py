import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")

...

@client.event
async def on_message(message):
    if message.content.startswith("읔엌"):
        await message.channel.send("끜끜")
    if message.content.startswith("칭호획득:갑분싸 마스터"):
        await message.channel.send("아니다아아아아악")
    if message.content.startswith("1빠다 엌엌"):
        await message.channel.send("오 1빠누 ㅊㅊ")
    if message.content.startswith("2빠다 엌엌"):
        await message.channel.send("2빠누 ㄲㅂ")
    if message.content.startswith("3빠다 엌엌"):
        await message.channel.send("3빠누")


client.run("NzgxNzkzMDAyMDY2NDExNTU5.X8CzeA.Tk6gYlkVP2BOgZ-4aNLaM8Qlt4o")