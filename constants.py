# CONSTANTES PARA A AERONAVE C-95

#POSIÇÃO DOS INSTRUMENTOS DE VOO
SPEED = [306, 339, 69, 137]
ALT =   [310, 338, 780, 872]

#LISTA DOS INSTRUMENTOS DE VOO
inst_voo = {'SPEED': SPEED, 'ALT': ALT}

#POSIÇÃO DOS INSTRUMENTOS DO MOTOR
FUEL_L =       [73, 100, 1009, 1092]
FUEL_R =       [73, 100, 1306, 1389]
T5_L =         [131, 157, 1015, 1096]
T5_R =         [131, 157, 1298, 1377]
TRQ_L =        [271, 297, 1015, 1096]
TRQ_R =        [271, 297, 1298, 1377]
NH_L =         [411, 437, 1015, 1099]
NH_R =         [411, 437, 1298, 1380]
NG_L =         [553, 579, 1015, 1099]
NG_R =         [553, 579, 1298, 1383]
OIL_TEMP_L =   [697, 723, 1015, 1093]
OIL_TEMP_R =   [697, 723, 1307, 1389]
OIL_PRESS_L =  [739, 765, 1015, 1093]
OIL_PRESS_R =  [739, 765, 1307, 1389]
HYD_PRESS_L =  [838, 864, 1015, 1093]
HYD_PRESS_R =  [838, 864, 1307, 1389]
FF_L =         [954, 980, 1015, 1093]
FF_R =         [954, 980, 1307, 1389]
FUEL_PRESS_L = [997, 1026, 1015, 1093]
FUEL_PRESS_R = [997, 1025, 1307, 1389]

#LISTA DOS INSTRUMENTOS DO MOTOR
inst_motor_c95 = {'SPEED': SPEED, 'ALT': ALT,
              'FUEL_L':FUEL_L, 'FUEL_R': FUEL_R,
              'T5_L':T5_L, 'T5_R':T5_R,
              'TRQ_L': TRQ_L, 'TRQ_R': TRQ_R,
              'NH_L': NH_L, 'NH_R': NH_R,
              'NG_L': NG_L, 'NG_R': NG_R,
              'OIL_TEMP_L': OIL_TEMP_L, 'OIL_TEMP_R': OIL_TEMP_R,
              'OIL_PRESS_L': OIL_PRESS_L, 'OIL_PRESS_R': OIL_PRESS_R,
              'HYD_PRESS_L': HYD_PRESS_L, 'HYD_PRESS_R': HYD_PRESS_R,
              'FF_L': FF_L, 'FF_R': FF_R,
              'FUEL_PRESS_L': FUEL_PRESS_L, 'FUEL_PRESS_R': FUEL_PRESS_R
              }

scale = {"SPEED"       : 1,  #velocidade max = VMO =230
        "VS"            : 10,
        "ALT"           : 10, # ALT max 14000 voos sem oxigênio
        "FUEL_L"        : 10,   "FUEL_R"        : 10,
        "TRQ_L"         : 10,   "TRQ_R"         : 10,
        "NH_L"          : 0.5,  "NH_R"          : 0.5,
        "NG_L"          : 0.5,  "NG_R"          : 0.5,
        "T5_L"          : 10,   "T5_R"          : 10,
        "OIL_TEMP_L"    : 1,    "OIL_TEMP_R"    : 1,
        "OIL_PRESS_L"   : 1,    "OIL_PRESS_R"   : 1,
        "HYD_PRESS_L"   : 100,  "HYD_PRESS_R"   : 100,
        "BRAKE_PRESS_L" : 10,   "BRAKE_PRESS_R" : 10,
        "FF_L"          : 10,   "FF_R"          : 10,
        "FUEL_PRESS_L"  : 1,    "FUEL_PRESS_R"  : 1,
        "T2_L"          : 1,
        "OAT"           : 1,
        "FOB"           : 10,
        "TOT"           : 10}



