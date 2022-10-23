from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import jsonify
from dataclasses import dataclass

from twilio.rest import Client 
import random
import time

import mysql.connector
from mysql.connector import Error
import boto3
import os
import sys
import pymysql

import pygame
 
account_sid = 'AC58a9d44499f8868207a5089273eb3adc' 
auth_token = ' ' 
client = Client(account_sid, auth_token) 


import pygame
from pygame.locals import *
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"

BLOCK_SIZE=16
SCREEN_WIDTH = (BLOCK_SIZE*20)+(1*BLOCK_SIZE)
SCREEN_HEIGHT = (BLOCK_SIZE*20)+(3*BLOCK_SIZE)
SIZE = SCREEN_WIDTH, SCREEN_HEIGHT

BLUE = (0,0,255)
GRAY = (150, 150, 150)


board = [
[0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
[0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
[0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
]


obj_board = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,34,32,32,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,33,33,33,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,30,31,30,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
[0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
[0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]


grid_image = pygame.image.load("res/grid.png")


grass_tiles = []
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass1.png"))
grass_tiles.append(pygame.image.load("res/grass2.png"))
grass_tiles.append(pygame.image.load("res/grass3.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))


floor_tiles = []
floor_tiles.append(pygame.image.load("res/floor0.png"))
floor_tiles.append(pygame.image.load("res/floor0.png"))
floor_tiles.append(pygame.image.load("res/floor1.png"))
floor_tiles.append(pygame.image.load("res/floor2.png"))
floor_tiles.append(pygame.image.load("res/floor3.png"))
floor_tiles.append(pygame.image.load("res/floor4.png"))
floor_tiles.append(pygame.image.load("res/floor0.png"))

tall_grass_tiles = []
tall_grass_tiles.append(pygame.image.load("res/tall_grass_0.png"))
tall_grass_tiles.append(pygame.image.load("res/tall_grass_1.png"))
tall_grass_tiles.append(pygame.image.load("res/tall_grass_2.png"))
tall_grass_tiles.append(pygame.image.load("res/tall_grass_3.png"))
tall_grass_tiles.append(pygame.image.load("res/tall_grass_4.png"))

player_tiles = []
player_tiles.append(pygame.image.load("res/char0.png"))
player_tiles.append(pygame.image.load("res/char1.png"))
player_tiles.append(pygame.image.load("res/char2.png"))
player_tiles.append(pygame.image.load("res/char3.png"))
player_tiles.append(pygame.image.load("res/char4.png"))
player_tiles.append(pygame.image.load("res/char5.png"))
player_tiles.append(pygame.image.load("res/char6.png"))
player_tiles.append(pygame.image.load("res/char7.png"))
player_tiles.append(pygame.image.load("res/char8.png"))
player_tiles.append(pygame.image.load("res/char9.png"))
player_tiles.append(pygame.image.load("res/char10.png"))
player_tiles.append(pygame.image.load("res/char11.png"))

#30
b_wall = pygame.image.load("res/b_wall.png")
#31
b_door = pygame.image.load("res/b_door.png")
#32
b_roof = pygame.image.load("res/b_roof.png")
#33
b_roof_edge = pygame.image.load("res/b_roof_edge.png")
#34
b_chiminey = pygame.image.load("res/b_chiminey.png")



#                 Database stuff
#-----------------------------------------------------
ENDPOINT='mysql-database.ciliflj0ubbb.us-east-2.rds.amazonaws.com'
PORT = "3306"
USER="admin"
REGION="us-east-2c"
DBNAME='a'
ACC_KEY="AKIAROKV6GQLZSY5QNAW"
SEC_KEY="AqrpO9Ot7KzES//Y+ckURRYL43/AmmHFtoUxW9bp"
REGION='us-east-2c'
PASSWD='3JDPtkVMC83y482'

class Result:
    def __init__(self, phone_num, num_guess):
        self.phone_num=phone_num
        self.num_guess=num_guess

def add_num(cur, result):
  
    val=(str(result.phone_num),)
    cur.execute("SELECT phone_num from main_table")
    query_results = cur.fetchall()
    #print(query_results)
    cur.execute("SELECT * from main_table WHERE phone_num=%s", val)
    query_results = cur.fetchall()
    #print("row", query_results)

    win=result.num_guess<7

    if(query_results):
        #ur.execute("SELECT num_games from main_table WHERE phone_num={1}".format(result.phone_num))
        cur.execute('UPDATE main_table SET loss=loss+(-{0}+1), num_games=num_games+1, win_percent=(num_games-loss)/num_games, win_streak=(win_streak+1)*{0} WHERE phone_num = {1}'.format(win,result.phone_num))
        var=(str(result.phone_num),)
        cur.execute("SELECT win_streak FROM main_table WHERE phone_num={0}".format(str(result.phone_num)))
        win_streak=cur.fetchall()[0][0]
        cur.execute("SELECT high_streak FROM main_table WHERE phone_num={0}".format(str(result.phone_num)))
        high_streak=cur.fetchall()[0][0]
        if(win_streak>high_streak):
            cur.execute('UPDATE main_table SET high_streak=win_streak  WHERE phone_num = {0}'.format(result.phone_num))
            
    else:  
   
        val=(str(result.phone_num), str(1), str(win), str(win), str(win), str(-win+1))
        cur.execute("INSERT INTO main_table (phone_num, num_games, win_percent, win_streak, high_streak, loss) VALUES (%s,%s,%s,%s,%s,%s)",val)
     
def display_stats(cur, phone_num):
    cur.execute("SELECT * FROM main_table WHERE phone_num={0}".format(phone_num))
    query=cur.fetchall()[0]

    ret_string = ".\n"
    ret_string += str("Games Played: "+ str(query[1])+'\n')
    ret_string += str("Win Percentage: "+ str(round(query[2],2))+"%\n")
    ret_string += str("Winning Streak: " + str(query[3])+'\n')
    ret_string += str("Longest Winning Streak: " + str(query[4])+'\n')
    ret_string += str("Losses: "+ str(query[5])+'\n')
    print(ret_string)
    return ret_string

def display_info(phone_number):
 
    session = boto3.Session(
        aws_access_key_id=ACC_KEY,
        aws_secret_access_key=SEC_KEY,
    )

    client = session.client('rds', region_name=REGION)
    token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

    try:
    
        conn =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd=PASSWD, port=PORT, database=DBNAME)
        cur = conn.cursor()
        #cur.execute("CREATE TABLE table1(phone_num int, high_score int, time double, num_guess int)")
        #result=Result(18697856, 7)
        #cur.execute("SHOW TABLES from a")
        #query_results = cur.fetchall()
        #print(query_results)
        
        ret_str = display_stats(cur,phone_number)

        #add_num(cur, result)
        cur.execute("SELECT * FROM main_table") 
        query_results = cur.fetchall()
        #print(query_results)
        #cur.execute("truncate main_table")
        cur.execute("COMMIT")

        return ret_str
   
    except Exception as error:
        print("{0}".format(error))  



def mod_db(phone_number, num_guess):
 
    session = boto3.Session(
        aws_access_key_id=ACC_KEY,
        aws_secret_access_key=SEC_KEY,
    )

    client = session.client('rds', region_name=REGION)
    token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

    try:
    
        conn =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd=PASSWD, port=PORT, database=DBNAME)
        cur = conn.cursor()
        #cur.execute("CREATE TABLE table1(phone_num int, high_score int, time double, num_guess int)")
        result=Result(phone_number, num_guess)
        #cur.execute("SHOW TABLES from a")
        #query_results = cur.fetchall()
        #print(query_results)

        add_num(cur, result)
        cur.execute("SELECT * FROM main_table") 
        query_results = cur.fetchall()
        print(query_results)
        #cur.execute("truncate main_table")
        cur.execute("COMMIT")


   
    except Exception as error:
        print("{0}".format(error))

#-----------------------------------------------------



random.seed()

with open('wordbank.txt') as dict:
    word_bank_lines = dict.readlines()

# Uppercases and strips new line from word bank
for i in range(0,len(word_bank_lines)):
  word_bank_lines[i] = word_bank_lines[i].upper().strip()

with open('guessbank.txt') as pool:
    playwords = pool.readlines()

for i in range(0,len(playwords)):
    playwords[i] = playwords[i].upper().strip()

#collect input
def CheckInput(userinput,player_object):
    player_object.info_matrix[player_object.guess_num]
    info_string = ""
    print("Userinput: "+str(userinput))
    print("current_word: "+player_object.current_word)
    for i in range(0,5):
        if userinput[i] == player_object.current_word[i]:
            info_string += "✅"
        elif userinput[i] in player_object.current_word:
            info_string += "👍"
        else:
            info_string += "❌"
    for i in range(0,len(info_string)):
        player_object.info_matrix[player_object.guess_num][i] = info_string[i]




phone_number_list = []
player_list = []

@dataclass
class PlayerData:
    guess_num : int
    output_matrix : list
    info_matrix : list
    phone_number : str
    current_word : str

def addPlayer(phone_number):
    output_matrix = [
    ['_','_','_','_','_'],
    ['_','_','_','_','_'],
    ['_','_','_','_','_'],
    ['_','_','_','_','_'],
    ['_','_','_','_','_']
    ]

    info_matrix = [
    ['=','=','=','=','='],
    ['=','=','=','=','='],
    ['=','=','=','=','='],
    ['=','=','=','=','='],
    ['=','=','=','=','=']
    ]
    guess_num=0

    playword = playwords[random.randint(0,len(playwords)-1)]

    newPlayer = PlayerData(guess_num, output_matrix, info_matrix,phone_number,playword)
    phone_number_list.append(phone_number)
    player_list.append(newPlayer)

def genMessage(guess,phone_number):

    global guess_num
    
    found_number_index = -1
    for i in range(0,len(phone_number_list)):
        if phone_number == phone_number_list[i]:
            found_number_index=i
            print("Found Player: "+phone_number)
            break
    if found_number_index==-1:
        addPlayer(phone_number)
        found_number_index = len(phone_number_list)-1
        print("Created New Player: "+phone_number)
     
    CheckInput(guess,player_list[found_number_index])
    
    for i in range(0,len(guess)):
        player_list[found_number_index].output_matrix[player_list[found_number_index].guess_num][i] = guess[i]

    #for i in range(0,5):
    #    player_list[found_number_index].output_matrix[player_list[found_number_index].guess_num][i] = guess[i]

    #info_string=""
    #for i in range(0,5):
    #    r_num = random.randint(0, 10)
    #    if r_num<3:
    #        player_list[found_number_index].info_matrix[player_list[found_number_index].guess_num][i] = '✅'
    #    elif r_num<7:
    #        player_list[found_number_index].info_matrix[player_list[found_number_index].guess_num][i] = '👍'
    #    else:
    #        player_list[found_number_index].info_matrix[player_list[found_number_index].guess_num][i] = '❌'

    # This is needed to prevent the Twilio Free Trial from fucking it up
    intro = ".\n"

    # Send string is what is passed to twilio
    send_string = intro

    # Which line are we currently working on
    index=0
    # Loop through both matrices, both info(checks and thumbs up) and and letters
    for line in player_list[found_number_index].output_matrix:

        # Only display rightness information on lines that have guesses done already
        # this just adds data from info_matrix to a string with spaces
        if player_list[found_number_index].guess_num>=index:
            for digit in range(0,5):
                send_string = send_string + player_list[found_number_index].info_matrix[index][digit] + ' '
            send_string += '\n'

        # Adds some extra spaces at the beginning
        send_string += " "
        for character in line:
            send_string = send_string + character + "    "
        send_string = send_string + '\n'
        index+=1

    player_list[found_number_index].guess_num += 1
    #message = client.messages.create(  messaging_service_sid='MG3d88d073ce764188540241341785e4af', body=send_string,      to='+19375104157' )
    
    # Complete Hack due to poor planning
    if player_list[found_number_index].current_word.upper() == guess.upper() or player_list[found_number_index].guess_num>4:
        if player_list[found_number_index].guess_num>4:
            # Lose Here
            send_string += "\nYou Lose!"
            player_list[found_number_index].guess_num += 1
        else:
            # Win Here
            send_string += "\nYou Win!"
        
        #new_result = Result(int(player_list[found_number_index].phone_number[1:]),player_list[found_number_index].guess_num)
        #Send Data to the DB
        mod_db(int(player_list[found_number_index].phone_number[1:]),player_list[found_number_index].guess_num)

        
        ret_val = display_info(player_list[found_number_index].phone_number[1:])
        send_string = send_string + "\n" + str(ret_val)

        player_list[found_number_index].current_word = playwords[random.randint(0,len(playwords)-1)]
        player_list[found_number_index].guess_num = 0
        player_list[found_number_index].info_matrix = [
                                                        ['=','=','=','=','='],
                                                        ['=','=','=','=','='],
                                                        ['=','=','=','=','='],
                                                        ['=','=','=','=','='],
                                                        ['=','=','=','=','=']
                                                      ]
        player_list[found_number_index].output_matrix = [
                                                        ['_','_','_','_','_'],
                                                        ['_','_','_','_','_'],
                                                        ['_','_','_','_','_'],
                                                        ['_','_','_','_','_'],
                                                        ['_','_','_','_','_']
                                                        ]


    return send_string


@dataclass
class RPG_player:
    x : int
    y : int
    img_index : int

rpg_phone_number_list = []
rpg_player_list = []


def add_rpg_player(phone_num):
    x = random.randint(2,17)
    y = random.randint(2,17)
    img_index = hash(phone_num[1:])%11
    new_player = RPG_player(x,y,img_index)
    rpg_player_list.append(new_player)
    rpg_phone_number_list.append(phone_num)

def gen_board():
    pygame.init()
    canvas = pygame.Surface(SIZE)
    canvas.fill(GRAY)

    canvas.blit(grid_image,(0,0))
    
    # Backdrop
    for y in range(0,20):
        for x in range(0,20):
            color_index = board[y][x]
            if color_index==0:
                grass_index = hash(hash(x)-hash(y)+hash(x*x)-hash(x*y))%18
                canvas.blit(grass_tiles[grass_index], ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))
            else:
                floor_index = hash(hash(y)-hash(x)+hash(y*y-x)-hash(x*y))%7
                canvas.blit(floor_tiles[floor_index], ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))

    # Objects
    for y in range(0,20):
        for x in range(0,20):
            tile_index = obj_board[y][x]
            if tile_index==0:
                pass
            elif tile_index==1:
                tall_grass_index = hash(hash(y)-hash(x)+hash(y*y-x)-hash(x*y))%4
                canvas.blit(tall_grass_tiles[tall_grass_index], ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))
            elif tile_index==30:
                canvas.blit(b_wall, ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))
            elif tile_index==31:
                canvas.blit(b_door, ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))
            elif tile_index==32:
                canvas.blit(b_roof, ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))
            elif tile_index==33:
                canvas.blit(b_roof_edge, ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))
            elif tile_index==34:
                canvas.blit(b_chiminey, ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))


    # Draw Players
    for player in rpg_player_list:
        canvas.blit(player_tiles[player.img_index],((player.x+1)*BLOCK_SIZE,(player.y+1)*BLOCK_SIZE))

    try:
        os.system("rm images/img.jpg")
    except:
        print("image rm failed")
    canvas = pygame.transform.scale(canvas,(SCREEN_WIDTH*2,SCREEN_HEIGHT*2))
    pygame.image.save_extended(canvas,"images/img.jpg")
    pygame.quit()

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    
    mode="rpg"

    global guess_num
    #print("Received")
    data = request.form.to_dict(flat=False)

    #print(data)

    body = data['Body'][0].upper()
    from_num = data["From"][0]
    
    # Start out TwiML response
    resp = MessagingResponse()

    if mode=="wordle":
        if body=="show-stats":
            send_msg = ".\n"+get_stats()
        if len(body)==5:
            send_msg = genMessage(body,from_num)
            print(send_msg)
        else:
            send_msg = ".\nGuess Must be 5 Letters."
        # Add a message
        resp.message(send_msg)
    elif mode=="rpg":
        rpg_found_number_index = -1
        for i in range(0,len(rpg_phone_number_list)):
            if rpg_phone_number_list[i]==from_num:
                rpg_found_number_index = i
                break
        if rpg_found_number_index==-1:
            add_rpg_player(from_num)
            rpg_found_number_index = len(rpg_phone_number_list)-1

        if "move".upper() in body.upper():
            parsed = body.split(" ")
            movx = parsed[1].upper()
            movy = int(parsed[2])
            
            movx_num=0
            if movx=='A':
	            movx_num=1
            elif movx=='B':
	            movx_num=2
            elif movx=='C':
	            movx_num=3
            elif movx=='D':
	            movx_num=4
            elif movx=='E':
	            movx_num=5
            elif movx=='F':
	            movx_num=6
            elif movx=='G':
	            movx_num=7
            elif movx=='H':
	            movx_num=8
            elif movx=='I':
	            movx_num=9
            elif movx=='J':
	            movx_num=10
            elif movx=='K':
	            movx_num=11
            elif movx=='L':
	            movx_num=12
            elif movx=='M':
	            movx_num=13
            elif movx=='N':
	            movx_num=14
            elif movx=='O':
	            movx_num=15
            elif movx=='P':
	            movx_num=16
            elif movx=='Q':
	            movx_num=17
            elif movx=='R':
	            movx_num=18
            elif movx=='S':
	            movx_num=19
            elif movx=='T':
	            movx_num=20

            rpg_player_list[rpg_found_number_index].x=movx_num
            rpg_player_list[rpg_found_number_index].y=movy

        gen_board()
        # Run python http server in images folder, hti control-z to suspend
        # type bg to run last suspended task in background
        message = client.messages.create(body="hello",media_url=['http://3.16.1.25:8000/img.jpg'],to=from_num,from_="19894478157")

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
