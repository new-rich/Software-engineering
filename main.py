import wx
from views import frame

class EditorApp(wx.App):
    def OnInit(self):
        frame().Show()
        return True

if __name__ == "__main__":
    app = EditorApp()
    app.MainLoop()