# VALORES RETIRADOS DO MANUAL
limits = {"SPEED_MIN"       : 41,    "SPEED_MAX"       : 250,  #velocidade max = VMO =230
          "VS_MIN"          : 300,   "VS_MAX"          : 4000, 
          "ALT_MIN"         : -2000, "ALT_MAX"         : 14000, # ALT max 14000 voos sem oxigênio
          "FUEL_MIN"        : 0,     "FUEL_MAX"        : 1650,  
          "TRQ_MIN"         : 0,     "TRQ_MAX"         : 2200, 
          "NH_MIN"          : 0,     "NH_MAX"          : 120, 
          "NG_MIN"          : 0,     "NG_MAX"          : 120,   
          "T5_MIN"          : 0,     "T5_MAX"          : 1200,  
          "OIL_TEMP_MIN"    : -10,   "OIL_TEMP_MAX"    : 150,   
          "OIL_PRESS_MIN"   : 0,     "OIL_PRESS_MAX"   : 130,   
          "T2_MIN"          : -70 ,  "T2_MAX"          : 80,    
          "HYD_PRESS_MIN"   : 0,     "HYD_PRESS_MAX"   : 5000,  
          "BRAKE_PRESS_MIN" : 0,     "BRAKE_PRESS_MAX" : 5000,  
          "FF_MIN"          : 0,     "FF_MAX"          : 500,  
          "FUEL_PRESS_MIN"  : 0,     "FUEL_PRESS_MAX"  : 50,   
          "OAT_MIN"         : -40,   "OAT_MAX"         : 70,   
          "FOB_MIN"         : 0,     "FOB_MAX"         : 3500, 
          "TOT_MIN"         : 0,     "TOT_MAX"         : 3500}

valores_iniciais = {"SPEED"       : None,   
                    "VS"          : 0,
                    "ALT"         : 2060,  
                    "FUEL_L"      : 1350,   "FUEL_R"      : 1340,
                    "TRQ_L"       : 200,    "TRQ_R"       : 200,
                    "NH_L"        : 56.0,   "NH_R"        : 59.0,
                    "NG_L"        : 63.0,   "NG_R"        : 64.5,
                    "T5_L"        : 520,    "T5_R"        : 540,
                    "OIL_TEMP_L"  : 58,     "OIL_TEMP_R"  : 65, 
                    "OIL_PRESS_L" : 98,     "OIL_PRESS_R" : 94,
                    "HYD_PRESS_L" : 3000,   "HYD_PRESS_R" : 3100, 
                    "FF_L"        : 120,    "FF_R"        : 130,
                    "FUEL_PRESS_L": 22,     "FUEL_PRESS_R": 22,
                    "OAT"         : 23,
                    "FOB"         : 2660,  
                    "TOT"         : 40}


#FAIXAS
TRQ = [(0,400),(400,1970),(1970,2200)]
NH  = [(0,81),(81,100),(100,120)]
NG  = [(0,50),(50,101.5),(101.5,120)]
T5  = [(0,400),(400,740),(740,790),(790,1200)]

#ANGLE

W = 112
G = 189
R = 213

TRQ_W = (TRQ[0][1]-TRQ[0][0])/W
TRQ_G = (TRQ[1][1]-TRQ[1][0])/(G-W)
TRQ_R = (TRQ[2][1]-TRQ[2][0])/(R-G)

NH_W = (NH[0][1]-NH[0][0])/W
NH_G = (NH[1][1]-NH[1][0])/(G-W)
NH_R = (NH[2][1]-NH[2][0])/(R-G)

NG_W = (NG[0][1]-NG[0][0])/W
NG_G = (NG[1][1]-NG[1][0])/(G-W)
NG_R = (NG[2][1]-NG[2][0])/(R-G)


T5_W = (T5[0][1]-T5[0][0])/W
T5_G = (T5[1][1]-T5[1][0])/(G-W)
T5_R = (T5[2][1]-T5[2][0])/(R-G)



T5_L1   = [150,238,1010,1098]
T5_R1   = [150,238,1293,1381]

TRQ_L1  = [291,379,1010,1098]
TRQ_R1  = [291,379,1293,1381]

NH_L1   = [432,520,1010,1098]
NH_R1   = [432,520,1293,1381]

NG_L1   = [573,661,1010,1098]
NG_R1   = [573,661,1293,1381]

