document.addEventListener("DOMContentLoaded", function () {
  console.log("Hello");
  let elems = document.querySelectorAll(".collapsible");
  let instances = M.Collapsible.init(elems);

  let elements = document.querySelectorAll(".sidenav");
  let instance = M.Sidenav.init(elements);
});
