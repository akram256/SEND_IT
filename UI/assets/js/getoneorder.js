//  document.getElementById('search').addEventListener('keyup' , search)
if(/adminorder.html/.test(window.location.href)){

  let parcel_url = window.location.href
  let url = new URL(parcel_url)
  let parcel_id = url.searchParams.get("parcel")
    console.log(parcel_id);

    fetch("http://127.0.0.1:5000/api/v2/parcels/"+parcel_id,  {

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
                    //  for(i = 0; i < data["Orders"].length; i++){

                          table += 
                          "<tr><td><a href ='#' onclick='change_current_location()' id='current-value'>"+data["message"][0]["current_location"]
                          +"</td><td>"+data["message"][0]["destination"]
                          +"</td><td>"+data["message"][0]["order_date"]
                          +"</td><td>"+data["message"][0]["parcel_id"]
                          +"</td><td>"+data["message"][0]["parcel_name"]
                          +"</td><td> <a href ='#' onclick='change_status()' id='status-value'>"+data["message"][0]["parcel_status"]
                          +"</td><td>"+data["message"][0]["pickup_location"]
                          +"</td><td>"+data["message"][0]["reciever"]
                          +"</td><td>"+data["message"][0]["user_id"]
                          +"</td><td>"+data["message"][0]["weight"]
                          +"</td></tr>";
                          
                        
                    //   }
                 
                     document.getElementById('oneparcels_table').innerHTML = table+"</table>";
                    //  alert(table);
                    
                     });
                     

}

function change_status(){
    let status = window.prompt("change status ?")
    console.log(status)

    let parcel_url = window.location.href
    let url = new URL(parcel_url)
    let parcel_id = url.searchParams.get("parcel")
      console.log(parcel_id);

    const data = {"parcel_status": status};


fetch('http://127.0.0.1:5000/api/v2/parcels/'+parcel_id+'/status', {
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
        document.getElementById('status-value').innerHTML = status
        alert(result.message)
        //window.location.href="admin_viewOrder.html";

    }
    else{
        alert(result.message)
    }
    
})


}

function change_current_location(){
    let current = window.prompt("change current?")
    console.log(current)

    let parcel_url = window.location.href
    let url = new URL(parcel_url)
    let parcel_id = url.searchParams.get("parcel")
      console.log(parcel_id);

    const data = {"current_location": current};


fetch('http://127.0.0.1:5000/api/v2/parcels/'+parcel_id+'/currentlocation', {
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
        document.getElementById('current-value').innerHTML = current
        alert(result.message)
        //window.location.href="admin_viewOrder.html";

    }
    else{
        alert(result.message)
    }
    
})


}

