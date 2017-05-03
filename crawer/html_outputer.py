# coding=utf-8

class Outputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return

        self.datas.append(data)

    def outputHTML(self):
        file_op = open('./craws.html', 'w')

        str = '<html>'
        str += '<head>'
        str += '<meta charset="utf-8">'
        str += '</head>'
        str += '<body>'
        str += '<table>'

        for data in self.datas:
            str += '<tr>'
            str += "<td width='%s'>%s</td>" % ('15%',data['url'].encode('utf-8'))
            str += '<td width=\'%s\'>%s</td>' % ('10%',data['title'].encode('utf-8'))
            str += '<td>%s</td>' % data['summary'].encode('utf-8')
            str += '</tr>'

        str += '</table>'
        str += '</body>'
        str += '</html>'

        file_op.write(str)
        file_op.close()

