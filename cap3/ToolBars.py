import wx

ART_MAP = { wx.ID_CUT : wx.ART_CUT,
            wx.ID_COPY : wx.ART_COPY,
            wx.ID_PASTE : wx.ART_PASTE }

class EasyToolBar(wx.ToolBar):
  def AddEasyTool(self, id, shortHelp="", longHelp=""):
    """Simplifies adding a tool to the toolbar
    @param id: Stock ID

    """
    assert id in ART_MAP, "Unknown Stock ID"
    art_id = ART_MAP.get(id)
    bmp = wx.ArtProvider.GetBitmap(art_id, wx.ART_TOOLBAR)
    self.AddSimpleTool(id, bmp, shortHelp, longHelp)

class ToolBarFrame(wx.Frame):
  def __init__(self, *args, **kwargs):
    super(ToolBarFrame, self).__init__(*args, **kwargs)
    # Setup the ToolBar
    toolb = EasyToolBar(self)
    toolb.AddEasyTool(wx.ID_CUT)
    toolb.AddEasyTool(wx.ID_COPY)
    toolb.AddEasyTool(wx.ID_PASTE)
    toolb.Realize()
    self.SetToolBar(toolb)
    # Event Handlers
    self.Bind(wx.EVT_TOOL, self.OnToolBar)
  def OnToolBar(self, event):
    print "ToolBarItem Clicked", event.GetId()

class MyApp(wx.App):
  def OnInit(self):
    #como eh a janela principal parent=None
    self.frame = ToolBarFrame(None, title="The ToolBar Frame")
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
      # Setup the Menu (menubar is responsible for managing submenus)
      menub = wx.MenuBar()
      # File Menu
      filem = wx.Menu()
      filem.Append(wx.ID_OPEN, "Open\tCtrl+O")
      menub.Append(filem, "&File")
      # Edit Menu
      editm = wx.Menu()
      #Tab character(\t) followed by "Ctrl+C" setup keyboard shortcut
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
