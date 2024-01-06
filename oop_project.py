#Variables
PG_PPG = 11.8
PG_AST = 4.3
PG_REB = 3
PG_STL = 0.9
PG_BLK = 0.3
PG_TOS = 1.6
PG_FGP = 44.6
PG_FTP = 81.5
PG_TPP = 35.7

SG_PPG = 11.5
SG_AST = 2.5
SG_REB = 3
SG_STL = 0.7
SG_BLK = 0.3
SG_TOS = 1.3
SG_FGP = 45
SG_FTP = 81.2
SG_TPP = 37

SF_PPG = 11.1 
SF_AST = 2
SF_REB = 4
SF_STL = 0.7
SF_BLK = 0.4
SF_TOS = 1.2
SF_FGP = 46.1
SF_FTP = 80.6
SF_TPP = 36

PF_PPG = 9.9
PF_AST = 1.7
PF_REB = 4.9
PF_STL = 0.6
PF_BLK = 0.5
PF_TOS = 1.1
PF_FGP = 49.6
PF_FTP = 74.1
PF_TPP = 35.1

C_PPG = 9.9
C_AST = 1.6
C_REB = 6.4
C_STL = 0.5
C_BLK = 0.9
C_TOS = 1.2
C_FGP = 57.4
C_FTP = 71.5
C_TPP = 34.8

class Player():
        def __init__(self, first, last, ppg, ast, reb, stl, blk, tos, fgp, ftp, tpp):
            self.first = first
            self.last = last
            self.ppg = ppg
            self.ast = ast
            self.reb = reb
            self.stl = stl
            self.blk = blk
            self.tos = tos
            self.fgp = fgp
            self.ftp = ftp
            self.tpp = tpp
        
        def full_name(self):
             return '{} {}'.format(self.first, self.last)

class PointGuard(Player):
    # overall score calculation using point guard average stats from the 2023 NBA SEASON
    def ovr_score(self):
        ppg_scr = self.ppg / PG_PPG
        ast_scr = self.ast / PG_AST
        reb_scr = self.reb / PG_REB
        stl_scr = self.stl / PG_STL
        blk_scr = self.blk / PG_BLK
        tos_scr = self.tos / PG_TOS
        fgp_scr = self.fgp / PG_FGP
        ftp_scr = self.ftp / PG_FTP
        tpp_scr = self.tpp / PG_TPP
        ovr_scr = (ppg_scr + ast_scr + reb_scr + stl_scr + blk_scr + fgp_scr + ftp_scr + tpp_scr) - tos_scr
        return ovr_scr

class ShootingGuard(Player):
    def ovr_score(self):
        ppg_scr = self.ppg / SG_PPG
        ast_scr = self.ast / PG_AST
        reb_scr = self.reb / PG_REB
        stl_scr = self.stl / PG_STL
        blk_scr = self.blk / PG_BLK
        tos_scr = self.blk / PG_TOS
        fgp_scr = self.fgp / PG_FGP
        ftp_scr = self.ftp / PG_FTP
        tpp_scr = self.tpp / PG_TPP
        ovr_scr = ppg_scr + ast_scr + reb_scr + stl_scr + blk_scr + fgp_scr + ftp_scr + tpp_scr - tos_scr
        return ovr_scr
    
class SmallForward(Player):
    def ovr_score(self):
        ppg_scr = self.ppg / SF_PPG
        ast_scr = self.ast / SF_AST
        reb_scr = self.reb / SF_REB
        stl_scr = self.stl / SF_STL
        blk_scr = self.blk / SF_BLK
        tos_scr = self.tos / SF_TOS
        fgp_scr = self.fgp / SF_FGP
        ftp_scr = self.ftp / SF_FTP
        tpp_scr = self.tpp / SF_TPP
        ovr_scr = ppg_scr + ast_scr + reb_scr + stl_scr + blk_scr + fgp_scr + ftp_scr + tpp_scr - tos_scr
        return ovr_scr

class PowerForward(Player):
    def ovr_score(self):
        ppg_scr = self.ppg / PF_PPG
        ast_scr = self.ast / PF_AST
        reb_scr = self.reb / PF_REB
        stl_scr = self.stl / PF_STL
        blk_scr = self.blk / PF_BLK
        tos_scr = self.tos / PF_TOS
        fgp_scr = self.fgp / PF_FGP
        ftp_scr = self.ftp / PF_FTP
        tpp_scr = self.tpp / PF_TPP
        ovr_scr = ppg_scr + ast_scr + reb_scr + stl_scr + blk_scr + fgp_scr + ftp_scr + tpp_scr - tos_scr
        return ovr_scr

class Center(Player):
    def ovr_score(self):
        ppg_scr = self.ppg / C_PPG
        ast_scr = self.ast / C_AST
        reb_scr = self.reb / C_REB
        stl_scr = self.stl / C_STL
        blk_scr = self.blk / C_BLK
        tos_scr = self.tos / C_TOS
        fgp_scr = self.fgp / C_FGP
        ftp_scr = self.ftp / C_FTP
        tpp_scr = self.tpp / C_TPP
        ovr_scr = ppg_scr + ast_scr + reb_scr + stl_scr + blk_scr + fgp_scr + ftp_scr + tpp_scr - tos_scr
        return ovr_scr
     
# player variables with positional arguments
player_1 = PointGuard('Tyrese', 'Haliburton', 24.6, 12.8, 4, 1.0, 0.6, 2.6, 50, 90, 41.6)
player_2 = ShootingGuard('Shai', 'Gilgeous-Alexander', 31.4, 6.3, 5.7, 2.7, 0.8, 2, 55, 91, 31)
player_3 = SmallForward('Jayson', 'Tatum', 27, 4.4, 8.4, 1.1, 0.5, 2.9, 47, 78, 34)
player_4 = PowerForward('Giannis', 'Antetokounmpo', 30.9, 5.5, 11.1, 1.3, 1.2, 3.7, 61, 67, 22)
player_5 = Center('Nikola', 'Jokic', 26.1, 9.2, 12.3, 1.2, 0.8, 2.7, 56, 82, 33)

p1_name = player_1.full_name()
p1_scr = str(player_1.ovr_score())

p2_name = player_2.full_name()
p2_scr = str(player_2.ovr_score())

p3_name = player_3.full_name()
p3_scr = str(player_3.ovr_score())

p4_name = player_4.full_name()
p4_scr = str(player_4.ovr_score())

p5_name = player_5.full_name()
p5_scr = str(player_5.ovr_score())

player_dict = {p1_name:p1_scr, p2_name:p2_scr, p3_name:p3_scr, p4_name:p4_scr, p5_name:p5_scr}

def main():
    print("Player Name | Program Score")
    for p, s in player_dict.items():
        print(p, s + "\n")

main()