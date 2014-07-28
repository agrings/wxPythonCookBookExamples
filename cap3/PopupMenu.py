import wx

ART_MAP = { wx.ID_CUT : wx.ART_CUT,
            wx.ID_COPY : wx.ART_COPY,
            wx.ID_PASTE : wx.ART_PASTE }

class PopupMenuMixin(object):
  def __init__(self):
    super(PopupMenuMixin, self).__init__()
    
    # Attributes
    self._menu = None
    # Event Handlers
    self.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)
  
  def OnContextMenu(self, event):
    """Creates and shows the Menu"""
    if self._menu is not None:
      self._menu.Destroy()
    self._menu = wx.Menu()
    self.CreateContextMenu(self._menu)
    self.PopupMenu(self._menu)

  def CreateContextMenu(self, menu):
    """Override in subclass to create the menu"""
    raise NotImplementedError

class PanelWithMenu(wx.Panel, PopupMenuMixin):
  def __init__(self, parent):
    wx.Panel.__init__(self, parent)
    PopupMenuMixin.__init__(self)
  
  def CreateContextMenu(self, menu):
    """PopupMenuMixin Implementation"""
    menu.Append(wx.ID_CUT)
    menu.Append(wx.ID_COPY)
    menu.Append(wx.ID_PASTE)

class ContextMenuFrame(wx.Frame):
  def __init__(self, *args, **kwargs):
    super(ContextMenuFrame, self).__init__(*args, **kwargs)
    
    self.panel = PanelWithMenu(self)
    self.txtctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        
    # Layout
    sizer = wx.BoxSizer(wx.HORIZONTAL)
    sizer.Add(self.txtctrl, 1, wx.EXPAND)
    self.panel.SetSizer(sizer)



class MyApp(wx.App):
  def OnInit(self):
    #como eh a janela principal parent=None
    self.frame = ContextMenuFrame(None, title="The Context Menu Frame")
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
