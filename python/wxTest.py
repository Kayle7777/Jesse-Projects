import wx

# This is an application object

app = wx.App()

# This is a frame

frame = wx.Frame(None, title="Hello World")

# Show it with this...

frame.Show()

# "Event Main Loop..."

app.MainLoop()
