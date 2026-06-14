import logging

logging.basicConfig(
    filename="roster_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)

roster = [
    {"player_id": "P01", "name": "Faker", "role": "Mid Lane", "salary": 5000.0, "status": "Active"},
    {"player_id": "P02", "name": "Oner", "role": "Jungle", "salary": 3500.0, "status": "Active"},
    {"player_id": "P03", "name": "Ruler", "role": "ADC", "salary": 6000.0, "status": "Benched"}
]


def display_roster(roster_list):
    if not roster_list:
        print("Đội hình hiện đang trống.")
        return

    print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")
    print("ID       | Tên tuyển thủ        | Vị trí          | Lương      | Trạng thái")
    print("-" * 80)

    for p in roster_list:
        name = p.get("name", "Unknown")
        status = p.get("status", "Unknown")

        match status:
            case "Benched":
                name = name + " [DỰ BỊ]"

        print(
            f"{p.get('player_id','N/A'):<8} | "
            f"{name:<20} | "
            f"{p.get('role','Unknown'):<15} | "
            f"{p.get('salary',0):<10} | "
            f"{status}"
        )

    logging.info("Coach viewed the team roster.")


def sign_player(roster_list):
    print("\n--- CHIÊU MỘ TUYỂN THỦ MỚI ---")
    player_id = input("Nhập mã tuyển thủ: ").strip().upper()

    for p in roster_list:
        if p["player_id"] == player_id:
            print(f"Lỗi: Mã tuyển thủ {player_id} đã tồn tại.")
            logging.warning(f"Failed to sign player - Duplicate player ID {player_id}")
            return

    name = input("Nhập tên tuyển thủ: ").strip()
    role = input("Nhập vị trí thi đấu: ").strip()

    while True:
        try:
            salary = float(input("Nhập mức lương hàng tháng: "))
            if salary <= 0:
                print("Lương phải là số dương.")
                continue
            break
        except ValueError:
            print("Lương phải là số.")
            logging.warning("Failed to sign player - Invalid salary input")

    roster_list.append({
        "player_id": player_id,
        "name": name,
        "role": role,
        "salary": salary,
        "status": "Active"
    })

    print(f"Thành công: Đã chiêu mộ tuyển thủ {name}.")
    logging.info(f"Signed new player {name} with salary {salary}")


def update_player_status(roster_list):
    print("\n--- CẬP NHẬT LƯƠNG & TRẠNG THÁI THI ĐẤU ---")
    player_id = input("Nhập mã tuyển thủ: ").strip().upper()

    for p in roster_list:
        if p["player_id"] == player_id:
            print(f"Tuyển thủ: {p['name']}")
            print(f"Lương: {p['salary']}")
            print(f"Trạng thái: {p['status']}")

            choice = input("1. Lương | 2. Trạng thái: ")

            match choice:
                case "1":
                    while True:
                        try:
                            new_salary = float(input("Nhập lương mới: "))
                            if new_salary <= 0:
                                print("Lương phải là số dương.")
                                continue
                            old = p["salary"]
                            p["salary"] = new_salary
                            logging.info(
                                f"Updated player {player_id} salary from {old} to {new_salary}"
                            )
                            return
                        except ValueError:
                            print("Lương phải là số.")
                case "2":
                    status_choice = input("1. Active | 2. Benched: ")
                    match status_choice:
                        case "1":
                            p["status"] = "Active"
                        case "2":
                            p["status"] = "Benched"
                        case _:
                            print("Không hợp lệ.")
                            return
                    logging.info(
                        f"Updated player {player_id} status to {p['status']}"
                    )
                    return
                case _:
                    print("Không hợp lệ.")
                    return

    print(f"Không tìm thấy tuyển thủ {player_id}.")
    logging.warning(f"Failed to update player - Player ID {player_id} not found")


def calculate_actual_pay(player):
    match player.get("status"):
        case "Benched":
            return player["salary"] * 0.5
        case _:
            return player["salary"]


def generate_payroll_report(roster_list):
    print("\n--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---")

    if not roster_list:
        print("Đội hình trống. Tổng quỹ lương: 0.0")
        return

    total = 0
    print("ID       | Tên         | Trạng thái | Lương gốc | Thực nhận")
    print("-" * 70)

    for p in roster_list:
        try:
            pay = calculate_actual_pay(p)
            total += pay
            print(
                f"{p['player_id']:<8} | "
                f"{p['name']:<11} | "
                f"{p['status']:<10} | "
                f"{p['salary']:<10} | "
                f"{pay}"
            )
        except KeyError as e:
            print("Lỗi dữ liệu.")
            logging.error(f"Missing key while generating payroll report: {e}")
            return

    print("-" * 70)
    print(f"Tổng quỹ lương hàng tháng: {total}")
    logging.info(f"Generated monthly payroll report. Total: {total}")


def main():
    while True:
        print("""
===== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH RIKKEI ESPORTS ===== 
Xem đội hình thi đấu hiện tại
Chiêu mộ tuyển thủ mới
Cập nhật lương & Trạng thái thi đấu
Báo cáo quỹ lương hàng tháng
Thoát hệ thống
================================================== 
        """)

        choice = input("Chọn (1-5): ")

        match choice:
            case "1":
                display_roster(roster)
            case "2":
                sign_player(roster)
            case "3":
                update_player_status(roster)
            case "4":
                generate_payroll_report(roster)
            case "5":
                logging.info("System exited.")
                break
            case _:
                print("Không hợp lệ.")


if __name__ == "__main__":
    main()