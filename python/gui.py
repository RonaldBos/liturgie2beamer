import sys
import wx
from liturgie import convertStream
from opensong import OpenSongLibrary
from antlr4.InputStream import InputStream

def removeNonAscii(s):
    nonAscii = "".join(i for i in s if ord(i) < 128)
    # lexer returns only lower-case tokens
    return nonAscii.lower()

class RedirectText(object):
    def __init__(self,aWxTextCtrl):
        self.out=aWxTextCtrl

    def write(self,string):
        self.out.WriteText(string)
 
class MyForm(wx.Frame):
 
    def __init__(self):
        self.database = None
        
        wx.Frame.__init__(self, None, wx.ID_ANY, "Liedteksten uit liturgie", size=(800, 800))
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        self.inText = wx.TextCtrl(panel, wx.ID_ABORT, size=(800, 600), style = wx.TE_MULTILINE|wx.HSCROLL)
        self.stdoutText = wx.TextCtrl(panel, wx.ID_ANY, size=(800, 600), style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        stderrText = wx.TextCtrl(panel, wx.ID_ANY, size=(800, 600), style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        stderrText.SetForegroundColour("#555555")
        buttonGenerate = wx.Button(panel, wx.ID_ANY, 'Genereer liedteksten')
        buttonGenerate.SetDefault()
        self.Bind(wx.EVT_BUTTON, self.onButton, buttonGenerate)

        # In/out hbox1
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        vbox11 = wx.BoxSizer(wx.VERTICAL)
        labelLiturgie = wx.StaticText(panel, wx.ID_ANY, 'Liturgie (invoer)')
        vbox11.Add(labelLiturgie, 0, wx.LEFT, 5)
        vbox11.Add(self.inText, 1, wx.ALL|wx.EXPAND, 5)
        vbox12 = wx.BoxSizer(wx.VERTICAL)
        labelUitvoer = wx.StaticText(panel, wx.ID_ANY, 'Liedteksten (uitvoer)')
        vbox12.Add(labelUitvoer, 0, wx.LEFT, 5)
        vbox12.Add(self.stdoutText, 1, wx.ALL|wx.EXPAND, 5)
        hbox1.Add(vbox11, 1, wx.ALL|wx.EXPAND, 5)
        hbox1.Add(vbox12, 1, wx.ALL|wx.EXPAND, 5)
        
        # Console hbox1
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(stderrText, 1, wx.ALL|wx.EXPAND, 5)
        hbox2.Add(buttonGenerate, 0, wx.ALL|wx.EXPAND, 5)

        # Top-level hbox1
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1, 5, wx.ALL|wx.EXPAND, 0)
        vbox.Add(hbox2, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(vbox)
        
        # Add a menu bar
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Afsluiten\tCtrl+Q', 'Applicatie sluiten')
        editMenu = wx.Menu()
        copy = editMenu.Append(wx.ID_COPY, 'Kopieren\tCtrl+C', 'Kopieer selectie')
        paste = editMenu.Append(wx.ID_PASTE, 'Plakken\tCtrl+V', 'Plak inhoud van klembord')
        selectAll = editMenu.Append(wx.ID_SELECTALL, 'Alles selecteren\tCtrl+A', 'Selecteer alles')
        undo = editMenu.Append(wx.ID_UNDO, 'Ongedaan maken\tCtrl+Z', 'Ongedaan maken')
        aboutMenu = wx.Menu()
        about = aboutMenu.Append(wx.ID_ABOUT, '&Over dit programma', 'Informatie over dit programma')
        menubar.Append(fileMenu, '&Bestand')
        menubar.Append(editMenu, 'Be&werken')
        menubar.Append(aboutMenu, '&Hulp')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.onQuit, fitem)
        self.Bind(wx.EVT_MENU, self.onSelectAll, selectAll)
        self.Bind(wx.EVT_MENU, self.onUndo, undo)
        self.Bind(wx.EVT_MENU, self.onAbout, about)

        # redirect text here
        sys.stdout = RedirectText(self.stdoutText)
        sys.stderr = RedirectText(stderrText)
        
    def onButton(self, event):
        # clear output text
        self.stdoutText.Clear()
        
        # read in database
        if self.database is None:
            sys.stderr.write("Reading song database...\n")
            self.database = OpenSongLibrary("..\\songs\\")

        str = self.inText.GetValue()
        instream = InputStream(removeNonAscii(str))
        convertStream(instream, self.database)
        
    def onQuit(self, event):
        self.Close()
        
    def onSelectAll(self, event):
        text = self.FindFocus()
        if text is not None:
            text.SelectAll()
            
    def onUndo(self, event):
        text = self.FindFocus()
        if text is not None:
            text.Undo()
            
    def onAbout(self, event):
        description = """Liturgie2Beamer genereert liedteksten op basis
van een liturgie en een OpenSong database."""

        license = """Liturgie2Beamer is free software; you can redistribute 
it and/or modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation; either version 2 of the License, 
or (at your option) any later version.

File Hunter is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the GNU General Public License for more details. You should have 
received a copy of the GNU General Public License along with File Hunter; 
if not, write to the Free Software Foundation, Inc., 59 Temple Place, 
Suite 330, Boston, MA  02111-1307  USA"""

        info = wx.AboutDialogInfo()

        #info.SetIcon(wx.Icon('hunter.png', wx.BITMAP_TYPE_PNG))
        info.SetName('Liturgie2Beamer')
        info.SetVersion('0.1')
        info.SetDescription(description)
        info.SetCopyright('(C) 2015 Ronald Bos <ronald.bos.msc@gmail.com>')
        info.SetWebSite('https://github.com/RonaldBos/liturgie2beamer/')
        #info.SetLicence(license)
        #info.AddDeveloper('Ronald Bos')
        #info.AddDocWriter('Jan Bodnar')
        #info.AddArtist('The Tango crew')
        #info.AddTranslator('Jan Bodnar')

        wx.AboutBox(info)
        
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()
