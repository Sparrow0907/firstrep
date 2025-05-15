import platform
import psutil
import socket
import random
import subprocess

def get_os_version():
    return platform.platform()

def get_total_memory():
    return psutil.virtual_memory().total

def get_cpu_info():
    return platform.processor() or "Не определен"

def get_hostname():
    try:
        return socket.gethostname()
    except:
        return "Не определен"

def detect_hardware():
    com_ports = random.randint(1, 4)
    joystick = random.choice([True, False])
    printers = random.randint(0, 2)

    rom_address = "c000"
    rom_length = random.randint(16384, 32768)

    return com_ports, joystick, printers, rom_address, rom_length

def get_graphics_card():

            output = subprocess.check_output("wmic path win32_VideoController get name", shell=True, encoding="utf-8")
            print("Windows WMIC Output:\n", output)
            lines = output.strip().split('\n')
            if len(lines) > 1:
                return lines[1].strip()
            else:
                return "Не определен"



def print_system_info(hostname, os_version, total_memory, cpu_info, com_ports, joystick, printers, rom_address, rom_length, graphics_card):
    print("Тип компьютера:", hostname)

    print("Конфигурация оборудования:")
    print("  Процессор:", cpu_info)

    print("  Портов RS232:", com_ports)
    print("  Джойстик:", "есть" if joystick else "нет")
    print("  Принтеров:", printers)
    print("  Видеоадаптер:", graphics_card)

    print("Объем оперативной памяти:", total_memory // 1024, "Кбайт")

    extended_memory_present = random.choice([True, False])
    if extended_memory_present:
        extended_memory_size = random.randint(256, 4096)
        print("Объем расширенной памяти:", extended_memory_size, "Кбайт")
    else:
        print("Расширенная память: Отсутствует")

    if rom_address != "Не найден":
        print("Адрес ПЗУ =", rom_address + ". Длина модуля =", rom_length, "байт")
    else:
        print("Дополнительные ПЗУ не найдены.")

    print("Версия операционной системы:", os_version)


if __name__ == "__main__":
    hostname = get_hostname()
    os_version = get_os_version()
    total_memory = get_total_memory()
    cpu_info = get_cpu_info()
    com_ports, joystick, printers, rom_address, rom_length = detect_hardware()
    graphics_card = get_graphics_card()

    print_system_info(hostname, os_version, total_memory,
                      cpu_info, com_ports, joystick,
                      printers, rom_address, rom_length, graphics_card)