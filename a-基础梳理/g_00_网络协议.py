"""
@author: yrmt
@contact: butanoler@gmail.com
@file: g_00_协议.py
@time: 2019/9/2
"""
# https://www.cnblogs.com/awkflf11/p/9190309.html
# # 网络7层协议 (OSI七层协议模型)
# 01.物理层:
#   定义物理设备标准(网线的接口类型、光纤的接口类型、各种传输介质的传输速率...)
#   它的主要作用是传输比特流，这一层的数据叫做比特。
#   eg: 以太网路卡 · 调制解调器 · 电力线通信(PLC) · SONET/SDH（光同步数字传输网） · G.709（光传输网络） · 光导纤维 · 同轴电缆 · 双绞线
# 02.数据链路层:
#   定义了如何让格式化数据以进行传输，以及如何让控制对物理介质的访问
#   这一层通常还提供错误检测和纠正，以确保数据的可靠传输
#   eg: Wi-Fi(IEEE 802.11) · WiMAX(IEEE 802.16) ·ATM · DTM · 令牌环 · 以太网路 ·FDDI · 帧中继 · GPRS · EVDO
#   · HSPA · HDLC · PPP · L2TP · ISDN ·STP
# 03.网络层:
#   在位于不同地理位置的网络中的两个主机系统之间提供连接和路径选择，
#   Internet的发展使得从世界各站点访问信息的用户数大大增加，而网络层正是管理这种连接的层。
#   eg: IP (IPv4 · IPv6) · ICMP · ICMPv6 · IGMP ·IS-IS · IPsec · BGP · RIP · OSPF ·ARP · RARP
# 04.传输层:
#   定义了一些传输数据的协议和端口号（WWW端口80等），
#   主要是将从下层接收的数据进行分段和传输，到达目的地址后再进行重组，常常把这一层数据叫做段。
#   eg: TCP · UDP · TLS · DCCP · SCTP ·RSVP · PPTP
# 05.会话层:
#   通过传输层（端口号：传输端口与接收端口）建立数据传输的通路，
#   主要在你的系统之间发起会话或者接受会话请求（设备之间需要互相认识可以是IP也可以是MAC或者是主机名）。
#   eg: ADSP ·ASP ·H.245·ISO-SP ·iSNS ·NetBIOS ·PAP ·RPC ·RTCP ·SMPP ·SCP ·SSH ·ZIP ·SDP（具有会话层功能）
# 06.表示层:
#   可确保一个系统的应用层所发送的信息可以被另一个系统的应用层读取。
#   eg: HTTP/HTML · FTP · Telnet · ASN.1（具有表示层功能）
# 07.应用层:
#   是最靠近用户的OSI层，这一层为用户的应用程序（例如电子邮件、文件传输和终端仿真）提供网络服务。
#   eg: DHCP · DNS · FTP · Gopher ·GTP · HTTP · IMAP4 · IRC · NNTP · NTP · POP3 · RPC · RTCP · RTP ·RTSP · SIP
#   · SMTP ·SNMP · SSH · SDP · SOAP .STUN. SSDP · TELNET · XMPP


# # 四层网络模型(TCP/IP协议模型)
# 应用层  对应 七层中应用层，表示层，会话层
# 运输层  对应 七层中运输层
# 网际层  对应 七层中网络层
# 网络接口层 对应 七层中数据链路层，物理层

# 五层网络模型
# 应用层  对应 七层中应用层，表示层，会话层
# 运输层  对应 七层中运输层
# 网际层  对应 七层中网络层
# 数据链路层 对应 七层中数据链路层
# 物理层  对应 七层中数据物理层
