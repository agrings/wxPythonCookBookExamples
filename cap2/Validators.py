import wx
import sys

class IntRangeValidator(wx.PyValidator):
  """An integer range validator fpor a TxtCtrl """

  def __init__(self, min_=0, max_=sys.maxint):
    """Initialize the validator
    @keyword min: min value to accept
    @keyword max: max value to accept
    """
    super(IntRangeValidator, self).__init__()
    assert min_ >= 0, "Minumum Valule must be >= 0"
    self._min = min_ 
    self._max = max_
    #Event management
    self.Bind(wx.EVT_CHAR, self.OnChar)

  def Clone(self):
    """Required override"""
    return IntRangeValidator(self._min, self._max)

  def Validate(self, win):
    """Override called to validate the window's value.
     @return: bool
    """

    txtCtrl = self.GetWindow()
    val = txtCtrl.GetValue()
    isValid = False
    if val.isdigit():
      digit = int(val)
    if digit >= self._min and digit <= self._max:
      isValid = True
    if not isValid:
      # Notify the user of the invalid value
      msg = "Value must be between %d and %d" % \
            (self._min, self._max)
      wx.MessageBox(msg,
                    "Invalid Value",
                    style=wx.OK|wx.ICON_ERROR)
    return isValid

  def OnChar(self, event):
    txtCtrl = self.GetWindow()
    key = event.GetKeyCode()
    isDigit = False
    if key < 256:
      isDigit = chr(key).isdigit()
    if key in (wx.WXK_RETURN,
               wx.WXK_DELETE,
               wx.WXK_BACK) or \
       key > 255 or isDigit:
  
      if isDigit:
        # Check if in range
        val = txtCtrl.GetValue()
        digit = chr(key)
        pos = txtCtrl.GetInsertionPoint()
        if pos == len(val):
          val += digit
        else:
             val = val[:pos] + digit + val[pos:]
        val = int(val)
        if val < self._min or val > self._max:
          if not wx.Validator_IsSilent():
            wx.Bell()
            print "Ding"
          return
      event.Skip()
      return
    if not wx.Validator_IsSilent():
      # Beep to warn about invalid input
      wx.Bell()
      print "Ding 2"
    return

  def TransferToWindow(self):
    """Overridden to skip data transfer"""
    return True

  def TransferFromWindow(self):
    """Overridden to skip data transfer"""
    return True



class TextValidateDialog(wx.Dialog):
  def __init__(self, parent, *args, **kargs):
    super(TextValidateDialog, self).__init__(parent,
                                     *args,
                                     **kargs)
    #Attributes
    self.panel = wx.Panel(self)
    self.txtctrl = wx.TextCtrl(self, -1, "", validator = IntRangeValidator(4,8)) 

    buttons = wx.StdDialogButtonSizer() #wx.BoxSizer(wx.HORIZONTAL)
    b = wx.Button(self, wx.ID_OK, "OK")
    b.SetDefault()
    buttons.AddButton(b)
    buttons.AddButton(wx.Button(self, wx.ID_CANCEL, "Cancel"))
    buttons.Realize()

    #Layout
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(self.txtctrl)
    sizer.Add(buttons)
    self.panel.SetSizer(sizer)




class MyApp(wx.App):

  def OnInit(self):
    #como eh a janela principal parent=None
    f = wx.Frame(parent=None)
    f.Show()
    dlg=TextValidateDialog(f)
    dlg.ShowModal()
    dlg.Destroy()

    return True
    
if __name__ == "__main__":
  app = MyApp(False)
  app.MainLoop()
