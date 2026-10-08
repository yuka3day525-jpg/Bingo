import random

B = random.sample(range(1, 16), 5)
I = random.sample(range(16, 31), 5)
N = random.sample(range(31, 46), 5)
G = random.sample(range(46, 61), 5)
O = random.sample(range(61, 76), 5)
N[2] = "FREE"  # 真ん中をFREEにする
card = [list(row) for row in zip(B, I, N, G, O)] 

for row in card:
    for num in row:
        if num == "FREE":
            print("FREE", end=" ")
        else:
            print(f"{num:02d}", end="  ")
    print()

ball = random.sample(range(1, 76), 75)

def judge(card):
    reach = 0
    bingo = 0

    lines = [] 

    # 横5列
    for row in card:
        lines.append(row)

    # 縦5列
    for i in range(5):
        lines.append([card[j][i] for j in range(5)])
        # card[0][0]  # 1行目・1列目 → "@03"
        # card[1][0]  # 2行目・1列目 → 5
        # card[2][0]  # 3行目・1列目 → 7

    # 斜め2列
    lines.append([card[i][i] for i in range(5)])
    lines.append([card[i][4-i] for i in range(5)])

    # 判定
    for line in lines:
        count = 0

        for n in line:
            if isinstance(n, str) or n == "FREE":
                # isinstance(n, str)nが文字列かどうかを判定する関数だよ。
                # isinstance("@03", str)  # True
                # isinstance(63, str)     # False
                count += 1

        if count == 5:
            bingo += 1
        elif count == 4:
            reach += 1

    return reach, bingo

with open("bingo.txt", "a", encoding="utf-8") as f:
    f.write("\n========== 新しいゲーム ==========\n")
    # for row in card:
    #     for n in row:
    #         if isinstance(n, int):
    #             f.write(f"{n:02d}   ")
    #         else:
    #             f.write(f"{n:<5}")
    #     f.write("\n")
    f.write("\nEnterキーで抽選することができます\n\n")

while ball:
    input("Enterキーで抽選")
    num = ball.pop()
    print(f"出た数字：{num}")

    for row in card:
        for i, n in enumerate(row):
            if n == num:
                row[i] = f"@{n:02d}"

            if row[i] == "FREE":
                print("FREE", end=" ")
            elif isinstance(row[i], str):
                print(row[i], end=" ")
            else:
                print(f"{row[i]:02d}", end="  ")
        print()

    reach, bingo = judge(card)

    print(f"REACH: {reach}")
    print(f"BINGO: {bingo}")

    with open("bingo.txt", "a", encoding="utf-8") as f:
        f.write(f"\n出た数字：{num}\n")
        for row in card:
            for n in row:
                if isinstance(n, int):
                    f.write(f"{n:02d}   ")
                else:
                    f.write(f"{n:<5}")
            f.write("\n")

        f.write(f"REACH: {reach}\n")
        f.write(f"BINGO: {bingo}\n")
        f.write("-" * 35 + "\n")
        if bingo == 12:
            f.write("\nすべてのマスが埋まりました\n")
            print("すべてのマスが埋まりました")
            break







