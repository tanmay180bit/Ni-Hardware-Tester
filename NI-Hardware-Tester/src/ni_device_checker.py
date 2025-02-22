import health_checks

if __name__ == "__main__":
    print("🔍 Checking NI Hardware Connection...")

    if health_checks.check_ni_hardware():
        print("✅ NI Hardware Detected!")

        # Test voltage (Modify 'Dev1' based on your device name)
        voltage = health_checks.check_voltage("Dev1")

        if voltage is not None:
            print(f"✅ Voltage Level: {voltage}V")
        else:
            print("❌ Voltage Read Failed!")
    else:
        print("❌ No NI Hardware Found!")
