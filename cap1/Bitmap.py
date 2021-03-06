import os
import wx

class MyApp(wx.App):
  def OnInit(self):
    #como eh a janela principal parent=None
    self.frame = MyFrame(None, title="Bitmaps")
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
      img_path=os.path.abspath("./face-grin.png")
      bitmap = wx.Bitmap(img_path,type=wx.BITMAP_TYPE_PNG)
      self.bitmap = wx.StaticBitmap(self.panel, bitmap=bitmap)

if __name__ == "__main__":
  app = MyApp(False)
  app.MainLoop()
