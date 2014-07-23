import wx
import wx.lib.newevent

#Our first custom event
MyEvent, EVT_MY_EVENT = wx.lib.newevent.NewCommandEvent()

#Our second custom event
myEVT_TIME_EVENT = wx.NewEventType()
EVT_MY_TIME_EVENT = wx.PyEventBinder(myEVT_TIME_EVENT, 1)

class MyTimeEvent(wx.PyCommandEvent):
  def __init__(self,  id=0, time="12:00:00"):
    evttype = myEVT_TIME_EVENT
    super(MyTimeEvent, self).__init__(evttype, id)

    # Attributes
    self.time = time
    
    print "Foi"

  def GetTime(self):
    return self.time

class MyApp(wx.App):
  def OnInit(self):
    #como eh a janela principal parent=None
    self.frame = MouseFrame(None, title="Events")
    #Configura o frame como a janela no topo da aplicacao
    self.SetTopWindow(self.frame)
    self.frame.Show()

    return True

class MouseFrame(wx.Frame):
  def __init__(self,parent, *args, **kwargs):
      super(MouseFrame,self).__init__(parent,
                                      *args,
                                      **kwargs)
      
      #Attributes
      self.panel = wx.Panel(self) #Um frame sempre contem um painel
      self.btn = wx.Button(self.panel)

      #Event Handlers 
      
      self.panel.Bind(wx.EVT_ENTER_WINDOW, self.OnEnter)
      self.panel.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
      
      self.btn.Bind(wx.EVT_BUTTON, self.button1Click)

  def button1Click(self, event):
    event = MyTimeEvent(myEVT_TIME_EVENT, self.GetId())
    wx.PostEvent(self, event)
   
  def OnEnter(self,event):
    """Called when the mouse enters the panel """
    self.btn.SetForegroundColour(wx.BLACK)
    self.btn.SetLabel("EVT_ENTER_WINDOW")
    self.btn.SetInitialSize()
  

  def OnLeftUp(self, event):
    """Called  for left clicks on the panel """
    position = event.GetPosition()
    self.btn.SetLabel("EVT_LEFT_UP")
    # Move the button
    self.btn.SetPosition(position - (25,25))



if __name__ == "__main__":
  app = MyApp(False)
  app.MainLoop()
