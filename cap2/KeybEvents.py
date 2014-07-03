import wx
import curses

class MyApp(wx.App):
  def OnInit(self):
    #como eh a janela principal parent=None
    self.frame = MyFrame(None, title="Events")
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
      self.txtctrl = wx.TextCtrl(self.panel,
                                 style=wx.TE_MULTILINE)
      #Layout
      sizer = wx.BoxSizer(wx.HORIZONTAL)
      sizer.Add(self.txtctrl, 1 , wx.EXPAND)
      self.panel.SetSizer(sizer)
      self.CreateStatusBar() # For output display
      #Event Handlers 
      
      self.txtctrl.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
      self.txtctrl.Bind(wx.EVT_CHAR, self.OnChar)
      self.txtctrl.Bind(wx.EVT_KEY_UP, self.OnKeyUp)

  def OnKeyDown(self, event):
    """KeyDown event is sent first """
    print "OnKeyDown Called"
    #Get information about the event and log it to
    # the StatusBat for display.
    key_code = event.GetKeyCode()
    raw_code = event.GetRawKeyCode()
    modifiers = event.GetModifiers()
    msg = "key%d,raw:%d, modifiers:%d" % \
          (key_code, raw_code, modifiers)
    self.PushStatusText("KeyDown: " + msg)
    #Must skip the event to allow OnChar to be called
    event.Skip()
    
  def OnChar(self, event):
    """The Char event comes second and is
       where the character associated with the
       key is put into the control.
    """
    print "OnChar Called"
    key_code = event.GetKeyCode()
    modifiers = event.GetModifiers()
    # Beep at tje iuser of tje Shift key is down
    # and disallow input.
    if modifiers & wx.MOD_SHIFT:
      #wx.Bell()
      curses.beep()

    elif chr(key_code) in "aeiou":
      #When a wowel is pressed append a
      # question mark to the end.
      self.txtctrl.AppendText("?")
    else:
      # Let the text fo in to the buffer
      event.Skip()

  def OnKeyUp(self,event):
    """KeyUp comes last"""
    print "OnKeyUp Called"
    event.Skip()

if __name__ == "__main__":
  app = MyApp(False)
  app.MainLoop()
