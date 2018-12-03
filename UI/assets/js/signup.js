function SignupUser(){
    let  user_name = document.getElementById('user_name').value;
    let  email = document.getElementById('email').value;
    let  password = document.getElementById('password').value;
    const data = {"user_name":user_name,"email":email, "password":password};

    fetch('http://127.0.0.1:5000/api/v2/auth/signup', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
       
        cache: 'no-cache',
        body: JSON.stringify(data)
    })
        .then((res) => res.json())
        .then(result => {
            if(result.status === 'success'){
               alert(result.message)
               window.location.href = 'index.html';
            }
            else{
                alert(result.message)
            }
            
        })
        
}
