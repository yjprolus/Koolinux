#!/usr/bin/python3
# 作者：yjprolus，个人网站 https://yjprolus.top/
# 工具列表在30-60行，程序原理就是简单的添加源并进行apt安装 
import os
if os.geteuid() != 0:
    print("请以root身份运行此程序(sudo su) !\n\n")
    exit(0)

try:
    # 设置字体颜色
    R = '\033[91m'
    Y = '\033[92m'
    G = '\033[93m'
    W = '\033[94m'
    B = '\033[95m'
    CY = '\033[96m'

    def main():
        print(B+"""
##############################################################################"""+G+"""

>>> 主菜单"""+CY+"""

1) 添加Kali镜像源(请确保之前未配置kali镜像源到系统，有的话请自行删除)
2) 移除Kali镜像源
3) 运行apt update升级命令
4) 查看/etc/apt/source.list文件
5) 开始安装
6) 退出
"""+W)

    def install():
        print(B+"""
##############################################################################"""+G+"""

>>> Kali Linux 工具集"""+Y+"""

信息收集
漏洞扫描
Web相关
密码攻击
无线攻击
权限维持
硬件攻击
逆向工程
报告工具
嗅探/取证/欺骗/社工
//TODO

1] Aircrack-ng
2] Armitage
3] Apktool
4] Burpsuite
5] Dex2jar
6] John the Ripper
7] Kismet
8] Mdk3
9] Metasploit-Framework
10] Nmap
11] PixieWPS
12] RainbowCrack
13] Recon-ng
14] Setoolkit
15] Sqlmap
16] Wifite
17] Wireshark

0] 返回主菜单
"""+W)

    def menu():
        try:
            choose = int(input(R+"#"+Y+" 请选择序号： >> "+W))
            if choose == 1:
                try:
                    f = os.path.isfile("/usr/bin/wget")
                    if f == False:
                        print("开始安装wget工具")
                        os.system("apt-get install wget -y")
                    print(G+"\n正在备份sources.list...............\n")
                    os.system(
                        "cp /etc/apt/sources.list /etc/apt/sources.list.bak")
                    print(B+"\n备份文件保存为sources.list.bak \n")
                    print(G+"\n正在添加Kali依赖\n")
                    os.system(
                        "echo '# \n deb https://mirrors.aliyun.com/kali kali-rolling main non-free contrib' >> /etc/apt/sources.list")
                    os.system(
                        "wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add")
                    print(Y+"\nKali依赖添加成功\n"+W)
                except ConnectionError:
                    print("出现错误，请检查网络后重试:(")
                main()
                menu()
            elif choose == 3:
                print(CY+"运行apt更新中...\n"+W)
                os.system("apt-get update")
                main()
                menu()
            elif choose == 2:
                try:
                    with open("/etc/apt/sources.list", "r") as inp:
                        with open("/etc/apt/sources.list.rf", "w") as out:
                            for line in inp:
                                if line.strip("\n") != "deb https://mirrors.aliyun.com/kali kali-rolling main non-free contrib":
                                    out.write(line)
                    out.close()
                    os.remove("/etc/apt/sources.list")
                    os.system(
                        "mv /etc/apt/sources.list.rf /etc/apt/sources.list")
                    print(R+"\nKali依赖已经全部移除成功！\n")
                    print(CY+"\n再次更新系统中\n"+W)
                    os.system("sudo apt-get update")
                except FileNotFoundError:
                    print(R+"未找到文件!"+W)
                main()
                menu()
            elif choose == 4:
                print(Y+"\nsources.list文件内容如下：\n"+W)
                os.system("cat /etc/apt/sources.list")
                main()
                menu()
            elif choose == 5:
                install()

                def tool():
                    tool_choose = int(input(R+"#"+Y+" 请根据分类选择工具： >> "+W))
                    os.system("echo '\e[97m'")
                    if tool_choose == 1:
                        os.system("sudo apt-get install aircrack-ng -y")
                        install()
                        tool()
                    elif tool_choose == 2:
                        os.system("sudo apt-get install armitage -y")
                        install()
                        tool()
                    elif tool_choose == 3:
                        os.system("sudo apt-get install apktool -y")
                        install()
                        tool()
                    elif tool_choose == 4:
                        os.system("sudo apt-get install burpsuite -y")
                        install()
                        tool()
                    elif tool_choose == 5:
                        os.system("sudo apt-get install dex2jar -y")
                        install()
                        tool()
                    elif tool_choose == 6:
                        os.system("sudo apt-get install john -y")
                        install()
                        tool()
                    elif tool_choose == 7:
                        os.system("sudo apt-get install kismet -y")
                        install()
                        tool()
                    elif tool_choose == 8:
                        os.system("sudo apt-get install mdk3 -y")
                        install()
                        tool()
                    elif tool_choose == 9:
                        os.system("sudo apt-get install metasploit-framework -y")
                        install()
                        tool()
                    elif tool_choose == 10:
                        os.system("sudo apt-get install nmap -y")
                        install()
                        tool()
                    elif tool_choose == 11:
                        os.system("susdo apt-get install pixiewps -y")
                        install()
                        tool()
                    elif tool_choose == 12:
                        os.system("sudo apt-get install rainbowcrack -y")
                        install()
                        tool()
                    elif tool_choose == 13:
                        os.system("sudo apt-get install recon-ng -y")
                        install()
                        tool()
                    elif tool_choose == 14:
                        os.system("sudo apt-get install set -y")
                        install()
                        tool()
                    elif tool_choose == 15:
                        os.system("sudo apt-get install sqlmap -y")
                        install()
                        tool()
                    elif tool_choose == 16:
                        os.system("sudo apt-get install wifite -y")
                        install()
                        tool()
                    elif tool_choose == 17:
                        os.system("sudo apt-get install wireshark -y")
                        install()
                        tool()
                    elif tool_choose == 0:
                        main()
                        menu()
                    else:
                        print(R+"无效输入！请重试"+W)
                        tool()
                tool()
            elif choose == 6:
                 print(Y+"\n感谢使用Koolinux工具\n")
                 exit(0)
            else:
                print(R+"\n无效输入！请重试：( \n")
                menu()
        except ValueError:
            print(R+"\n无效输入！请重试：( \n")
            menu()
    main()
    menu()
except KeyboardInterrupt:
    print(Y+"\n感谢使用Koolinux工具\n")
