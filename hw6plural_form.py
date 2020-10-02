def plural_form(count, form1, form2, form3):
    if 5<=count<=19 or count%10 == 0 or 5<= count%10 <=9:
        print(count, form3)
    elif count%2 == 1 and count%10 !=3:
        print(count, form1)
    elif 2<= count%10 <5: 
        print(count, form2)
    

plural_form(241, 'яблоко','яблока','яблок')
plural_form(3, 'яблоко','яблока','яблок')
plural_form(506, 'яблоко','яблока','яблок')
plural_form(100, 'яблоко','яблока','яблок')
