import pandas as pd
import numpy as np

gs = pd.read_csv('goalscores.csv')
gs = gs.set_index('Player')
##gs = gs.dropna()


best = gs[['Goals','Minutes','Shots','Touches','Woodwork','Offsides','Dispossessions','BCM']]
best = best.groupby('Player').agg({'Goals':np.sum, 'Minutes':np.sum, 'Shots':np.sum,'Touches':np.sum,'Woodwork':np.sum,'Offsides':np.sum,'Dispossessions':np.sum,'BCM':np.sum})
best = best[(best[['Minutes']] >=  9000).all(axis=1)]
best['Shot Conversion'] = best['Goals']/best['Shots'] #higher=better
best['BCM per Shot'] = best['BCM']/best['Shots'] #lower=better
best['Mins per Shot'] = best['Minutes']/best['Shots'] #lower=better
best['Mins per Goal'] = best['Minutes']/best['Goals'] #lower=better
best['Touches per Min'] = best['Touches']/best['Minutes'] #higher=better
best['Touches per Goal'] = best['Touches']/best['Shots'] #lower=better
best['Touches per Offside'] = best['Touches']/best['Offsides'] #higher=better
best['Woodwork per Shots'] = best['Woodwork']/best['Shots'] #lower=better
best['Touches per Diss'] = best['Touches']/best['Dispossessions'] #higher=better
best['Goals to Offsides'] = best['Goals']/best['Offsides'] #higher=better
best['Goals to BCM'] = best['Goals']/best['BCM'] #higher=better
best = best.dropna()
    
SC_pts = pd.cut(best['Shot Conversion'],21,labels=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
BCMperS_pts = pd.cut(best['BCM per Shot'],21,labels=['20','19','18','17','16','15','14','13','12','11','10','9','8','7','6','5','4','3','2','1','0'])
MperG_pts = pd.cut(best['Mins per Goal'],21,labels=['20','19','18','17','16','15','14','13','12','11','10','9','8','7','6','5','4','3','2','1','0'])
MperS_pts = pd.cut(best['Mins per Shot'],21,labels=['20','19','18','17','16','15','14','13','12','11','10','9','8','7','6','5','4','3','2','1','0'])
TperM_pts = pd.cut(best['Touches per Min'],21,labels=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
TperG_pts = pd.cut(best['Touches per Goal'],21,labels=['20','19','18','17','16','15','14','13','12','11','10','9','8','7','6','5','4','3','2','1','0'])
TperO_pts = pd.cut(best['Touches per Offside'],21,labels=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])    
WperS_pts = pd.cut(best['Woodwork per Shots'],21,labels=['20','19','18','17','16','15','14','13','12','11','10','9','8','7','6','5','4','3','2','1','0'])       
TperD_pts = pd.cut(best['Touches per Diss'],21,labels=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
GtoO_pts = pd.cut(best['Goals to Offsides'],21,labels=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
GtoBCM_pts = pd.cut(best['Goals to BCM'],21,labels=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    
    
##print(best.index)
##print(SC_pts)
##print(MperG_pts)
##print(MperS_pts)
points = pd.DataFrame([SC_pts,BCMperS_pts,MperG_pts,MperS_pts,TperM_pts,TperG_pts,TperO_pts,WperS_pts,TperD_pts,GtoO_pts,GtoBCM_pts], index=['Shot Conversion','BCM per Shot','Mins per Goal','Mins per Shot','Touches per Min','Touches per Goal','Touches per Offside','Woodwork per Shots','Touches per Diss','Goals to Offsides','Goals to BCM'])
points = points.T
points['Shot Conversion'] = points['Shot Conversion'].apply(np.int64)
points['BCM per Shot'] = points['BCM per Shot'].apply(np.int64)
points['Mins per Goal'] = points['Mins per Goal'].apply(np.int64)
points['Mins per Shot'] = points['Mins per Shot'].apply(np.int64)
points['Touches per Min'] = points['Touches per Min'].apply(np.int64)
points['Touches per Goal'] = points['Touches per Goal'].apply(np.int64)
points['Touches per Offside'] = points['Touches per Offside'].apply(np.int64)
points['Woodwork per Shots'] = points['Woodwork per Shots'].apply(np.int64)
points['Touches per Diss'] = points['Touches per Diss'].apply(np.int64)
points['Goals to Offsides'] = points['Goals to Offsides'].apply(np.int64)
points['Goals to BCM'] = points['Goals to BCM'].apply(np.int64)
##print(points)
    
player_index = (points['Mins per Goal']+points['Mins per Shot']+points['Shot Conversion']+points['BCM per Shot']+points['Touches per Min']+points['Touches per Goal']+points['Touches per Offside']+points['Woodwork per Shots']+points['Touches per Diss']+points['Goals to Offsides']+points['Goals to BCM'])
player_index.iloc[:] = player_index.iloc[:]/player_index.max()
player_index = player_index.sort_values(ascending=False).round(3)


print('\nBest EPL forward in last 12 seasons:\n')
print(player_index.argmax())
print('\n\nFull list:\n')
print(player_index)
print('\n\nRankings limited to only attackers with +9000 minute EPL playtime since 06/07 season\n\n\n')
        
    

    
