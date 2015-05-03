# coding: utf-8

import xbmcgui,xbmcplugin

plugin_handle = int(sys.argv[1])
_id = 'plugin.video.direto-master'
_icondir = "special://home/addons/" + _id + "/icons/"

def menu():
    addDir('PORTUGAL',’url’,1)
    addDir(‘CANADA',’url’,2)

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)

# Entertainment
add_video_item('https://glblvhalifax-lh.akamaihd.net/i/glblvHalifax_1@119843/master.m3u8',{ 'title': 'Global TV Halifax HD'}, '%s/global_tv_halifax.png'% _icondir)

add_video_item('https://glblvestu-f.akamaihd.net/i/glblvPSTu_1@80128/master.m3u8',{ 'title': 'Global TV Vancouver HD'}, '%s/global_tv_vancouver.png'% _icondir)

add_video_item('https://glblvestu-f.akamaihd.net/i/glblvestu_1@78149/master.m3u8',{ 'title': 'Global TV Toronto HD'}, '%s/global_tv_toronto.png'% _icondir)

add_video_item('rtmp://54.85.197.21:1935/live/news live=1 timeout=15',{ 'title': 'CHCH Hamilton HD'}, '%s/CHCH.png'% _icondir)

add_video_item('http://198.179.31.198/live/2059.high.stream/2059.high.stream/index.m3u8',{ 'title': 'CFCN CTV Lethbridge'}, '%s/CTV_Lethbridge.png'% _icondir)

add_video_item('http://198.179.31.198/live/2053.high.stream/2053.high.stream/index.m3u8',{ 'title': 'CFRN CTV Edmonton'}, '%s/CTV_Edmonton.png'% _icondir)

add_video_item('http://198.179.31.198/live/2062.high.stream/2062.high.stream/index.m3u8',{ 'title': 'CICC CTV Yorkton'}, '%s/CTV_Yorkton.png'% _icondir)

add_video_item('http://198.179.31.198/live/2056.high.stream/2056.high.stream/index.m3u8',{ 'title': 'CKCK CTV Regina'}, '%s/CTV_Regina.png'% _icondir)

add_video_item('http://tscstreaming-lh.akamaihd.net/i/TSCLiveStreaming_1@91031/index_3_av-p.m3u8',{ 'title': 'The Shopping Channel HD'}, '%s/tsc.png'% _icondir)

add_video_item('https://history-lh.akamaihd.net/i/History_1@156885/master.m3u8',{ 'title': 'History (Canada) HD'}, '%s/history.png'% _icondir)



# News
add_video_item('http://bcoveliveios-i.akamaihd.net/hls/live/207737/1942203455001/nat/master_Layer5.m3u8',{ 'title': 'Weather Network National HD'}, '%s/twn.png' % _icondir)

#DOWN add_video_item('http://bcoveliveios-i.akamaihd.net/hls/live/207737/1942203455001/atl/master.m3u8',{ 'title': 'Weather Network Atlantic HD'}, '%s/twn.png' % _icondir)

add_video_item('rtmp://a.cdn.newschat.tv/edge playpath=cbc_live swfUrl=http://msnbclive.eu/player.swf pageUrl=http://www.livenewschat.eu/canada/ live=1',{ 'title': 'CBC News'}, '%s/cbcnewsnetwork.png' % _icondir)

add_video_item('http://ams-lp3.9c9media.com/hls-live/livepkgr/_definst_/liveeventNoDRM/cp24Open8.m3u8',{ 'title': 'CP24 News HD'}, '%s/CP24.png' % _icondir)

add_video_item('http://ams-lp2.9c9media.com/hls-live/livepkgr/_definst_/liveeventNoDRM/ctvnewsOpen8.m3u8',{ 'title': 'CTV News HD'}, '%s/ctv_news.png' % _icondir)

add_video_item('http://ams-lp10.9c9media.com/hls-live/livepkgr/_definst_/liveNews/News18.m3u8',{ 'title': 'CTV News Live Feed 1 HD'}, '%s/CTVNews.png' % _icondir)

add_video_item('http://ams-lp7.9c9media.com/hls-live/livepkgr/_definst_/liveNews/News28.m3u8',{ 'title': 'CTV News Live Feed 2 HD'}, '%s/CTVNews.png' % _icondir)

add_video_item('http://ams-lp6.9c9media.com/hls-live/livepkgr/_definst_/liveNews/News38.m3u8',{ 'title': 'CTV News Live Feed 3 HD'}, '%s/CTVNews.png' % _icondir)

add_video_item('http://ams-lp5.9c9media.com/hls-live/livepkgr/_definst_/liveNews/News48.m3u8',{ 'title': 'CTV News Live Feed 4 HD'}, '%s/CTVNews.png' % _icondir)

# Sports
add_video_item('http://nlds187.cdnak.neulion.com/nlds/sportsnetnow/sn_360/as/live/sn_360_hd_ipad.m3u8',{ 'title': 'Sportsnet 360 HD'}, '%s/sportsnet_360.png'% _icondir)

add_video_item('http://ams-lp5.9c9media.com/hls-live/livepkgr/_definst_/liveeventNoDRM/tsnOpen8.m3u8',{ 'title': 'TSN1 HD'}, '%s/tsn_1.png'% _icondir)

add_video_item('http://ams-lp7.9c9media.com/hls-live/livepkgr/_definst_/liveeventNoDRM/TSN2Open8.m3u8',{ 'title': 'TSN2 HD'}, '%s/tsn_2.png'% _icondir)

add_video_item('http://ams-lp1.9c9media.com/hls-live/livepkgr/_definst_/liveeventNoDRM/TSN3Open8.m3u8',{ 'title': 'TSN3 HD)'}, '%s/tsn_3.png'% _icondir)

add_video_item('http://ams-lp2.9c9media.com/hls-live/livepkgr/_definst_/liveeventNoDRM/TSN4Open8.m3u8',{ 'title': 'TSN4 HD'}, '%s/tsn_4.png'% _icondir)

add_video_item('http://ams-lp3.9c9media.com/hls-live/livepkgr/_definst_/liveeventNoDRM/TSN5Open8.m3u8',{ 'title': 'TSN5 HD'}, '%s/tsn_5.png'% _icondir)

add_video_item('http://ams-lp9.9c9media.com/hls-live/livepkgr/_definst_/liveeventNoDRM/RDSOpen8.m3u8',{ 'title': 'RDS (French) HD'}, '%s/rds.png'% _icondir)

add_video_item('http://ams-lp10.9c9media.com/hls-live/livepkgr/_definst_/liveeventNoDRM/RDS2Open8.m3u8',{ 'title': 'RDS2 (French) HD'}, '%s/rds2.png'% _icondir)

add_video_item('http://ams-lp11.9c9media.com/hls-live/livepkgr/_definst_/liveeventNoDRM/RDSiOpen8.m3u8',{ 'title': 'RDS Info(French) HD'}, '%s/rds_info.png'% _icondir)

add_video_item('rtmp://cp39414.live.edgefcs.net/live/event1@9756',{ 'title': 'TVA Sports (French)'}, '%s/TVA_Sports.png'% _icondir)

xbmcplugin.endOfDirectory(plugin_handle)
xbmc.executebuiltin("Container.SetViewMode(500)")

