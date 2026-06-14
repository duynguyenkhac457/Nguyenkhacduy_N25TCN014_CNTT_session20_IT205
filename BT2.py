data = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]


def is_number(value):
    return isinstance(value, int)


def calculate_bonus(matches, mmr):
    return (matches * 10) + (mmr * 0.5)


def show_rp_bonus(players):
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for player in players:
        if len(player) != 3:
            print(f"Tuyển thủ {player[0]}: Lỗi dữ liệu thiếu thông tin!")
            continue

        name, matches, mmr = player

        if not is_number(matches) or not is_number(mmr):
            print(f"Tuyển thủ {name}: Lỗi dữ liệu không hợp lệ!")
            continue

        bonus = calculate_bonus(matches, mmr)
        print(f"Tuyển thủ {name} nhận được {bonus} RP")

    print("--- HOÀN TẤT ---")


show_rp_bonus(data)