function LoginUser(){
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    const data = {"email":email, "password":password};


    fetch('http://127.0.0.1:5000/api/v2/auth/login', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
       
        cache: 'no-cache',
        body: JSON.stringify(data)
    })
        .then((res) => res.json())
        .then(result => {
            var token = result["access_token"];
            if(result["status"] === 'success'){
                if(email == "admin@gmail.com"){
                    localStorage.setItem("accessToken", token)
                    alert(data.access_token);
                    window.location.href = 'adminhistory.html';
                }
                else{
                    localStorage.setItem("accessToken", token)
                    window.location.href = 'parcel_order.html';
                }
            }
            else{

            }

        
            
        })
    
        
}