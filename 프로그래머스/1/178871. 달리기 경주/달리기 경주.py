# def solution(players, callings):
#     for i in callings:
#         p_index = players.index(i)
#         players.remove(i)
#         players.insert(p_index-1, i)
        

#     return players
# input이 커지면 시간 초과 발생

# def solution(players, callings):
#     rank = {player: idx + 1 for idx, player in enumerate(players)}
    
#     for calling in callings:
#         current_rank = rank[calling]
        
#         for player, value in rank.items():
#             if value == current_rank - 1:
#                 rank[player] = value + 1
#             elif value == current_rank: 
#                 rank[player] = value - 1
    
#     sorted_players = sorted(rank, key=lambda x: rank[x])
    
#     return sorted_players
# 시간 초과 발생
def solution(players, callings):
    player_indices = {player: idx for idx, player in enumerate(players)}

    for calling in callings:
        current_idx = player_indices[calling]
        prev_idx = current_idx - 1

        # 현재 인덱스와 이전 인덱스를 Swap
        players[current_idx], players[prev_idx] = players[prev_idx], players[current_idx]
        player_indices[players[current_idx]], player_indices[players[prev_idx]] = player_indices[players[prev_idx]], player_indices[players[current_idx]]

    return players
        