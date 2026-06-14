data = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5")
]


def parse_int(value):
    if value.isdigit():
        return int(value)
    return None


def calculate_kda(kills, deaths, assists):
    if deaths == 0:
        return "perfect"
    return (kills + assists) / deaths


def show_kda_ranking(players):
    print("--- BẢNG XẾP HẠNG KDA ---")

    for name, kills, deaths, assists in players:
        kills = parse_int(kills)
        deaths = parse_int(deaths)
        assists = parse_int(assists)

        if kills is None or deaths is None or assists is None:
            print(f"Tuyển thủ {name}: Lỗi dữ liệu không hợp lệ!")
            continue

        kda = calculate_kda(kills, deaths, assists)

        if kda == "perfect":
            print(f"Tuyển thủ {name}: KDA Hoàn hảo (Perfect Game)!")
        else:
            print(f"Tuyển thủ {name} có chỉ số KDA là: {kda}")

    print("--- HOÀN TẤT ---")


show_kda_ranking(data)