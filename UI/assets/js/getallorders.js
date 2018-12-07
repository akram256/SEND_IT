

function all_parcels(){

    
    fetch('http://127.0.0.1:5000/api/v2/parcels', {

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

                    // let out_put = "";

                    // console.log(data.parcel_list.length);
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
                     for(i = 0; i < data["Orders"].length; i++){

                          table += 
                          "<tr><td>"+data["Orders"][i]["current_location"]
                          +"</td><td>"+data["Orders"][i]["destination"]
                          +"</td><td>"+data["Orders"][i]["order_date"]
                          +"</td><td>"+data["Orders"][i]["parcel_id"]
                          +"</td><td><a href ='adminorder.html?parcel="+data["Orders"][i]["parcel_id"]+"'>"+data["Orders"][i]["parcel_name"]
                          +"</a></td><td>"+data["Orders"][i]["parcel_status"]
                          +"</td><td>"+data["Orders"][i]["pickup_location"]
                          +"</td><td>"+data["Orders"][i]["reciever"]
                          +"</td><td>"+data["Orders"][i]["user_id"]
                          +"</td><td>"+data["Orders"][i]["weight"]
                          +"</td></tr>";
                          
                        
                      }
                 
                     document.getElementById('parcels_table').innerHTML = table+"</table>";
                    //  alert(table);
                    
                     });
                     

}

