if(/adminorder.html/.test(window.location.href)){

  let parcel_url = window.location.href
  let url = new URL(parcel_url)
  let parcel_id = url.searchParams.get("parcel")
    console.log(parcel_id);

    fetch(" http://127.0.0.1:5000/api/v2/parcels/"+parcel_id,  {

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
                          table += 
                          "<tr><td><a href ='#' onclick='chg_dst()' id='current-value'>"+data["message"][0]["current_location"]
                          +"</td><td>"+data["message"][0]["destination"]
                          +"</td><td>"+data["message"][0]["order_date"]
                          +"</td><td>"+data["message"][0]["parcel_id"]
                          +"</td><td>"+data["message"][0]["parcel_name"]
                          +"</td><td> <a href ='#' onclick='chg_sts()' id='status-value'>"+data["message"][0]["parcel_status"]
                          +"</a></td><td>"+data["message"][0]["pickup_location"]
                          +"</td><td>"+data["message"][0]["reciever"]
                          +"</td><td>"+data["message"][0]["user_id"]
                          +"</td><td >"+data["message"][0]["weight"]
                          +"</td></tr>";
                 
                     document.getElementById('oneparcels_table').innerHTML = table+"</table>";
                    
                    
                     });
                     
}

function chg_sts(){
    document.getElementById("main-out").style.display = 'block'
}

function cls(){
    document.getElementById("main-out").style.display = 'none'
}

function change_status(){
    
    let status = document.getElementById("chng-status").value
    console.log(status)

    let parcel_url = window.location.href
    let url = new URL(parcel_url)
    let parcel_id = url.searchParams.get("parcel")
      console.log(parcel_id);

    const data = {"parcel_status": status};


fetch(' http://127.0.0.1:5000/api/v2/parcels/'+parcel_id+'/status', {
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
    if(result.status == 'success'){
        alert(result.message)
    }
    else{
        document.getElementById('status-value').innerHTML = status
        document.getElementById("main-out").style.display = 'none'
        alert(result.message)
    }
    
})


}
function chg_dst(){
    document.getElementById("main-dest").style.display = 'block'
}

function cls_current(){
    document.getElementById("main-dest").style.display = 'none'
}

function change_current_location(){
    let current = document.getElementById("chng-current").value
    // let current = window.prompt("change current?")
    console.log(current)

    let parcel_url = window.location.href
    let url = new URL(parcel_url)
    let parcel_id = url.searchParams.get("parcel")
      console.log(parcel_id);

    const data = {"current_location": current};


fetch(' http://127.0.0.1:5000/api/v2/parcels/'+parcel_id+'/currentlocation', {
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
        //window.location.href="admin_viewOrder.html";

    }
    else{
        document.getElementById('current-value').innerHTML = current
        document.getElementById("main-dest").style.display = 'none'
        alert(result.message)
    }
    
})


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
