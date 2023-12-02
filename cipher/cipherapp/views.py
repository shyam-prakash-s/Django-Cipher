from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def user(request):
    if request.method == "POST":
        guess = int(request.POST.get('gess'))
        choice = int(request.POST.get('choce'))
        message = request.POST.get('mesage')
        skip = int(request.POST.get('sip'))

        numbers = ['1','2','3','4','5','6','7','8','9','0']
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        symbols = ['!','+','=','-','_','(',')','@','#','$','*','/',' ','.',',',':',';','?','\'','\"','\\']
        alphabets = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        temp = ''
        encrypted_message = ''
        decrypted_message = ''
        num = 0

        def choosen(choice,guess):
            if choice == 1:
                cipher = numbers + letters + symbols + alphabets
            elif choice == 2:
                cipher = alphabets + numbers + symbols + letters
            elif choice == 3:
                cipher = letters  + symbols + alphabets + numbers
            elif choice == 4:
                cipher = symbols + numbers + alphabets + letters
            elif choice == 5:
                cipher = alphabets + letters + symbols + numbers
            elif choice == 6:
                cipher = alphabets + numbers + letters  + symbols
            else:
                return HttpResponse('wrong choice!!!')
            length = len(cipher)
            if guess == 0:
                return encryption(encrypted_message,temp,cipher,length)
            elif guess == 1:
                return decryption(decrypted_message,temp,cipher,length)

        #start of the encryption function 
        def encryption(encrypted_message,temp,cipher,length):
            '''global temp,encrypted_message'''
            
            for i in message:
                # if i ==  ' ':
                #     temp += '?'
                # else: 
                    num = cipher.index(i) + skip
                    if num >= length:
                        num %= length
                    temp += cipher[num]
            encrypted_message += temp
            # encr = '<!DOCTYPE html><html><head></head><body style="text-align: center; background-color: azure; margin: 100px;font-size: 2em;">'+encrypted_message+'<br><br><a href="http://127.0.0.1:8000/hello/">Home</a></body></html>'
            return render(request,'index.html',{'msg':encrypted_message})
        #end of encryption function 


        #start of decryption function 
        def decryption(decrypted_message,temp,cipher,length):
            '''global temp,decrypted_message'''
            for i in message:
                # if i ==  '?':
                #     temp += ' '
                # else:
                    num = cipher.index(i) - skip
                    if num < 0:
                        num = length - ((num*-1) % length)
                        '''num *= -1 ; num = num % length ; num = length - num'''
                        if num == length:
                            num = 0
                    temp += cipher[num]
            decrypted_message += temp
            # decr = '<!DOCTYPE html><html><head></head><body style="text-align: center; background-color: azure; margin: 100px;font-size: 2em;">'+decrypted_message+'<br><br><a href="http://127.0.0.1:8000/hello/">Home</a></body></html>'
            # return HttpResponse(decr)
        #end of decryption function
            # encr = '<!DOCTYPE html><html><head></head><body style="text-align: center; background-color: azure; margin: 100px;font-size: 2em;">'+encrypted_message+'<br><br><a href="http://127.0.0.1:8000/hello/">Home</a></body></html>'
            return render(request,'index.html',{'msg':decrypted_message})
        return choosen(choice,guess)
    else: 
        return render(request,'user.html')