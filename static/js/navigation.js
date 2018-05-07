$(document).ready(function () {
    var page = parseInt($("#page").text());
    updateTabs(page);
    updateButtons(page);
});

// The button style
function updateButtons(page) {
    $("#prevBtn1").hide();
    $("#nextBtn1").hide();
    $("#prevBtn2").hide();
    $("#nextBtn2").hide();
    $("#nextBtn2").attr("onclick", "nextPage()");
    if (page == 1) {
        $("#nextBtn1").html("Next<span class=\"glyphicon glyphicon glyphicon-menu-right\" aria-hidden=\"true\"></span>");
        $("#nextBtn2").html("Next<span class=\"glyphicon glyphicon glyphicon-menu-right\" aria-hidden=\"true\"></span>");
        $("#nextBtn1").show();
        $("#nextBtn2").show();
    } else if (page == 18) {
        $("#prevBtn1").html("<span class=\"glyphicon glyphicon glyphicon-menu-left\" aria-hidden=\"true\"></span>Previous");
        $("#prevBtn2").html("<span class=\"glyphicon glyphicon glyphicon-menu-left\" aria-hidden=\"true\"></span>Previous");
        $("#nextBtn2").text("Review");
        $("#prevBtn1").show();
        $("#prevBtn2").show();
        $("#nextBtn2").show();
    } else if (page == 19) {
        return;
    } else {
        $("#prevBtn1").html("<span class=\"glyphicon glyphicon glyphicon-menu-left\" aria-hidden=\"true\"></span>Previous");
        $("#prevBtn2").html("<span class=\"glyphicon glyphicon glyphicon-menu-left\" aria-hidden=\"true\"></span>Previous");
        $("#nextBtn1").html("Next<span class=\"glyphicon glyphicon glyphicon-menu-right\" aria-hidden=\"true\"></span>");
        $("#nextBtn2").html("Next<span class=\"glyphicon glyphicon glyphicon-menu-right\" aria-hidden=\"true\"></span>");
        $("#prevBtn1").show();
        $("#prevBtn2").show();
        $("#nextBtn1").show();
        $("#nextBtn2").show();
    }
}

function updateTabs(page) {
    $("#tabs li").removeClass("active");
    switch (page) {
        case 1:
        case 2:
            $("#tab1").addClass("active");
            break;
        case 3:
            $("#tab2").addClass("active");
            break;
        case 4:
            $("#tab3").addClass("active");
            break;
        case 5:
            $("#tab4").addClass("active");
            break;
        case 6:
        case 7:
        case 8:
            $("#tab5").addClass("active");
            break;
        case 9:
        case 10:
        case 11:
        case 12:
        case 13:
            $("#tab6").addClass("active");
            break;
        case 14:
        case 15:
            $("#tab7").addClass("active");
            break;
        case 16:
        case 17:
        case 18:
            $("#tab8").addClass("active");
            break;
    }
}

function nextPage() {
    var page = parseInt($("#page").text());
    page++;
    $("#content").load("/" + page.toString());
    updateButtons(page);
    updateTabs(page);
}

function prevPage() {
    var page = parseInt($("#page").text());
    page--;
    $("#content").load("/" + page.toString());
    updateButtons(page);
    updateTabs(page);
}

function gotoPage(pageID) {
    $("#content").load("/" + pageID.toString());
    updateButtons(pageID);
    updateTabs(pageID);
}

function submit() {
    var endTime = Date.now();
    var data = {startTime: startTime, endTime: endTime, email: email, answers: answers};
    $.post("/summary",
        {
            data: JSON.stringify(data)
        },
        function (data, status) {
            $("#container").html(data);
        })
}