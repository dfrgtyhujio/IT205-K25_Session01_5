print("=== KIOSK KHAI BÁO Y TẾ TỰ ĐỘNG ===")
patient_name = input("Nhập họ và tên bệnh nhân: ")
patient_id = input("Nhập mã bệnh nhân: ")
body_temperature = float(input("Nhập nhiệt độ cơ thể: "))
heart_rate = int(input("Nhập nhịp tim: "))
body_weight = float(input("Nhập cân nặng kg: "))



print("\n--- PHIẾU KHÁM BỆNH ĐIỆN TỬ ---")
print("Bệnh nhân:", patient_name)
print("Mã số bệnh án:", patient_id)
print("Nhiệt độ cơ thể:", body_temperature, "độ C")
print("Nhịp tim:", heart_rate, "nhịp/phút")
print("Cân nặng:", body_weight, "kg")


print("\n--- KIỂM TRA KIỂU DỮ LIỆU (SYSTEM LOGS) ---")
print("Biến patient_name có kiểu là:", type(patient_name))
print("Biến patient_id có kiểu là:", type(patient_id))
print("Biến body_temperature có kiểu là:", type(body_temperature))
print("Biến heart_rate có kiểu là:", type(heart_rate))
print("Biến body_weight có kiểu là:", type(body_weight))