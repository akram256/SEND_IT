
function post_parcel(){

        var parcel_name = document.getElementById('parcel_name').value;
        var pickup_location = document.getElementById('pickup_location').value;
        var destination = document.getElementById('destination').value;
        var reciever = document.getElementById('reciever').value;
        var weight = document.getElementById('weight').value;
        const data = {"parcel_name":parcel_name, "pickup_location":pickup_location,"destination":destination,"reciever":reciever,"weight":weight};
        console.log(data);
        // alert(JSON.stringify(data));

        
            fetch('http://127.0.0.1:5000/api/v2/parcels', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-type':'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,
                    'Access-Control-Allow-Origin': '*'

                    
                },
                body: JSON.stringify({data})
            })
            .then((res) => res.json())
            .then((data) => {
                alert(JSON.stringify(data));

                let message = data.message;
                // localStorage.setItem("auth-token", data.auth-token)
                console.log(message);
                if(message == 'Order has been Placed successfully'){

                    alert(message);

                    window.location = 'history.html';
                }
                else {

                    alert(message);
                    }
                    });
                }


