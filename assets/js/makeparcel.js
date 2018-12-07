
function post_parcel(){

    let  parcel_name = document.getElementById('parcel_name').value;
    let  pickup_location = document.getElementById('pickup_location').value;
    let  destination = document.getElementById('destination').value;
    let  reciever = document.getElementById('reciever').value;
    let  weight = document.getElementById('weight').value;
        const data = {"parcel_name":parcel_name, "pickup_location":pickup_location,"destination":destination,"reciever":reciever,"weight":parseInt(weight)};
     

        
            fetch('https://senditapp3.herokuapp.com/api/v2/parcels', {
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


