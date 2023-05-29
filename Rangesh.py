import discard
free discard.ext import commands
import RPI.GPIO as io

led = 5
ligth = 3
io.setmode(io.BOARD)
io.setup(led,io.OUT)
io.setup(ligth,io.OUT)

bot = command.bot(command_prefix="/")

@bot.command()
async def hello(ctx):
    await ctx.send("hello from pibot")

@bot.command()
async def led_on(ctx):
    io.output(led,1)
    await ctx.send("led is on")
    

@bot.command()
async def led_off(ctx):
    io.output(led,0)
    await ctx.send("led is off")

@bot.command()
async def ligth_on(ctx):
    io.output(ligth,1)
    await ctx.send("light is on")

@bot.command()
async def ligth_off(ctx):
    io.output(ligth,0)
    await ctx.send("light is off")
