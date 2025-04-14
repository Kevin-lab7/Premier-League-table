import json
import requests
import pandas as pd
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
}
url="https://webapi.sporttery.cn/gateway/uniform/football/league/getTablesV2.qry?seasonId=11817&uniformLeagueId=72"
response=requests.get(url,headers=headers)
# 原始数据（包含多个球队信息）
def crawl_data():
    a=json.loads(response.text)
    return a
data=crawl_data()
def exact_team_data1(data):
    teams=[]
    for away_table in data['value']['awayTables']:
        for group in away_table['groups']:
            teams.extend(group['tables'])
    return teams
def exact_team_data2(data):
    teams=[]
    for away_table in data['value']['totalTables']:
        for group in away_table['groups']:
            teams.extend(group['tables'])
    return teams
def exact_team_data3(data):
    teams=[]
    for away_table in data['value']['homeTables']:
        for group in away_table['groups']:
            teams.extend(group['tables'])
    return teams
all_teams1=exact_team_data1(data)
all_teams2=exact_team_data2(data)
all_teams3=exact_team_data3(data)
# 创建DataFrame
df = pd.DataFrame(all_teams1)
da = pd.DataFrame(all_teams2)
db = pd.DataFrame(all_teams3)
# 按需调整列顺序（可选）
columns_order = [
    'ranking', 'abbCnName','totalLegCnt',
    'winGoalMatchCnt', 'drawMatchCnt', 'lossGoalMatchCnt',
    'goalCnt', 'lossGoalCnt', 'netGoal',
    'winProbability', 'points','phaseName'
]
df = df[columns_order]
da = da[columns_order]
db = db[columns_order]
# 重命名中文列名（可选）
df = df.rename(columns={
    'ranking':'排名',
    'abbCnName': '球队',
    'totalLegCnt':'场次',
    'points': '积分',
    'winGoalMatchCnt': '胜场',
    'drawMatchCnt': '平局',
    'lossGoalMatchCnt': '负场',
    'goalCnt': '进球',
    'lossGoalCnt': '失球',
    'netGoal': '净胜球',
    'winProbability': '胜率',
    'phaseName': '阶段'
})
da = da.rename(columns={
    'ranking':'排名',
    'abbCnName': '球队',
    'totalLegCnt':'场次',
    'points': '积分',
    'winGoalMatchCnt': '胜场',
    'drawMatchCnt': '平局',
    'lossGoalMatchCnt': '负场',
    'goalCnt': '进球',
    'lossGoalCnt': '失球',
    'netGoal': '净胜球',
    'winProbability': '胜率',
    'phaseName': '阶段'
})
db = db.rename(columns={
    'ranking':'排名',
    'abbCnName': '球队',
    'totalLegCnt':'场次',
    'points': '积分',
    'winGoalMatchCnt': '胜场',
    'drawMatchCnt': '平局',
    'lossGoalMatchCnt': '负场',
    'goalCnt': '进球',
    'lossGoalCnt': '失球',
    'netGoal': '净胜球',
    'winProbability': '胜率',
    'phaseName': '阶段'
})
# 保存为CSV文件
df.to_csv('英超积分榜（客场）.csv', index=False, encoding='utf-8-sig')
da.to_csv('英超积分榜（主客场）.csv', index=False, encoding='utf-8-sig')
db.to_csv('英超积分榜（主场）.csv', index=False, encoding='utf-8-sig')