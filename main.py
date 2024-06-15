import psutil
import platform
import argparse
import os
import time
import json

try:
    import GPUtil
except ImportError:
    GPUtil = None


# Function to get OS information
def get_os_info():
    return {
        "System": platform.system(),
        "OS Release": platform.release(),
        "OS Version": platform.version(),
    }


# Function to get CPU information
def get_cpu_info():
    cpu_usage_percent = psutil.cpu_percent(interval=1, percpu=False)

    return {
        "Processor": platform.processor(),
        "Core count": psutil.cpu_count(logical=True),
        "Physical cores": psutil.cpu_count(logical=False),
        "CPU Usage (%)": cpu_usage_percent,
    }


# Function to get RAM information
def get_ram_info():
    svmem = psutil.virtual_memory()

    return {
        "Total memory (GB)": round(svmem.total / (1024**3), 2),
        "Available memory (GB)": round(svmem.available / (1024**3), 2),
        "Used memory (%)": svmem.percent,
    }


# Function to get Disk information
def get_disk_info():
    disk_info = {}
    partitions = psutil.disk_partitions()

    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            disk_info[partition.device] = {
                "Total size (GB)": round(partition_usage.total / (1024**3), 2),
                "Used size (GB)": round(partition_usage.used / (1024**3), 2),
                "Free size (GB)": round(partition_usage.free / (1024**3), 2),
                "Usage (%)": partition_usage.percent,
            }
        except PermissionError:
            continue

    return disk_info


# Function to get GPU information
def get_gpu_info():
    if GPUtil is None:
        return {"Error": "GPU Information - GPUtil not available"}

    gpu_info = GPUtil.getGPUs()
    gpu_data = {}

    for gpu in gpu_info:
        gpu_data[gpu.name] = {
            "Memory Total (GB)": gpu.memoryTotal,
            "Memory Used (%)": gpu.memoryUsed,
        }

    return gpu_data


# Function to get Network interface information
def get_network_info():
    network_info = {}
    for interface, addresses in psutil.net_if_addrs().items():
        network_info[interface] = [address.address for address in addresses]

    return network_info


# Function to get Process information
def get_process_info():
    processes = []
    for process in psutil.process_iter():
        processes.append(
            {
                "PID": process.pid,
                "Name": process.name(),
                "CPU Usage (%)": process.cpu_percent(),
                "Memory Usage (MB)": round(
                    process.memory_info().rss / (1024 * 1024), 2
                ),
            }
        )

    return processes


# Function to get System Uptime
def get_system_uptime():
    uptime = round(time.time() - psutil.boot_time())
    days, remainder = divmod(uptime, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    return {
        "Uptime": f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds",
    }


# Function to get Network Usage
def get_network_usage():
    net_io = psutil.net_io_counters()

    return {
        "Total Bytes Sent": net_io.bytes_sent,
        "Total Bytes Received": net_io.bytes_recv,
    }


# Function to get User Information
def get_user_info():
    username = os.getlogin()
    home_directory = os.path.expanduser("~")

    return {
        "Username": username,
        "Home Directory": home_directory,
    }


# Function to get System Temperature
def get_system_temperature():
    sensors = psutil.sensors_temperatures()

    return {
        sensor: [(item.label, item.current) for item in data]
        for sensor, data in sensors.items()
    }


# Add command line argument parser
parser = argparse.ArgumentParser(
    description="Display system information in JSON format"
)
parser.add_argument("--all", action="store_true", help="Display All information")
parser.add_argument("--os", action="store_true", help="Display OS information")
parser.add_argument("--cpu", action="store_true", help="Display CPU information")
parser.add_argument("--ram", action="store_true", help="Display RAM information")
parser.add_argument("--disk", action="store_true", help="Display Disk information")
parser.add_argument("--gpu", action="store_true", help="Display GPU information")
parser.add_argument(
    "--network", action="store_true", help="Display Network interface information"
)
parser.add_argument(
    "--process", action="store_true", help="Display Process information"
)
parser.add_argument("--uptime", action="store_true", help="Display System Uptime")
parser.add_argument(
    "--network_usage", action="store_true", help="Display Network Usage"
)
parser.add_argument("--user", action="store_true", help="Display User Information")
parser.add_argument(
    "--temperature", action="store_true", help="Display System Temperature"
)

args = parser.parse_args()


# Function to display system information based on user input
def display_system_info(args):
    system_info = {}
    if args.all:
        system_info["OS"] = get_os_info()
        system_info["Uptime"] = get_system_uptime()
        system_info["CPU"] = get_cpu_info()
        system_info["RAM"] = get_ram_info()
        system_info["Disk"] = get_disk_info()
        system_info["GPU"] = get_gpu_info()
        system_info["Network"] = get_network_info()
        system_info["Process"] = get_process_info()
        system_info["Network Usage"] = get_network_usage()
        system_info["User"] = get_user_info()
        system_info["Temperature"] = get_system_temperature()
    if args.os:
        system_info["OS"] = get_os_info()
    if args.cpu:
        system_info["CPU"] = get_cpu_info()
    if args.ram:
        system_info["RAM"] = get_ram_info()
    if args.disk:
        system_info["Disk"] = get_disk_info()
    if args.gpu:
        system_info["GPU"] = get_gpu_info()
    if args.network:
        system_info["Network"] = get_network_info()
    if args.process:
        system_info["Process"] = get_process_info()
    if args.uptime:
        system_info["Uptime"] = get_system_uptime()
    if args.network_usage:
        system_info["Network Usage"] = get_network_usage()
    if args.user:
        system_info["User"] = get_user_info()
    if args.temperature:
        system_info["Temperature"] = get_system_temperature()

    return system_info


if __name__ == "__main__":
    system_info = display_system_info(args)

    print(json.dumps(system_info, indent=4))
