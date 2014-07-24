import wx

class MyApp(wx.App):
  def OnInit(self):
    #como eh a janela principal parent=None
    self.frame = MyFrame(None, title="The Main Frame")
    #Configura o frame como a janela no topo da aplicacao
    self.SetTopWindow(self.frame)
    self.frame.Show()

    return True


class MyFrame(wx.Frame):
  def __init__(self,parent, id=wx.ID_ANY, title="",
               pos=wx.DefaultPosition, size=wx.DefaultSize,
               style=wx.DEFAULT_FRAME_STYLE,
               name="MyFrame"):
      super(MyFrame,self).__init__(parent,id,title,
                                   pos,size,style,name)
      
      #Attributes
      self.panel = wx.Panel(self) #Um frame sempre contem um painel
      self.checkbox1 = wx.CheckBox(self.panel, label="2 State CheckBox")
      style = wx.CHK_3STATE|wx.CHK_ALLOW_3RD_STATE_FOR_USER
      self.checkbox2 = wx.CheckBox(self.panel,
                                   label="3 State CheckBox",
                                   style=style)
      # Layout
      sizer = wx.BoxSizer(wx.VERTICAL)
      sizer.Add(self.checkbox1, 0, wx.ALL, 15)
      sizer.Add(self.checkbox2, 0, wx.ALL, 15)
      self.panel.SetSizer(sizer)
      self.CreateStatusBar()
      # Event Handlers
      self.Bind(wx.EVT_CHECKBOX, self.OnCheck)

  def OnCheck(self, event):
    e_obj = event.GetEventObject()
    if e_obj == self.checkbox1:
      checked = self.checkbox1.GetValue()
      msg = "Two State Clicked: %s" % checked
      self.PushStatusText(msg)
    elif e_obj == self.checkbox2:
      state = self.checkbox2.Get3StateValue()
      msg = "Three State Clicked: %d" % state
      self.PushStatusText(msg)
    else:
      event.Skip()
        

if __name__ == "__main__":
  app = MyApp(False)
  app.MainLoop()
