def sustract(a,b):
        print(a-b)   
def smart(function):

    def swap(a,b):
        if a<b:
            a,b=b,a
        function(a,b)
    return swap

sub=smart(sustract)
sub(10,50)

def division(a,b):
    div(10,20)




