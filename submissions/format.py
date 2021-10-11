# formatting text into numbers

def test():
    text_to_transform='baby'
    transform_way=str.maketrans('abcy','1234')
    print(text_to_transform)
    print(text_to_transform.translate(transform_way))