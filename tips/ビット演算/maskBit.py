BIT_FLAG_DAMAGE = 1<<0 
BIT_FLAG_DOKU = 1<<1
BIT_FLAG_MAHI = 1<<2
BIT_FLAG_SENTOFUNO = 1<<3

# atackしてダメージを受ける
MASK_ATTACK = BIT_FLAG_DAMAGE
# punchしてダメージをうっけて、麻痺にもなる
MASK_PUNCH = BIT_FLAG_DAMAGE | BIT_FLAG_MAHI
# defeatして相手のhPを0にする
MASK_DEFEAT = BIT_FLAG_DAMAGE | BIT_FLAG_SENTOFUNO
#「毒」と「麻痺」を回復させる: ~MASK_DOKU_MAHI をかけることで回復
MASK_DOKU_MAHI = BIT_FLAG_DOKU | BIT_FLAG_MAHI

if __name__=='__main__':
    status = 0
    print('Start', status)

    #  attacked: 0001 になる
    status |= MASK_ATTACK
    print("attacked", bin(status))

    # punched  0101になる
    status |= MASK_PUNCH
    print("punched", bin(status))

    # 「毒」または「麻痺」かどうかを判定する
    if (status & MASK_DOKU_MAHI):
        print("You are doku or mahi.")
        
    status &= ~MASK_DOKU_MAHI
    print("kaihuk", bin(status))

    status |= MASK_DEFEAT
    print('戦闘不能', bin(status))
    
    status &= ~MASK_DOKU_MAHI
    print("戦闘不能のまま", bin(status))


