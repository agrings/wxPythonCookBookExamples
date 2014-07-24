import wx
import wx.lib.platebtn as pbtn
import wx.lib.agw.gradientbutton as gbtn

class MyApp(wx.App):
  def OnInit(self):
    #como eh a janela principal parent=None
    self.frame = MyFrame(None, title="The Main Frame")
    #Configura o frame como a janela no topo da aplicacao
    self.SetTopWindow(self.frame)
    self.frame.Show()

    return True

class LoginPanel(wx.Panel):
  def __init__(self, parent):
    super(LoginPanel, self).__init__(parent)

    # Attributes
    self._username = wx.TextCtrl(self)
    self._passwd = wx.TextCtrl(self, style=wx.TE_PASSWORD)

    # Layout
    sizer = wx.FlexGridSizer(2, 2, 8, 8)
    sizer.Add(wx.StaticText(self, label="Username:"),
                            0, wx.ALIGN_CENTER_VERTICAL)
    sizer.Add(self._username, 0, wx.EXPAND)
    sizer.Add(wx.StaticText(self, label="Password:"),
                            0, wx.ALIGN_CENTER_VERTICAL)
    sizer.Add(self._passwd, 0, wx.EXPAND)
    msizer = wx.BoxSizer(wx.VERTICAL)
    msizer.Add(sizer, 1, wx.EXPAND|wx.ALL, 20)
    btnszr = wx.StdDialogButtonSizer()
    button = wx.Button(self, wx.ID_OK)
    button.SetDefault()
    btnszr.AddButton(button)
    msizer.Add(btnszr, 0, wx.ALIGN_CENTER|wx.ALL, 12)
    btnszr.Realize()
    self.SetSizer(msizer)

    def GetUsername(self):
      return self._username.GetValue()
    def GetPassword(self):
      return self._passwd.GetValue()

class LoginDialog(wx.Dialog):
  def __init__(self, *args, **kwargs):
    super(LoginDialog, self).__init__(*args, **kwargs)
    # Attributes
    self.panel = LoginPanel(self)
    # Layout
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(self.panel, 1, wx.EXPAND)
    self.SetSizer(sizer)
    self.SetInitialSize()

  def GetUsername(self):
    return self.panel.GetUsername()

  def GetPassword(self):
    return self.panel.GetPassword()

class MyFrame(wx.Frame):
  def __init__(self,parent, id=wx.ID_ANY, title="",
               pos=wx.DefaultPosition, size=wx.DefaultSize,
               style=wx.DEFAULT_FRAME_STYLE,
               name="MyFrame"):
      super(MyFrame,self).__init__(parent,id,title,
                                   pos,size,style,name)
      
      #Attributes
      self.panel = wx.Panel(self) #Um frame sempre contem um painel
      # Make a BitmapButton
      bmp = wx.Bitmap("./face-monkey.png",wx.BITMAP_TYPE_PNG)
      self.bmpbtn = wx.BitmapButton(self, bitmap=bmp)

      # Layout
      vsizer = wx.BoxSizer(wx.VERTICAL)
      vsizer.Add(self.bmpbtn, 0, wx.ALL, 12)
      
      # Events
      self.Bind(wx.EVT_BUTTON, self.OnButton, self.bmpbtn)        
      

  def OnButton(self, event):
     ld = LoginDialog(self)
     ld.ShowModal()
     print "Username:%s" % ld.GetUsername,"\n"
     print "Password:%s" % ld.GetPassword,"\n"

     ld.Destroy()

if __name__ == "__main__":
  app = MyApp(False)
  app.MainLoop()
