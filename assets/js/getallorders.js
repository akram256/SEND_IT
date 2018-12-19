

if(/adminhistory.html/.test(window.location.href)){

    
    fetch(' http://127.0.0.1:5000/api/v2/parcels', {

            method: 'GET',
            headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-type':'application/json',
            
            'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,
            'Access-Control-Allow-Origin': '*'
             }})
                .then((res) => res.json())
                .then(function(data){

              
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

