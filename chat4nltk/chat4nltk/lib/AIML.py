#def __init__():
    #if __name__ == "__main__":
    #    main()
    
import xml.etree.ElementTree as xmlparser    

class Parser(object):
#    def __init__(self):
#    def main(self):
# !!! na próxima versar fazer a validação por XMLSchema - http://lxml.de/validation.html#xmlschema !!!

    def parse(self, file):
        tree = xmlparser.parse(file)
        root = tree.getroot()

        assert self._isAIML(root) == True
        assert self._isCorrectVersion(root) == True
        pairs = []
        for item in root:
            pairs.append(self._parseCategory(item))
        return pairs

    def _parseCategory(self, category):
        assert self._isCategory(category) == True
        pair = []
        for item in category:
            if str(item.tag) == 'pattern': pair.append(self._parsePattern(item))
            elif str(item.tag) == 'template': pair.append(self._parseTemplate(item))
            else: raise AIMLError(str(item.tag)+': '+str(item.text), 'The file may be ill-formaed.')
        return pair
                        
    def _parsePattern(self, pattern):
        assert self._isPattern(pattern) == True
        pattern = pattern.text
        pattern = pattern.replace('*', '(.*)')
        pattern = pattern.replace('?', r'\?')
        return self._noSpaces(pattern)

    def _parseTemplate(self, template):
        assert self._isTemplate(template) == True
        if template[0].tag == 'random': template = self._parseList(template)
        elif template.text != None: template = [self._parseText(template)]
        else: raise AIMLError(str(item.tag)+': '+str(item.text), 'The file may be ill-formaed.')
        return template

    def _parseList(self, template):
        assert self._isList(template) ==True
        templateList = []
        for item in template[0]: templateList.append(self._parseText(item))
        return templateList

    def _parseText(self, text):
        assert self._isText(text) == True
        phrase = ''
        if text.text != None: phrase = str(text.text)
        for item in text:
            if str(item.tag) == 'star': phrase += str(self._parseStar(item))
            elif str(item.tag) == 'person': phrase += str(self._parsePerson(item))
            else: raise AIMLError(str(item.tag)+': '+str(item.text), 'The file may be ill-formaed.')
        return self._noSpaces(phrase)
            
    def _parsePerson(self, text):
        assert self._isPerson(template) == True    
        if str(text[0].tag) == 'star': reflection = str(self._parseStar(text[0]))
        else: reflection = '%1'
        if str(text.tail) != None: reflection += str(text.tail)
        return reflection
                 
    def _parseStar(self, text):
        assert self._isStar(text) == True
        if str(text.attrib): star = '%'+str(text.attrib['index'])
        else: star = '%1'
        if str(text.tail) != None: star += str(text.tail)
        return star

    def _isStar(self, node):
        if str(node.tag) == 'star': return True
        else: raise AIMLError(str(node.tag), "Expected 'star' and '"+str(node.tag)+"' was found, the file may be ill-formed.")

    def _isPerson(self, node):
        if str(node.tag) == 'person': return True
        else: raise AIMLError(str(node.tag), "Expected 'person' and '"+str(node.tag)+"' was found, the file may be ill-formed.")

    def _isText(self, node):
        if str(node.text) != None: return True
        else: raise AIMLError(str(node.tag), "Expected a 'template' text and '"+str(node.text)+"' was found, the file may be ill-formed.")
        
    def _isList(self, node) :
        if str(node[0].tag) == 'random' and str(node[0][0].tag) == 'li' : return True
        else: raise AIMLError(str(node[0].tag), "Expected 'random' seguido de 'li' and '"+str(node[0].tag)+"' was found, the file may be ill-formed.")
        
    def _isTemplate(self, node):
        if str(node.tag) == 'template': return True
        else: raise AIMLError(str(node.tag), "Expected 'template' and '"+str(node.tag)+"' was found, the file may be ill-formed.")

    def _isPattern(self, node):
        if str(node.tag) == 'pattern': return True
        else: raise AIMLError(str(node.tag), "Expected 'pattern' and '"+str(node.tag)+"' was found, the file may be ill-formed.")

    def _isCategory(self, node):
        if str(node.tag) == 'category': return True
        else: raise AIMLError(str(node.tag), "Expected 'category' and '"+str(node.tag)+"' was found, the file may be ill-formed.")
        
    def _isAIML(self, root):
        if str(root.tag) == 'aiml': return True
        else: raise AIMLError(str(root.tag), 'Not an AIML file')

    def _isCorrectVersion(self, root):
        if str(root.attrib['version']) == 'short': return True
        else: raise AIMLError(str(root.attrib), "Can't parse this version, must use version='short'. See intructions for details.")
                
    def _noSpaces(self, phrase):
        while phrase[0] is ' ': phrase = phrase[1:]
        while phrase[len(phrase)-1] is ' ': phrase = phrase[:-1]
        return phrase

        
class AIMLError(Exception):
    """Basic exception for errors raised by aiml"""
    def __init__(self, nodeInfo, msg=None):
        msg = "An error occured during parsing AIML on %s. %s" % (nodeInfo, msg)
        super(AIMLError, self).__init__(msg)
        self.nodeInfo = nodeInfo

     

