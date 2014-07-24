import wx

class MyApp(wx.App):
  def OnInit(self):
    #como eh a janela principal parent=None
    self.frame = MyFrame(None, title="The Main Frame")
    #Configura o frame como a janela no topo da aplicacao
    self.SetTopWindow(self.frame)
    self.frame.Show()

    return True

class MyPanel(wx.Panel):
  def __init__(self, parent):
    super(MyPanel, self).__init__(parent)
    #Make some buttons
    sizer = wx.BoxSizer(wx.HORIZONTAL)
    for bid in(wx.ID_OK, wx.ID_CANCEL,
               wx.ID_APPLY, wx.ID_HELP):
      button = wx.Button(self, bid)
      sizer.Add(button, 0, wx.ALL, 5)
      self.SetSizer(sizer)

class MyFrame(wx.Frame):
  def __init__(self,parent, id=wx.ID_ANY, title="",
               pos=wx.DefaultPosition, size=wx.DefaultSize,
               style=wx.DEFAULT_FRAME_STYLE,
               name="MyFrame"):
      super(MyFrame,self).__init__(parent,id,title,
                                   pos,size,style,name)
      
      #Attributes
      self.panel = MyPanel(self) #Um frame sempre contem um painel
        

if __name__ == "__main__":
  print "Stock Buttons:"
  for x in dir(wx):
    if x.startswith('ID_'):
      print x
  app = MyApp(False)
  app.MainLoop()
