import service.database_service as dbs
import service.replay_service as rs
import service.file_service as fs

replay = fs.load_json('fileJson')
rs.index_replay(replay)
print([p for p in rs.analyze_frames(replay)])

# json = fs.decompile('twoGoalsWin')
# print(json)

# dbs.cursor.execute("SELECT * FROM game")
# print(dbs.cursor.fetchone())
