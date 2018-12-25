#encoding=utf-8
import socket
import wx

ipPort = ("127.0.0.1", 12580)

class InitPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id = -1)
        
        self.login_btn = wx.Button(self, label='登录', size=(80, 30))  # 添加按钮控件
        self.registe_btn = wx.Button(self, label='注册', size=(80, 30))  # 添加按钮控件
        static_text = wx.StaticText(self, -1, u'请选择注册或登录', style=wx.ALIGN_CENTER)

        hbox = wx.BoxSizer()
        hbox.Add(self.login_btn, proportion = 0, flag = wx.EXPAND, border = 10)
        hbox.Add(self.registe_btn, proportion = 0, flag = wx.EXPAND, border = 10)
        
        vbox = wx.BoxSizer(wx.VERTICAL)  # 创建垂直容器
        vbox.Add(static_text, proportion=0, flag=wx.EXPAND)
        vbox.Add(hbox, proportion=0, flag=wx.EXPAND)  # 将水平容器添加到垂直容器
        
        self.SetSizer(vbox)

class LoginPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id = -1)
        
        username_label = wx.StaticText(self, -1, u'用户名:')
        passward_label = wx.StaticText(self, -1, u'密   码:')
        self.username = wx.TextCtrl(self, -1, size = (180, 30))
        self.passward = wx.TextCtrl(self, -1, size = (180, 30))
        self.login_btn = wx.Button(self, label='登录', size=(80, 30))  # 添加按钮控件
        self.back_btn = wx.Button(self, label='返回', size=(80, 30))  # 添加按钮控件
        
        hbox1 = wx.BoxSizer()
        hbox1.Add(username_label, proportion = 0, flag = wx.EXPAND, border = 3)
        hbox1.Add(self.username, proportion = 0, flag = wx.EXPAND, border = 3)
        
        hbox2 = wx.BoxSizer()
        hbox2.Add(passward_label, proportion = 0, flag = wx.EXPAND, border = 3)
        hbox2.Add(self.passward, proportion = 0, flag = wx.EXPAND, border = 3)
        
        hbox3 = wx.BoxSizer()
        hbox3.Add(self.login_btn, proportion = 0, flag = wx.EXPAND, border = 3)
        hbox3.Add(self.back_btn, proportion = 0, flag = wx.EXPAND, border = 3)
        
        vbox = wx.BoxSizer(wx.VERTICAL)  # 创建垂直容器
        vbox.Add(hbox1, proportion=0, flag=wx.EXPAND)
        vbox.Add(hbox2, proportion=0, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=0, flag=wx.EXPAND)
        
        self.SetSizer(vbox)
        
class RegistePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id = -1)
        
        username_label = wx.StaticText(self, -1, u'用户名:')
        passward_label = wx.StaticText(self, -1, u'密   码:')
        self.username = wx.TextCtrl(self, -1, size = (180, 30))
        self.passward = wx.TextCtrl(self, -1, size = (180, 30))
        self.registe_btn = wx.Button(self, label='注册', size=(80, 30))  # 添加按钮控件
        self.back_btn = wx.Button(self, label='返回', size=(80, 30))  # 添加按钮控件
        
        hbox1 = wx.BoxSizer()
        hbox1.Add(username_label, proportion = 0, flag = wx.EXPAND, border = 3)
        hbox1.Add(self.username, proportion = 0, flag = wx.EXPAND, border = 3)
        
        hbox2 = wx.BoxSizer()
        hbox2.Add(passward_label, proportion = 0, flag = wx.EXPAND, border = 3)
        hbox2.Add(self.passward, proportion = 0, flag = wx.EXPAND, border = 3)
        
        hbox3 = wx.BoxSizer()
        hbox3.Add(self.registe_btn, proportion = 0, flag = wx.EXPAND, border = 3)
        hbox3.Add(self.back_btn, proportion = 0, flag = wx.EXPAND, border = 3)
        
        vbox = wx.BoxSizer(wx.VERTICAL)  # 创建垂直容器
        vbox.Add(hbox1, proportion=0, flag=wx.EXPAND)
        vbox.Add(hbox2, proportion=0, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=0, flag=wx.EXPAND)
        
        self.SetSizer(vbox)
        
        
