import wx
import wx.lib.eventStack as eventStack

class EventMgrApp(wx.App, eventStack.AppEventHandlerMixin):
    
  """Application object base class that
    event handler management.
  """
  def __init__(self, *args, **kwargs):
    eventStack.AppEventHandlerMixin.__init__(self)
    wx.App.__init__(self, *args, **kwargs)
  

class EventMgrFrame(wx.Frame):
  """Frame base class that provides event
     handler management.
  """

  def __init__(self,parent, *args, **kwargs):
      super(EventMgrFrame,self).__init__(parent,
                                      *args,
                                      **kwargs)
      
      #Attributes
      self._menu_handlers = []
      self._ui_handlers = []


      #Event Handlers 
      
      self.Bind(wx.EVT_ACTIVATE, self._OnActivate)


  def _OnActivate(self, event):
    """ Pushes/Pops event handlers"""
    app = wx.GetApp()
    active = event.GetActive()
    if active:
      mode = wx.UPDATE_UI_PROCESS_SPECIFIED
      wx.UpdateUIEvent.SetMode(mode)
      self.SetExtraStyle(wx.WS_EX_PROCESS_UI_UPDATES)
      
      # Push this instance handlers
      for handler in self._menu_handlers:
        app.AddUIHandlerForID(*handler)
    else:
      self.SetExtraStyle(0)
      wx.UodateUIEvent.SetMode(wx.UPDATE_UI_PROCESS_ALL)
      # Pop this instance handlers
      for handler in self._menu_handlers:
        app.RemoveHandlerForID(handler[0])
      for handler in self._ui_handlers:
        app.RemoveUIHandlerForID(handler[0])

  def RegisterMenuHandler(self,event_id, handler):
    """Register a MenuEventHandler
    @param event_id: MenuItem ID
    @param handler: Event handler functio
    """
    self._men_handlers.append((event_id, handler))

  def RegisterUpdateUIHandler(sef, event_id, handler):
    """Register a contrl UpdateUI handler
    @param event_id: Control ID
    @param handler: Event handler function
    """
    self._ui_handlers.append((event_id,handler))
 
           

if __name__ == "__main__":
  app = EventMgrApp(False)
  app.MainLoop()
