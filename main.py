from BracketsLegals import BracketsLegals

bl = BracketsLegals()
legal_list = ['(()[[]][])',
              '[[]{}{{}}]',
              '{[]{[][]}}',
              '()((){[]})',
              '{([][]{})}',
              '[[][()]]{}',
              '(([]{[]}))',
              '[]{[[]{}]}',
              '{[[]]{}}()',
              '{{}}[{()}]']

illegal = ['}}))[{)({]',
           '{)({([)){}',
           '{{}[((]}}]',
           '[){{{{{)}(',
           '{}[[}]}(]{',
           '}[]]{[})[{',
           '][[([}[)()',
           '[)(]){]}(]',
           '(]}}[)})]]',
           '[)((])]{(}']

if __name__ == '__main__':
    print(f'the ilegal = {bl.check_list(illegal)}')
    print(f'the legal list = {bl.check_list(legal_list)}')
