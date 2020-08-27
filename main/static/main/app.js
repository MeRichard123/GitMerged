document.addEventListener("DOMContentLoaded", function () {
  M.AutoInit();
  let elems = document.querySelectorAll(".collapsible");
  let instances = M.Collapsible.init(elems);

  let elements = document.querySelectorAll(".sidenav");
  let instance = M.Sidenav.init(elements);

  var elems2 = document.querySelectorAll("select");
  var instances2 = M.FormSelect.init(elems2);
});
