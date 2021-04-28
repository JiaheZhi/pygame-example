import game_functions as gf


class GameStats():
    """ 跟踪游戏的统计信息 """

    def __init__(self, ai_settings):
        """ 初始化统计信息 """
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动时处于活动状态
        self.game_active = False
        # 最高得分
        self.highest_score = 0
        self.read_highest_score()

    def reset_stats(self):
        """ 初始化在游戏运行期间可能变化的统计信息 """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def read_highest_score(self):
        """ 把历史最高得分中文件中读出 """
        with open("data.txt", 'r+') as file_object:
            content = file_object.read().strip()
            self.highest_score = int(content[14:])