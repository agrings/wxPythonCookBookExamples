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

      #Setup
      ok_btn = wx.Button(self.panel, wx.ID_OK)
      cancel_btn = wx.Button(self.panel, wx.ID_CANCEL, pos=(100,0))
      
      menu_bar = wx.MenuBar()
      edit_menu = wx.Menu()
      edit_menu.Append(wx.NewId(), "Test")
      edit_menu.Append(wx.ID_PREFERENCES)
      menu_bar.Append(edit_menu,"Edit")
      self.SetMenuBar(menu_bar) 

        

if __name__ == "__main__":
  app = MyApp(False)
  app.MainLoop()
