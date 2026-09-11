import discord
from discord.ext import commands

TOKEN = "MTU0ODAzODg2OTU3MDU1NTk0NA.GPpon5.UDXcEnCokJ40Z7XyzIIuS1fkeGwYBGy5i-zZLc"

CANAL_GERAL_ID = [
    1499824532175978516,   # canal geral original
    1499817906563842108,   # canal geral 2
    1524580316919103628,   # canal geral 3
]   # onde as pessoas conversam normalmente
CANAL_WL_ID = 1533874576835215491      # canal específico de whitelist
CANAL_WIPE_ID = 1499817401653399612    # canal específico de wipe

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# Cada item da lista é um "grupo" de palavras.
# Se TODAS as palavras de um grupo estiverem na mensagem, o gatilho ativa.
GATILHOS_WL = [
    ["wl"],
    ["whitelist"],
    ["wlist"],
    ["quando", "wl"],
    ["quando", "whitelist"],
    ["como", "wl"],
    ["como", "whitelist"],
    ["quero", "wl"],
    ["quero", "whitelist"],
    ["vaga", "wl"],
    ["vagas", "wl"],
    ["abriu", "wl"],
    ["abre", "wl"],
    ["liberou", "wl"],
    ["fazer", "wl"],
    ["preencher", "wl"],

    # Mais genéricas — descomente por sua conta e risco (mais chance de falso positivo)
    # ["entrar", "server"],
    # ["processo", "seletivo"],
]

GATILHOS_WIPE = [
    ["wipe"],
    ["wipezão"],
    ["wipezao"],
    ["reset"],
    ["quando", "wipe"],
    ["vai ser", "wipe"],
    ["vai ser", "wipezão"],
    ["vai ser", "wipezao"],
    ["data", "wipe"],
    ["dia", "wipe"],
    ["próximo", "wipe"],
    ["proximo", "wipe"],
    ["novo", "wipe"],
    ["vai ter", "wipe"],
    ["como", "reset"],
    ["quando", "reset"],

    # Mais genéricas — descomente por sua conta e risco (mais chance de falso positivo)
    # ["novo", "mapa"],
    # ["nova", "season"],
    # ["zerar", "tudo"],
]


def ativa(conteudo: str, gatilhos: list) -> bool:
    for grupo in gatilhos:
        if all(palavra in conteudo for palavra in grupo):
            return True
    return False


@bot.event
async def on_ready():
    print("--------------------------------")
    print("BOT ONLINE!")
    print(f"Nome: {bot.user}")
    print(f"ID: {bot.user.id}")
    print("--------------------------------")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id in CANAL_GERAL_ID:
        conteudo = message.content.strip().lower()

        if ativa(conteudo, GATILHOS_WL):
            canal_wl = message.guild.get_channel(CANAL_WL_ID)
            await message.channel.send(
                f"{message.author.mention} Para solicitar whitelist, vá até {canal_wl.mention} 🔑"
            )

        elif ativa(conteudo, GATILHOS_WIPE):
            canal_wipe = message.guild.get_channel(CANAL_WIPE_ID)
            await message.channel.send(
                f"{message.author.mention} 📢 Fique de olho no canal de anúncios para não perder novidades! {canal_wipe.mention} 🧹"
            )

    await bot.process_commands(message)


bot.run("MTU0ODAzODg2OTU3MDU1NTk0NA.GPpon5.UDXcEnCokJ40Z7XyzIIuS1fkeGwYBGy5i-zZLc")