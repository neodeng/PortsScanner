#!/usr/bin/env python
#encoding: UTF-8

"""
Name:         PortsScanner
Version:      1.0
Requirements: Python2.7 scapy wxPython

Author:       neodeng
Created:      03/26/2016
Email:        dyq9109@163.com

MVC: 
     Model:     
     View:
     Controller:
"""

import wx 
import os

class Frame(wx.Frame):
    """ GUI of the PortsScanner Frame"""
    
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'PortsScanner', size=(500,300))
        
        panel = wx.Panel(self)
        wx.StaticText(panel, -1, 'IP地址', (50,50))
        ip = wx.TextCtrl(panel, -1, '', (110,48), (150,25))
        ip.SetInsertionPoint(0)
        wx.StaticText(panel, -1, '(示例:192.168.1.2/24)', (270,50))
        
        wx.StaticText(panel, -1, '扫描方式', (50,90))
        syn = wx.RadioButton(panel, -1, 'SYN', (120,90), style=wx.RB_GROUP)
        tcp_con = wx.RadioButton(panel, -1, 'TCP connection', (200,90))
        
        wx.StaticText(panel, -1, '线程数', (350,90))
        nThread = wx.TextCtrl(panel, -1, '4', (400,88), (30,25))
        
        wx.StaticText(panel, -1, '输出路径', (50,130))
        oFile = wx.TextCtrl(panel, -1, '', (110,128), (250,25))
        
        wx.StaticText(panel, -1, '添加端口', (50,170))
        
                
class PortsScanner(wx.App):
    """ App of PortsScanner"""
    
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
                 
if __name__ == '__main__':
    app = PortsScanner()
    app.MainLoop()
        


