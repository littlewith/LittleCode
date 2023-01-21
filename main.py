import tkinter as tk
from tkinter import messagebox as msg, END
import time
import coding
import writeicon

class window:
    mainWindow = tk.Tk()

    def __init__(self, width, height):
        writeicon.write()
        self.mainWindow.title("加密解密小工具~By Littlewith")
        size_geo = self.getwindow(width, height)
        self.mainWindow.resizable(False, False)
        print("Windows info: "+size_geo)
        self.mainWindow.iconbitmap("./demo.ico")
        writeicon.delfile()
        self.mainWindow.geometry(size_geo)
        self.mainWindow.minsize(1000, 600)
        time.sleep(0.5)
        self.welcome()
        # self.mainWindow.config(background="#96b97d")
        self.input = self.inputcon()
        self.md516 = self.md5rescon()
        self.base64 = self.base64con()
        self.hex = self.hexcon()
        self.md532 = self.md5rescon64()
        self.url = self.urlcodecon()
        self.des = self.descodecon()
        self.aes = self.aescodecon()
        self.asc = self.asccodecon()
        # self.sql = self.sqlencon()
        self.logo(width, height)
        self.code(width/2-200, height-88)
        self.uncode(width/2+100, height-88)
        print("Service launch!")
        pass

    def getwindow(self, width, height):
        screenwidth = self.mainWindow.winfo_screenwidth()
        screenheight = self.mainWindow.winfo_screenheight()
        size_geo = "%dx%d+%d+%d" % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
        return size_geo
        pass

    def welcome(self):
        msg.showinfo("欢迎", "感谢您使用本小工具!\n\t——Littlewith")

    def logo(self, width, height):
        logo = tk.Label(self.mainWindow, height=3, text="加密解密小工具~ByLittleWith", font=('Times', 20, 'bold'))
        logo.place(x=width/2-180, y=3, width=360, height=30)
    '''
    def sqlencon(self):
        sqlenarea = tk.Text(self.mainWindow, height=1, font=('Times', 14, 'bold italic'), width=60)
        sqlenlabel = tk.Label(self.mainWindow, text="Sql_En处理后的结果: ", font=('Times', 14, 'bold italic'), width=30, height=2)
        sqlenlabel.grid(row=10, column=0, sticky='w')
        sqlenarea.grid(row=10, column=1, sticky='w')
        return sqlenarea
    '''

    def asccodecon(self):
        ascarea = tk.Text(self.mainWindow, height=1, font=('Times', 12, 'bold'), width=77)
        asclabel = tk.Label(self.mainWindow, text="ASCII处理后的结果: ", font=('Times', 14, 'bold italic'), width=30, height=2)
        asclabel.grid(row=9, column=0, sticky='w')
        ascarea.grid(row=9, column=1, sticky='w')
        return ascarea

    def aescodecon(self):
        aesarea = tk.Text(self.mainWindow, height=1, font=('Times', 12, 'bold'), width=53)
        aeslabel = tk.Label(self.mainWindow, text="AES处理后的结果: ", font=('Times', 14, 'bold italic'), width=30, height=2)
        aespasslabel = tk.Label(self.mainWindow, text="AES密钥: ", font=('Times', 12), width=30, height=2)
        aespassarea = tk.Text(self.mainWindow, height=1, font=('Times', 14))
        aespasslabel.place(x=685, y=390, width=100, height=50)
        aespassarea.place(x=775, y=402, width=180, height=25)
        aeslabel.grid(row=8, column=0, sticky='w')
        aesarea.grid(row=8, column=1, sticky='w')
        aeswg = []
        aeswg.append(aesarea)
        aeswg.append(aespassarea)
        return aeswg

    def descodecon(self):
        desarea = tk.Text(self.mainWindow, height=1, font=('Times', 12, 'bold'), width=53)
        deslabel = tk.Label(self.mainWindow, text="DES处理后的结果: ", font=('Times', 14, 'bold italic'), width=30, height=2)
        despasslabel = tk.Label(self.mainWindow, text="DES密钥: ", font=('Times', 12), width=30, height=2)
        despassarea = tk.Text(self.mainWindow, height=1, font=('Times', 14))
        despasslabel.place(x=685, y=341, width=100, height=50)
        despassarea.place(x=775, y=352, width=180, height=25)
        deslabel.grid(row=7, column=0, sticky='w')
        desarea.grid(row=7, column=1, sticky='w')
        deswg = []
        deswg.append(desarea)
        deswg.append(despassarea)
        return deswg

    def urlcodecon(self):
        urlarea = tk.Text(self.mainWindow, height=1, font=('Times', 12, 'bold'), width=77)
        urllabel = tk.Label(self.mainWindow, text="Url编码处理后的结果: ", font=('Times', 14, 'bold italic'), width=30, height=2)
        urllabel.grid(row=6, column=0, sticky='w')
        urlarea.grid(row=6, column=1, sticky='w')
        return urlarea

    def md5rescon64(self):
        md5area = tk.Text(self.mainWindow, height=1, font=('Times', 12, 'bold'), width=77)
        md5label = tk.Label(self.mainWindow, text="Md5处理后的结果(32位): ", font=('Times', 14, 'bold italic'), width=30, height=2)
        md5label.grid(row=3, column=0, sticky='w')
        md5area.grid(row=3, column=1, sticky='w')
        return md5area

    def hexcon(self):
        hexarea = tk.Text(self.mainWindow, height=1, font=('Times', 12, 'bold'), width=77)
        hexlabel = tk.Label(self.mainWindow, text="Hex处理后的结果: ", font=('Times', 14, 'bold italic'), width=30, height=2)
        hexlabel.grid(row=5, column=0, sticky='w')
        hexarea.grid(row=5, column=1, sticky='w')
        return hexarea

    def base64con(self):
        base64area = tk.Text(self.mainWindow, height=1, font=('Times', 12, 'bold'), width=77)
        base64label = tk.Label(self.mainWindow, text="Base64处理后的结果: ", font=('Times', 14, 'bold italic'), width=30, height=2)
        base64label.grid(row=4, column=0, sticky='w')
        base64area.grid(row=4, column=1, sticky='w')
        return base64area

    # 输入控件2 md532
    def md5rescon(self):
        md5area = tk.Text(self.mainWindow, height=1, font=('Times', 12, 'bold'), width=77)
        md5label = tk.Label(self.mainWindow, text="Md5处理后的结果(16位): ", font=('Times', 14, 'bold italic'), width=30, height=2)
        md5label.grid(row=2, column=0, sticky='w')
        md5area.grid(row=2, column=1, sticky='w')
        return md5area

    # 输入控件1
    def inputcon(self):
        whitearea = tk.Label(self.mainWindow, height=2)
        inputarea = tk.Text(self.mainWindow, height=1, font=('Times', 12, 'bold'), width=77)
        inputlabel = tk.Label(self.mainWindow, text="在这里输入要处理的字符串: ", font=('Times', 14, 'bold italic'), width=30, height=2)
        whitearea.grid(row=0)
        inputarea.grid(row=1, column=1, sticky="w")
        inputlabel.grid(row=1, column=0, sticky='w')
        return inputarea

    def code(self, x, y):
        codebutton = tk.Button(self.mainWindow, text="加密！", command=self.codeall, height=3, width=20, font=('Times', 14, 'bold italic'))
        codebutton.place(x=x, y=y, width=100, height=50)

    def uncode(self, x, y):
        uncodebutton = tk.Button(self.mainWindow, text="解密！", command=self.uncodeall, height=3, width=20, font=('Times', 14, 'bold italic'))
        uncodebutton.place(x=x, y=y, width=100, height=50)

    def launch(self):
        self.mainWindow.mainloop()

    # 所有都解密！
    def uncodeall(self):
        # 获得用户输入
        inputcontent = self.input.get("1.0", END)
        self.md532.delete("1.0", END)
        self.base64.delete("1.0", END)
        self.asc.delete("1.0", END)
        self.aes[0].delete("1.0", END)
        self.hex.delete("1.0", END)
        self.md516.delete("1.0", END)
        # self.sql.delete("1.0", END)
        self.des[0].delete("1.0", END)
        self.url.delete("1.0", END)
        inputcontent = "%s" % inputcontent
        inputcontent = inputcontent[0:-1]
        warn_message = "啊这......你想干什么？你想逆向破解md5吗！....自己上百度找脚本..."
        while True:
            aespass = self.aes[1].get("1.0", END)
            despass = self.des[1].get("1.0", END)
            despass = "%s" % despass
            aespass = "%s" % aespass
            despass = despass[0:-1]
            aespass = aespass[0:-1]
            if len(despass) % 8 != 0:
                msg.showwarning("警告", "DES的密钥必须为8的倍数！")
                return
            else:
                if len(aespass) % 16 != 0:
                    msg.showwarning("警告", "AES的密钥必须为16的倍数！")
                    return
                else:
                    break
        msg.showinfo("解密状态", "解密完成！(md5不可逆加密，可以尝试爆破)")
        self.md516.insert("1.0", warn_message)
        self.md532.insert("1.0", warn_message)
        self.base64.insert("1.0", coding.base64uncode(inputcontent))
        self.hex.insert("1.0", coding.hexuncode(inputcontent))
        self.url.insert("1.0", coding.urluncode(inputcontent))
        self.asc.insert("1.0", coding.ascuncode(inputcontent))
        self.des[0].insert("1.0", coding.desuncode(inputcontent, despass))
        self.aes[0].insert("1.0", coding.aesuncode(inputcontent, aespass))

        pass

    # 所有都加密!
    def codeall(self):
        # 获得用户输入
        inputcontent = self.input.get("1.0", END)
        self.md532.delete("1.0", END)
        self.base64.delete("1.0", END)
        self.asc.delete("1.0", END)
        self.aes[0].delete("1.0", END)
        self.hex.delete("1.0", END)
        self.md516.delete("1.0", END)
        # self.sql.delete("1.0", END)
        self.des[0].delete("1.0", END)
        self.url.delete("1.0", END)
        inputcontent = "%s" % inputcontent
        inputcontent = inputcontent[0:-1]

        while True:
            aespass = self.aes[1].get("1.0", END)
            despass = self.des[1].get("1.0", END)
            despass = "%s" % despass
            aespass = "%s" % aespass
            despass = despass[0:-1]
            aespass = aespass[0:-1]
            if len(despass) % 8 != 0:
                msg.showwarning("警告", "DES加密的密钥必须为8位！")
                return
            else:
                if len(aespass) % 16 != 0:
                    msg.showwarning("警告", "AES加密的密钥必须为16位！")
                    return
                else:
                    break
        msg.showinfo("加密状态", "加密完成！")
        # 去掉末尾自动添加的\n
        self.md516.insert("1.0", coding.md5code16(inputcontent))
        self.md532.insert("1.0", coding.md5code32(inputcontent))
        self.base64.insert("1.0", coding.base64code(inputcontent))
        self.hex.insert("1.0", coding.hexcode(inputcontent))
        self.url.insert("1.0", coding.urlcode(inputcontent))
        self.asc.insert("1.0", coding.asccode(inputcontent))
        self.des[0].insert("1.0", coding.descode(inputcontent, despass))
        self.aes[0].insert("1.0", coding.aescode(inputcontent, aespass))

        pass

    def writeico(self):

        pass

    def __del__(self):
        pass


def main():
    root_window = window(1000, 600)
    root_window.launch()
    pass


if __name__ == "__main__":
    main()