class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id = -1)

        file_btn = wx.FilePickerCtrl(self)  # 添加文件选择控件
        file_btn.GetPickerCtrl().SetLabel('选择')  # 设置选择控件文本
        upload_btn = wx.Button(self, label='上传', size=(80, 30))  # 添加按钮控件
        look_btn = wx.Button(self, label='查看已上传', size=(80, 30))  # 添加按钮控件
        listbox = wx.ListBox(self, size=(375, 240), style=wx.LB_SINGLE)  # 添加文本控件
        firstRow = wx.StaticText(self, -1, u'  文件名'.ljust(20)+'  文件大小'.ljust(20)+'  用户名'.ljust(20)+'  是否在线'.ljust(20))
        listbox.SetItems([u'a22d'.ljust(20)+u'sadiqw'.ljust(20)+u'as'.ljust(20)+u'asdr'.ljust(20),u'asde'.ljust(20)+u'wefda'.ljust(20)+u'main'.ljust(20)+u'adas'.ljust(20),'2'])
        
        hbox = wx.BoxSizer()  # 尺寸器实例化（默认水平）
        hbox.Add(file_btn, proportion=1, flag=wx.EXPAND)  # 添加控件到尺寸器
        hbox.Add(upload_btn, proportion=0, flag=wx.LEFT, border=5)  # 添加控件到尺寸器
        hbox.Add(look_btn, proportion=0, flag=wx.LEFT, border=5)  # 添加控件到尺寸器

        vbox = wx.BoxSizer(wx.VERTICAL)  # 尺寸器实例化（垂直）
        vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)  # 添加尺寸器到尺寸器
        vbox.Add(firstRow, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)  # 添加尺寸器到尺寸器
        vbox.Add(listbox, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)  # 添加控件到尺寸器

        self.SetSizer(vbox)  # 为窗口设置尺寸器
        
class Client(wx.App):
    def __init__(self):
        super(Client, self).__init__()
       
    def OnInit(self):
        self.win = wx.Frame(None, title = 'p2p客户端', pos = (400, 300), size = (500, 380))
        
        self.initPan = InitPanel(self.win)
        self.initPan.login_btn.Bind(wx.EVT_BUTTON, self.login)
        self.initPan.registe_btn.Bind(wx.EVT_BUTTON, self.registe)
        
        # pan = wx.Panel(win)  # 添加面板
        # pan.SetBackgroundColour('#666666')  # 设置面板颜色

        # file_btn = wx.FilePickerCtrl(pan, pos=(5, 5))  # 添加文件选择控件
        # file_btn.GetPickerCtrl().SetLabel('选择')  # 设置选择控件文本
        # open_btn = wx.Button(pan, label='打开', pos=(215, 5), size=(80, 30))  # 添加按钮控件
        # save_btn = wx.Button(pan, label='保存', pos=(300, 5), size=(80, 30))  # 添加按钮控件
        # cont_ipt = wx.TextCtrl(pan, pos=(5, 40), size=(375, 240), style=wx.TE_MULTILINE | wx.HSCROLL)  # 添加文本控件

        
        
        self.hbox = wx.BoxSizer()  # 尺寸器实例化（默认水平）
        self.hbox.Add(self.initPan, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT)  # 添加控件到尺寸器
        
        self.win.SetSizer(self.hbox)
        self.win.Show()  # 显示框架
        return True
        
    def login(self, event):    
        self.loginPan = LoginPanel(self.win)
        self.loginPan.login_btn.Bind(wx.EVT_BUTTON, self.login2)
        self.hbox.Hide(self.initPan)
        self.hbox.Replace(self.initPan, self.loginPan)
        self.hbox.Layout()
    def registe(self, event):    
        self.registePan = RegistePanel(self.win)
        self.hbox.Hide(self.initPan)
        self.hbox.Replace(self.initPan, self.registePan)
        self.hbox.Layout()
    def login2(self, event):
        obj = socket.socket()
        obj.connect(ipPort)
        ret_bytes = obj.recv(1024)
        ret_str = unicode(ret_bytes)
        print(ret_str)
        print type(self.loginPan.username.GetValue())
        obj.sendall(bytes([self.loginPan.username.GetValue(), self.loginPan.passward.GetValue()]))
        print obj.getsockname()
        
        self.mainPan = MainPanel(self.win)
        self.hbox.Hide(self.loginPan)
        self.hbox.Replace(self.loginPan, self.mainPan)
        self.hbox.Layout()
    def registe2(self, event):    
        self.registePan = RegistePanel(self.win)
        self.hbox.Hide(self.initPan)
        self.hbox.Replace(self.initPan, self.registePan)
        self.hbox.Layout()
        
client = Client()
client.MainLoop()
    

# obj = socket.socket()

# ip = "54.147.119.99"
# ipPort = ("127.0.0.1", 12580)
# obj.connect((ip, 12580))
# print('connect sucess')
# ret = str(obj.recv(1024))

# print(ret)