# Sysinfo-json

This is another version of the [sysinfo](https://github.com/mobin-gpr/sysinfo.git) tool, with the difference that the output of this program is instead of json text format table. The purpose of developing this script is to use the information in other programs. The options of this tool are the same as the options of the sysinfo tool and only They differ in the output format. Using this tool, you can view the software and hardware information of your system in detail. this information includes the OS, CPU, RAM, Disks, GPU, Process, Network interface & ...
## Author

- [@mobin-ghanbarpour](https://github.com/mobin-gpr/)


## Run Project
Clone the project

```bash
git clone https://github.com/mobin-gpr/sysinfo-json.git
```

Go to the project directory

```bash
cd sysinfo-json
```

Install dependencies

```bash
pip install -r requirements.txt
```

Show helps

```bash
python main.py --help
```

## Guide


```text
usage: main.py [-h] [--all] [--os] [--cpu]
               [--ram] [--disk] [--gpu]
               [--network] [--process]
               [--uptime] [--network_usage]
               [--user] [--temperature]

Display system information

optional arguments:
  -h, --help       show this help message and
                   exit
  --all            Display All information
  --os             Display OS information
  --uptime         Display System Uptime
  --cpu            Display CPU information
  --ram            Display RAM information
  --disk           Display Disk information
  --gpu            Display GPU information
  --network        Display Network interface
                   information
  --process        Display Process information
  --network_usage  Display Network Usage
  --user           Display User Information
  --temperature    Display System Temperature
```

## License

[MIT](https://choosealicense.com/licenses/mit/)