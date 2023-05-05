 
//----------------------------------------------------------------------------------------------------------
function selectRow(row) {
    // Get the data from the selected row
    var name = row.cells[1].innerText;
    var itemId = row.cells[0].innerText;
    var quantity = document.getElementById('quantity-' + itemId).value; // Get quantity from input field
    var price = row.cells[3].innerText;
    var totalPrice = parseFloat(quantity) * parseFloat(price); // Calculate total price
  
    // Create a new row in the second table
    var newRow = document.createElement("tr");
    newRow.innerHTML = "<td>" + name + "</td><td>" + quantity + "</td><td>" + totalPrice + " &#8377;</td><td>" + "<button onclick='removeRow(this)' class='btn btn-outline-danger'>Remove </button>"  + "</td>";
    document.getElementById("table2").appendChild(newRow);
  
   // Update total price
  var table2_total = parseFloat(document.getElementById("table2_total").innerText);
  table2_total += totalPrice;
  document.getElementById("table2_total").innerText = table2_total.toFixed(2);
   
  }

//------------------------------------------------------------------------------------------------------------

  function validateQuantity(input) {
    if (input.value > 25) {
      input.value = 25; // Set value to 25 if it's greater than 25
    }
    if(input.value<1 || input.value===0 || input.value===null){
      input.value=1
    }
    
  }

//----------------------------------------------------------------------------------------------------------

  function removeRow(button) {

  var row = button.parentNode.parentNode; // Get the parent row of the clicked button
  var table2 = document.getElementById("table2"); // Get table2
  var price = parseFloat(row.cells[2].innerText); // Get price from the row
  var table2_total = parseFloat(document.getElementById("table2_total").innerText);
  row.remove(); // Remove the row from the table
 // Update total price with value to subtract price
 table2_total =table2_total-price;
 document.getElementById("table2_total").innerText = table2_total.toFixed(2);
 
}

//----------------------------------------------------------------------------------------------------------------------
  
function search_menu() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("searchbar");
    filter = input.value.toUpperCase();
    table = document.getElementById("table1");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those that don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[1]; // Column index of the name in the table
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
        
      }
    }
  }
  
//-----