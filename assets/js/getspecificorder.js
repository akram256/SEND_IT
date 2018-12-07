
if(/history.html/.test(window.location.href)){

    
    fetch('http://127.0.0.1:5000/api/v2/users/parcels', {

            method: 'GET',
            headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type':'application/json',
            
            'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,
            'Access-Control-Allow-Origin': '*'
             }})
                .then((res) => res.json())
                .then(function(data){
                    // alert(JSON.stringify(data));
                let pending = new Array()
                let in_transit = new Array()
                let delivered = new Array()
                let cancelled = new Array()

                 
                let i = 0;

                let table = '<table border="2px">'+
                            '<tr>'+
                            '<th>current_location</th>'+
                            '<th>destination</th>'+
                            '<th>order_date</th>'+
                            '<th>parcel_id</th>'+
                            '<th>parcel_name</th>'+
                            '<th>parcel_status</th>'+
                            '<th>pickup_location</th>'+
                            '<th>reciever</th>'+
                            '<th>user_id</th>'+
                            '<th>weight</th>'+
                           ' </tr>'; 
                  
                           for(i = 0; i < data["message"].length; i++){
                          table += 
                          "<tr><td>"+data["message"][i]["current_location"]
                          +"</td><td><a href ='oneorderhistory.html?parcel="+data["message"][i]["parcel_id"]+"'>"+data["message"][i]["destination"]
                          +"</td><td>"+data["message"][i]["order_date"]
                          +"</td><td>"+data["message"][i]["parcel_id"]
                          +"</td><td>"+data["message"][i]["parcel_name"]
                          +"</td><td><a href ='cancelstatus.html?parcel="+data["message"][i]["parcel_id"]+"'>"+data["message"][i]["parcel_status"]
                          +"</td><td>"+data["message"][i]["pickup_location"]
                          +"</td><td>"+data["message"][i]["reciever"]
                          +"</td><td>"+data["message"][i]["user_id"]
                          +"</td><td>"+data["message"][i]["weight"]
                          +"</td></tr>";
                          
                        
                 
                     document.getElementById('specificparcels_table').innerHTML = table+"</table>";
                    //  alert(table);




                   
                
                
                           }
                     });
                     
                    
}


if(/profile.html/.test(window.location.href)){

    fetch('http://127.0.0.1:5000/api/v2/users/parcels', {

        method: 'GET',
        headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-type':'application/json',
        
        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,
        'Access-Control-Allow-Origin': '*'
            }})
        .then((res) => res.json())
        .then(function(data){
            // alert(JSON.stringify(data));
        let pending = new Array()
        let in_transit = new Array()
        let delivered = new Array()
        let cancelled = new Array()

            
        let i = 0;
        
        for(i = 0; i < data["message"].length; i++){
            if(data['message'][i]['parcel_status'] == 'pending'){
                pending.push(data['message'][i]['StatusProfile'])
            }
        
            if(data['message'][i]['parcel_status'] == 'in-transit'){
                in_transit.push(data['message'][i]['StatusProfile'])
            }
        
            if(data['message'][i]['parcel_status'] == 'delivered'){
                delivered.push(data['message'][i]['StatusProfile'])
            }
        
            if(data['message'][i]['parcel_status'] == 'cancelled'){
                cancelled.push(data['message'][i]['StatusProfile'])
            }
        }

        document.getElementById('num_parcel_pending').innerHTML = (pending.length);
        document.getElementById('num_parcel_delivered').innerHTML = (in_transit.length);
        document.getElementById('num_parcel_in_transit').innerHTML = (delivered.length);
        document.getElementById('num_parcel_cancel').innerHTML = (cancelled.length);
    });
}

// function change_destination(){
    if(/oneorderhistory.html/.test(window.location.href)){
    let destination = window.prompt("change destination ?")
    console.log(destination)

    let parcel_url = window.location.href
    let url = new URL(parcel_url)
    let parcel_id = url.searchParams.get("parcel")
      console.log(parcel_id);

    const data = {"destination": destination};


fetch('http://127.0.0.1:5000/api/v2/parcels/'+parcel_id+'/destination', {
method: 'PUT',
headers: {
    'Accept': 'application/json',
    'Content-type': 'application/json',
    'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,
},
cache: 'no-cache',
body: JSON.stringify(data)

})
.then((res) => res.json())
.then(result => {
    if(result.status === 'success'){
        // document.getElementById('destination').innerHTML = destination
        alert(result.message)
      

    }
    else{
        alert(result.message)
    }
    
})


}
// }

if(/cancelstatus.html/.test(window.location.href)){
    let status = window.prompt("cancel status ?")
    console.log(status)

    let parcel_url = window.location.href
    let url = new URL(parcel_url)
    let parcel_id = url.searchParams.get("parcel")
      console.log(parcel_id);

    const data = {"parcel_status": status};


fetch('http://127.0.0.1:5000/api/v2/parcels/'+parcel_id+'/cancel', {
method: 'PUT',
headers: {
    'Accept': 'application/json',
    'Content-type': 'application/json',
    'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,
},
cache: 'no-cache',
body: JSON.stringify(data)

})
.then((res) => res.json())
.then(result => {
    if(result.status === 'success'){
        alert(result.message)
      

    }
    else{
        alert(result.message)
    }
    
})


}