
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

                let table = '<table id="tables">'+
                '<tr>'+
                '<th class="left">CURRENT LOCATION</th>'+
                '<th class="center">DESTINATION</th>'+
                '<th class="center">ORDER DATE</th>'+
                '<th class="center">PARCEL ID</th>'+
                '<th class="center">PARCEL NAME</th>'+
                '<th class="center">PARCEL STATUS</th>'+
                '<th class="center">PICKUP LOCATION</th>'+
                '<th class="center">RECIEVER</th>'+
                '<th class="center">USER ID</th>'+
                '<th class="right">WEIGHT</th>'+
               
               ' </tr>';
                  
                           for(i = 0; i < data["message"].length; i++){
                          table += 
                          "<tr><td>"+data["message"][i]["current_location"]
                          +"</td><td><a href ='oneorderhistory.html?parcel="+data["message"][i]["parcel_id"]+"'>"+data["message"][i]["destination"]
                          +"</td><td>"+data["message"][i]["order_date"]
                          +"</td><td>"+data["message"][i]["parcel_id"]
                          +"</td><td>"+data["message"][i]["parcel_name"]
                          +"</td><td><a href ='oneorderhistory.html?parcel="+data["message"][i]["parcel_id"]+"'>"+data["message"][i]["parcel_status"]
                          +"</td><td>"+data["message"][i]["pickup_location"]
                          +"</td><td>"+data["message"][i]["reciever"]
                          +"</td><td>"+data["message"][i]["user_id"]
                          +"</td><td>"+data["message"][i]["weight"]
                          +"</td></tr>";
                          
                        
                 
                     document.getElementById('specificparcels_table').innerHTML = table+"</table>";

                
                           }
                     });
}

function mysearch(){
    let input, filter, table,tr,td,i,txtValue;
    input = document.getElementById("input");
    filter = input.value.toUpperCase();
    table= document.getElementById("tables")
    tr = table.getElementsByTagName("tr");
    
    for (i=0; i<tr.length;i++){
        td = tr[i].getElementsByTagName("td")[5];

        if (td){
            console.log(td)
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter)>-1){
                tr[i].style.display="";
            }else
            tr[i].style.display = "none";
        }
    }
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

