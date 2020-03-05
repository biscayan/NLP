import re

class Porter:
    
    def VC_count (self,stem):
        vowel=['a','e','i','o','u'] #vowel list
        consonant=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'] #consonant list
        VC_list=[]
        
        for i in range(len(stem)):
            if stem[i] in vowel:
                if stem[i+1] in consonant:
                    VC_list.append(stem[i])
                    VC_list.append(stem[i+1])
                
        return len(VC_list)/2

    # m = the number of 'VC' sequence 

    def m_no_condition(self,word,affix,new_affix):
        matching=word.rfind(affix)
        stem=word[:matching]
        new_word=stem+new_affix
        return new_word        

    def m_over0(self,word,affix,new_affix):
        matching=word.rfind(affix)
        stem=word[:matching]
        
        if self.VC_count(stem)>0:
            new_word=stem+new_affix
            return new_word
        else:
            return word

    def m_over1(self,word,affix,new_affix):
        matching=word.rfind(affix)
        stem=word[:matching]
        
        if self.VC_count(stem)>1:
            new_word=stem+new_affix
            return new_word
        else:
            return word

    def step_1a(self,word):
        if word.endswith('sses'):
            word=self.m_no_condition(word,'sses','ss')   

        elif word.endswith('ies'):
            word=self.m_no_condition(word,'ies','i')
            
        elif word.endswith('ss'):
            word=self.m_no_condition(word,'ss','ss')
            
        elif word.endswith('s'):
            word=self.m_no_condition(word,'s','')
            
        return word

    def step_1b(self,word):
        if word.endswith('eed'):
            word=self.m_over0(word,'eed','ee')
            
        return word
  
    def step_2(self,word):
        if word.endswith('ational'):
            word=self.m_over0(word,'ational','ate')
            
        elif word.endswith('tional'):
            word=self.m_over0(word,'tional','tion')

        elif word.endswith('enci'):
            word=self.m_over0(word,'enci','ence')

        elif word.endswith('anci'):
            word=self.m_over0(word,'anci','ance')
            
        elif word.endswith('izer'):
            word=self.m_over0(word,'izer','ize')

        elif word.endswith('abli'):
            word=self.m_over0(word,'abli','able')

        elif word.endswith('alli'):
            word=self.m_over0(word,'alli','al')
            
        elif word.endswith('entli'):
            word=self.m_over0(word,'entli','ent')

        elif word.endswith('eli'):
            word=self.m_over0(word,'eli','e')

        elif word.endswith('ousli'):
            word=self.m_over0(word,'ousli','ous')

        elif word.endswith('ization'):
            word=self.m_over0(word,'ization','ize')

        elif word.endswith('ation'):
            word=self.m_over0(word,'ation','ate')

        elif word.endswith('ator'):
            word=self.m_over0(word,'ator','ate')

        elif word.endswith('alism'):
            word=self.m_over0(word,'alism','al')

        elif word.endswith('iveness'):
            word=self.m_over0(word,'iveness','ive')

        elif word.endswith('fulness'):
            word=self.m_over0(word,'fulness','ful')

        elif word.endswith('ousness'):
            word=self.m_over0(word,'ousness','ous')

        elif word.endswith('aliti'):
            word=self.m_over0(word,'aliti','al')

        elif word.endswith('iviti'):
            word=self.m_over0(word,'iviti','ive')

        elif word.endswith('biliti'):
            word=self.m_over0(word,'biliti','ble')
            
        return word

    def step_3(self,word):
        if word.endswith('icate'):
            word=self.m_over0(word,'icate','ic')
            
        elif word.endswith('ative'):
            word=self.m_over0(word,'ative','')
            
        elif word.endswith('alize'):
            word=self.m_over0(word,'alize','al')
            
        elif word.endswith('ical'):
            word=self.m_over0(word,'ical','ic')

        elif word.endswith('ful'):
            word=self.m_over0(word,'ful','')

        elif word.endswith('ness'):
            word=self.m_over0(word,'ness','')

        return word

    def step_4(self,word):
        if word.endswith('al'):
            word=self.m_over1(word,'al','')

        elif word.endswith('ance'):
            word=self.m_over1(word,'ance','')

        elif word.endswith('ence'):
            word=self.m_over1(word,'ence','')

        elif word.endswith('er'):
            word=self.m_over1(word,'er','')

        elif word.endswith('ic'):
            word=self.m_over1(word,'ic','')

        elif word.endswith('able'):
            word=self.m_over1(word,'able','')

        elif word.endswith('ible'):
            word=self.m_over1(word,'ible','')

        elif word.endswith('ant'):
            word=self.m_over1(word,'ant','')

        elif word.endswith('ement'):
            word=self.m_over1(word,'ement','')

        elif word.endswith('ment'):
            word=self.m_over1(word,'ment','')

        elif word.endswith('ent'):
            word=self.m_over1(word,'ent','')

        elif word.endswith('ion'):
            word=self.m_over1(word,'ion','')

        elif word.endswith('ou'):
            word=self.m_over1(word,'ou','')

        elif word.endswith('ism'):
            word=self.m_over1(word,'ism','')

        elif word.endswith('ate'):
            word=self.m_over1(word,'ate','')

        elif word.endswith('iti'):
            word=self.m_over1(word,'iti','')

        elif word.endswith('ous'):
            word=self.m_over1(word,'ous','')

        elif word.endswith('ive'):
            word=self.m_over1(word,'ive','')

        elif word.endswith('ize'):
            word=self.m_over1(word,'ize','')

        return word

    def stemming(self,word): #applying the algorithm stey by step.
        word=self.step_1a(word)
        word=self.step_1b(word)
        word=self.step_2(word)
        word=self.step_3(word)
        word=self.step_4(word)

        return word
      
        
if __name__=='__main__':
    porter=Porter()
    input_word=input("Input a word: ").lower()
    print("Stem: {0}" .format(porter.stemming(input_word)))
 
