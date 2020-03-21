// JavaScript Document
//	Threshold based data

    function convert_vampire() {
      // var magic
      if (num_vampire == 1) {
        window.alert("Only one vampire left. No more conversion.");
      }
      else if (num_vampire == 2) {
        window.alert("Only two vampires left. Mercy please.");
        num_vampire -= 1;
        num_human += 1;
        data.removeRow(1);
        data.removeRow(0);
        data.insertRows(0, [['Human', num_human]]);
        data.insertRows(1, [['Vampire', num_vampire]]);
        chart.draw(data, options);
      }
      else {
        num_vampire -= 1;
        num_human += 1;
        data.removeRow(1);
        data.removeRow(0);
        data.insertRows(0, [['Human', num_human]]);
        data.insertRows(1, [['Vampire', num_vampire]]);
        chart.draw(data, options);
      }
    }

  
    function create_table() {
      //Creating intial table to display
      var table = document.getElementById("student_table");
      var row = table.insertRow(1);

      var cell1 = row.insertCell(0);
      var cell2 = row.insertCell(1);
      var cell3 = row.insertCell(2);
      var cell4 = row.insertCell(3);
      for (var i = 0; i <= classmate_data.length - 1; i++) {
        console.log(classmate_data[i]['name']);
        console.log(classmate_data[i]['shadow']);
        console.log(classmate_data[i]['galic']);
        console.log(classmate_data[i]['complexion']);
      }
      for (var i = 0; i <= classmate_data.length - 1; i++) {
        var row = table.insertRow(i + 1);

        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        cell1.innerHTML = classmate_data[i]['name'];
        cell2.innerHTML = classmate_data[i]['shadow'];
        cell3.innerHTML = classmate_data[i]['galic'];
        cell4.innerHTML = classmate_data[i]['complexion'];
      }

      delete_last_row()
    }

    function insert_row() {
      var table = document.getElementById("student_table");
      // Create an empty <tr> element and add it to the 1st position of the table:
      // BE CAREFUL!!! row 0 is our heading row
      var row = table.insertRow(1);

      var cell1 = row.insertCell(0);
      var cell2 = row.insertCell(1);
      var cell3 = row.insertCell(2);
      var cell4 = row.insertCell(3);
      var shadow;
      var galic;
      if (document.getElementById("shadow_checkbox").checked) {
        shadow = "yes";
      }
      else {
        shadow = "no";
      }
      if (document.getElementById("galic_checkbox").checked) {
        galic = "yes";
      }
      else {
        galic = "no";
      }

      // Add some text to the new cells:
      cell1.innerHTML = document.getElementById("first_name").value;
      cell2.innerHTML = shadow;
      cell3.innerHTML = galic;
      cell4.innerHTML = document.getElementById("Complexion").value;

      //Adds new student to classmate_data
      classmate_data[classmate_data.length] = {
        'name': document.getElementById("first_name").value,
        'shadow': shadow,
        'galic': galic,
        'complexion': document.getElementById("Complexion").value,
		'vampirism' : 'no'  
      };
      console.log(classmate_data);
    }

    function delete_row() {
      // delete the second row
      document.getElementById("student_table").deleteRow(1);
    }

    // based on https://stackoverflow.com/questions/10686888/delete-last-row-in-table
    function delete_last_row() {
      var table = document.getElementById('student_table');
      var row_count = table.rows.length;

      table.deleteRow(row_count - 1);
    }