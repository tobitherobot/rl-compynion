import carball

json = carball.decompile_replay('C:/Users/Tobias/Documents/GitHub/py-rlstats/resources/twoGoalsWin.replay', 
                                output_path='C:/Users/Tobias/Documents/GitHub/py-rlstats/resources/fileJson.json', 
                                overwrite=True)

print(json)