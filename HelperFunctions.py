import random
import discord
from discord.ext import commands

#-------------------------------------------------------------#
""" Takes 3 possible numbers to roll X number of Y dice """
def roll(interaction: discord.Interaction,dice:str):
    try:
            splitplus = dice.split("+")
            splitNumbers = list()
            for item in splitplus:
                splitNumbers.append(item.split("d"))

            add, total, re = 0, 0, list()

            for item in splitNumbers:
                if len(item) == 1:
                    add += int(item[0])
                    total += int(item[0])
                elif len(item) == 2:
                    re.append(list())
                    for X in range(int(item[0])):
                        re[-1].append(random.randint(1, int(item[1])))
                        total += re[-1][-1]
                    tuple(re[-1])

            return [add,total,re]
    except ValueError as err:
        print(f"Value Error in rolling: {err}")
        return "Value Error"


#-------------------------------------------------------------#
