
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
                          +"</td><td><a onclick='change_destination(this)' href='#' data-id ='"+data["message"][i]["parcel_id"]+"'>"+data["message"][i]["destination"]
                      
                          +"</td><td>"+data["message"][i]["order_date"]
                          +"</td><td>"+data["message"][i]["parcel_id"]
                          +"</td><td>"+data["message"][i]["parcel_name"]
                          +"</td><td><a href ='cancelstatus.html?parcel="+data["message"][i]["parcel_id"]+"'>"+data["message"][i]["parcel_status"]
                        // +"</td><td><<select onclick='change_status'><option value='User'>User id</option><option value='User'>User id</option></select>"+data["message"][i]["parcel_status"]
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
// function myFunction(){
//     var td, i, tdArr, j;
//     var input = document.getElementById("myInput");
//     var filter = input.value.toUpperCase();
//     var table = document.getElementById("myTable");
//     var tr = table.getElementsByTagName("tr");
  
//     // Loop through all table rows
//     for (i = 0; i < tr.length; i++) {
//       tdArr = tr[i].getElementsByTagName("td");
//       // Loop through all table columns in the current row, and hide those who don't match the search query
//       for (j = 0; j < tdArr.length; j++) {
//         td = tdArr[j];
//         if (td) {
//           if (td.innerHTML.toUpperCase().indexOf(filter) > -1 ) {
//             tr[i].style.display = "";
//           } else {
//             tr[i].style.display = "none";
//           }
//         }
//       }        
//     }
//   }


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

function update_status(){
    destination = document.getElementById('chng-destination').value
    console.log(destination)

    //let parcel_url = window.location.href
    ///let url = new URL(parcel_url)
    //let parcel_id = url.searchParams.get("parcel")
    let parcel_id = d.getAttribute("data-id")
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

function change_destination(d){
    alert(d.getAttribute(d.getAttribute("data-id")))
    document.getElementById('main-out').style.display = 'block';
}

function cls(){
    document.getElementById('chng-destination').value = '';
    document.getElementById('main-out').style.display = 'none';
}
// function mysearch(){
//     let input, filter, table,tr,td,i,txtValue;
// input = document.getElementById("input");
// filter = input.nodeValue.toUpperCase();
// table= document.getElementById("specificparcels_table")
// tr = table.getElementsByTagName("tr");

// for (i=0; i<tr.length;i++){
//     td= tr(i).getElementsByTagName("td")[0];
//     if (td){
//         txtValue=td.textContent 
//         || td.innerText;
//         if (txtValue.toUpperCase().indexOf(filter)>-1)
//         {
//             tr[i].style.display="";

//         }else
//         tr[i].style.display = "none";
//     }
// }
// }

