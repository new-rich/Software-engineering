
import wx
import os
from .webview import Webview

class TextEditor(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self._init_ui()

    def _init_ui(self):
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_title()
        self._init_webview()
        self.SetSizer(self.main_sizer)


    def _init_title(self):
        self.main_sizer.AddSpacer(20)
        self.tc_title = wx.TextCtrl(self, style=0)
        self.main_sizer.Add(self.tc_title, flag=wx.EXPAND,border=15)
        self.main_sizer.AddSpacer(20)


    def _init_webview(self):
        root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        editor_url = f"file://{os.path.join(root_path, 'assert', 'text_editor', 'index.html')}"
        self.webview=Webview(self)
        self.webview.load_url(editor_url)

        self.main_sizer.Add(self.webview, flag=wx.EXPAND, proportion=1)
"""
import wx
import os
import wx.html2

class TextEditor(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self._init_ui()

    def _init_ui(self):
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self._init_webview()
        self.SetSizer(self.main_sizer)

    def _init_webview(self):
        root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        editor_url = os.path.join(root_path, 'assert', 'text_editor', 'index.html')

        self.webview = wx.html2.WebView.New(self)
        self.webview.SetPage("<html><title>a</title></html>","")

        self.main_sizer.Add(self.webview, flag=wx.EXPAND, proportion=1)
"""