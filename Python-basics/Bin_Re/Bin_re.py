import re
path = '''<img data-original="http://browser9.qhimg.com/bdm/768_474_0/t010448c46c1ecf7cab.jpg" alt="卡通人物 动漫卡通" title="关键字：卡通人物 动漫卡通" data-realurl="http://browser9.qhimg.com/bdr/__85/t010448c46c1ecf7cab.jpg" src="http://browser9.qhimg.com/bdm/768_474_0/t010448c46c1ecf7cab.jpg" style="display: inline;">
'''
result = re.match(r'<img data-original="http://browser9.qhimg.com/bdm/768_474_0/t010448c46c1ecf7cab.jpg" alt="卡通人物 动漫卡通" title="关键字：卡通人物 动漫卡通" data-realurl="http://browser9.qhimg.com/bdr/__85/t010448c46c1ecf7cab.jpg" src="(.*?)"',path)
print(result.group(1))