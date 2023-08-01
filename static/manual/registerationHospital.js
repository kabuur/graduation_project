

let HospitalName = document.querySelector("#HospitalName");
let tell = document.querySelector("#tell");
let email = document.querySelector("#email");
let password = document.querySelector("#password");
let password2 = document.querySelector("#password2");
let address = document.querySelector("#Address")
let userName = document.querySelector("#userName")

let register = document.querySelector('#register');
let dangerAlert = document.querySelector('#dangerAlert');
let passwordHelper = document.querySelector("#passwordHelper")
let confirmpasswordHelper = document.querySelector("#confirmpasswordHelper")

register.addEventListener('submit',(event)=>{

 

    
   if(checkemty(HospitalName) && checkemty(tell) && checkemty(email) && checkemty(password) && checkemty(password2) && checkemty(address) && checkemty(userName)){
      
        if(!checkPasswordLength){
            event.preventDefault();
            checkPasswordLength()
           
            return
        }
        if (!checkconfirmPassword){
            event.preventDefault();
            checkconfirmPassword()
           
            return
        }
    else{
        
    checkemty(HospitalName);
    checkemty(tell);
    checkemty(email);
    checkemty(password);
    checkemty(password2);
    checkemty(address);
    checkemty(userName)
    }

   }



   
   



})


function checkemty(field){
   
    if(field.value == ""){
        field.classList.add("border",'border-danger');
        dangerAlert.textContent ="All field must not emty....";
        dangerAlert.classList.add("alert", "alert-danger");
     
       
        return ;
    }
    else{
        field.classList.remove('border-danger');
        dangerAlert.textContent ="";
        dangerAlert.classList.remove("alert-danger");
        return true
    }
}

function checkPasswordLength(){
    if (password.value.length < 6){
        password.classList.add('border',"border-warning")
        passwordHelper.textContent = "At least 6 charactor..... "
        passwordHelper.style.color="red";

        return
    }else{
        password.classList.remove("border-warning")
        passwordHelper.textContent = ""
        return true
    }
}


function checkconfirmPassword(){
    if (password.value != password2.value){
        password2.classList.add('border',"border-warning")
        confirmpasswordHelper.textContent = "must be same..... "
        confirmpasswordHelper.style.color="red";

        return
    }else{
        password2.classList.remove("border-warning")
        confirmpasswordHelper.textContent = ""
        return true
    }
}