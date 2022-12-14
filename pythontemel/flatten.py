def flatten(flat_lists):
    if isinstance(flat_lists, list): #liste içindeki veri tiplerini karşılaştırmada yardımcı olur.
        temp = []  # boş bir liste atıyoruz. Karşılatırdıklarımızı bu listeye atıyoruz.
        for i in flat_lists:
            temp.extend(flatten(i)) #liste birleştirme komutunu kullanıyoruz.
        return temp

    else:
        return [flat_lists]

flat_lists = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

result = flatten(flat_lists) # flatten komutunu kullanıyoruz.

print(str(result))