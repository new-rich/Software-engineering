import wx
import wx.aui
from .editor import TextEditor

class frame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Editor',size=(800,600))
        self.aui_manager = wx.aui.AuiManager(self,wx.aui.AUI_MGR_TRANSPARENT_HINT)
        self.editor_panel = TextEditor(self)

        self.aui_manager.AddPane(self.editor_panel, self._get_default_pane_info().CenterPane().Position(0).BestSize(400,-1))
        self.aui_manager.GetArtProvider().SetMetric(wx.aui.AUI_DOCKART_SASH_SIZE,0)
        self.aui_manager.Update()
        #self.Maximize(True)
        self._register_listeners()

    def _get_default_pane_info(self):
        return wx.aui.AuiPaneInfo().CaptionVisible(False).PaneBorder(False).CloseButton(False).PinButton(False).Gripper(
            False)

    def on_frame_closing(self, e):
        self.aui_manager.UnInit()
        del self.aui_manager
        self.Destroy()

    def _register_listeners(self):
        self.Bind(wx.EVT_CLOSE, self.on_frame_closing)