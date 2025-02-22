 
import os
import logging
import nidaqmx
import nidaqmx.system

# Ensure logs directory exists
log_dir = os.path.join(os.path.dirname(__file__), '../logs')
os.makedirs(log_dir, exist_ok=True)

# Set up logging
logging.basicConfig(
    filename=os.path.join(log_dir, 'ni_hardware_status.log'),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_ni_hardware():
    """Check if NI hardware is connected."""
    try:
        system = nidaqmx.system.System.local()
        devices = list(system.devices)

        if devices:
            logging.info(f"✅ NI Hardware Found: {[device.name for device in devices]}")
            return True
        else:
            logging.error("❌ No NI Hardware Detected!")
            return False

    except Exception as e:
        logging.error(f"❌ Error Checking Hardware: {str(e)}")
        return False

def check_voltage(device_name, channel="ai0"):
    """Check voltage levels from an NI device."""
    try:
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(f"{device_name}/{channel}")
            voltage = task.read()
            logging.info(f"✅ Voltage Read from {device_name}/{channel}: {voltage}V")
            return voltage
    except Exception as e:
        logging.error(f"❌ Voltage Check Failed: {str(e)}")
        return None
