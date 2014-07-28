import wx
import wx.lib.platebtn as pbtn
import wx.lib.agw.gradientbutton as gbtn

ID_READ_ONLY = wx.NewId()

class MyApp(wx.App):
  def OnInit(self):
    #como eh a janela principal parent=None
    self.frame = MenuFrame(None, title="The Main Frame")
    #Configura o frame como a janela no topo da aplicacao
    self.SetTopWindow(self.frame)
    self.frame.Show()

    return True


class MenuFrame(wx.Frame):
  def __init__(self, *args, **kwargs):
      super(MenuFrame,self).__init__(*args, **kwargs)
      
      #Attributes
      self.panel = wx.Panel(self)
      self.txtctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        
      # Layout
      sizer = wx.BoxSizer(wx.HORIZONTAL)
      sizer.Add(self.txtctrl, 1, wx.EXPAND)
      self.panel.SetSizer(sizer)
      self.CreateStatusBar() # For output display
      # Setup the Menu
      menub = wx.MenuBar()
      # File Menu
      filem = wx.Menu()
      filem.Append(wx.ID_OPEN, "Open\tCtrl+O")
      menub.Append(filem, "&File")
      # Edit Menu
      editm = wx.Menu()
      editm.Append(wx.ID_COPY, "Copy\tCtrl+C")
      editm.Append(wx.ID_CUT, "Cut\tCtrl+X")
      editm.Append(wx.ID_PASTE, "Paste\tCtrl+V")
      editm.AppendSeparator()
      editm.Append(ID_READ_ONLY, "Read Only", kind=wx.ITEM_CHECK)
      menub.Append(editm, "E&dit")
      self.SetMenuBar(menub)
      # Event Handlers
      self.Bind(wx.EVT_MENU, self.OnMenu)

  def OnMenu(self, event):
    """Handle menu clicks"""
    evt_id = event.GetId()
    actions = { wx.ID_COPY : self.txtctrl.Copy,
                wx.ID_CUT  : self.txtctrl.Cut,
                wx.ID_PASTE : self.txtctrl.Paste }
    action = actions.get(evt_id, None)
    if action:
      action()
    elif evt_id == ID_READ_ONLY:
      # Toggle enabled state
      self.txtctrl.Enable(not self.txtctrl.Enabled)
    elif evt_id == wx.ID_OPEN:
      dlg = wx.FileDialog(self, "Open File", style=wx.FD_OPEN)
      if dlg.ShowModal() == wx.ID_OK:
        fname = dlg.GetPath()
        handle = open(fname, 'r')
        self.txtctrl.SetValue(handle.read())
        handle.close()
    else:
      event.Skip()

if __name__ == "__main__":
  app = MyApp(False)
  app.MainLoop()