faixas = {"TRQ": TRQ, "NH" : NH, "NG" : NG, "T5" : T5}

angles = [W, G, R]

fator_de_conversão = {"TRQ": [TRQ_W, TRQ_G, TRQ_R],
                      "NH" : [NH_W, NH_G, NH_R],
                      "NG" : [NG_W, NG_G,NG_R],
                      "T5" : [T5_W, T5_G,T5_R]}

analog_inst = { "T5_L" : T5_L1,  "T5_R" : T5_R1,
                "TRQ_L": TRQ_L1, "TRQ_R": TRQ_R1,
                "NH_L" : NH_L1,  "NH_R" : NH_R1,
                "NG_L" : NG_L1,  "NG_R" : NG_R1,
               }

#################################################################################
#                                                                               #
#                               T27                                             #
#                                                                               #
#################################################################################

TRQ_1 = [336,356,1145,1197]
NG_1 = [427,447,1145,1197]
NH_1 = [515,535,1145,1197]
T5_1 = [608,628,1145,1197]
FF_1 = [642,663,1218,1262]
OIL_TEMP_1 = [705,724,1218,1262]
OIL_PRESS_1 = [760,781,1218,1262]

TRQ_2 = [767,789,1488,1542]
NG_2 = [817,839,1501,1560]
NH_2 = [856,879,1501,1560]
T5_2 = [767,789,1628,1690]
FF_2 = [856,879,1648,1703]
OIL_PRESS_2 = [817,839,1648,1703]

inst_motor_T27 = {
                'NG_1': NG_1, 'NG_2': NG_2,
                'NH_1': NH_1, 'NH_2' : NH_2,
                'T5_1' : T5_1, 'T5_2' : T5_2,
                'TRQ_1' : TRQ_1,  'TRQ_2' : TRQ_2,
                'OIL_PRESS_1' : OIL_PRESS_1, 'OIL_PRESS_2' : OIL_PRESS_2,
                'OIL_TEMP_1' : OIL_TEMP_1, 
                'FF_1' : FF_1, 'FF_2' : FF_2,
              }



#################################################################################
#                                                                               #
#                               C105                                            #
#                                                                               #
#################################################################################

TRQ_L = [[339,878],[371,886],[389,789],[358,781]]
TRQ_R = [[358,781],[389,789],[411,696],[378,693]]
ITT_L = [[382,677],[413,682],[437,595],[405,595]]
ITT_R = [[405,595],[437,595],[465,506],[434,504]]
NP_L  = [[437,496],[465,496],[489,428],[460,427]]
NP_R  = [[460,427],[489,428],[514,363],[487,365]]
NH_L  = [[489,357],[516,358],[537,300],[513,300]]
NH_R  = [[513,300],[537,300],[564,245],[536,245]]
OIL_PRESS_L = [[1437,914],[1481,905],[1472,832],[1426,840]]
OIL_PRESS_R = [[1382,606],[1423,604],[1411,547],[1372,547]]
OIL_TEMP_L = [[1410,740],[1453,735],[1442,670],[1397,670]]
OIL_TEMP_R = [[1347,468],[1388,470],[1373,422],[1335,423]]

inst_motor_C105 = {
                    "TRQ_L" : TRQ_L, "TRQ_R" : TRQ_R,
                    "ITT_L" : ITT_L, "ITT_R" : ITT_R,
                    "NP_L"  : NP_L , "NP_R"  : NP_R ,
                    "NH_L"  : NH_L , "NH_R"  : NH_R ,
                    "OIL_PRESS_L":OIL_PRESS_L, "OIL_PRESS_R":OIL_PRESS_R,
                    "OIL_TEMP_L":OIL_TEMP_L, "OIL_TEMP_R":OIL_TEMP_R
              }

#################################################################################
#                                                                               #
#                               F5                                            #
#                                                                               #
#################################################################################

HZ = [158,316,428,648]
HZ_POS2 = [265,409,69,273]
tri = [75,87,8,13]
F5_pitch_escala = 10
F5_dist_pitch_escala = 45

NORMAL_POS = 1
DORSO_IN = 2
DORSO_OUT = 3
NORMAL_NEG = 4