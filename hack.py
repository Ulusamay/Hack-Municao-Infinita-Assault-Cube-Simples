from ReadWriteMemory import ReadWriteMemory
import psutil, win32process, win32api, win32gui

def enderecoBase():
    PROCESS_ALL_ACCESS = 0x1F0FFF
    for proc in psutil.process_iter():
        if proc.name() == 'ac_client.exe':
            pid = proc.pid
    PROCESS_ALL_ACCESS = 0x1F0FFF
    processHandle = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    modules = win32process.EnumProcessModules(processHandle)
    processHandle.close()
    base_addr = modules[0]
    return base_addr

base = enderecoBase()

rwm = ReadWriteMemory()

process = rwm.get_process_by_name('ac_client.exe')
#print(0x0010F418 + 0x58+ 0x1EC+ 0x8+ 0x150)
process.open()
while True:
    municao = process.get_pointer(base + 0x0010F418, offsets=[0x58, 0x1EC, 0x8, 0x150])
    process.write(municao, 5000)
