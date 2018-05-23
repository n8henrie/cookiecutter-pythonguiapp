import wx

from {{ cookiecutter.repo_name }}.{{ cookiecutter.repo_name }} import MainFrame

if __name__ == '__main__':
    app = wx.App()
    frm = MainFrame(None, title='This is the title')
    frm.Show()
    app.MainLoop()
