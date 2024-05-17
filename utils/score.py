from datetime import datetime

class Score:
    def __init__(self, username, game_id="", points=0, stage_score=0):
        self.username = username
        self.game_id = game_id
        self.points = points
        self.stage_score = stage_score
    
    def update_score(self, points, stage_score):
        self.points += points
        self.stage_score += stage_score
    
    def set_game_id_date(self):
        self.game_id = datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
        return self.username, self.points, self.stage_score, self.game_id
