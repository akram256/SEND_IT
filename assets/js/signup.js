function SignupUser(){
    let  user_name = document.getElementById('user_name').value;
    let  email = document.getElementById('email').value;
    let  password = document.getElementById('password').value;
    const data = {"user_name":user_name,"email":email, "password":password};
    // console.log(data);

    fetch('https://senditapp3.herokuapp.com/api/v2/auth/signup', {
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
            alert(JSON.stringify(data));
            if(result.status === 'success'){
               alert(result.message)
               window.location.href = 'index.html';
            }
            else{
                alert(result.message)
            }
            
        })
        
}
