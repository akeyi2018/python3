webiopi().ready( function()
{	// Initialize
	//webiopi().callMacro("MoveForward", 0);
        webiopi().callMacro( "MoveForward", [0] );
} );


var title = ['<hr size="3" color="#000000">',
             '<B><center> Car Controller<br><br>'].join("");

var table = ['<table id="tbl" boarder=2>',
             '<tr><th>稼働状態</th><th>距離計測</th></tr>',
             '<tr><th>-</th><th>-</th></tr></table>'].join("");

var button = ['<hr size="3" color="#000000">',
              '<input type="button" value="前進" onclick="MoveCar(1)" style="width:80px;height:80px"><br>',
              '<input type="button" value="左折" onclick="MoveCar(2)" style="width:80px;height:80px">',
              '<input type="button" value="停止" onclick="MoveCar(5)" style="width:80px;height:80px;color:#ff0000">',
              '<input type="button" value="右折" onclick="MoveCar(3)" style="width:80px;height:80px"><br>',
              '<input type="button" value="後退" onclick="MoveCar(4)" style="width:80px;height:80px"><br>'
              ].join("");

function MoveCar(direct){

    if (1 == direct){
        webiopi().callMacro("MoveForward", [direct], callBackMove);
        //webiopi().digitalWrite(19,[1], callBackMove);
        //webiopi().digitalWrite(6,[1],callBackMove);
        }
    if (2 == direct){ webiopi().callMacro("MoveForward", [direct], callBackMove); }
    if (3 == direct){ webiopi().callMacro("MoveForward", [direct], callBackMove); }
    if (4 == direct){ webiopi().callMacro("MoveForward", [direct], callBackMove); }
    if (5 == direct){ webiopi().callMacro("MoveForward", [direct], callBackMove); }
}


function callBackMove(macro, direct, data){

    var status = new Array("Forward","TurnLeft","TrunRight","back","stop");
    document.getElementById("tbl").rows[1].cells[0].innerHTML= status[direct-1];
    document.getElementById("tbl").rows[1].cells[1].innerHTML= data;
    
    }

function ShowButton(){

    var form = document.createElement('form');
    form.setAttribute("name","robot");
    form.setAttribute("method","post");
    form.setAttribute("target","hiddeniframe");
    
    form.innerHTML = title+table+button;
    form.style.display = "block";
    document.body.appendChild(form);
    form.submit();
    
    }

window.onload = function(){

    ShowButton();
    
    
    };
