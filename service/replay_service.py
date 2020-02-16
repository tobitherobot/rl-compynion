from module.replay_classes import *


# def insert_replay(Replay):

# GUIDE:
# Team1Score : Team 1 Goals (int)
# MatchType : Online | Offline (string)
# TODO create guide


# TODO gather all important information on players and game events
def index_replay(replay):
    contents = replay['header']['body']['properties']['value']
    player_stats = get_value(contents['PlayerStats'])
    players = get_all_players(replay['content']['body']['frames'][0], player_stats)
    # print_scoreboard(players)
    data = {'label': replay['header']['body']['label'],
            'team1score': 0, 'team2score': 0,
            'match_type': get_value(contents['MatchType']),
            'map_name': get_value(contents['MapName']),
            'date': get_value(contents['Date']),
            'replay_id': get_value(contents['Id']),
            'team_size': get_value(contents['TeamSize']),
            'frames_count': get_value(contents['NumFrames']),
            'record_fps': get_value(contents['RecordFPS'])}
    if 'Team1Score' in contents:
        team1_score = get_value(contents['Team1Score'])
    if 'Team2Score' in contents:
        team2_score = get_value(contents['Team2Score'])
    goals = contents['Goals']  # TODO goal information


# TODO meant to gather information by iterating through each frame in the replay
def analyze_frames(replay):
    frames = replay['content']['body']['frames']
    players = get_actors(frames[0])
    for i in range(1, len(frames)):
        for actor in frames[i]['replications']:
            actor_id = actor['actor_id']['value']
            if actor_id in [p.get_actor_id() for p in players]:
                print(i, actor_id, actor, actor_id, i)
    return players


# provide first frame of a replay to gather actor_id of players
# TODO get last frame for end of game stats
def get_actors(frame_zero):
    players = []
    for actor in frame_zero['replications']:
        name = ''
        online_id = ''
        if 'updated' in actor['value']:
            for u in actor['value']['updated']:
                value = u['value']
                if u['name'] == 'Engine.PlayerReplicationInfo:PlayerName':
                    name = value['string']
                elif u['name'] == 'Engine.PlayerReplicationInfo:UniqueId':
                    online_id = value['unique_id']['remote_id']['steam']
        if online_id != '':
            players.append(Player(actor['actor_id']['value'], name, online_id))
    return players


# provide first frame and the PlayerStats data from header to return Player Objects for each player in the game
def get_all_players(frame0, player_stats):
    players = get_actors(frame0)
    for player in players:
        for data in player_stats:
            data = data['value']
            if get_value(data['OnlineID']) == player.get_online_id():
                player.set_team(get_value(data['Team']))
                player.set_platform(get_value(data['Platform']))
                stats = ['Score', 'Goals', 'Saves', 'Shots']
                for stat in stats:
                    exec('player.set_' + stat.lower() + '(' + (str(get_value(data[stat])) if stat in data.keys() else 0) + ')')
                break
    return players


# provide any field from the header section of a replay to get its value
def get_value(attribute):
    value = attribute['value']
    if 'str' in value:
        return value['str']
    if 'int' in value:
        return value['int']
    if 'float' in value:
        return value['float']
    if 'array' in value:
        return value['array']
    if 'name' in value:
        return value['name']
    if 'q_word' in value:
        return value['q_word']
    if 'byte' in value:
        return value['byte'][1]


def print_scoreboard(players):
    team1 = sorted([player for player in players if player.get_team() == 1], key = lambda pl: pl.get_score())
    team2 = sorted([player for player in players if player.get_team() == 0], key = lambda pl: pl.get_score())
    print('TEAM 1')
    print('PLAYER                     SCR  G  A  S  S')
    for p in team1:
        print(str(p))
    print('\nTEAM 2')
    print('PLAYER                     SCR  G  A  S  S')
    for p in team2:
        print(str(p))
