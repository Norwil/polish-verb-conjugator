
verb = input('Please enter a verb:\n')

def conjugator(verb): # A limited version of Polish verb conjugation function.
    newverb = verb[-4:]
    if newverb == 'ować':
        print(verb)
        conjugated_verb = verb[:-4]
        conjugate = [conjugated_verb+'uję', conjugated_verb+'ujesz', conjugated_verb+'uje', conjugated_verb+'ujemy', conjugated_verb+'ujecie', conjugated_verb+'ują']
        for i in conjugate:
            print(i)
            
    elif newverb == 'ywać':
        print(verb)
        conjugated_verb = verb[:-4]
        conjugate = [conjugated_verb+'uję', conjugated_verb+'ujesz', conjugated_verb+'uje', conjugated_verb+'ujemy', conjugated_verb+'ujecie', conjugated_verb+'ują']
        for i in conjugate:
            print(i)
            
    elif newverb == 'iwać':
        print(verb)
        conjugated_verb = verb[:-4]
        conjugate = [conjugated_verb+'uję', conjugated_verb+'ujesz', conjugated_verb+'uje', conjugated_verb+'ujemy', conjugated_verb+'ujecie', conjugated_verb+'ują']
        for i in conjugate:
            print(i)
            
    elif newverb == 'awać':
        print(verb)
        conjugated_verb = verb[:-4]
        conjugate = [conjugated_verb+'aję', conjugated_verb+'ajesz', conjugated_verb+'aje', conjugated_verb+'ajemy', conjugated_verb+'ajecie', conjugated_verb+'ają']
        for i in conjugate:
            print(i)
            
    else:
        print('Your verb has an irregular conjugation')

conjugator(verb)
