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

class ChoicePanel(wx.Panel):
  def __init__(self, parent):
    super(ChoicePanel, self).__init__(parent)

    #Attributes
    items = ["item 1", "item 2", "item 3"]
    self.choice = wx.Choice(self,choices=items)
    self.choice.SetSelection(0)

    # Layout
    sizer = wx.BoxSizer()
    sizer.Add(self.choice,1, wx.EXPAND|wx.ALL, 20)
    self.SetSizer(sizer)
    #Event Handlers
    self.Bind(wx.EVT_CHOICE, self.OnChoice)
  
  def OnChoice(self, event):
    selection = self.choice.GetStringSelection()
    index = self.choice.GetSelection()
    print "Selected Item: %d '%s'" % (index, selection)

class MyFrame(wx.Frame):
  def __init__(self,parent, id=wx.ID_ANY, title="",
               pos=wx.DefaultPosition, size=wx.DefaultSize,
               style=wx.DEFAULT_FRAME_STYLE,
               name="MyFrame"):
      super(MyFrame,self).__init__(parent,id,title,
                                   pos,size,style,name)
      
      #Attributes
      self.panel = ChoicePanel(self) #Um frame sempre contem um painel
        

if __name__ == "__main__":
  app = MyApp(False)
  app.MainLoop()
