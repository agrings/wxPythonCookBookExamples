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
      self.panel.SetBackgroundColour(wx.BLACK)
      button = wx.Button(self.panel,
                              label="Get Children",
                              pos=(50,50))
      self.btnId = button.GetId()
      # Event Handlers
      self.Bind(wx.EVT_BUTTON, self.OnButton, button)
  
  def OnButton(self, event):
    """Called when the Button is clicked"""
    print "\nFrame GetChldren:"
    for child in self.GetChildren():
      print "%s" % repr(child)
      
    print "\nPanel FindWindowById:"
    button = self.panel.FindWindowById(self.btnId)
    print "%s" % repr(button)
    #Change the Button's label
    button.SetLabel("Changed Label")

    print "\nButton GetParent:"
    panel = button.GetParent()
    print "%s" % repr(panel)
    
    print "\nGet the Application Object:"
    app =wx.GetApp()
    print "%s" % repr(app)

    print "\nGet the Frame from the App:"
    frame = app.GetTopWindow()
    print "%s" % repr(frame)

        

if __name__ == "__main__":
  app = MyApp(False)
  app.MainLoop()
